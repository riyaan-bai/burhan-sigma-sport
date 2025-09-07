Tautan menuju aplikasi PWS yang sudah di deploy: 
https://riyaan-baihaqi-burhansigmasport.pbp.cs.ui.ac.id/

1. Untuk memenuhi checklist, saya memulai dengan persiapan direktori dan inisialisasi lingkungan virtual. Langkah ini bertujuan untuk mengisolasi dependensi proyek. Selanjutnya, semua dependensi yang dibutuhkan oleh proyek diinstal dan melakukan konfigurasi awal dilakukan pada file settings.py, termasuk penyesuaian basis data yang akan menggunakan SQLite untuk pengembangan lokal dan PostgreSQL untuk produksi, serta pengaturan ALLOWED_HOSTS untuk keamanan. Untuk memverifikasi bahwa konfigurasi awal telah berhasil, saya pun menjalankan server pengembangan lokal.

Setelah struktur proyek dasar terbentuk, sebuah aplikasi baru bernama main dibuat di dalam proyek. Kemudian, aplikasi tersebut dimuat ke dalam daftar INSTALLED_APPS pada file settings.py agar dapat dikenali dan diintegrasikan dengan proyek Django secara keseluruhan. Selanjutnya pada file models.py di dalam aplikasi main, sebuah model data bernama Product didefinisikan untuk merepresentasikan struktur tabel produk dalam basis data dan memiliki atribut-atribut sebagai berikut:
•	name: CharField, untuk menyimpan nama produk.
•	price: IntegerField, untuk menyimpan harga produk.
•	description: TextField, untuk deskripsi detail produk.
•	thumbnail: URLField, untuk menyimpan tautan gambar produk.
•	category: CharField, untuk mengkategorikan produk.
•	is_featured: BooleanField, untuk menandai apakah produk tersebut unggulan atau tidak.

Setelah model didefinisikan, proses migrasi basis data (makemigrations dan migrate) dijalankan untuk membuat skema tabel yang sesuai di dalam basis data.

Berikutnya, fungsi tampilan (view) dikonfigurasi dalam file views.py pada aplikasi main. Fungsi ini dirancang untuk merender sebuah template HTML dan mengirimkan data konteks yang berisi nama dan kelas pengembang. Selain itu, file template bernama main.html dibuat dan dikustomisasi untuk menampilkan data yang diterima dari view secara dinamis. 

Proses URL routing dilakukan dalam dua tahap untuk menghubungkan permintaan pengguna ke view yang sesuai:
1.	Routing Tingkat Aplikasi: Di dalam direktori aplikasi main, dibuat sebuah file urls.py untuk memetakan sebuah pola URL ke fungsi view yang telah dibuat sebelumnya.
2.	Routing Tingkat Proyek: File urls.py pada direktori utama proyek dimodifikasi untuk mengarahkan (include) semua permintaan dengan awalan path tertentu ke file urls.py milik aplikasi main.

Setelah semua fungsionalitas terverifikasi secara lokal, kode sumber proyek diunggah ke repositori GitHub dan selanjutnya di-deploy ke Pacil Web Service (PWS). Proses ini membuat aplikasi dapat diakses secara publik melalui internet oleh pengguna lain.

2. Bagan request client tercantum pada link berikut.
https://www.canva.com/design/DAGyS8boMRM/VHdNjEqB7Lo7h95izYr-JA/edit?utm_content=DAGyS8boMRM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
Penjelasan bagan ialah sebagai berikut.
Request client diterima oleh urls.py level proyek sebagai gerbang utama atau distributor yang mengarahkan ke aplikasi yang relevan menggunakan fungsi include(). Jika tidak ada aplikasi yang relevan, Django akan menampilkan Error 404 dan menampilkan page not found kepada client. Di dalam urls.py level aplikasi, pola URL yang lebih spesifik dicocokkan dengan fungsi yang sesuai pada file views.py. Fungsi di views.py kemudian mengeksekusi logika yang diperlukan. Jika logika memerlukan interaksi dengan database, maka view akan berkomunikasi dengan models.py. Models.py berfungsi sebagai jembatan ke database yang menerjemahkan permintaan dari view menjadi quary untuk mengambil atau memanipulasi data. Setelah mendapatkan data yang dibutuhkan, view akan memuat sebuah berkas .html dan memasukkan data tersebut ke dalamnya. Template ini akan dirender menjadi halaman HTML utuh dan dikemas sebagai respons dan dikirim kembali ke browser client.

3. File settings.py berfungsi sebagai pusat kendali keseluruhan proyek Django. Di dalam file ini semua konfigurasi fundamental dilakukan, seperti mendaftarkan aplikasi main ke dalam INSTALLED_APPS agar dikenali oleh proyek, mengatur koneksi ke basis data yang akan digunakan (baik SQLite untuk pengembangan maupun PostgreSQL untuk deployment di PWS), dan sebagainya. Selain itu, settings.py juga digunakan untuk mengelola pengaturan keamanan seperti SECRET_KEY dan ALLOWED_HOSTS dan mendefinisikan lokasi file template dan file statis. File ini juga adalah peta konfigurasi yang menghubungkan semua komponen, mulai dari aplikasi, model, basis data, hingga URL agar dapat bekerja sama secara harmonis sebagai satu kesatuan aplikasi web.

4. Cara kerja migrasi database di Django melalui proses dua langkah yang terotomatisasi untuk sinkronisasi perubahan pada file models.py dengan struktur database. Pertama, perintah makemigrations akan memindai model untuk mendeteksi perubahan, lalu membuat sebuah "blueprint" atau yang berisi instruksi perubahan tanpa menyentuh database. Selanjutnya, perintah migrate akan membaca "blueprint" lalu menerjemahkannya menjadi perintah SQL dan mengeksekusinya untuk mengubah struktur tabel di dalam database. Sistem ini pada berfungsi sebagai version control untuk skema databas dan memastikan perubahan dapat dilacak serta diterapkan secara konsisten di lingkungan pengembangan maupun produksi.

5. Django menjadi titik awal pembelajaran perangkat lunak karena telah menyediakan hal-hal yang dibutuhkan untuk membuat website, seperti sistem untuk mengelola database tanpa perlu menulis kode SQL yang rumit, panel admin otomatis untuk mengelola data, dan sistem login pengguna yang siap pakai. Hal ini membuat pengguna bisa berfokus pada logika utama aplikasi dan dapat melihat hasil yang instan. Selain itu, Django punya struktur yang rapi sehingga aplikasi menjadi lebih yang terorganisir, aman, dan mudah dikembangkan di kemudian hari.

6. Menurut saya, penjelasan yang diberikan sudah sangat jelas dan sangat membantu. Terima kasih kakak-kakak asisten dosen yang telah menyusun tutorial ini.
