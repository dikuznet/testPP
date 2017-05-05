import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(10)
bk=False
while not bk:	
		conn, addr = s.accept()
		while True:
			data = conn.recv(1024)
			if len(data) > 1024 or data==b'close': 
				conn.close()
				bk=True
				break
			if data:
				conn.send(data)
				print(data)
			if not data:
				conn.close()
				break

s.close()				 
