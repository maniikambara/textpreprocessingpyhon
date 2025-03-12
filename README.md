# Pengolahan Teks dengan Sastrawi (Tokenisasi, Filtering, Stemming)

## Deskripsi
Repositori ini merupakan proyek Python sederhana untuk **pengolahan teks bahasa Indonesia** yang meliputi **Tokenisasi, Filtering, dan Stemming**, menggunakan library **Sastrawi**.  
Selain itu, proyek ini menggunakan daftar stopwords tambahan dari [masdevid/ID-Stopwords](https://github.com/masdevid/ID-Stopwords) untuk meningkatkan akurasi proses filtering (penghilangan kata-kata tidak penting).  

## Fitur
- **Tokenisasi**: Memecah kalimat menjadi kata-kata atau token.
- **Filtering**: Menghapus stopwords (kata-kata umum yang tidak memiliki makna penting dalam analisis) berdasarkan daftar ID-Stopwords dan daftar kustom.
- **Stemming**: Mengubah kata ke bentuk dasar (akar kata) menggunakan Sastrawi Stemmer.

## Kebutuhan
- Python 3.x
- Library Sastrawi

## Instalasi
1. Clone repositori ini ke perangkat lokal Anda:
```bash
git clone https://github.com/your-username/text-preprocessing-sastrawi.git

cd text-preprocessing-sastrawi
```
2. Install library yang dibutuhkan:
```bash
pip install Sastrawi
```
3. Unduh file ID-Stopwords dari masdevid/ID-Stopwords dan letakkan file stopwords tersebut (misalnya stopwords.txt) di dalam folder utama proyek.

## Cara Penggunaan
1. Siapkan dataset teks Anda (bisa dalam format .txt atau langsung dimasukkan di dalam script Python).
2. Jalankan script Python utama untuk memproses teks:
```bash
python textpreproc.py
```

## Contoh
Teks Awal:
elearning di PTIIK di atas jam 6 malam kok selalu gak bisa dibuka ya?

Setelah Diproses:

Tokenisasi: elearning di ptiik di atas jam 6 malam kok selalu gak bisa dibuka ya

Filtering: elearning ptiik jam 6 malam gak dibuka

Stemming: elearning ptiik jam 6 malam gak buka

## Struktur Folder
```graphql
text-preprocessing-sastrawi/
│
├── ID-Stopwords-master.zip   # File zip ID-Stopwords (mentahan)
├── PySastrawi-1.2.0.zip      # File zip PySastrawi (mentahan)
├── id.stopwords.02.01.2016.txt # File stopwords hasil ekstrak (digunakan untuk filtering)
├── input.txt                 # File input teks (dokumen yang diproses)
├── output.txt                # Hasil output setelah diproses
├── textpreproc.py            # Script utama Python untuk tokenisasi, filtering, stemming
```

## Kredit
Sastrawi - Library stemming untuk Bahasa Indonesia.

masdevid/ID-Stopwords - Daftar kata-kata stopwords tambahan untuk Bahasa Indonesia.

## Lisensi
Proyek ini dilisensikan di bawah MIT License.
