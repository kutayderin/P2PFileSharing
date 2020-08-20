import socket
import os
import math

s = socket.socket()
s.bind((socket.gethostname(), 8081))
s.listen(1)

print(socket.gethostname())

print('waiting for connections...')
conn, address = s.accept()
print(address, ' connected to server')

while 1:
    print("press 1 for send a file \npress 0 to exit program")
    secim = input()
    if secim == '1':
        wait = input(str('enter the filename: '))

        filename =  wait + '.png'
        c = os.path.getsize(filename)
        CHUNK_SIZE = math.ceil(math.ceil(c) / 2)
        index = 1
        with open(filename, 'rb') as infile:
            chunk = infile.read(int(CHUNK_SIZE))
            while chunk:
                chunkname = wait+ '_' + str(index)
                with open(chunkname, 'wb+') as chunk_file:
                    chunk_file.write(chunk)
                index += 1
                chunk = infile.read(int(CHUNK_SIZE))
        chunk_file.close()

        i = 1
        for x in range(2):
            fname = wait + '_' + str(i)
            fi = open(fname, 'rb')
            f_d = fi.read(51200)
            conn.send(f_d)
            i += 1
        print('file sended')
        continue
    elif secim == '0':
        print('ending program...')
        break
    else:
        print('wrong input')
        continue
