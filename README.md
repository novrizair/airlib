# Novrizal Airsyahputra (2206081780) PBP-A
---

Tautan menuju Adaptable: 

---

**1. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).**

JAWAB: Berikut merupakan cara saya dalam mengimplementasikan _checklist_ di atas:

a) Setelah membuat _dependencies_ dalam berkas requirements.txt dan menjalankan _environment_,  waktunya membuat sebuah proyek Django baru yang bernama airlib. Perintah yang ditulis pada cmd adalah: **django-admin startproject airlib .** (gunakan . )

b) Kemudian, buat aplikasi yang bernama "main" pada proyek, dengan cara perintah: **python manage.py startapp main**. Tak lupa, setelah itu, buka _file_ settings.py dalam direktori proyek airlib dan tambahkan code 'main' ke dalam variabel INSTALLED_APPS.

C) Selanjutnya, routing proyek dilakukan agar aplikasi main dapat dijalankan. Jadi, rute URL akan ditambahkan ke dalam urls.py proyek yang bertanggung jawab untuk mengatur rute URL proyek. Lakukan sedikit perubahan pada _file_ urls.py, yaitu dengan: **from django.urls import path, include**. Fungsi _include_ ini berguna untuk mengimpor rute URL dari aplikasi main ke dalam _file_ urls.py proyek. Selain itu, tambahkan juga: **path('main/', include('main.urls'))** ke dalam variabel urlpatterns. Jadi, path URL 'main/' selanjutnya diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main.

d) Untuk pembuatan model pada aplikasi main diberi nama Item dan memiliki atribut:

-**name** sebagai nama item dengan tipe CharField.

-**amount** sebagai jumlah item dengan tipe IntegerField.

-**description** sebagai deskripsi item dengan tipe TextField.

-**price** sebagai harga item dengan tipe IntegerField.

-**nama** sebagai nama saya dengan tipe CharField.

-**kelas** sebagai kelas PBP dengan tipe CharField.

-**aplikasi** sebagai nama aplikasi saya dengan tipe CharField.

e) Kemudian, membuat fungsi dalam views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas saya. Hal ini dilakukan dengan adanya **context = {'books': books, 'nama': 'Novrizal Airsyahputra', 'kelas': 'PBP-A', 'aplikasi': 'airlib'}** di dalam _function_ show_main (request). Kemudian, mengembalikannya dengan cara: **return render(request, "main.html", context)**


 f) Selanjutnya, pembuatan routing pada urls.py aplikasi main ---_file_ ini bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main --- untuk memetakan fungsi yang telah dibuat pada views.py. Jadi, hal yang dilakukan adalah: **from django.urls import path** untuk mendefinisikan pola URL. Kemudian: **from main.views import show_main** _function_ ini sebagai tampilan yang akan ditampilkan saat URL diakses. **app_name = 'main'** agar nama unik pada pola URL aplikasi. 

g) Lakukan _deployment_ aplikasi tersebut ke website adaptable.io. Jadi, teman-teman akan dapat mengakses website yang telah saya buat melalui internet mereka. _Template deployment_ yang digunakan adalah Python App Template dan tipe basis data yang digunakan adalah PostgreSQL. Kemudian, _start command_ diisi dengan **python manage.py migrate && gunicorn shopping_list.wsgi**

h) Membuat README.md (ini) dan berisi tautan menuju aplikasi Adaptable yang sudah di-deploy sebelumnya dan jawaban dari 4 pertanyaan.

---

**2. Buatlah bagan yang berisi _request client_ ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

