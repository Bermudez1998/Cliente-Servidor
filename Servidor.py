import socket
import math

server_socket = socket.socket()
server_socket.bind(('localhost',8000))
server_socket.listen(5)

while True:
    conexion, addr = server_socket.accept()
    print "Nueva conexion establecida"
    print addr
    a = conexion.recv(1024)
    conexion.send("Dato recibido")   
    b = conexion.recv(1024)
    conexion.send("Dato recibido")
    suma = str(int(a) + int(b))
    resta = str(int(a) - int(b))
    mult = str(int(a) * int(b))
    if b == "0":
        div = "No se puede dividir por 0"
    else:
        div = str(int(a) / int(b))
    potencia = str(int(a)**(int(b)))
    if ((int(a) > 0) and (int(b)))>1:
        logaritmo = str(math.log(int(a),int(b)))
    else:
        logaritmo = "Operacion invalida, verifique los valores"

    respuesta = str("suma = "+suma+"\n"+"resta = "+resta+"\n"+"mult = "+mult+"\n"+"div = "+div+"\n"+"potencia = "+potencia+"\n"+"logaritmo = "+logaritmo)
    conexion.send(respuesta)
    conexion.close()