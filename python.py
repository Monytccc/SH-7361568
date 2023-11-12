import time
import requests

url = "https://qlizz.com/bif/send"
params = {'userId': 'herl4mbang'}

def run_script():
    # Lakukan POST request
    response = requests.post(url, params=params)

    # Cek status code
    if response.status_code == 200:
        print("Request berhasil dengan status code 200")
        print("Response:")
        print(response.text)
    else:
        print(f"Request gagal dengan status code {response.status_code}")

# Buat loop untuk menjalankan script setiap 12 jam
while True:
    run_script()
    time.sleep(43200)  # 43200 detik = 12 jam
