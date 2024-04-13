from sympy import nextprime
import socket
import time
from math import gcd

ip = '165.232.161.196'
port = 1303
token = 'vyGHUZR7Sb'

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

input = 2 # Inisialisasi
# Tambahin simple mutex lock biar ga bablas dikirim 1 input doang
has_sent_input = False

while True:
    data = sk.recv(1024 * 100)

    # Ambil 10 pasangan ciphertext dan plaintext
    if len(cm_pairs) < 20:
        if b'Masukkan perintah:' in data:
            sk.send(b'1\n')
        elif b'Masukkan nomor arsip (dalam bentuk integer):' in data and not has_sent_input:
            sk.send(str(input).encode() + b'\n')
            has_sent_input = True
        elif b'Masukkan isi arsip:' in data:
            # print("Sedang mengirim input {}".format(input))
            sk.send(b'Hai\n')
        elif b'Token akses nomor arsip:' in data:
            # print("Mau parsing token arsip")
            # Parse output
            token = data.decode().split(': ')[1].strip()
            # print('Untuk input {}, token = {}'.format(input, token))
            cm_pairs.append([input, int(token)])
            # print("Selesai untuk input {}".format(input))
            has_sent_input = False
            input += 1
        elif error_message in data:
            print('Terjadi kesalahan')
            break
    else:
        print('Selesai mengambil 20 pasangan ciphertext dan plaintext')
        break

print("Isi cm_pairs saat ini: {}".format(cm_pairs))

# Cari nilai e dengan cara bruteforce dari 2^15 sampai 2^16
gcd_options = []
for e in range(2**15, 2**16):
    # Alasan kenapa e harus ganjil adalah karena harus koprima dengan phi (hasil kali (p-1)(q-1))
    # Karena p dan q adalah bilangan prima, maka p-1 dan q-1 adalah bilangan genap
    # Maka dari itu, phi adalah bilangan genap, sehingga e harus ganjil
    if e % 2 == 0:
        continue

    calculation_results = [] # Berisikan selisih antara C dengan M^e

    for cm_pair in cm_pairs:
        c = cm_pair[1]
        m = cm_pair[0]
        calculation_results.append(c - m**e)
    
    gcd_val = calculation_results[0]
    for result in calculation_results:
        gcd_val = gcd(gcd_val, result)
    
    if gcd_val != 1:
        gcd_options.append([e, gcd_val])

print("Hasil perhitungan (Kemungkinan Nilai N):")
print(gcd_options)

# Ambil nilai nomor arsip admin
nomor_admin = 0
sk.send(b'3\n')

while True:
    data = sk.recv(1024 * 100)

    if b'Nomor arsip admin:' in data:
        nomor_admin = int(data.decode().split(': ')[1].strip())
        break

print("Nomor arsip admin: {}".format(nomor_admin))

# Generate nomor token akses admin
token_admin = pow(nomor_admin, gcd_options[0][0], gcd_options[0][1])

print("Token akses admin: {}".format(token_admin))

# Kirim token akses admin
sk.send(b'2\n')

while True:
    data = sk.recv(1024 * 100)

    if b'Masukkan token akses nomor arsip (dalam bentuk integer):' in data:
        sk.send(str(token_admin).encode() + b'\n')
        break

data = sk.recv(1024 * 100)
print(data.decode())
