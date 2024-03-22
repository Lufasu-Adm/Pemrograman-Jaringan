
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
##

## Client

Klien dibuat dengan menggunakan modul socket di Python. Klien ini diatur untuk 
terhubung ke server pada alamat IP ‘localhost’ dan port 12345. Setelah klien 
terhubung ke server, i mengirimkan pesan ke server. Pesan ini adalah inputan
dari pengguna yang diasumsikan sebagai angka. Klien kemudian menunggu dan 
menerima balasan dari server. Balasan ini adalah penentuan apakah angka 
tersebut genap atau ganjil. Setelah menerima balasan dari server, klien 
menampilkan balasan tersebut dan menutup koneksi.

[![LINK PRAKTIKUM]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Minggu%202/Client%20%E2%80%93%20Server%20(Single%20Thread)/Praktikum%202/Client)



## Tugas
Membuat sebuah program server yang dapat menerima koneksi dari klien 
menggunakan protokol TCP. Server ini akan menerima pesan dari klien dan 
mengirimkan pesan balasan berisi jumlah karakter pada pesan tersebut. Gunakan port 
12345 untuk server. 
##

## Server
Server dibuat dengan menggunakan modul socket di Python. Server ini diatur untuk 
mendengarkan koneksi yang masuk dari klien pada alamat IP ‘localhost’ dan port 12345.
Setelah server menerima koneksi dari klien, ia membaca data yang dikirim oleh klien. Data 
ini adalah pesan yang dikirim dalam format string. Server kemudian membuat respons yang 
berisi pesan tersebut dan jumlah karakter dalam pesan tersebut. Respons ini kemudian 
dikodekan kembali menjadi string dan dikirim kembali ke klien. Setelah itu, soket klien dan 
server ditutup

[![LINK Tugas]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Minggu%202/Client%20%E2%80%93%20Server%20(Single%20Thread)/Praktikum%202/Tugas/Server)
##

## Client
Klien dibuat dengan menggunakan modul socket di Python. Klien ini diatur untuk terhubung 
ke server pada alamat IP ‘localhost’ dan port 12345. Setelah klien terhubung ke server, ia 
mengirimkan pesan ke server. Pesan ini adalah inputan dari pengguna dalam format string.
Klien kemudian menunggu dan menerima balasan dari server. Balasan ini adalah jumlah 
karakter dalam pesan tersebut. Setelah menerima balasan dari server, klien menampilkan 
balasan tersebut dan menutup koneksi

[![LINK Tugas]()](https://github.com/Lufasu-Adm/Pemrograman-Jaringan/blob/main/Minggu%202/Client%20%E2%80%93%20Server%20(Single%20Thread)/Praktikum%202/Tugas/Client)
##






