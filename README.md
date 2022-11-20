## College Assignment Needs

### Kelompok 5 C1 2021 Universitas Pendidikan Indonesia

Mata Kuliah : Kecerdasan Buatan

Dosen Pengampu : Yaya Wihardi, S.Kom., M.Kom.

Anggota Kelompok :

- NIM : 2100137
- Nama : Muhamad Nur Yasin Amadudin

- NIM : 2103703
- Nama : Fauziyyah Zayyan Nur

- NIM : 2108927
- Nama : Muhammad Fahru Rozi

- NIM : 2102843
- Nama : Najma Qalbi Dwiharani

## Link Production

[ga-timetable.herokuapp.com](https://ga-timetable.herokuapp.com/)

## About The Project

Project ini merupakan aplikasi berbasis website untuk men-simulasikan algoritma genetika yang digunakan untuk membuat jadwal di Sekolah Menengah Pertama (SMP).

## Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Heroku](https://www.heroku.com/)

## Deploy to Heroku

### Prerequisites

Sebelum melakukan deploy aplikasi pastikan Anda sudah memiliki atau sudah menginstall Heroku CLI.

### Installation

Dibawah ini merupakan langkah - langkah untuk deploy aplikasi menggunakan Heroku.

- Login ke dalam Heroku

   ```sh
   heroku login
   ```

- Install HTTP Server untuk Python

   ```sh
   pip install gunicorn
   ```

- Buat Procfile untuk menentukan perintah yang dijalankan pertama kali di Heroku

   ```sh
   touch Procfile
   ```

- Tambahkan keterangan aplikasi di Procfile

   ```sh
   web: gunicorn app:app
   ```

- Buat requirements yang akan digunakan di Heroku

   ```sh
   pip freeze > requirements.txt
   ```

- Hapus library/package yang tidak digunakan

- Buat repository

   ```sh
   git init
   ```

- Tambahkan file ke repository

   ```sh
   git add .
   ```

- Simpan perubahan

   ```sh
   git commit -m "Initial Commit"
   ```

- Login to Heroku

- Create new app

- Lakukan remote ke applikasi Heroku

   ```sh
   heroku git:remote -a [app_name]
   ```

- Push ke aplikasi Heroku

   ```sh
   git push heroku master
   ```