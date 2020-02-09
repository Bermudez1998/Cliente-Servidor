import socket

client_socket = socket.socket()
client_socket.connect(("localhost",8000))


client_socket.send("10")
respuesta = client_socket.recv(1024)
print (respuesta)

client_socket.send("0")
respuesta = client_socket.recv(1024)
print (respuesta)

respuesta = client_socket.recv(1024)
print (respuesta)

client_socket.close()

