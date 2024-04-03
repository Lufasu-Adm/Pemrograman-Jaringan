
## Client – Server (Single Thread)

TUGAS DAN LATIHAN PRAKTIKUM


##

Membuat laporan percobaan praktikum dan beri Analisa Hasil Percobaan tadi yang 
sudah dibuat Pembuatan Aplikasi Client-Server Sederhana (Single Thread)



## Praktikum


## Server
Dalam percobaan ini, server menunggu koneksi dari client dan membaca data yang 
dikirimkan oleh client. Server kemudian mengirim balasan ke client dan menutup 
koneksi. Client mengirimkan pesan ke server dan menunggu balasan dari server. 
Setelah menerima balasan dari server, koneksi ditutup. Ini adalah contoh sederhana 
dari aplikasi client-server dengan model single-threaded, di mana server hanya 
mampu melayani satu koneksi pada suatu waktu. Jika terdapat lebih dari satu koneksi 
yang masuk, maka koneksi tersebut akan diantre dan dilayani secara berurutan.

Server dibuat dengan menggunakan modul socket di Python. Server ini diatur 
untuk mendengarkan koneksi yang masuk dari klien pada alamat IP ‘localhost’ 
dan port 12345. Setelah server menerima koneksi dari klien, membaca data 
yang dikirim oleh klien. Data ini diasumsikan sebagai angka yang dikirim dalam 
format string, yang kemudian didekode dan dikonversi menjadi integer.
Server kemudian memeriksa apakah angka tersebut genap atau ganjil dan 
membuat respons yang sesuai. Respons ini kemudian dikodekan kembali 
menjadi string dan dikirim kembali ke klien. Setelah itu, soket klien dan server 
ditutup.

[![LINK PRAKTIKUM]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Minggu%202/Client%20%E2%80%93%20Server%20(Single%20Thread)/Praktikum%202/Server)

## Client

Klien dibuat dengan menggunakan modul socket di Python. Klien ini diatur untuk 
terhubung ke server pada alamat IP ‘localhost’ dan port 12345. Setelah klien 
terhubung ke server, i mengirimkan pesan ke server. Pesan ini adalah inputan
dari pengguna yang diasumsikan sebagai angka. Klien kemudian menunggu dan 
menerima balasan dari server. Balasan ini adalah penentuan apakah angka 
tersebut genap atau ganjil. Setelah menerima balasan dari server, klien 
menampilkan balasan tersebut dan menutup koneksi.

[![LINK PRAKTIKUM]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Minggu%202/Client%20%E2%80%93%20Server%20(Single%20Thread)/Praktikum%202/Client)


##


## Tugas
Membuat sebuah program server yang dapat menerima koneksi dari klien 
menggunakan protokol TCP. Server ini akan menerima pesan dari klien dan 
mengirimkan pesan balasan berisi jumlah karakter pada pesan tersebut. Gunakan port 
12345 untuk server. 

## Server
Server dibuat dengan menggunakan modul socket di Python. Server ini diatur untuk 
mendengarkan koneksi yang masuk dari klien pada alamat IP ‘localhost’ dan port 12345.
Setelah server menerima koneksi dari klien, ia membaca data yang dikirim oleh klien. Data 
ini adalah pesan yang dikirim dalam format string. Server kemudian membuat respons yang 
berisi pesan tersebut dan jumlah karakter dalam pesan tersebut. Respons ini kemudian 
dikodekan kembali menjadi string dan dikirim kembali ke klien. Setelah itu, soket klien dan 
server ditutup

[![LINK Tugas]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Minggu%202/Client%20%E2%80%93%20Server%20(Single%20Thread)/Praktikum%202/Tugas/Server)

## Client
Klien dibuat dengan menggunakan modul socket di Python. Klien ini diatur untuk terhubung 
ke server pada alamat IP ‘localhost’ dan port 12345. Setelah klien terhubung ke server, ia 
mengirimkan pesan ke server. Pesan ini adalah inputan dari pengguna dalam format string.
Klien kemudian menunggu dan menerima balasan dari server. Balasan ini adalah jumlah 
karakter dalam pesan tersebut. Setelah menerima balasan dari server, klien menampilkan 
balasan tersebut dan menutup koneksi

[![LINK Tugas]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Minggu%202/Client%20%E2%80%93%20Server%20(Single%20Thread)/Praktikum%202/Tugas/Client)
##







## Tugas 2 - FTP Socket Programming On python

##

## pendahuluan
Dokumen ini akan menjelaskan sebuah program file transfer protocol menggunakan 
socket programming dengan beberapa perintah dari client

##

## Server
[![LINK code server.py]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Tugas%202%20-%20FTP%20Socket%20Programming%20On%20python/client.py)

memungkinkan server untuk menerima perintah dari klien, memprosesnya, dan mengirimkan 
respons atau data yang sesuai kembali ke klien. Ini bisa digunakan sebagai dasar untuk 
sistem penyimpanan file jarak jauh atau aplikasi berbagi file.

## Command
* Menerima perintah seperti ls, rm, download, upload, size, conme,dan byebye ke server.
* Melakukan operasi seperti menampilkan daftar file, menghapus file, mendapatkan ukuran file, mengunduh file, dan     
  mengunggah file.
* Menangani berbagai jenis kesalahan seperti file tidak ditemukan atau kesalahan saat membaca/menulis file.

## Penggunaan
1. Run server.py
2. Program akan menunggu koneksi dari klien. (Menunggu client mengirimkan perintah conme)
3. Setelah server terhubung
4. Klien dapat mengirim command seperti ls, rm, size, download, upload, dan byebye.
5. Server akan menanggapi perintah tersebut dan menjalankan operasi yang sesuai pada sistem file server.
6. Klien dapat terus berinteraksi dengan server sampai mengirim perintah byebye untuk menutup koneksi.

##

## Client
client bertugas berkomunikasi dengan server untuk mengirim dan menerima file.
Berikut adalah fitur dan cara penggunaan klien
[![LINK code client.py()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Tugas%202%20-%20FTP%20Socket%20Programming%20On%20python/client.py)

## Fitur
* Mengirim command seperti ls, rm, download, upload, size, conme,dan byebye ke server.
* Menerima respons dari server dan menampilkannya kepada pengguna.
* Mengunggah file ke server dan mengunduh file dari server.

## penggunaan
1. Run client.py
2. Program akan berjalan dan menampilkan pesan bahwa klien sedang aktif.
3. Gunakan command connme untuk menghubungkan klien ke server.
4. Masukkan command yang diinginkan, seperti  ls, rm, download, upload, size,dan byebye
5. Klien akan mengirim perintah tersebut ke server dan menampilkan respons yang diterima dari server.
6. Pengguna dapat terus berinteraksi dengan server sampai mengirim perintah byebye untuk menutup koneksi.

##

## Kesimpulan
Ini adalah implementasi dasar dari sistem komunikasi file antara klien dan server melalui protokol TCP. Pengguna dapat berinteraksi dengan server untuk menjalankan tugas-tugas seperti melihat isi direktori, menghapus konten, serta mengirim dan menerima dokumen. Untuk meningkatkan sistem ini, penambahan proteksi data dan mekanisme error handling yang lebih canggih akan sangat bermanfaat.
  




