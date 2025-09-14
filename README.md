
# Sistem Manajemen Proyek Digital

Program ini digunakan untuk menentukan apakah sebuah ide bisnis layak untuk dijalankan. Dalam konteks freelance digital, program ini bisa menjadi alat pribadi seorang freelancer untuk menilai apakah sebuah proyek tertentu memiliki potensi keuntungan berdasarkan estimasi biaya dan tingkat kesulitannya.

## Flowchart

![Flowchart](https://github.com/sitinursinta044-design/Mini_project_1_DDP/blob/main/file/flowchart.jpg)

Penjelasan : 
1. START
Flowchart dimulai dari simbol Start untuk menandai awal program dimulai.

2. Sistem Input
Program meminta pengguna untuk menginputkan nama proyek, harga, dan tingkat kesulitan untuk 3 proyek.

Data ini disimpan ke dalam list:
- nama_proyek
- harga_proyek
- kesulitan_proyek

Tujuannya adalah untuk menyimpan data agar bisa diakses kembali menggunakan index list.

3. Inisialisasi Variabel

Variabel rekomendasi = -1, artinya belum ada proyek yang direkomendasikan.

Variabel harga_tertinggi = 0, nantinya digunakan untuk membandingkan harga agar selalu memilih proyek dengan harga tertinggi setelah melewati logika seleksi tingkat kesulitan.

4. Penerapan Conditional Statement (Logika penentuan rekomendasi proyek)

Untuk setiap proyek (0, 1, 2), dilakukan percabangan (if – elif – else) sesuai kriteria:

- Mudah, harga minimal 1 juta
- Sedang, harga minimal 2 juta
- Sulit, harga minimal 3 juta
- Jika ketiga proyek memenuhi syarat harga minimal, ambil harga tertinggi

Jika proyek memenuhi syarat, program akan mengecek:
- Apakah harga proyek lebih tinggi dari harga_tertinggi?
Jika iya, update rekomendasi dengan index proyek tersebut dan simpan harga_tertinggi.
Jika tidak, abaikan dan lanjut ke proses berikutnya.

Conditional statement disini digunakan berlapis (nested if) untuk mengecek kondisi tingkat kesulitan dan batas harga untuk setiap proyek.
Hasil akhirnya, variabel rekomendasi akan berisi angka sebagai index untuk menunjuk proyek mana dari tuple data proyek yang merupakan proyek rekomendasi. Jika semua proyek tidak memenuhi kriteria, maka variabel rekomendasi akan tetap berisi -1.

5. Menentukan Hasil

Setelah memproses data proyek, program mengevaluasi nilai rekomendasi:
- Jika rekomendasi != -1, artinya ada proyek yang valid dan dipilih.
- Hasil rekomendasi ditampilkan dengan mengambil data dari list:
nama_proyek[rekomendasi], harga_proyek[rekomendasi], kesulitan_proyek[rekomendasi].
- Data hasil rekomendasi ini juga disimpan dalam tuple berikut :
    `hasil = (nama_proyek[rekomendasi], harga_proyek[rekomendasi], kesulitan_proyek[rekomendasi])`
- Jika rekomendasi masih -1, artinya tidak ada proyek yang valid, dan progrm akan menampilkan pesan “Tidak ada proyek yang memenuhi kriteria.”

## Screenshot Hasil Program

Program ini memiliki sistem input yang dapat digunakan pengguna untuk menginput data nama proyek, estimasi harga, dan tingkat kesulitan (CREATE), menyimpannya dalam list, kemudian menampilkan data hasil input. Data tersebut akan melewati logika penentuan rekomendasi menggunakan conditional statement dan menyimpan hasilnya dalam tuple. hasil rekomendasi akan ditampilkan sebagai output (READ). 

Screenshot alur program keseluruhan : 

![Screenshot alur program keseluruhan](https://github.com/sitinursinta044-design/Mini_project_1_DDP/blob/main/file/input.png)

Berikut adalah hasil pengujian output program berdasarkan variasi input yang diberikan untuk menguji semua kondisi : 

1. Output kondisi 1
   
Kondisi 1 menggunakan input : 
- Jasa Copywriting, 1500000, mudah
- Jasa Desain Infografis, 1000000, sedang
- Jasa Pengelola Media Sosial, 2000000, sulit
Screenshot Output : 

![Screenshot alur program keseluruhan](https://github.com/sitinursinta044-design/Mini_project_1_DDP/blob/main/file/output_case_1.png)

Keterangan : 
Rekomendasinya adalah Copywriting, masuk dalam kriteria yaitu (mudah, harga 1.5 jt ≥ 1 jt).

2. Output kondisi 2
   
Kondisi 2 menggunakan input : 
- Jasa Copywriting, 1000000, mudah
- Jasa Desain Infografis, 2500000, sedang
- Jasa Pengelola Media Sosial, 2000000, sulit
Screenshot Output : 

![Screenshot alur program keseluruhan](https://github.com/sitinursinta044-design/Mini_project_1_DDP/blob/main/file/output_case_2.png)

Keterangan : 
Rekomendasinya adalah Desain Infografis, masuk dalam kriteria yaitu (sedang, harga 2.5 jt ≥ 2 jt). dan merupakan proyek dengan estimasi harga tertinggi.

3. Output kondisi 3
   
Kondisi 3 menggunakan input : 
- Jasa Copywriting, 1000000, mudah
- Jasa Desain Infografis, 2000000, sedang
- Jasa Pengelola Media Sosial, 4000000, sulit
Screenshot Output : 

![Screenshot alur program keseluruhan](https://github.com/sitinursinta044-design/Mini_project_1_DDP/blob/main/file/output_case_3.png)

Keterangan : 
Rekomendasinya adalah Pengelola Media Sosial, masuk dalam kriteria yaitu (sulit, harga 4 jt ≥ 3 jt). meskipun tergolong sulit, namun melebihi harga minimum dan juga merupakan proyek dengan estimasi harga tertinggi.

4. Output kondisi 4
   
Kondisi 3 menggunakan input : 
- Jasa Copywriting, 1000000, mudah
- Jasa Desain Infografis, 2000000, sedang
- Jasa Pengelola Media Sosial, 4000000, sulit
Screenshot Output : 

![Screenshot alur program keseluruhan](https://github.com/sitinursinta044-design/Mini_project_1_DDP/blob/main/file/output_case_4.png)

Keterangan : 
Rekomendasinya adalah Pengelola Media Sosial, masuk dalam kriteria yaitu (sulit, harga 4 jt ≥ 3 jt). meskipun tergolong sulit, namun melebihi harga minimum dan juga merupakan proyek dengan estimasi harga tertinggi.

