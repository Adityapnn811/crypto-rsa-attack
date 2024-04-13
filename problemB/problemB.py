from sympy import nextprime
import socket
import sys, time

ip = '165.232.161.196'
port = 1303
token = 'vyGHUZR7Sb'

max_wait_time = 10 # dalam detik
error_message = b'Terjadi kesalahan'

# Butuh paling tidak (hipotesis) 10 pasangan ciphertext dan plaintext untuk memastikan jawabannya benar
# Plaintext dimulai dari 2 sampai 11 (1 tidak dimasukkan karena 1 pangkat apa pun adalah 1 dan 1 modulus apa pun tetap 1)
cm_pairs = []

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect((ip, port))
data = sk.recv(1024 * 100)

while b'Masukkan token terlebih dahulu!' not in data:
    time.sleep(0.001)

sk.send(token.encode() + b'\n')


while True:
    data = sk.recv(1024 * 100)

    # Ambil 10 pasangan ciphertext dan plaintext
    input = 2 # Inisialisasi
    # print(data.decode()) # Debugging
    if len(cm_pairs) < 10:
        if b'Masukkan perintah:' in data:
            sk.send(b'1\n')
        elif b'Masukkan nomor arsip (dalam bentuk integer):' in data:
            sk.send(str(input).encode() + b'\n')
        elif b'Masukkan isi arsip:' in data:
            sk.send(b'Hai\n')
        elif b'Token akses nomor arsip:' in data:
            print("Mau parsing token arsip")
            # Parse output
            token = data.decode().split(': ')[1].strip()
            print('Untuk input {}, token = {}'.format(input, token))
            cm_pairs.append([input, int(token)])
            print("Selesai untuk input {}".format(input))
            input += 1
        elif error_message in data:
            print('Terjadi kesalahan')
            break
    else:
        print('Selesai mengambil 10 pasangan ciphertext dan plaintext')
        break