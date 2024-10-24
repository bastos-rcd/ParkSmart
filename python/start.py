import subprocess
import time

save = subprocess.Popen(["python3", "save.py"])

time.sleep(1)

calculate = subprocess.Popen(["python3", "calculate.py"])

time.sleep(1)

simulation = subprocess.Popen(["python3", "simulation.py"])

while True:
    if save.poll() is not None:
        calculate.terminate()
        simulation.terminate()
        break

    if calculate.poll() is not None:
        save.terminate()
        simulation.terminate()
        break

    if simulation.poll() is not None:
        save.terminate()
        calculate.terminate()
        break
