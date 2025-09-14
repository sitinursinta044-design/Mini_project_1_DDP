# Nama    : Siti Nursinta
# Nim     : 2509116087
# Kelas   : Information System C 2025
# program : Mini project 1 (Praktikum DDP)
# Tema    : Sistem Manajemen Proyek Digital

print("=== Sistem Manajemen Proyek Digital ===")

nama_proyek = []
harga_proyek = []
kesulitan_proyek = []

print("-----------Input Proyek 1--------------")
input_nama_1 = input("Masukkan nama proyek 1: ")
input_harga_1 = float(input("Masukkan harga proyek 1: "))
input_kesulitan_1 = input("Masukkan tingkat kesulitan proyek 1 (mudah/sedang/sulit): ")
print("-----------Input Proyek 2--------------")
input_nama_2 = input("Masukkan nama proyek 2: ")
input_harga_2 = float(input("Masukkan harga proyek 2: "))
input_kesulitan_2 = input("Masukkan tingkat kesulitan proyek 2 (mudah/sedang/sulit): ")
print("-----------Input Proyek 3--------------")
input_nama_3 = input("Masukkan nama proyek 3: ")
input_harga_3 = float(input("Masukkan harga proyek 3: "))
input_kesulitan_3 = input("Masukkan tingkat kesulitan proyek 3 (mudah/sedang/sulit): ")

nama_proyek.append(input_nama_1)
harga_proyek.append(input_harga_1)
kesulitan_proyek.append(input_kesulitan_1)
nama_proyek.append(input_nama_2)
harga_proyek.append(input_harga_2)
kesulitan_proyek.append(input_kesulitan_2)
nama_proyek.append(input_nama_3)
harga_proyek.append(input_harga_3)
kesulitan_proyek.append(input_kesulitan_3)

print("")
print("===================== List Proyek =====================")
print("No | Nama Proyek | Estimasi Harga | Tingkat Kesulitan")
print("=======================================================")
print("1. |", nama_proyek[0], "|", harga_proyek[0], "|", kesulitan_proyek[0])
print("2. |", nama_proyek[1], "|", harga_proyek[1], "|", kesulitan_proyek[1])
print("3. |", nama_proyek[2], "|", harga_proyek[2], "|", kesulitan_proyek[2])
print("=======================================================")

rekomendasi = -1
harga_tertinggi = 0

if kesulitan_proyek[0] == "mudah":
    if harga_proyek[0] >= 1000000:
        if harga_proyek[0] > harga_tertinggi:
            rekomendasi = 0
            harga_tertinggi = harga_proyek[0]
elif kesulitan_proyek[0] == "sedang":
    if harga_proyek[0] >= 2000000:
        if harga_proyek[0] > harga_tertinggi:
            rekomendasi = 0
            harga_tertinggi = harga_proyek[0]
elif kesulitan_proyek[0] == "sulit":
    if harga_proyek[0] >= 3000000:
        if harga_proyek[0] > harga_tertinggi:
            rekomendasi = 0
            harga_tertinggi = harga_proyek[0]

if kesulitan_proyek[1] == "mudah":
    if harga_proyek[1] >= 1000000:
        if harga_proyek[1] > harga_tertinggi:
            rekomendasi = 1
            harga_tertinggi = harga_proyek[1]
elif kesulitan_proyek[1] == "sedang":
    if harga_proyek[1] >= 2000000:
        if harga_proyek[1] > harga_tertinggi:
            rekomendasi = 1
            harga_tertinggi = harga_proyek[1]
elif kesulitan_proyek[1] == "sulit":
    if harga_proyek[1] >= 3000000:
        if harga_proyek[1] > harga_tertinggi:
            rekomendasi = 1
            harga_tertinggi = harga_proyek[1]

if kesulitan_proyek[2] == "mudah":
    if harga_proyek[2] >= 1000000:
        if harga_proyek[2] > harga_tertinggi:
            rekomendasi = 2
            harga_tertinggi = harga_proyek[2]
elif kesulitan_proyek[2] == "sedang":
    if harga_proyek[2] >= 2000000:
        if harga_proyek[2] > harga_tertinggi:
            rekomendasi = 2
            harga_tertinggi = harga_proyek[2]
elif kesulitan_proyek[2] == "sulit":
    if harga_proyek[2] >= 3000000:
        if harga_proyek[2] > harga_tertinggi:
            rekomendasi = 2
            harga_tertinggi = harga_proyek[2]

hasil = (nama_proyek[rekomendasi], harga_proyek[rekomendasi], kesulitan_proyek[rekomendasi]) 

print("")
print("Hasil Rekomendasi Proyek : ")
if rekomendasi != -1:
    print("Nama Proyek       :", hasil[0])
    print("Estimasi Harga    :", hasil[1])
    print("Tingkat Kesulitan :", hasil[2])
else:
    print("Tidak ada proyek yang memenuhi kriteria.")

