import paho.mqtt.client as mqtt
import mysql.connector
import json

db_config = {
    "host": "localhost",
    "user": "admin",
    "password": "admin",
    "database": "ParkSmart",
}


def on_connect(client, userdata, flags, rc, properties=None):
    print("CALCULATE connected to MQTT server")
    client.subscribe(
        [
            ("init_parking", 0),
            ("parking_sensor", 0),
            ("parking_average", 0),
        ]
    )


def on_message(client, userdata, msg):
    if msg.topic == "init_parking":
        save_init_parking(json.loads(msg.payload))
    elif msg.topic == "parking_sensor":
        save_parking_sensor(json.loads(msg.payload))
    elif msg.topic == "parking_average":
        save_parking_average(json.loads(msg.payload))
    else:
        return


def save_init_parking(data):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        sql = """
        INSERT INTO Parking (
            id, lon, lat, name, city, address, public, free, max_height,
            price_pmr, price_1h, price_2h, price_3h, price_4h, price_24h, price_sub_resident, price_sub_no_resident, 
            cars, free_cars, free_cars_average,
            pr, free_pr, free_pr_average,
            pmr, free_pmr, free_pmr_average,
            elec_cars, free_elec_cars, free_elec_cars_average,
            bycicles, free_bycicles, free_bycicles_average,
            two_wheels_elec, free_two_wheels_elec, free_two_wheels_elec_average,
            autoshare, free_autoshare, free_autoshare_average, 
            two_wheels, free_two_wheels, free_two_wheels_average,
            covoit, free_covoit, free_covoit_average,
            amodies, free_amodies, free_amodies_average,
            stop_minute, free_stop_minute, free_stop_minute_average
        )
        VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0,
            %s, 0, 0
        )
        """

        values = (
            data["id"],
            data["infos"]["lon"],
            data["infos"]["lat"],
            data["infos"]["name"],
            data["infos"]["city"],
            data["infos"]["address"],
            data["infos"]["public"],
            data["infos"]["free"],
            data["infos"]["max_height"],
            data["prices"]["price_pmr"],
            data["prices"]["price_1h"],
            data["prices"]["price_2h"],
            data["prices"]["price_3h"],
            data["prices"]["price_4h"],
            data["prices"]["price_24h"],
            data["prices"]["price_sub_resident"],
            data["prices"]["price_sub_no_resident"],
            data["places"]["cars"],
            data["places"]["pr"],
            data["places"]["pmr"],
            data["places"]["elec_cars"],
            data["places"]["bycicles"],
            data["places"]["2wheels_elec"],
            data["places"]["autoshare"],
            data["places"]["2wheels"],
            data["places"]["covoit"],
            data["places"]["amodies"],
            data["places"]["stop_minute"],
        )
        cursor.execute(sql, values)

        db.commit()
    except mysql.connector.Error as err:
        print("Error connecting to MySQL: ", err)
    finally:
        cursor.close()
        db.close()


def save_parking_sensor(data):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        sql = """
        UPDATE Parking
        SET free_cars = %s,
            free_pr = %s,
            free_pmr = %s,
            free_elec_cars = %s,
            free_bycicles = %s,
            free_two_wheels_elec = %s,
            free_autoshare = %s,
            free_two_wheels = %s,
            free_covoit = %s,
            free_amodies = %s,
            free_stop_minute = %s
        WHERE id = %s
        """

        values = (
            data["places"]["free_cars"],
            data["places"]["free_pr"],
            data["places"]["free_pmr"],
            data["places"]["free_elec_cars"],
            data["places"]["free_bycicles"],
            data["places"]["free_2wheels_elec"],
            data["places"]["free_autoshare"],
            data["places"]["free_2wheels"],
            data["places"]["free_covoit"],
            data["places"]["free_amodies"],
            data["places"]["free_stop_minute"],
            data["id"],
        )
        cursor.execute(sql, values)

        db.commit()
    except mysql.connector.Error as err:
        print("Error connecting to MySQL: ", err)
    finally:
        cursor.close()
        db.close()


def save_parking_average(data):
    try:
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()

        sql = """
        UPDATE Parking
        SET free_cars_average = %s,
            free_pr_average = %s,
            free_pmr_average = %s,
            free_elec_cars_average = %s,
            free_bycicles_average = %s,
            free_two_wheels_elec_average = %s,
            free_autoshare_average = %s,
            free_two_wheels_average = %s,
            free_covoit_average = %s,
            free_amodies_average = %s,
            free_stop_minute_average = %s
        WHERE id = %s
        """

        values = (
            data["averages"]["free_cars_average"],
            data["averages"]["free_pr_average"],
            data["averages"]["free_pmr_average"],
            data["averages"]["free_elec_cars_average"],
            data["averages"]["free_bycicles_average"],
            data["averages"]["free_2wheels_elec_average"],
            data["averages"]["free_autoshare_average"],
            data["averages"]["free_2wheels_average"],
            data["averages"]["free_covoit_average"],
            data["averages"]["free_amodies_average"],
            data["averages"]["free_stop_minute_average"],
            data["id"],
        )
        cursor.execute(sql, values)

        db.commit()
    except mysql.connector.Error as err:
        print("Error connecting to MySQL: ", err)
    finally:
        cursor.close()
        db.close()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(
    "localhost",
    1884,
    60,
)

client.loop_forever()
