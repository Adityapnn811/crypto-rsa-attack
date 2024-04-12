from sympy import nextprime
import socket
import sys, time

ip = '165.232.161.196'
port = 1303
token = 'vyGHUZR7Sb'

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect((ip, port))
data = sk.recv(1024 * 100)

while b'Masukkan token terlebih dahulu!' not in data:
    time.sleep(0.001)

sk.send(token.encode() + b'\n')

max_wait_time = 10 # dalam detik
error_message = b'Terjadi kesalahan'

# Butuh paling tidak (hipotesis) 10 pasangan ciphertext dan plaintext untuk memastikan jawabannya benar
# Plaintext dimulai dari 2 sampai 11 (1 tidak dimasukkan karena 1 pangkat apa pun adalah 1 dan 1 modulus apa pun tetap 1)
cm_pairs = []

while True:
    data = sk.recv(1024 * 100)

    # Ambil 10 pasangan ciphertext dan plaintext
    input = 2 # Inisialisasi
    try:
        while len(cm_pairs) < 10:
            print("baru sampai sini")
            print(data)

            while b'Masukkan perintah:' not in data:
                time.sleep(0.001)

            print("Mau masukin input perintah 1")
            sk.send(b'1\n')
            data = sk.recv(1024 * 100)

            while b'Masukkan token akses nomor arsip (dalam bentuk integer):' not in data:
                time.sleep(0.001)
            
            print("Mau masukin token arsip {}".format(input))
            sk.send(b'{}\n'.format(input))
            data = sk.recv(1024 * 100)

            while b'Masukkan isi arsip:' not in data:
                time.sleep(0.001)
            
            print("Mau masukin isi arsip Hai")
            sk.send(b'Hai\n') # Ga penting, yang penting ga kosong
            data = sk.recv(1024 * 1000)

            while b'Token akses nomor arsip:' not in data:
                time.sleep(0.001)
            
            print("Mau parsing token arsip")
            # Parse output
            token = data.decode().split(': ')[1].strip()
            print('Untuk input {}, token = {}'.format(input, token))
            cm_pairs.append([input, int(token)])
            print("Selesai untuk input {}".format(input))
            input += 1

    except error_message in data:
        print('Terjadi kesalahan')
        break
    
    print("SELESAI")