# Latihan 1.6 — Implementasi Class Diagram

Implementasi Python dari latihan pencatatan perkuliahan pada modul.

## Isi project
- `not_yet_set_exception.py`: exception untuk nilai yang belum diatur.
- `student.py`: class mahasiswa.
- `assignment.py`: class tugas dan nilai.
- `course_record.py`: menghubungkan mahasiswa dengan daftar tugas.
- `course.py`: class mata kuliah dan tiga method cetak yang diminta.
- `main.py`: contoh penggunaan seluruh class.

## Cara menjalankan di VS Code
1. Ekstrak ZIP.
2. Buka folder `Latihan_1_6_Pencatatan_Perkuliahan` di VS Code.
3. Pastikan Python sudah terpasang.
4. Buka terminal VS Code (`Terminal > New Terminal`).
5. Jalankan:

   ```bash
   python main.py
   ```

   Jika perintah itu tidak bekerja di Windows, coba `py main.py`.

## Aturan yang digunakan
- Nilai `-1` berarti nilai belum diatur dan memunculkan `NotYetSetException`.
- Nilai yang belum diatur tidak dimasukkan ke perhitungan rata-rata.
- Mahasiswa layak mengikuti ujian akhir jika rata-rata nilainya minimal 60. Ambang 60 merupakan asumsi implementasi karena modul pada gambar tidak menyebutkan batas kelulusan secara eksplisit.

## Commit melalui SourceTree
1. Ekstrak folder ZIP ke lokasi tugasmu.
2. Buka SourceTree dan tambahkan folder ini sebagai repository lokal, atau salin file-file ini ke repository tugas yang sudah ada.
3. Isi pesan commit, misalnya `Implementasi class diagram latihan 1.6`.
4. Klik **Commit**.
5. Untuk mengirim ke GitHub, pastikan remote sudah terhubung, lalu klik **Push** dan pilih branch yang sesuai.
