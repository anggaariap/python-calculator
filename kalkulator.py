# header
print('=' * 50) #angka 50 hanya permisalan dalam satu baris
print('Program kalkulator sederhana'.center(50))
print('=' * 50)

# inputan nilai
a = int(input('masukan angka pertama : ')) #fungsi int untuk mengkonversi nilai input dari string ke integer
b = int(input('masukan angka kedua : '))

# proses aritmatika
penjumlahan = a + b
pengurangan = a - b
perkalian = a * b
pembagian = a / b
modulus = a % b


# menampilkan hasil
print(f'{a} + {b} = {penjumlahan}')
print(f'{a} - {b} = {pengurangan}')
print(f'{a} * {b} = {perkalian}')
print(f'{a} / {b} = {pembagian}')
print(f'{a} % {b} = {modulus}')
