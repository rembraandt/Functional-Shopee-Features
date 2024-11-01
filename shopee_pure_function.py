# Fitur 1: Pencarian Produk

def cari_produk(produk_list, kata_kunci):
    # Mencari produk yang mengandung kata kunci
    return [produk for produk in produk_list if kata_kunci.lower() in produk['nama'].lower()]

def filter_produk(produk_list, kategori):
    # Menyaring produk berdasarkan kategori
    return [produk for produk in produk_list if produk['kategori'] == kategori]

def sortir_produk(produk_list, kriteria):
    # Menyortir produk berdasarkan kriteria (misalnya: harga terendah)
    return sorted(produk_list, key=lambda produk: produk[kriteria])


# Fitur 2: Keranjang Belanja

def tambah_produk_ke_keranjang(keranjang, produk, jumlah):
    # Menambah produk ke keranjang (pure function, menghasilkan keranjang baru)
    produk_baru = {'produk': produk, 'jumlah': jumlah}
    return keranjang + [produk_baru]

def hitung_total_harga(keranjang):
    # Menghitung total harga dari semua produk di keranjang
    return sum(item['produk']['harga'] * item['jumlah'] for item in keranjang)

def hapus_produk_dari_keranjang(keranjang, produk_id):
    # Menghapus produk berdasarkan id dari keranjang
    return [item for item in keranjang if item['produk']['id'] != produk_id]


# Fitur 3: Pembayaran

def pilih_metode_pembayaran(opsi_pembayaran, metode_terpilih):
    # Memilih metode pembayaran (pure function)
    return metode_terpilih if metode_terpilih in opsi_pembayaran else None

def hitung_total_biaya(harga_total, ongkir):
    # Menghitung total biaya (harga produk + ongkir)
    return harga_total + ongkir

def cek_diskon(harga_total, diskon):
    # Menghitung harga setelah diskon
    return harga_total * (1 - diskon/100) if diskon else harga_total


# Fitur 4: Pengiriman

def pilih_jasa_pengiriman(opsi_jasa_pengiriman, jasa_terpilih):
    # Memilih jasa pengiriman (pure function)
    return jasa_terpilih if jasa_terpilih in opsi_jasa_pengiriman else None

def estimasi_waktu_pengiriman(jarak, kecepatan):
    # Menghitung estimasi waktu pengiriman (jarak / kecepatan)
    return jarak / kecepatan

def status_pengiriman(id_order, data_pengiriman):
    # Mendapatkan status pengiriman dari id_order
    return next((pengiriman['status'] for pengiriman in data_pengiriman if pengiriman['id_order'] == id_order), "Tidak ditemukan")


# Fitur 5: Penilaian Produk

def beri_penilaian(daftar_penilaian, id_produk, rating, ulasan):
    # Memberikan penilaian baru untuk produk (pure function)
    penilaian_baru = {'id_produk': id_produk, 'rating': rating, 'ulasan': ulasan}
    return daftar_penilaian + [penilaian_baru]

def filter_ulasan(daftar_penilaian, bintang):
    # Menyaring ulasan berdasarkan jumlah bintang
    return [penilaian for penilaian in daftar_penilaian if penilaian['rating'] == bintang]

def rata_rata_penilaian(daftar_penilaian):
    # Menghitung rata-rata penilaian
    total_rating = sum(penilaian['rating'] for penilaian in daftar_penilaian)
    jumlah_ulasan = len(daftar_penilaian)
    return total_rating / jumlah_ulasan if jumlah_ulasan > 0 else 0


# Test Program
if __name__ == "__main__":
    # Contoh data produk
    produk_list = [
        {'id': 1, 'nama': 'Handphone', 'kategori': 'Elektronik', 'harga': 3000000},
        {'id': 2, 'nama': 'Laptop', 'kategori': 'Elektronik', 'harga': 8000000},
        {'id': 3, 'nama': 'Kamera', 'kategori': 'Elektronik', 'harga': 5000000},
        {'id': 4, 'nama': 'Baju', 'kategori': 'Fashion', 'harga': 150000},
    ]

    # Contoh data keranjang
    keranjang = [
        {'produk': produk_list[0], 'jumlah': 2},
        {'produk': produk_list[1], 'jumlah': 1}
    ]

    # Contoh data pengiriman
    data_pengiriman = [
        {'id_order': 101, 'status': 'Sedang dikirim'},
        {'id_order': 102, 'status': 'Sudah sampai'},
    ]

    # Contoh penilaian produk
    daftar_penilaian = [
        {'id_produk': 1, 'rating': 5, 'ulasan': 'Bagus sekali!'},
        {'id_produk': 2, 'rating': 4, 'ulasan': 'Baik, tapi bisa lebih baik.'},
    ]

    # Fitur Pencarian Produk
    hasil_cari = cari_produk(produk_list, 'handphone')
    hasil_filter = filter_produk(produk_list, 'Elektronik')
    hasil_sortir = sortir_produk(produk_list, 'harga')
    
    print("Hasil Pencarian Produk:", hasil_cari)
    print("Hasil Filter Produk:", hasil_filter)
    print("Hasil Sortir Produk:", hasil_sortir)

    # Fitur Keranjang Belanja
    keranjang_baru = tambah_produk_ke_keranjang(keranjang, produk_list[2], 1)
    total_harga = hitung_total_harga(keranjang_baru)
    keranjang_setelah_hapus = hapus_produk_dari_keranjang(keranjang_baru, 1)
    
    print("\nKeranjang Baru:", keranjang_baru)
    print("Total Harga:", total_harga)
    print("Keranjang Setelah Hapus:", keranjang_setelah_hapus)

    # Fitur Pembayaran
    metode_pembayaran = pilih_metode_pembayaran(['Transfer', 'COD', 'E-Wallet'], 'COD')
    total_biaya = hitung_total_biaya(1000000, 20000)
    harga_diskon = cek_diskon(total_biaya, 10)
    
    print("\nMetode Pembayaran:", metode_pembayaran)
    print("Total Biaya:", total_biaya)
    print("Harga Setelah Diskon:", harga_diskon)

    # Fitur Pengiriman
    jasa_terpilih = pilih_jasa_pengiriman(['JNE', 'J&T', 'Shopee Express'], 'J&T')
    estimasi = estimasi_waktu_pengiriman(100, 60)
    status = status_pengiriman(101, data_pengiriman)
    
    print("\nJasa Pengiriman Terpilih:", jasa_terpilih)
    print("Estimasi Waktu Pengiriman (jam):", estimasi)
    print("Status Pengiriman:", status)

    # Fitur Penilaian Produk
    penilaian_baru = beri_penilaian(daftar_penilaian, 3, 4, "Cukup bagus")
    ulasan_bintang_5 = filter_ulasan(penilaian_baru, 5)
    rata_rata = rata_rata_penilaian(penilaian_baru)
    
    print("\nPenilaian Baru:", penilaian_baru)
    print("Ulasan Bintang 5:", ulasan_bintang_5)
    print("Rata-rata Penilaian:", rata_rata)
