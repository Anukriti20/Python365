import socket                 
s=socket.socket()             
print('Socket Created')        
s.bind(('localhost',9999)) 
s.listen(3)
print('waiting for connections')
while True:
    c, addr = s.accept
    print("Connected with",addr)
    c.send(bytes('Welcome to CCN project','utf-8'))
    c.close()