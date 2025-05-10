import socket

# as server
server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(('127.0.0.1', 443)) # ip address and port number
server_sock.listen(1)

conn, addr = server_sock.accept()
# print(conn, addr)
data = conn.recv(1024) # bytes size

server_sock.close()


# as client
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_sock.connect(('127.0.0.1', 443)) # ip address and port number

data = client_sock.recv(1024) # bytes size

client_sock.close()