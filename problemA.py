import socket

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

while(True):
    data = sk.recv(1024 * 100)
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
                print('n = ', n)
    if b'e =' in data:
        words = data.decode().split('\n')
        for word in words:
            if 'e =' in word:
                e = int(word.split('=')[1].strip())
                print('e = ', e)
    if b'c =' in data:
        words = data.decode().split('\n')
        for word in words:
            if 'c =' in word:
                c = int(word.split('=')[1].strip())
                print('c = ',c)
    # Process the data here
    if b'Jawaban' in data:
        break
    # sk.send(b'1\n')
