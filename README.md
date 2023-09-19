# Novrizal Airsyahputra (2206081780) PBP-A
---

TUGAS 2 PBP

---

**1. Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_ (bukan hanya sekadar mengikuti tutorial).**

JAWAB: Berikut merupakan cara saya dalam mengimplementasikan _checklist_ di atas:

a) Setelah membuat _dependencies_ dalam berkas requirements.txt dan menjalankan _environment_,  waktunya membuat sebuah proyek Django baru yang bernama airlib. Perintah yang ditulis pada cmd adalah: **django-admin startproject airlib .**

b) Kemudian, buat aplikasi yang bernama "main" pada proyek, dengan cara perintah: **python manage.py startapp main**. Tak lupa setelah itu, buka _file_ settings.py dalam direktori proyek airlib dan tambahkan code 'main' ke dalam variabel INSTALLED_APPS.

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

g) Lakukan _deployment_ aplikasi tersebut ke website adaptable.io. Jadi, teman-teman akan dapat mengakses website yang telah saya buat melalui internet mereka. _Template deployment_ yang digunakan adalah Python App Template dan tipe basis data yang digunakan adalah PostgreSQL. Kemudian, _start command_ diisi dengan **python manage.py migrate && gunicorn airlib.wsgi**

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
# **Sumber Referensi Tugas 2**

https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-0

https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-1

https://www.niagahoster.co.id/blog/django-framework/

https://docs.djangoproject.com/id/4.2/intro/tutorial01/

https://levelup.gitconnected.com/mvc-vs-mvp-vs-mvvm-35e0d4b933b4

https://www.guru99.com/mvc-vs-mvvm.html

https://www.geeksforgeeks.org/difference-between-mvc-and-mvt-design-patterns/


---

TUGAS 3 PBP

---
**1. Apa perbedaan antara form POST dan form GET dalam Django?**

JAWAB: Django Forms (POST dan GET) merupakan sebuah _built-in feature_ dari Django. Berikut ini merupakan perbedaan dari keduanya:

a.	**Segi _Data Types_ ---** _Method post_ dapat menggunakan _data types_ yang berbeda seperti, _string_, _binary_, _numeric_, dan lain-lain. Sedangkan, _method get_, hanya dapat menggunakan _string data type_.

b.	**Segi Penggunaan ---** _Method post_ digunakan saat ingin melakukan pemrosesan pengiriman data dari _form_ ke _server_. Sebagai contoh, permintaan untuk mengubah status server atau menyimpan data di dalam _database_. Sedangkan, _method get_ digunakan saat ingin mendapatkan data dari server. Jadi, proses mendapatkan data ini tidak melakukan perubahan pada status _server_ yang digunakan.

c.	**Segi _Cacheable_---** Pada umumnya, _method post_ bersifat _hardly cacheable_. Sedangkan, _method get_, pada umumnya, bersifat _cacheable_.

d.	**Segi Security ---** _Method post_ lebih aman daripada _method get_ untuk melakukan pengiriman data sensitif (tak nampak pada URL dan tak mudah diakses oleh _user_). Sedangkan, pada method get, data sensitif dapat nampak di URL, jadi kurang aman untuk digunakan.

e.	**Segi Ukuran Pengiriman Data ---** _Method post_ dapat mengirim data dalam jumlah yang lebih besar. Jadi, _post_ cocok untuk meng-_upload_ file dengan size yang besar. Sedangkan, _method get_, data yang dapat dikirimkan _size_-nya lebih rendah.

---

**2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?**

JAWAB: Berikut ini perbedaan utama dari ketiganya berdasarkan beberapa segi:

a. **Segi Security ---** XML dalam penggunaannya, developers harus berhati-hati karena tak ada hal seperti _built-in_ untuk _handle_ masalah _security_; Pada JSON meski strukturnya lebih _simple_, tetap perlu untuk dilindungi. Hanya saja, risikonya tidak setinggi XML; Sedangkan, untuk HTML, memiliki beberapa masalah _security_ yang harus di-_handle_ seperti CSRF (Cross-Site Request Forgery).

