# QUIZGAME SERVER
import socket

print("starting derwin's quizgame server")

# receive a UDP packet

s = socket.socket(type=socket.SOCK_DGRAM)
s.bind(('0.0.0.0', 15000))
payload, addr = s.recvfrom(4096)
print('PAYLOAD:', payload.decode())
print('ADDR:', addr)
s.close()




file = open('status.html', 'w')
file.write('QUIZGAME STATUS')
file.close()









print('quizgame server complete')
