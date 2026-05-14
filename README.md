# Projek_Perintah_Array
#  Tugas Individu — Pemrograman Python

> **Mata Pelajaran:** Pemrograman Dasar  
> **Bahasa:** Python 3  
> **Tugas:** Implementasi Array & Operasional Perhitungan

---

##  Struktur Proyek

```
tugas-python/
│
├──  README.md              ← Dokumentasi ini
├──  program_array.py       ← Program 1: Implementasi Array
└──  program_kalkulator.py  ← Program 2: Operasional Perhitungan
```

---

##  Program 1 — Implementasi Array

### Deskripsi
Program ini mendemonstrasikan penggunaan **array (list)** di Python.  
Mencakup operasi membuat, mengakses, menambah, menghapus, mengurutkan, dan menelusuri elemen array.

### Fitur
| Operasi | Method | Keterangan |
|---|---|---|
| Buat array | `list = [...]` | Inisialisasi array dengan nilai awal |
| Akses elemen | `list[index]` | Mengambil elemen berdasarkan posisi |
| Tambah di akhir | `list.append(x)` | Menyisipkan elemen di akhir array |
| Sisipkan di posisi | `list.insert(i, x)` | Menyisipkan di index tertentu |
| Hapus by nilai | `list.remove(x)` | Menghapus elemen berdasarkan nilai |
| Hapus by index | `list.pop(i)` | Menghapus elemen berdasarkan index |
| Panjang array | `len(list)` | Menghitung jumlah elemen |
| Urutkan | `list.sort()` | Mengurutkan dari kecil ke besar |
| Balik urutan | `list.reverse()` | Membalik urutan elemen |
| Iterasi | `for i, x in enumerate(list)` | Menelusuri semua elemen |

### Cara Menjalankan
```bash
python program_array.py
```

### Contoh Output
```
========================================
        PROGRAM ARRAY PYTHON
========================================

 Data Array Buah:
['Apel', 'Mangga', 'Jeruk', 'Pisang', 'Anggur']

 Akses Elemen:
Index ke-0 : Apel
Index ke-2 : Jeruk
Index ke-4 : Anggur

➕ Setelah append 'Semangka': ['Apel', 'Mangga', 'Jeruk', 'Pisang', 'Anggur', 'Semangka']
➕ Setelah insert 'Melon' di index 2: ['Apel', 'Mangga', 'Melon', 'Jeruk', 'Pisang', 'Anggur', 'Semangka']
➖ Setelah remove 'Jeruk': ['Apel', 'Mangga', 'Melon', 'Pisang', 'Anggur', 'Semangka']
➖ Setelah pop index 0: ['Mangga', 'Melon', 'Pisang', 'Anggur', 'Semangka']

📏 Panjang array: 5
🔤 Setelah diurutkan: ['Anggur', 'Mangga', 'Melon', 'Pisang', 'Semangka']
🔄 Setelah dibalik: ['Semangka', 'Pisang', 'Melon', 'Mangga', 'Anggur']

🔁 Menampilkan dengan looping:
  Index 0: Semangka
  Index 1: Pisang
  Index 2: Melon
  Index 3: Mangga
  Index 4: Anggur
```

---

##  Program 2 — Operasional Perhitungan

### Deskripsi
Program ini adalah **kalkulator interaktif** yang menerima dua angka dari pengguna dan menampilkan hasil dari berbagai operasi matematika dan perbandingan.

### Fitur
| Operasi | Simbol | Keterangan |
|---|---|---|
| Penjumlahan | `a + b` | Menambahkan dua angka |
| Pengurangan | `a - b` | Mengurangkan dua angka |
| Perkalian | `a * b` | Mengalikan dua angka |
| Pembagian | `a / b` | Membagi (hasil desimal) |
| Pembagian Bulat | `a // b` | Membagi (hasil bilangan bulat) |
| Sisa Bagi | `a % b` | Modulo — sisa hasil bagi |
| Perpangkatan | `a ** b` | Memangkatkan angka |
| Perbandingan | `>, <, >=, <=, ==, !=` | Membandingkan dua angka |

### Penanganan Error
Program dilengkapi pengecekan **pembagian dengan nol (ZeroDivisionError)**.  
Jika `b == 0`, program akan menampilkan pesan error dan melewati operasi pembagian.

### Cara Menjalankan
```bash
python program_kalkulator.py
```

### Contoh Output
```
========================================
   KALKULATOR OPERASIONAL PERHITUNGAN
========================================

Masukkan angka pertama  : 10
Masukkan angka kedua    : 3

----------------------------------------
         HASIL PERHITUNGAN
----------------------------------------

➕ Penjumlahan      : 10.0 + 3.0 = 13.0
➖ Pengurangan      : 10.0 - 3.0 = 7.0
✖️  Perkalian        : 10.0 x 3.0 = 30.0
➗ Pembagian        : 10.0 / 3.0 = 3.33
📐 Pembagian Bulat  : 10.0 // 3.0 = 3.0
🔢 Sisa Bagi (Mod)  : 10.0 % 3.0 = 1.0
🔺 Perpangkatan     : 10.0 ** 3.0 = 1000.0

----------------------------------------
       OPERASI PERBANDINGAN
----------------------------------------
  10.0 > 3.0  : True
  10.0 < 3.0  : False
  10.0 >= 3.0 : True
  10.0 <= 3.0 : False
  10.0 == 3.0 : False
  10.0 != 3.0 : True
```

---

## Persyaratan Sistem

- **Python versi:** 3.x (direkomendasikan Python 3.8 ke atas)
- **Library tambahan:** Tidak ada (hanya built-in Python)
- **OS:** Windows / macOS / Linux

### Cara Cek Versi Python
```bash
python --version
```

---

##  Konsep yang Dipelajari

### Program Array
- Struktur data **List** di Python
- Indexing dan slicing
- Method bawaan list: `append`, `insert`, `remove`, `pop`, `sort`, `reverse`
- Fungsi `len()` untuk panjang array
- Iterasi dengan `enumerate()`

### Program Kalkulator
- Tipe data `float` untuk angka desimal
- Operator aritmatika: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Operator perbandingan: `>`, `<`, `>=`, `<=`, `==`, `!=`
- Kondisional `if-else` untuk penanganan error
- Fungsi `input()` untuk input pengguna
- F-string untuk formatting output

---

##  Flowchart

Flowchart untuk kedua program tersedia di dalam dokumen README ini sebagai referensi visual alur kerja program.

```
Program Array:
MULAI → Buat Array → Akses Elemen → Tambah Elemen → Hapus Elemen → Sort/Reverse → Looping → SELESAI

Program Kalkulator:
MULAI → Input 2 Angka → Hitung Dasar → [Cek b==0?] → Ya: Tampilkan Error
                                                      → Tidak: Hitung Pembagian → Perbandingan → Tampilkan Hasil → SELESAI
```

---

##  Informasi Tugas

| | |
|---|---|
| **Jenis Tugas** | Tugas Individu |
| **Bahasa** | Python |
| **Program 1** | Implementasi Perintah Array |
| **Program 2** | Implementasi Operasional Perhitungan |

---

*Dibuat dengan Python *
