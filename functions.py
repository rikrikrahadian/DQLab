"""
File `functions.py` ini merupakan tempat untuk penyimpanan berbagai fungsi dan data yang dipergunakan dalam pembelajaran pemrograman python.
Berbagai fungsi dan data yang telah dibuat pada file ini dapat dipergunakan dengan cara diimport seperti berikut di bawah:
   ```from functions import <nama_fungsi>```
"""
import pandas as pd, os,  matplotlib.pyplot as plt, ipywidgets as widgets

# DATA
Part_3 = {
    'Q1' : (False, False, False, True, False),
    'Q2' : (False, True, False, True, False),
    'Q3' : (False, False, False),
    'Q4' : (True, False, False),
    'Q5' : (True, True, True, False),
    'Q6' : (True, True, False, True),
    'Q7' : (False, True, True, True),
    'Q8' : (False, False, False, False, True),
    'Q9' : (False, False, False, False)
}
PART_4 = {
    'Q1' : (False, False, False, True),
    'Q2' : (False, False, False, True),
    'Q3' : (False, False, False, True)
} 
layouts = widgets.Layout(width='auto')


# FUNCTIONS
def check_answers(correct_answers, options, result_widget):
    # Terima Jawaban User
    user_answers = tuple(option.value for option in options)

    # Check apakah jawaban user sesuai kunci
    if user_answers == correct_answers:
        feedback = "Pilihan anda tepat!"
    else:
        feedback = "Pilihan anda kurang tepat, silahkan coba lagi!"

    result_widget.value = feedback

def validasi_file_data(nama_file):
  return nama_file.count('.')==1 and nama_file.split('.')[-1] in ['txt', 'csv', 'xls', 'xlsx', 'json']

def validasi_file_ada(file_path: str) -> bool:
  import os
  return os.path.exists(file_path)

def parsing_file_data(nama_folder: str, nama_file: str) -> object | None:
    """
    Fungsi untuk melakukan parsing data dari beberapa jenis file data

    ARGUMENTS:
    1. nama_folder: str, nama folder dimana file data disimpan;
    2. nama_file  : str, nama file yang akan diparsing, nama file
                 harus ditulis lengkap dengan ekstensinya.
    OUTPUT:
    Object berupa pandas.dataframe atau None
    """

    # Validasi filename : apakah penulisan file benar dan merupakan file data?
    if validasi_file_data(nama_file) is False:
      raise ValueError(f"'{nama_file}': penulisan nama tidak valid / bukan file Data.")

    # Membuat file_path, berdasarkan info dari argument pada fungsi
    file_path = os.path.join(nama_folder, nama_file)

    # Validasi file_path : apakah file dimaksud ada?
    if validasi_file_ada(file_path) is False:
      raise FileNotFoundError(f"File '{file_path}' tidak ditemukan.")

    # Mengambil info ekstensi file
    ekstensi = nama_file.split('.')[-1]

    # Proses Parsing, menggunakan metode yang disesuaikan dengan ekstensi file
    if ekstensi in ['csv', 'txt']:      # Jika ekstensi `csv` atau `txt`
        df = pd.read_csv(file_path)
    elif ekstensi == 'json':            # Jika ekstensi `json`
        df = pd.read_json(file_path)
    elif ekstensi in ['xls', 'xlsx']:   # Jika ekstensi `xls` atau `xlsx`
        df = pd.read_excel(file_path)

    return df

def print_satu_persatu(
    jdl : str,
    deret : list, 
    margin : int
) -> None:
    """
    Fungsi untuk menampilkan isi sebuah list secara animasi
    PARAMETERS:
        1. jdl -> string yang ditampilkan sebagai dari judul deret;
        2. deret -> list yang akan dianimasikan;
        3. margin -> sebuah angka bulat yang menentukan panjang margin layar.
    """
    # 1. Mengimpor fungsi yang diperlukan
    import time
    
    # 2. Buat sebuah list kosong
    elemens = []
    
    # 3. Iterasikan setiap elemen pada deret
    for elemen in deret:
        # Masukkan setiap elemen dari deret ke list kosong pada proses 3
        elemens.append(elemen)
        # Tampilkan list `elemens` ke layar secara animasi
        item = f"{jdl} {elemens}"
        print(f"\r{item: ^{margin}}", end="", flush=True)
        # Berikan jeda agar animasi dapat terlihat
        time.sleep(0.3)