b. **Segi Tujuan Penggunaan ---** XML memiliki tujuan untuk merepresentasikan atau menukar data yang terstruktur antara sistem yang berbeda-beda. XML bersifat sangat fleksibel dan biasanya digunakan dalam _file configure_, web services, dan lain-lain; JSON sering digunakan untuk pertukaran data dan _modern webite development_. Utamanya, JSON dipakai untuk mengirim data antara _browser_ dan _server_ pada aplikasi web modern; Sedangkan, untuk HTML digunakan sebagai pembuat tampilan web _pages_ kepada browser dan pembuatan struktur web.

c. **Segi _Data Structure_ ---** Pada XML, _data structure_-nya didefinisikan dengan menggunakan tags dan atribut; JSON menggunakan konsep _key-value pairs_ untuk merepresentasikan datanya (terutama pada saat _nested array_); Sedangkan, untuk mengatur struktur web _pages_ pada HTML, digunakanlah tags.

**Fun Fact!** JSON diciptakan sebagai alternatif dari XML (dulu pernah dominan sebagai format untuk pertukaran data).

---

**3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?**

JAWAB: JSON atau JavaScript Object Notation sering disebut sebagai _de-facto standard_ dalam pertukaran data antara aplikasi web modern. JSON memiliki banyak kelebihan yang menyebabkannya sering digunakan dalam pertukaran data antara aplikasi web modern. Berikut ini beberapa kelebihan yang dimilikinya:

a. JSON merupakan **_text-based format_**. Jadi, dapat dibaca oleh mesin dan manusia. JSON juga menggunakan konsep _key-value pairs_ seperti yang telah dijelaskan sebelumnya.

b. JSON **didukung oleh banyak bahasa pemrograman lainnya**. Jadi, JSON berguna untuk pertukaran data antara sistem yang beraneka ragam.

c. JSON adalah **alat yang sangat serbaguna** dari _data structure_-nya. 

d. JSON memiliki **pemrosesan yang cepat dan mudah** dari sisi _client_. Hal tersebut disebabkan oleh _data structure_ yang dimiliki JSON kedudukannya sejajar dengan objek JavaScript. 

e. JSON mudah untuk mengubah data: **serialisasi dan deserialisasi**.

f. JSON **mendukung banyak _data types_** seperti _string_, _numeric_, _array_, _boolean_, dan lain-lain.

---

**4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

JAWAB:

a. Pertama-tama, **buat _input form_** yang berfungsi untuk menambahkan objek _model_ pada _app_ sebelumnya. Caranya adalah dengan:

- Membuat _new file_ diberi nama `forms.py` dalam direktori `main`. _File_ ini berguna untuk pembuatan struktur _form_ yang dapat menerima data _item_ baru. _Import_-lah `ModelForm` dan `Item`, serta _class_-nya diberi nama `ItemForm` dengan _parameter_-nya `ModelForm`.

- Selanjutnya, bukalah _file_ `views.py` dalam _folder_ `main`. Tambahkan import `HttpResponseRedirect`, `ItemForm`, dan `reverse`.

- Buat _function_ bernama `create_item` dan _parameter_-nya `request`. _Function_ ini berfungsi untuk menghasilkan formulir yang otomatis akan dapat menambahkan data _item_ saat ada yang di-_submit_.

- Pada _function_ `show_main` dalam _file_ `views.py`, tambahkan `items = Item.objects.all()`. Hal tersebut berfungsi untuk ambil semua _object_ dalam _database_.

- Buka _file_` urls.py`. _Import_-lah create_item dan tambahkan _path url_ ke dalam `urlpatterns`(untuk akses _function_).

- Buat _file_ baru bernama `create_item.html` dalam ditektori `main/templates`. _File_ tersebut berisikan _method_ "POST".

- Buka `main.html` dan tambahkan kode yang berfungsi untuk menunjukkan data item dalam bentuk _table_ dan _button_ "Add New Item". _Button_ tersebut akan mengarahkan _user_ ke _form page_.

b. Kemudian, menambahkan sebanyak 5 fungsi _views_ untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML _by_ ID, dan JSON _by_ ID. Berikut beberapa langkah yang diterapkan:

