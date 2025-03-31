import socket
import time # for delay

s = socket.socket()
# TODO: replace niagaracomputing.org with the external IP address of your server
target = '34.138.137.239'
s.connect((target, 80)) # recall 80 is the required http port #

# TODO: change the text below to use the http request command/verb to get a
# web page
http_verb1 = 'GET'

request1 = http_verb1 + ' / HTTP/1.0\r\n'

# TODO, uncomment and finish the code below to encode and send the request
s.sendall(request1.encode())

# TODO: modify the string below to represent the only required header field.
http_verb2 = 'HOST'

# TODO, modify string below so that it is carriage return + newline + carriage
# return + newline
newlines = '\r\n\r\n'

request2 = http_verb2 + ': ' + target + newlines
s.sendall(request2.encode())

response = s.recv(2048)
print(response.decode())
print('complete')
s.close()