JAWAB: ![bagan](https://i.imgur.com/QCx0zSf.jpg)

Seperti yang kita ketahui bersama, Django _framework_ menggunakan arsitektur MTV (Model-Template-View). Kemudian, tiap komponen tersebut memiliki peranan:

-**Model:** untuk mengolah data dari _database_ yang telah dipesan.

-**View & URLconf:** merupakan "Controller" Django. Berguna untuk pendistribusian data dari Model ke Template atau sebaliknya menerima _request_ data dari Client.

-**Template:** merupakan "View" Django. Berguna untuk menunjukkan data yang diterima dari database, sesuai perintahnya Client.

Django _framework_ merupakan _full stack framework_ karena segala aktivitas _back-end_ (query dan logika) dikerjakan Model. Kemudian, untuk _front-end_ dilakukan oleh Template. Jadi, membuat _website_ dengan Django sangatlah menguntungkan.

Kemudian, kaitan antara urls.py, views.py, models.py, dan html adalah:

-**urls.py:** Pengonfigurasi yang menghubungkan URL dengan views sesuai. Jadi, di sini urls.py bertanggung jawab untuk mengatur rute URL proyek.

-**views.py:** Untuk mendefinisikan views yang akan meng-_handle_ _request_ dari HTTP. Jadi, views.py bertanggung jawab untuk memproses permintaan dan merespons dengan data yang sesuai. Di sini, model juga dapat diakses untuk mengambil atau menyimpan data.

-**models.py:** Untuk mendefinisikan _data structure_dan _business logic_ aplikasi. Jadi, models.py ini berkaitan dengan pengambilan, penyimpanan, dan manipulasi data dalam _database_.

-**Berkas HTML:** berfungsi untuk mengatur tampilan halaman web untuk _users_ atau _clients_. 

---

**3. Jelaskan mengapa kita menggunakan _virtual environment_? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan _virtual environment_?**

JAWAB: Berikut ini beberapa alasan dari penggunaan _virtual environment_:

a. **Kebersihan dan Portabilitas ---** Penggunaan _virtual environment_ dapat membantu kita menjaga kebersihan proyek (dengan memisahkan paket dan file konfigurasi di dalam lingkungan terisolasi). Pemindahan proyek ke sistem lain juga dapat dilakukan dengan baik.

b. **Manajemen Dependensi ---** Pengaktifan _virtual environment_ akan mempermudah manajemen dependensi proyek. _Install_, _delete_, dan _upgrade package_ Python dapat dilakukan dengan mudah (menggunakan pip, sebuah .Python _package manager_)

c. **Isolasi Proyek ---** Dengan menggunakan _virtual environment_, kita dapat mengisolasi dependensi proyek dari dependensi sistem pada komputer yang digunakan. Jadi, sebagai contoh, kita dapat memiliki versi yang berbeda dari Python _package_ untuk setiap proyek tanpa memunculkan suatu konflik (pengelolaan dependensi proyek dapat dilakukan secara terpisah).

d. **Menghindari Konflik ---** Dengan env\Scripts\activate.bat pada Windows, kita dapat menghindari konflik yang dapat timbul seperti yang disebutkan di atas. Contohnya _install package_ Python global langsung di sistem dapat menyebabkan konflik antar proyek yang menggunakan versi berbeda dari _package_ yang sama (jika _install_ tersebut dilakukan tanpa mengaktifkan _virtual environment_).

Kemudian, untuk pertanyaan yang kedua jawabannya adalah ya, kita tetap dapat membuat sebuah app web berbasis Django tanpa _virtual environment_. Namun, hal tersebut tidak disarankan untuk dilakukan. Mengapa demikian? Sebab tanpa penggunaan _virtual environment_, program akan sangat mungkin  menemukan konflik antar-_package_ dan konflik portabilitas proyek ke _environment_ lainnya. Ditambah lagi dengan pengelolaan dependensi global akan membuat sistem menjadi tidak teratur.

Jadi, misalkan kita akan membuat banyak proyek Python secara bersamaan, sebaiknya tetap menggunakan _virtual environment_. Caranya adalah dengan: 

-> Buat _virtual environment_ dahulu: python -m venv env 

-> Aktifkan (Windows): env\Scripts\activate.bat

---

**4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**

JAWAB: Ketiganya termasuk pola arsitektur _software_ yang berfungsi untuk mengatur agar kode aplikasi terstruktur, berinteraksi, dan berkomunikasi. Untuk memilih penggunaannya, tergantung jenis app yang akan dikembangkan, bahasa pemrograman yang digunakan, dan lain-lain. Berikut ini adalah penjelasan masing-masingnya:

a. **MVC (Model-View-Controller):** Memiliki banyak keuntungan, di antaranya (i) pengembangan berbagai komponen dapat dilakukan secara paralel; (ii) menawarkan dukungan terbaik untuk pengembangan yang bersifat _test-driven_; (iii) dapat bekerja dengan baik untuk aplikasi webs (yang biasanya terdiri dari banyak _web designers_ dan _developers_) 
   
   - **Model ---** Merupakan sebuah komponen utama yang mengatur data, logik, dan _constrains_ aplikasi.
   
   - **View ---** Berguna untuk menampilkan data dari model kepada _users_ dan mengumpulkan _input_ dari _users_.
   
   - **Controller ---** Memanipulasi Model dan berfungsi untuk mengontrol aliran dari aplikasi.

b. **MVT (Model-View-Template):** Memiliki banyak keuntungan, di antaranya (i) mudah untuk dimodifikasi; (2) cocok untuk aplikasi besar dan kecil; (3) (funfact) digunakan oleh Django.
   
   - **Model ---** Membantu menangani _database_ dan bertindak sebagai _interface_ data. 
   
   - **View ---** Berguna untuk mengeksekusi _business logic_ dan berinteraksi dengan Model untuk _carry data_ dan _renders_ sebuah _template_.
   
   - **Template ---** Umumnya digunakan untuk pengembangan web dengan Python dan kerangka kerja web Django. Bagian yang berfungsi untuk mengatur tampilan bagian-bagian HTML yang berbeda dari halaman web. Dapat bersifat _static_ atau _dynamic_.

c. **MVVM (Model-View-ViewModel):** Memiliki banyak keuntungan, di antaranya (i) mudah untuk dites dan dirawat; (ii) logika bisnisnya dipisahkan dari UI; (iii) mudah untuk _reuse_ komponen-komponen.

   - **Model ---** Melakukan pengelolaan logika bisnis dan data-data.

   - **View ---** Berinteraksi dengan ViewModel dan berfungsi untuk menampilkan data dari Model.

   - **ViewModel ---** Berfungsi untuk menghubungkan Model dan View. ViewModel sediakan data yang digunakan View dan sebagai perantara View dengan Model. Selain itu, ViewModel meng-handle logika tampilan dan interaksi yang tidak cocok dalam Model atau View.

**Perbedaan utama dari ketiganya** ada di cara komponen-komponen utama aplikasinya berinteraksi dan pembagian tugasnya. Pada MVT "Template" bertanggung jawab untuk me-_render_ tampilannya. Sedangkan pada MVC, tanggung jawab tersebut dilakukan "View." Pada MVC, untuk memodifikasi sulit dan kurang cocok untuk aplikasi kecil, tetapi MVT dapat memodifikasi dengan lebih mudah dan cocok untuk aplikasi besar dan kecil.

Selain itu, controller pada MVC bertugas untuk mengelola interaksi antara "View" dengan "Model". Sedangkan MVT, "View" dan "Model"-nya berinteraksi lebih langsung

Terakhir, tampilan dari MVVM dipisahkan dari _business logics_ dengan perantaranya "View Model". Jadi, tampilan akan fokus ke presentasi data.

 ---
# **Sumber Referensi**

https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-0

https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-1

https://www.niagahoster.co.id/blog/django-framework/

https://docs.djangoproject.com/id/4.2/intro/tutorial01/

https://levelup.gitconnected.com/mvc-vs-mvp-vs-mvvm-35e0d4b933b4

https://www.guru99.com/mvc-vs-mvvm.html

https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/