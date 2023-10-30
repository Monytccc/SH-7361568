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

# Buat fungsi untuk mengeksekusi script
def execute_script():
    # Cetak waktu eksekusi
    print("Script dieksekusi pada:", time.strftime("%d %b %Y %H:%M:%S"))
    # Jalankan fungsi submit_form
    submit_form(url, userId)

# Eksekusi script
while True:
    execute_script()
    # Tunda eksekusi selama 12 jam
    time.sleep(60 * 60 * 12)
