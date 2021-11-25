# API
Model TimeSeriesForest dataset gladius


# Instalasi Python

Pastikan sudah terinstall python dan pip dalam system anda, jika system anda mengunakan linux
bisa mengikuti command di bawah ini

`
sudo apt install python3-pip
`

jika system mengunakan OS windows atau yang lain bisa minjau situs resmi python untuk instalasi python
https://www.python.org/downloads/

# Instalasi Dependency 
Agar code dapat berjalan di perlukan beberapa dependecy, dapat langsung menjalankan command di terminal 
berikut satu demi satu jika python dan pip sudah terinstall

```
pip install fastapi
pip install uvicorn[standard]
pip install pyts # Dependency baru
```

# Menjalankan API
untuk menjalankan API cukup mejalankan command berikut di terminal
```
uvicorn main:app --reload
```

secara default dia akan jalan secara lokal di 127.0.0.1 dengan port 8000 
Output jika runnning berhasil

