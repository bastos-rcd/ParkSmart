import paho.mqtt.client as mqtt
import json
import random
import time

with open("parking.json", "r") as f:
    parkings = json.load(f)


def on_connect(client, userdata, flags, rc, properties=None):
    print("SIMULATION connected to MQTT server")


def send_initial_data():
    for parking in parkings:
        data = {
            "id": parking["id"],
            "infos": {
                "lon": parking["geo_point_2d"]["lon"],
                "lat": parking["geo_point_2d"]["lat"],
                "name": parking["nom"],
                "city": parking["commune"],
                "address": parking["adresse"],
                "public": True if parking["public"] == "T" else False,
                "free": True if parking["gratuit"] == "T" else False,
                "max_height": parking["hauteur_max"],
            },
            "places": {
                "cars": parking["nb_voitures"],
                "pr": parking["nb_pr"],
                "pmr": parking["nb_pmr"],
                "elec_cars": parking["nb_voitures_electriques"],
                "bycicles": parking["nb_velo"],
                "2wheels_elec": parking["nb_2r_el"],
                "autoshare": parking["nb_autopartage"],
                "2wheels": parking["nb_2_rm"],
                "covoit": parking["nb_covoit"],
                "amodies": parking["nb_amodie"],
                "stop_minute": parking["nb_arretm"],
            },
            "prices": {
                "price_pmr": parking["tarif_pmr"],
                "price_1h": parking["tarif_1h"],
                "price_2h": parking["tarif_2h"],
                "price_3h": parking["tarif_3h"],
                "price_4h": parking["tarif_4h"],
                "price_24h": parking["tarif_24h"],
                "price_sub_resident": parking["abo_resident"],
                "price_sub_no_resident": parking["abo_non_resident"],
            },
        }
        client.publish("init_parking", json.dumps(data))


def simulate_sensors():
    for parking in parkings:
        data = {
            "id": parking["id"],
            "places": {
                "free_cars": random.randint(0, parking["nb_voitures"]),
                "free_pr": random.randint(0, parking["nb_pr"]),
                "free_pmr": random.randint(0, parking["nb_pmr"]),
                "free_elec_cars": random.randint(0, parking["nb_voitures_electriques"]),
                "free_bycicles": random.randint(0, parking["nb_velo"]),
                "free_2wheels_elec": random.randint(0, parking["nb_2r_el"]),
                "free_autoshare": random.randint(0, parking["nb_autopartage"]),
                "free_2wheels": random.randint(0, parking["nb_2_rm"]),
                "free_covoit": random.randint(0, parking["nb_covoit"]),
                "free_amodies": random.randint(0, parking["nb_amodie"]),
                "free_stop_minute": random.randint(0, parking["nb_arretm"]),
            },
        }
        client.publish("parking_sensor", json.dumps(data))


client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1884, 60)

client.loop_start()

try:
    send_initial_data()
    while True:
        simulate_sensors()
        time.sleep(60)

except KeyboardInterrupt:
    print("Stopping script...")

finally:
    client.loop_stop()
    client.disconnect()
