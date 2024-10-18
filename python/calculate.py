import paho.mqtt.client as mqtt
import json

parkings = []


def on_connect(client, userdata, flags, rc, properties=None):
    print("CALCULATE connected to MQTT server")
    client.subscribe([("init_parking", 0), ("parking_sensor", 0)])


def on_message(client, userdata, msg):
    if msg.topic == "init_parking":
        on_init_parking(json.loads(msg.payload))
    elif msg.topic == "parking_sensor":
        on_parking_sensor(json.loads(msg.payload))
    else:
        return


def get_parking_by_id(id):
    for parking in parkings:
        if parking["id"] == id:
            return parking
    return None


def on_init_parking(data):
    global parkings
    parking = {
        "id": data["id"],
        "car": data["places"]["cars"],
        "pr": data["places"]["pr"],
        "pmr": data["places"]["pmr"],
        "elec_cars": data["places"]["elec_cars"],
        "bycicles": data["places"]["bycicles"],
        "2wheels_elec": data["places"]["2wheels_elec"],
        "autoshare": data["places"]["autoshare"],
        "2wheels": data["places"]["2wheels"],
        "covoit": data["places"]["covoit"],
        "amodies": data["places"]["amodies"],
        "stop_minute": data["places"]["stop_minute"],
    }
    parkings.append(parking)


def on_parking_sensor(data):
    global parkings
    total = get_parking_by_id(data["id"])
    parking = {
        "id": data["id"],
        "averages": {
            "free_cars_average": int(
                (data["places"]["free_cars"] * 100) / total["car"]
                if total["car"] != 0
                else 0
            ),
            "free_pr_average": int(
                (data["places"]["free_pr"] * 100) / total["pr"]
                if total["pr"] != 0
                else 0
            ),
            "free_pmr_average": int(
                (data["places"]["free_pmr"] * 100) / total["pmr"]
                if total["pmr"] != 0
                else 0
            ),
            "free_elec_cars_average": int(
                (data["places"]["free_elec_cars"] * 100) / total["elec_cars"]
                if total["elec_cars"] != 0
                else 0
            ),
            "free_bycicles_average": int(
                (data["places"]["free_bycicles"] * 100) / total["bycicles"]
                if total["bycicles"] != 0
                else 0
            ),
            "free_2wheels_elec_average": int(
                (data["places"]["free_2wheels_elec"] * 100) / total["2wheels_elec"]
                if total["2wheels_elec"] != 0
                else 0
            ),
            "free_autoshare_average": int(
                (data["places"]["free_autoshare"] * 100) / total["autoshare"]
                if total["autoshare"] != 0
                else 0
            ),
            "free_2wheels_average": int(
                (data["places"]["free_2wheels"] * 100) / total["2wheels"]
                if total["2wheels"] != 0
                else 0
            ),
            "free_covoit_average": int(
                (data["places"]["free_covoit"] * 100) / total["covoit"]
                if total["covoit"] != 0
                else 0
            ),
            "free_amodies_average": int(
                (data["places"]["free_amodies"] * 100) / total["amodies"]
                if total["amodies"] != 0
                else 0
            ),
            "free_stop_minute_average": int(
                (data["places"]["free_stop_minute"] * 100) / total["stop_minute"]
                if total["stop_minute"] != 0
                else 0
            ),
        },
    }
    client.publish("parking_average", json.dumps(parking))


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1884, 60)

client.loop_forever()
