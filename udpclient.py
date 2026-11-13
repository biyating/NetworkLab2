from socket import *
serverName = '127.0.0.1'
serverPort = 5201
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input( ' 请输入小写字母： ')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print("收到服务器返回:", modifiedMessage.decode())
clientSocket.close()