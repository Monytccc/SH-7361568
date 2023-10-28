import requests
import time

def submit_form(url, userId):
    # Buat request POST ke URL formulir
    payload = {"userId": userId}
    response = requests.post(url, data=payload)

    # Cek status kode respons
    if response.status_code == 200:
        # Jika berhasil, cetak pesan sukses
        print("Formulir berhasil dikirim!")
    else:
        # Jika gagal, cetak pesan kesalahan
        print("Ada kesalahan saat mengirim formulir:", response.status_code)


# Contoh penggunaan
url = "https://buyinstafollowers.xyz/"
userId = "herl4mbang"

# Kirim formulir
submit_form(url, userId)

# Tunda pengiriman formulir selama 12 jam
time.sleep(43200)

# Kirim formulir lagi
submit_form(url, userId)