- HTML: Lakukan steps sebelumnya dan coba jalankan proyek Django dengan perintah **python manage.py runserver** dan buka http://localhost:8000.

- XML: Buka `views.py` pada _folder_ `main` dan _import_ `HttpResponse` dan `Serializer` (untuk _translate object model_). Kemudian, buat _function_ `show_xml` dengan parameternya `request`, serta beri _return function_ `HttpResponse` yang isinya adalah parameter data hasil _query_ dan parameter `content_type = "application/xml"`. Lalu, buka `urls.py` dalam _folder_ `main` dan _import function_ `show_xml`. Tak lupa, tambahkan _path url_-nya ke dalam `urlpatterns` agar dapat diakses.

- JSON: Buka `views.py` pada _folder_ `main`. Kemudian, buat _function_ `show_json` dengan parameternya `request`, serta beri _return function_ `HttpResponse` yang isinya adalah parameter data hasil _query_ dan parameter `content_type = "application/json"`. Lalu, buka `urls.py` dalam _folder_ `main` dan _import function_ `show_json`. Tak lupa, tambahkan _path url_-nya ke dalam `urlpatterns` agar dapat diakses.

- XML _and_ JSON _by_ ID: Buka `views.py` pada _folder_ `main`. Kemudian, buat _function_ `show_xml_by_id` dan `show_json_by_id`, keduanya memiliki parameter `request`, serta beri _return function_ `HttpResponse` yang isinya adalah parameter data hasil _query_ dan parameter `content_type="application/xml"` (untuk show_xml_by_id) dan `content_type="application/json"` (untuk show_json_by_id). Lalu, buka `urls.py` dalam _folder_ `main` dan _import_ kedua _function_. Tak lupa, tambahkan _path url_-nya ke dalam `urlpatterns` agar dapat diakses.

c. Lalu, membuat _routing_ URL untuk setiap _views_ yang telah ditambahkan. Caranya adalah pada _file_ `urls.py` yang ada di dalam _folder_ `main`, buatlah kode ini:

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
]

Dengan menambahkan _path_ URL, maka _routing_ URL tiap _views_ telah dibuat.

d. Menjawab beberapa pertanyaan pada README.md pada _root_ folder.

e. Lakukan akses terhadap kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md. Caranya adalah dengan:

- _Download_ aplikasi Postman.

- Jalankan perintah `python manage.py runserver`.

- Pada GET, tulislah `http://localhost:8000/` untuk HTML, `http://localhost:8000/xml` untuk XML,`http://localhost:8000/json` untuk JSON, `http://localhost:8000/xml/[ID]` untuk XML _by_ ID,`http://localhost:8000/json/[ID]` untuk JSON _by_ ID.

f. Terakhir, jangan lupa untuk melakukan `git add`, `git commit -m "PBP TUGAS 3 DONE"`, dan `git push origin main`.

---

**5. _Screeshot_ hasil URL dari Postman.**

JAWAB:

a. HTML
![html](https://i.imgur.com/nPp45lx.jpg)

b. XML
![xml](https://i.imgur.com/flUmiwh.jpg)

c. JSON
![json](https://i.imgur.com/nqqBLKo.jpg)

d. XML by ID
![xmlByID](https://i.imgur.com/zC0BCRe.jpg)

e. JSON by ID
![jsonByID](https://i.imgur.com/TDhgvFr.jpg)


---
# **Sumber Referensi Tugas 3**

https://docs.djangoproject.com/en/4.2/topics/forms/#:~:text=GET%20and%20POST 

https://www.geeksforgeeks.org/render-html-forms-get-post-in-django/

https://www.infoworld.com/article/3222851/what-is-json-a-better-format-for-data-exchange.html#:~:text=JSON%20is%20a%20wildly%20successful,Finally%2C%20it%20is%20human%20readable.

https://www.alphasoftware.com/blog/json-is-the-de-facto-standard-for-data-interchange-in-web-applications-alpha-anywhere

https://www.linkedin.com/pulse/understanding-json-backbone-behind-modern-data-approach-delali-azumah/