def quick_sort(
    deret : list
) -> list:
    """
    Fungsi untuk mengurutkan elemen pada suatu deret 
      yang dilakukan dengan algoritma 'quick sort`
    PARAMETERS:
        1. deret -> list yang belum disortir.
    """
    # 1. Cek jumlah elemen pada deret > 1
    if len(deret) <= 1:
        # Jika <= 1
        return deret
    
    # 2. Tentukan titik `pivot` = elemen yang berada di tengah
    pivot = deret[len(deret) // 2]
    
    # 3. Gunakan `pivot`, partisi elemen pada deret menjadi 3 deret:
    # elemen-elemen < `pivot`
    kiri = [x for x in deret if x < pivot]
    # elemen-elemen == `pivot`
    tengah = [x for x in deret if x == pivot]
    # elemen-elemen > `pivot`
    kanan = [x for x in deret if x > pivot]
    
    # 4. Susun output akhir
    return quick_sort(kiri) + tengah + quick_sort(kanan)

def quick_sort_show(
    deret : list,
    N : int,
    recursive = 1
) -> list:
    """
    Fungsi untuk memvisualisasikan proses pengurutan elemen suatu deret 
      yang dilakukan dengan algoritma `quick sort`
    PARAMETERS:
        1. deret -> list yang belum di sortir;
        2. N -> int berupa angka lebar layar;
        3. recursive -> penomoran proses dengan default angka 1.
    """
    # 1. Pastikan elemen deret > 1
    if len(deret) <= 1:
        # Jika tidak, proses berhenti dan kembalikan deret
        return deret
    
    # 2. Tentukan posisi dari elemen pivot
    pivot = deret[len(deret) // 2]

    # 3. Buat pesan pivot sebagai `keterangan`
    keterangan = f" PIVOT = {pivot} "
    
    # 5. Buat penanda progres partisi sebagai `item`
    item = f" PARTISI KE-{recursive} "

    # 6. Tampilkan `item` ke layar
    print(f"{item:=^{N}}")

    # 7. Tampilkan `deret` yang dipartisi dengan `print_satu_persatu`
    print_satu_persatu("", deret, N)

    # 8. Tampilkan `keterangan` ke layar sekaligus sebagai input
    input(f"\n{keterangan:-^{N}}")
    
    # 9. Proses deret untuk menghasilkan 3 partisi
    partisi_kiri = [x for x in deret if x < pivot]
    partisi_tengah = [x for x in deret if x == pivot]
    partisi_kanan = [x for x in deret if x > pivot]
    partisis = [partisi_kiri, partisi_tengah, partisi_kanan]
    
    # 10. Buat Pesan untuk masing-masing partisi
    pesans = [
      f"Elemen bernilai < {pivot}:", 
      f"Elemen bernilai = {pivot}:", 
      f"Elemen bernilai > {pivot}:"
    ]

    # 11. Tampilkan pesan dan partisi ke layar
    for pesan, partisi in zip(pesans, partisis):
      print_satu_persatu(pesan, partisi, N)
      input()
    # tengah = 
    # print_satu_persatu(tengah, partisi_tengah, N)
    # input()
    # kanan = 
    # print_satu_persatu(kanan, partisi_kanan, N)
    # input()

    # 12. Naikkan nomor proses untuk menandai progres recursive
    recursive +=1

    # 13. Gabungkan recursive partisi_kiri, partisi_tengah, dan recursive partisi_kanan sebagai output proses
    return quick_sort_show(partisi_kiri, N, recursive) + partisi_tengah + quick_sort_show(partisi_kanan, N, recursive)

def bubble_sort(
    deret : list
) -> list:
    """
    Fungsi untuk melakukan pengurutan elemen pada suatu deret 
      dengan menggunakan algoritma 'bubble sort`
    PARAMETERS:
        1. deret -> list yang belum disortir.
    """
    # 1. Buat copy dari `deret` yang diinput
    deret_ = deret.copy()
    
    # 2. Hitung jumlah elemen pada deret dan simpan sebagai `jumlah_elemen`
    jumlah_elemen = len(deret_)
    
    # 3. Lakukan iterasi untuk proses sorting sebanyak jumlah_elemen
    for i in range(jumlah_elemen):
        # Lakukan iterasi untuk proses perbandingan elemen dari kiri ke kanan
        for j in range(0, jumlah_elemen-i-1):
            # Jika elemen di kiri > elemen di kanan
            if deret_[j] > deret_[j+1]:
                # Tukar posisi elemen kiri ke sebelah kanan
                deret_[j], deret_[j+1] = deret_[j+1], deret_[j]

    # 4. Jadikan `deret_` sebagai output proses
    return deret_

def bubble_sort_show(
    deret : list,
    N : int
) -> list:
    """
    Fungsi untuk melakukan visualisasi bagi proses pengurutan deret 
      yang dilakukan dengan menggunakan algoritma `bubble sort`
    PARAMETERS:
        1. deret -> list yang belum disortir;
        2. N -> int dari angka lebar layar pada tampilan.
    """
    # 1. Mengimpor fungsi yang diperlukan
    import time

    # 2. Buat copy dari `deret` yang diinput
    deret_ = deret.copy()
    
    # 3. Hitung jumlah elemen pada deret yang akan di sort
    jumlah_elemen = len(deret_)
    
    # 4. Lakukan iterasi untuk proses sorting sebanyak `jumlah_elemen` kali
    for i in range(0, jumlah_elemen, 1):
        # A. Lakukan iterasi untuk proses perbandingan elemen paling kiri ke paling kanan pada deret
        for j in range(0, jumlah_elemen-i-1):
            # -. Apakah elemen di kiri > elemen di kanan
            if deret_[j] > deret_[j+1]:
                # Jika ya, tukar posisi elemen di kiri ke kanan
                deret_[j], deret_[j+1] = deret_[j+1], deret_[j]
            # -. Tampilkan hasil dari proses perbandingan secara animasi:
            # Buat Pesan simpan pada variabel `item`
            item=f"Proses ke-{i+1} : {deret_}"
            # Tampilkan `item` ke layar
            print(f"\r{item: ^{N}}", end="", flush=True)
            # - beri jeda antar proses agar animasi yang ditetapkan bisa terlihat
            time.sleep(0.9)
            
        # B. Tampilkan output akhir dari masing-masing iterasi proses
        item=f"Proses ke-{i+1} : {deret_}"
        print(f"\r{item: ^{N}}", end="")
        input()

    # 5. Jadikan `deret_` sebagai output proses
    return deret_

def elapsed_time(
    fungsi : object,
    deret : list
) -> object:
    """
    Fungsi untuk menghitung `elapsed time` pemrosesan 
      yang dilakukan oleh suatu fungsi terhadap sebuah deret
    PARAMETERS:
        1. fungsi -> object berupa fungsi yang akan dinilai `elapsed time`nya;
        2. deret -> list yang akan disortir dengan menggunakan fungsi.
    """
    # 1. Mengimpor fungsi yang akan dipergunakan
    import timeit
    
    # 2. Lakukan perhitungan elapsed time
    e_time = timeit.timeit(lambda: fungsi(deret), number=1)

    # 3. Jadikan `e_time` sebagai output proses
    return e_time

def generate_deret(
    jumlah_elemen : int,
    batas_bawah : int,
    batas_atas : int,
    seed : int = 10
) -> list:
    """
    FUNGSI UNTUK MEN-GENERATE DERET ACAK
    PARAMETERS:
      1. jumlah_elemen : Int, jumlah elemen deret yang akan digenerate;
      2. batas_bawah : Int, nilai batas bawah dari angka yang akan digenerate;
      3. batas_atas : Int, nilai batas atas dari angka yang akan digenerate;
      4. seed : Int, nilai seed bagi fungsi random, agar deret yang sama dapat
           digenerate ulang (nilai default = 10).
    """
    # 1. Mengimpor modul `random`
    import random
    
    # 2. Set seed pada nilai default = 10
    random.seed(seed)
    
    # 3. Generate deret
    deret = [random.randint(batas_bawah, batas_atas) for _ in range(0, jumlah_elemen)]
    
    # 4. Jadikan `deret` sebagai output proses
    return deret

def generate_time_complexity(
    fungsi1 : object,
    fungsi2 : object,
    ukuran_input : list,
    sims : int = 1
) -> tuple:
    """
    Fungsi untuk mencatat data jumlah elemen yang harus diproses (N), dan
      elapsed time yang diperlukan untuk memproses sejumlah elemen tersebut
      oleh dua buah proses sejenis yang menerapkan algoritma berbeda
    PARAMETERS:
        1. fungsi1 -> object, fungsi sortir pertama yang akan diperbandingkan;
        2. fungsi2 -> object, fungsi sortir kedua yang akan diperbandingkan;
        3. ukuran_input -> list berisi int, jumlah deret yang akan disortir;
        4. sims -> int, angka jumlah pengulangan simulasi yang dilakukan (secara default = 1 kali).
    """
    # 1. Mengimpor berbagai fungsi dan modul yang akan dipergunakan
    import pandas as pd, numpy as np, time
    
    # 2. List kosong untuk diisi dengan data hasil simulasi bernama `hasil`
    hasil = []
    
    # 3. Buat iterasi untuk simulasi sampling sebanyak `sims` kali
    for _ in range(0, sims, 1):
      # A. Buat iterasi untuk setiap elemen pada `ukuran_input`
      for ukuran in ukuran_input:
          # -. Generate deret acak menggunakan fungsi `generate_deret`
          deret = generate_deret(ukuran, 0, 100000)
          # -. Catat elapsed time dari `bubble_sort` pada `bubble_time`
          time1 = elapsed_time(fungsi1, deret)
          # -. Catat elapsed time dari `quick_sort` pada `quick_time`
          time2 = elapsed_time(fungsi2, deret)
          # -. Masukkan `dictionary` berisi hasil pencatatan ke list `hasil`
          hasil.append({'N':ukuran, 'simulasi_ke':_+1, fungsi1.__name__:time1, fungsi2.__name__:time2})
      # B. Buat Tampilan Notifikasi Progres Simulasi
      print(f"\rSimulasi ke-{_+1}", end="")
      time.sleep(0.2)
        
    # 4. Buat dataframe dari data pada list `hasil`, lalu rata-ratakan berdasarkan N
    df = pd.DataFrame(hasil)
    df_complexity = (df
                    .groupby("N")
                    .agg({fungsi1.__name__:'mean', fungsi2.__name__:'mean'}))
    
    # 5. Jadikan df_complexity sebagai output proses
    return df.set_index(['N', 'simulasi_ke']), df_complexity

def visual_sebaran(
    data: object, 
    output_path: str
) -> None:
    """
    Fungsi untuk membuat grafik sebaran dari sebuah dictionary
    dan menyimpan hasilnya dalam format `png`
    PARAMETERS:
    1. data -> object, dictionary;
    2. output_path -> str, path menyimpan file.
    """
    # 1. Import modul yang diperlukan
    import pandas as pd, matplotlib.pyplot as plt, seaborn as sns
    
    # 2. Buat dataframe dari `data` dictionary
    df = pd.DataFrame(data)
    
    # 3. Hitung jumlah data
    n = len(df)
    
    # 4. Set theme dan warna dari seaborn
    sns.set_theme('paper')
    sns.set_palette('pastel')

    # 5. Buat layer grafik
    fig, ax = plt.subplots(figsize=(10,5))

    # 6. Isikan data yang sudah dipersiapkan ke fungsi `boxplot`
    sns.violinplot(pd.melt(df), y='value', hue='variable', inner_kws=dict(box_width=5))

    # 7. Beri Label untuk y-axis
    ax.set_ylabel(f"Elapsed Time (detik)")

    # 8. Beri label untuk x-axis
    ax.set_xlabel(output_path)

    # 9. Beri Judul Grafik
    # ax.set_title(output_path)

    # 10. Simpan grafik ke file dan tampilkan ke layar
    plt.savefig(f"{output_path}.png", dpi=300, bbox_inches='tight')
    plt.show()

def buat_visualisasi(
    data : object,
    output_path : str
) -> None:
    """
    Fungsi untuk membuat grafik dari sebuah dataframe 
      dan menyimpan hasilnya dalam format `png`
    PARAMETERS:
        1. data -> object, dataframe yang akan divisualisasikan;
        2. output_path -> str, yang menunjukkan `path` dan nama_file dari output.
    """
    # 1. Mengimpor fungsi dan modul yang diperlukan
    import matplotlib.pyplot as plt, seaborn as sns
    
    # 2. Set `theme` dari grafik
    sns.set_theme('paper')
    sns.set_palette('pastel')
    
    # 3. Buat Layer Grafik
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # 4. Isikan data dari dataframe ke layer grafik yang telah dibuat
    sns.lineplot(data=data, ax=ax)
    
    # 5. Beri label untuk axis Y
    ax.set_ylabel("Average Elapsed Time (detik/proses)")
    
    # 6. Beri label untuk axis X
    ax.set_xlabel("Jumlah Elemen (N)")
    
    # 7. Simpan grafik ke file dan tampilkan ke layar
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()

def resize_picture():
    from PIL import Image
    file = input("Tuliskan Nama File:")
    image = Image.open(file)
    width = int(image.size[0]/2)
    height = int(image.size[1]/2)
    image.resize((width, height)).save(f"output/{file}")

def concat_list(daftar: list, joint: str) -> str:
  """
  Fungsi untuk menggabungkan elemen dari sebuah list menjadi sebuah string
  menggunakan sebuah karakter penghubung.
  ARGUMENTS:
    1. daftar: list, List yang elemennya akan digabungkan;
    2. joint: str, karakter yang dipergunakan sebagai penghubung.
  Output:
    Sebuah string yang merupakan gabungan dari elemen list yang diinput.
  """
  return f"{joint}".join(daftar)

def create_title_pattern(df: object, nama_kolom: str) -> str:
    """
    FUNGSI UNTUK MEMBUAT TITLE PATTERN DARI STR VALUE PADA SEBUAH KOLOM
    ARGUMENTS:
      1. df : object, dataframe yang akan dibuatkan pattern;
      2. nama_kolom : str, nama kolom yang valuenya berisi pattern.
    OUTPUT:
      Sebuah str berisi pattern titel.
    """
    import time

    # VALIDASI: Cek keberadaan nama_kolom
    if nama_kolom not in df.columns:
      raise ValueError(f"Kolom '{nama_kolom}' tidak ditemukan pada dataframe.")

    # List untuk menyimpan pattern yang diinput
    list_of_patterns = ['Mrs', 'Mr', 'Miss', 'Ms', 'Master']

    # Set variabel `tambah` ke True
    tambah = True
    while tambah:
        # Buat title_pattern, lakukan str concatenation (+) yang dikombinasikan dengan method .join()
        text_pattern = "("+concat_list(list_of_patterns, "|")+")"
        
        # Keterangan Proses
        print(f"{'':=^110}\n{'Pattern yang sudah ditambahkan ke list adalah sebagai berikut:': ^110}")
        print(f"{text_pattern: ^110}")
        input(f"{'':-^110}")

        # Cek df_titanic untuk title yang belum masuk list_of_titles
        list_of_names = list(df.loc[
          [False if len(y)>0 else True for y in df[nama_kolom].str.findall(pat=text_pattern)],
          [nama_kolom]][nama_kolom])
        jml_sisa_nama = len(list_of_names)
        
        print(f"{f'Nama-nama pada kolom Firstname = {jml_sisa_nama}': ^110}:")
        awal = 0
        for urutan in range(jml_sisa_nama//5):
          akhir = (urutan+1)*5
          print(list_of_names[awal:akhir])
          awal = akhir
        time.sleep(0.7)
        input(f"{'':-^110}")

        # Mintakan pattern baru ke user
        pattern_baru = input("Tuliskan title yang akan ditambahkan: ")

        # Tambahkan title_baru ke list_of_titles
        if pattern_baru not in list_of_patterns:
          list_of_patterns.append(pattern_baru)
          pesan = f"Pattern '{pattern_baru}' sudah ditambahkan ke list!"
        else:
          pesan = f"Pattern '{pattern_baru}' sudah ada sebelumnya pada list!"

        print(f"{pesan: ^110}\n{'':-^110}")

        # Tanya perlu tambah title_baru atau tidak?
        while True:
          pilihan = input(f"Masih ada pattern yang akan ditambahkan ke list? (1=ya/0=tidak)")
          if pilihan not in ['1', '0']:
            print(f"Pilihan '{pilihan}' tidak valid, silahkan diisi ulang!")
          else:
            tambah = True if pilihan=='1' else False
            print(f"{'':-^110}")
            break

    return "("+concat_list(list_of_patterns, "|")+")"

def explore_column_pattern(
    df: pd.DataFrame,
    kolom_filter: str,
    kolom_nilai: str,
    pattern: str,
    bins: int = 10
) -> None:
    """
    Fungsi untuk mengeksplorasi pola dari data pada kolom tertentu:
    1. Missing Values pada kolom dengan filter pattern;
    2. Statistik Deskriptif dari kolom nilai dengan filter pattern;
    3. Histogram sederhana.

    ARGUMEN:
        - df: pd.DataFrame, DataFrame yang berisi data;
        - kolom_filter: str, nama kolom yang akan difilter berdasarkan pattern;
        - kolom_nilai: str, nama kolom yang nilainya akan dianalisis;
        - pattern: str, pattern yang dicari dalam kolom_filter;
        - bins: int, jumlah bins untuk histogram.
    """
    # VALIDATION: Check if the columns exist
    if kolom_filter not in df.columns or kolom_nilai not in df.columns:
        raise ValueError(f"Kolom '{kolom_filter}' atau '{kolom_nilai}' tidak ditemukan dalam DataFrame.")

    # Filter DataFrame based on pattern in the specified column
    df_filtered = df[df[kolom_filter].str.contains(pattern, na=False)]

    # Display Missing Values for filtered rows
    print(
        f"{'':=^66}\n{'MISSING VALUES:': ^66}\n{'':-^66}\n",
        f"\r{df_filtered.isna().sum()}"
    )

    # Display Descriptive Statistics for filtered rows
    print(
        f"{'':=^66}\n{'DESCRIPTIVE STATS:': ^66}\n{'':-^66}\n",
        f"\r{df_filtered[kolom_nilai].describe()}"
    )

    # Plot histogram
    print(f"{'':=^66}\n{'SEBARAN DATA:': ^66}\n{'':-^66}\n")
    df_filtered[kolom_nilai].plot.hist(bins=bins)
    plt.title(f"Histogram of {kolom_nilai} for {pattern} in {kolom_filter}")
    plt.xlabel(kolom_nilai)
    plt.ylabel('Frequency')
    plt.show()

def fill_missing_value(
    df: pd.DataFrame,
    kolom_filter: str,
    filter_value: str,
    kolom_diisi: str,
    inplace: bool = True
) -> None:
  """
  Fungsi ini dipergunakan untuk melakukan pengisian nilai ke missing values
  pada kolom_diisi yang telah difilter pada kolom_filter.
  ARGUMEN:
    1. df: pd.DataFrame, dataframe yang akan diisi missing valuenya;
    2. kolom_filter: str, nama kolom pada dataframe yang akan difilter;
    3. filter_value: str, pattern dari filter yang diterapkan;
    4. kolom_diisi: str, kolom yang missing valuenya akan diisi;
    5. inplace: bool, default True merubah langsung pada df.
  """
  # VALIDASI: Cek keberadaan kolom
  if kolom_filter not in df.columns or kolom_diisi not in df.columns:
    raise ValueError(f"Kolom '{kolom_filter}' atau '{kolom_diisi}' tidak ditemukan dalam DataFrame.")

  # Siapkan berbagai filters
  filter_pertama = df[kolom_filter]==filter_value
  filter_kolom_kosong = df[kolom_diisi].isna()
  series_bahan = df.loc[filter_pertama][kolom_diisi]

  # Cek ketersediaan data setelah difilter
  if series_bahan.empty:
    raise ValueError(f"Tidak terdapat data yang cocok dengan filter '{filter_value}'!")

  # Pilih metode pengisian
  while True:
    pilihan = input(f"{'':=^66}\n\rPilih metode pengisian missing value: (1=Mean/2=Median/3=Modus) ")
    if pilihan in ['1', '2', '3']:
      break
    else:
      print("Pilihan tidak valid, silahkan pilih '1'. '2' atau '3'!")

  # Hitung nilai untuk missing value berdasarkan pilihan user
  isian = series_bahan.mean() if pilihan == '1' else series_bahan.median() if pilihan==2 else series_bahan.mode()

  # masukkan hasil perhitungan nilai ke dataframe
  if inplace:
    df.loc[filter_pertama & filter_kolom_kosong, [kolom_diisi]] = isian
    return df
  else:
    new_df = df.copy()
    new_df.loc[filter_pertama & filter_kolom_kosong, [kolom_diisi]] = isian
    return new_df
