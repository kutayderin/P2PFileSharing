import socket
import math
import os
import shutil

s = socket.socket()
host = input(str("Please enter the host name of the sender:"))
port = 8081
s.connect((host, port))
print("Connected...")

while 1:
    print("press 1 for download a file \npress 0 to exit program")
    secim = input()
    if secim == '1':
        wait = input(str('enter file name:'))
        i = 1
        for x in range(2):
            fname = wait + '_' + str(i)
            fi = open(fname, 'wb')
            f_d = s.recv(51200)
            fi.write(f_d)
            fi.close()
            i += 1
        chunknames = [wait + '_1', wait + '_2']
        with open(wait + '.png', 'wb') as outfile:
            for chunk in chunknames:
                with open(chunk, "rb") as infile:
                    shutil.copyfileobj(infile, outfile)
        print('file downloaded')
        continue
    elif secim == '0':
        print('ending program...')
        break
    else:
        print('wrong input')
        continue
