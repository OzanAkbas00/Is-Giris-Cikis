import sqlite3
from veritabani import baglanti_olustur
import random

# Rastgele kart ID oluşturma fonksiyonu
def rastgele_kart_id_olustur():
    return ''.join([str(random.randint(0, 9)) for _ in range(8)])  # 8 haneli rastgele bir sayı oluştur

# Kullanıcı ekleme fonksiyonu
def kullanici_ekle(isim, rol):
    try:
        kart_id = rastgele_kart_id_olustur()  # Rastgele kart ID oluştur
        baglanti = baglanti_olustur()  # Veritabanı bağlantısı oluştur
        imlec = baglanti.cursor()
        imlec.execute('INSERT INTO kullanicilar (isim, rol, kart_id) VALUES (?, ?, ?)', (isim, rol, kart_id))  # Kullanıcıyı veritabanına ekle
        baglanti.commit()
        print(f"Kullanıcı başarıyla eklendi. Kart ID: {kart_id}")  # Rastgele kart ID'yi yazdır
    except sqlite3.Error as e:
        raise  # Hata durumunda hatayı tekrar yükselt
    finally:
        baglanti.close()  # Bağlantıyı kapat

# Kart ID ile kullanıcı bulma fonksiyonu
def kart_id_ile_kullanici_bul(kart_id):
    try:
        baglanti = baglanti_olustur()  # Veritabanı bağlantısı oluştur
        imlec = baglanti.cursor()
        imlec.execute('SELECT * FROM kullanicilar WHERE kart_id = ?', (kart_id,))  # Kart ID ile kullanıcıyı bul
        kullanici = imlec.fetchone()  # Tek bir kullanıcıyı al
        return kullanici  # Kullanıcıyı döndür
    except sqlite3.Error as e:
        raise  # Hata durumunda hatayı tekrar yükselt
    finally:
        baglanti.close()  # Bağlantıyı kapat

# Tüm kullanıcıları getirme fonksiyonu
def tum_kullanicilari_getir():
    try:
        baglanti = baglanti_olustur()  # Veritabanı bağlantısı oluştur
        imlec = baglanti.cursor()
        imlec.execute('SELECT * FROM kullanicilar')  # Tüm kullanıcıları seç
        kullanicilar = imlec.fetchall()  # Tüm kullanıcıları al
        return kullanicilar  # Kullanıcıları döndür
    except sqlite3.Error as e:
        raise  # Hata durumunda hatayı tekrar yükselt
    finally:
        baglanti.close()  # Bağlantıyı kapat
