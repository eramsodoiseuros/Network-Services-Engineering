import socket
import sys

from ServerStreamer import ServerStreamer

if __name__ == "__main__":
	try:
		SERVER_PORT = int(sys.argv[1])
	except:
		print("[Usage: Server.py Port]\n")   

	SERVER_ADDR = "10.0.0.10"
	rtspSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	rtspSocket.bind((SERVER_ADDR, SERVER_PORT))
	print(f"Listening on {SERVER_ADDR}: {SERVER_PORT}")
	rtspSocket.listen(5)

	# Receive client info (address,port) through RTSP/TCP session
	while True:
		try:
			clientInfo = {'rtspSocket': rtspSocket.accept()}
			ServerStreamer(clientInfo).run()
		except Exception:
			break

	rtspSocket.close()