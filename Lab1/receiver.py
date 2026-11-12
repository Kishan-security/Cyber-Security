
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 5000))

server.listen(1)

print("Waiting for sender...")

conn, addr = server.accept()

print("Connected with:", addr)

while True:
    data = conn.recv(1024).decode()

    if data.lower() == "exit":
        break

    print("Sender:", data)

    reply = input("Receiver: ")

    conn.send(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server.close()
