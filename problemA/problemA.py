import socket
from decrypt import *

ip = '165.232.161.196'
port = 4020
token = 'vyGHUZR7Sb'

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect((ip, port))
sk.send(token.encode() + b'\n')

paket_soal = ''
n = 0
e = 0
c = 0
jawaban = ''

while(True):
    data = sk.recv(1024 * 100)
    if b'Tahap-' in data:
        # Reset
        jawaban = ''
        paket_soal = ''
        n = 0
        e = 0
        c = 0
        print(data.decode())

    # Parse input
    if b'paket_soal =' in data:
        words = data.decode().split('\n')
        for word in words:
            if 'paket_soal' in word:
                paket_soal = word.split('=')[1].strip()

    if b'n =' in data and b'Jawaban' not in data:
        words = data.decode().split('\n')
        for word in words:
            if 'n =' in word:
                n = int(word.split('=')[1].strip())

    if b'e =' in data:
        words = data.decode().split('\n')
        for word in words:
            if 'e =' in word:
                e = int(word.split('=')[1].strip())

    if b'c =' in data:
        words = data.decode().split('\n')
        for word in words:
            if 'c =' in word:
                c = int(word.split('=')[1].strip())

    if (paket_soal != '' and n != 0 and e != 0 and c != 0):
        # Decryption
        match paket_soal:
            case 'A':
                jawaban = decryptA(n, e, c)
            case 'B':
                jawaban = decryptB(n, e, c)
                print("jawaban = ", jawaban)
            case 'C':
                jawaban = decryptC(n, e, c)
                print("jawaban = ", jawaban)
            case 'D':
                jawaban = decryptD(n, e, c)
                print("jawaban = ", jawaban)
            case 'E':
                jawaban = decryptE(n, e, c)
                print("jawaban = ", jawaban)
        
    if b'Jawaban' in data:
        # break
        if (jawaban != ''):
            sk.send(jawaban)
