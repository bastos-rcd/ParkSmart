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
                "cars": parking["nb_voitures"] if parking["nb_voitures"] else 0,
                "pr": parking["nb_pr"] if parking["nb_pr"] else 0,
                "pmr": parking["nb_pmr"] if parking["nb_pmr"] else 0,
                "elec_cars": (
                    parking["nb_voitures_electriques"]
                    if parking["nb_voitures_electriques"]
                    else 0
                ),
                "bycicles": parking["nb_velo"] if parking["nb_velo"] else 0,
                "2wheels_elec": parking["nb_2r_el"] if parking["nb_2r_el"] else 0,
                "autoshare": (
                    parking["nb_autopartage"] if parking["nb_autopartage"] else 0
                ),
                "2wheels": parking["nb_2_rm"] if parking["nb_2_rm"] else 0,
                "covoit": parking["nb_covoit"] if parking["nb_covoit"] else 0,
                "amodies": parking["nb_amodie"] if parking["nb_amodie"] else 0,
                "stop_minute": parking["nb_arretm"] if parking["nb_arretm"] else 0,
            },
            "prices": {
                "price_pmr": parking["tarif_pmr"] if parking["tarif_pmr"] else 0,
                "price_1h": parking["tarif_1h"] if parking["tarif_1h"] else 0,
                "price_2h": parking["tarif_2h"] if parking["tarif_2h"] else 0,
                "price_3h": parking["tarif_3h"] if parking["tarif_3h"] else 0,
                "price_4h": parking["tarif_4h"] if parking["tarif_4h"] else 0,
                "price_24h": parking["tarif_24h"] if parking["tarif_24h"] else 0,
                "price_sub_resident": (
                    parking["abo_resident"] if parking["abo_resident"] else 0
                ),
                "price_sub_no_resident": (
                    parking["abo_non_resident"] if parking["abo_non_resident"] else 0
                ),
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

client.connect(
    "localhost",
    1884,
    60,
)

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
