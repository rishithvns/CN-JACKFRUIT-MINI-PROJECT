import socket
import base64
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("0.0.0.0", 9999))

print("=== Telemetry Server Started ===")
print("Waiting for telemetry data...\n")

packet_count = 0
start_time = time.time()

while True:
    data, addr = server.recvfrom(1024)
    packet_count += 1

    try:
        decoded = base64.b64decode(data).decode()
    except:
        print("Invalid data from", addr)
        continue

    print(f"[{packet_count}] From {addr} → {decoded}")

    if packet_count % 5 == 0:
        elapsed = time.time() - start_time
        print("\n--- Performance Stats ---")
        print("Packets:", packet_count)
        print("Time:", round(elapsed, 2), "sec")
        print("Throughput:", round(packet_count / elapsed, 2), "packets/sec")
        print("-------------------------\n")

    server.sendto(b"ACK", addr)