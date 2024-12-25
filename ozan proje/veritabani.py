import sqlite3

def baglanti_olustur():
    try:
        # SQLite veritabanına bağlan
        baglanti = sqlite3.connect('gecis_sistemi.db')
        return baglanti
    except sqlite3.Error as e:
        # Bağlantı hatası durumunda hatayı yukarıya ileterek işlemi durdur
        raise

def tablo_olustur():
    try:
        # Veritabanı bağlantısını oluştur
        baglanti = baglanti_olustur()
        
        # Bağlantı üzerinde bir imleç oluştur
        imlec = baglanti.cursor()

        # Kullanıcılar tablosunu oluştur
        imlec.execute('''CREATE TABLE IF NOT EXISTS kullanicilar (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            isim TEXT NOT NULL,
                            rol TEXT NOT NULL,
                            kart_id TEXT UNIQUE NOT NULL
                          )''')

        # Loglar tablosunu oluştur
        imlec.execute('''CREATE TABLE IF NOT EXISTS loglar (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            kullanici_id INTEGER,
                            zaman DATETIME DEFAULT CURRENT_TIMESTAMP,
                            islem TEXT NOT NULL,
                            FOREIGN KEY(kullanici_id) REFERENCES kullanicilar(id)
                          )''')

        # Değişiklikleri kaydet
        baglanti.commit()
    except sqlite3.Error as e:
        # SQLite hata durumunda hatayı yukarıya ileterek işlemi durdur
        raise
    finally:
        # Bağlantıyı kapat (hata olsa bile)
        baglanti.close()
