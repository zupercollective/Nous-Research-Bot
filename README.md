Penulis: [luthfi0x]([link_twt](https://x.com/luthfi0x))

# Pengenalan
Bab ini berisi pengenalan mengenai Nous Research

## Nous Research
> [!NOTE]
> Nous Research adalah sebuah project yang berfokus dalam pengembangan large-language model yang bersifat terbuka dan _human-centric_

### Investor
![image](https://github.com/user-attachments/assets/d8debf4c-3da4-4d80-9f13-4338156ae2e5)

# Tutorial Bot Nous Research
Bab ini berisi tutorial cara menjalankan bot conversation menggunakan API Nous

## Requirement
Syarat menjalankan bot
- Spek Komputer
  
| Name | Minimum |
| ------------- | ------------- |
| Operating System  | OS_NAME  |
| CPU  | 1 Cores  |
| RAM  | 1 GB  |
| SSD  | 25 GB  |
- API Key. Kalau belum buat dulu [keynya](https://portal.nousresearch.com/api-keys)

> [!TIP]
> Kami menggunakan Digital Ocean dengan speksifikasi `Singapore/ 1 Core/ 1 GB RAM/ 80 GB SSD`. Jika kamu membutuhkan VPS, kami memiliki link gratis credit VPS DigitalOcean sebesar $200. Cukup untuk menjalankan XXX selama XX . Daftar sekarang dengan [link utama]([link_reff_do_kamu](https://m.do.co/c/497333605c2e) untuk mendapatkannya.
  
## Dependencies

### Install Python3
```
sudo apt update
sudo apt install python3
```

## Menjalankan Nous Bot

### Download Repo ini
```
git pull https://github.com/zupercollective/Nous-Research-Bot.git
nano conversation.py
```

### Adjust API Key dan Model 
```
API_KEY = "masukkan_api_key"  # Ubah dengan API key milik kamu
MODEL = "masukkan_model" # Pilih model yang ingin kamu gunakan.
```

Jangan lupa disave. Control + X

### Run Bot
```
python3 covnersation.py
```

## Help

Join komunitas [Discord ZuperCollective](https://discord.com/invite/zupercollective) jika kamu ada pertanyaan.

## Change Logs

* 0.0.1
    * Initial Release
