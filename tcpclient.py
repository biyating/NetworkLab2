from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
print("正在尝试连接服务器...")
clientSocket.connect((serverName, serverPort))
sentence = input('请输入小写字母: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('收到服务器返回:', modifiedSentence.decode())
clientSocket.close()