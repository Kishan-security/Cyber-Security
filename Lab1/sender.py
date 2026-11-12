
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("RECEIVER_IP", 5000))

print("Connected to receiver!")

while True:
    message = input("Sender: ")

    client.send(message.encode())

    if message.lower() == "exit":
        break

    data = client.recv(1024).decode()

    print("Receiver:", data)

    if data.lower() == "exit":
        break

client.close()
