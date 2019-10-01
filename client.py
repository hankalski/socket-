import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))
address, port = s.getpeername()
msg = s.recv(1024)
print(msg.decode("utf-8"))

saveFile = open(f'{address}_{port}.txt','w')


saveFile.write(msg.decode("utf-8"))


saveFile.close()
