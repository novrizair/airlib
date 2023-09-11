# Novrizal Airsyahputra (2206081780) PBP-A
---

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
JAWAB: Cara saya mengimplementasikan checklists di atas adalah





**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**
JAWAB: 


**Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
JAWAB: 


**Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**
JAWAB: Ketiganya merupakan suatu pola arsitektur software yang berfungsi untuk mengatur agar kode aplikasi terstruktur, berinteraksi, dan berkomunikasi. Berikut ini penjelasan lebih rincinya:

Pemilihan antara ketiga pola ini tergantung pada jenis aplikasi yang Anda kembangkan, bahasa pemrograman yang Anda gunakan, dan preferensi tim pengembangan Anda. Setiap pola memiliki kelebihan dan kekurangan masing-masing,

1. **MVC (Model-View-Controller)**
   
   - **Model**: Representasi data dan logika bisnis aplikasi. Model mengelola data dan memberikan akses ke data tersebut. Ini adalah komponen yang berhubungan dengan basis data dan bisnis.
   
   - **View**: Tampilan yang mengatur tampilan dan tampilan yang diberikan kepada pengguna. View bertanggung jawab untuk menampilkan data dari model kepada pengguna dan mengumpulkan input dari pengguna.
   
   - **Controller**: Kontrol aliran logika aplikasi. Controller menerima input dari pengguna, memprosesnya, dan berinteraksi dengan model untuk memperbarui data atau memutuskan tampilan apa yang akan ditampilkan. Controller mengontrol aliran aplikasi.

   **Perbedaan Utama**: MVC adalah pola yang umum digunakan dalam pengembangan web tradisional. Dalam MVC, View dan Controller biasanya lebih terhubung secara langsung. Controller mengatur View dan berkomunikasi langsung dengan Model. MVC cenderung digunakan dalam pengembangan web dengan server-side rendering.

2. **MVT (Model-View-Template)**:
   
   - **Model**: Mirip dengan Model dalam MVC, Model dalam MVT adalah komponen yang menangani logika bisnis dan basis data.
   
   - **View**: View dalam MVT mirip dengan View dalam MVC dan bertanggung jawab untuk tampilan dan presentasi data.
   
   - **Template**: Template adalah bagian unik dari pola MVT yang berbeda dari MVC. Template adalah bagian yang mengatur tampilan bagian-bagian HTML yang berbeda dari halaman web Anda. Template digunakan dalam kerangka kerja web Django, yang umumnya digunakan untuk pengembangan web dengan Python.

   **Perbedaan Utama**: MVT adalah varian dari MVC yang digunakan dalam kerangka kerja web Django. MVT menggunakan template untuk mengatur tampilan, sedangkan dalam MVC, View biasanya mengatur tampilan.

3. **MVVM (Model-View-ViewModel)**:

   - **Model**: Mirip dengan Model dalam MVC dan MVT, Model dalam MVVM mengelola data dan logika bisnis.

   - **View**: View dalam MVVM adalah tampilan yang menampilkan data dari Model dan berinteraksi dengan ViewModel.

   - **ViewModel**: ViewModel adalah komponen yang menghubungkan Model dan View. Ini menyediakan data yang diperlukan oleh View dan berfungsi sebagai perantara antara Model dan View. ViewModel juga menangani logika tampilan dan interaksi yang tidak cocok dalam Model atau View.

   **Perbedaan Utama**: MVVM adalah pola arsitektur yang sering digunakan dalam pengembangan aplikasi berbasis klien (seperti aplikasi web berbasis JavaScript). Perbedaannya adalah adanya ViewModel, yang memisahkan logika tampilan dari View dan mengikuti pola "two-way data binding," yang memungkinkan perubahan dalam Model secara otomatis diperbarui dalam tampilan dan sebaliknya.