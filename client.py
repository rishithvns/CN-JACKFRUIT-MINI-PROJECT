import socket
import random
import time
import base64
import datetime

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = "10.166.67.186"
port = 9999

device_id = input("Enter Device ID: ")

while True:
    temperature = random.randint(20, 40)
    humidity = random.randint(40, 80)
    battery = random.randint(50, 100)

    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    telemetry = f"{device_id} | {timestamp} | TEMP:{temperature},HUM:{humidity},BAT:{battery}"

    encoded = base64.b64encode(telemetry.encode())

    print("Sending:", telemetry)

    client.sendto(encoded, (server_ip, port))

    data, addr = client.recvfrom(1024)
    print("Server:", data.decode())

    time.sleep(1) 