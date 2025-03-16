import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Fungsi untuk membaca isi file per baris
def baca_input(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

# Fungsi untuk menulis hasil ke file
def write(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)

# Fungsi tokenisasi
def tokenisasi(text):
    return re.findall(r'\b\w+\b', text.lower())

# Fungsi filtering dengan tambahan stopword
def filtering(text, stopword_tambahan):
    stop_factory = StopWordRemoverFactory()
    default_stopwords = stop_factory.get_stop_words()
    stopwords = set(word.lower() for word in default_stopwords + stopword_tambahan)
    tokens = tokenisasi(text)
    # Filter token
    return [word for word in tokens if word not in stopwords]

# Fungsi stemming
def stemming(tokens):
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    return [stemmer.stem(word) for word in tokens]

# Fungsi untuk membaca stopword tambahan dari file
def file_stopword(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return [line.strip().lower() for line in file if line.strip()]
    except FileNotFoundError:
        print("File stopword tambahan tidak ditemukan.")
        return []

if __name__ == "__main__":
    input_file = 'input.txt'
    stopword_file = 'id.stopwords.02.01.2016.txt'
    output_file = 'output.txt'

    # Baca data input dan stopword tambahan
    list_kalimat = baca_input(input_file)
    stopword_tambahan = file_stopword(stopword_file)

    hasil_akhir = ""

    for idx, kalimat in enumerate(list_kalimat):
        tokens = tokenisasi(kalimat)
        kalimat_filter = filtering(kalimat, stopword_tambahan)
        kalimat_stem = stemming(kalimat_filter)

        hasil_akhir += f"""Doc {idx + 1}
Isi :
{kalimat}

Tokenisasi :
{' '.join(tokens)}

Filtering :
{' '.join(kalimat_filter)}

Stemming :
{' '.join(kalimat_stem)}

"""

    # Tulis file txt
    write(output_file, hasil_akhir)
    print(f"Hasil preprocessing berhasil disimpan di {output_file}")