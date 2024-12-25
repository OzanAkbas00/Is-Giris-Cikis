from kullanici_yonetimi import kart_id_ile_kullanici_bul
from log_yonetimi import log_kaydet
from veritabani import tablo_olustur
import admin_modulu as admin

# Ana fonksiyon
def ana():
    tablo_olustur()  # Veritabanı tablolarını oluştur
    while True:
        # Kullanıcıya menü seçeneklerini göster
        print("\nGiriş Çıkış Sistemi")
        print("1. Yeni Kullanıcı Ekle (Admin Yetkisi Gerektirir)")
        print("2. Kullanıcı Girişi")
        print("3. Kullanıcı Çıkışı")
        print("4. Tüm Kullanıcıları Görüntüle (Admin Yetkisi Gerektirir)")
        print("5. Çıkış")
        secim = input("Bir seçenek seçin: ")  # Kullanıcıdan seçim yapmasını iste

        if secim == '1':
            admin.yeni_kullanici_ekle()  # Yeni kullanıcı ekle

        elif secim == '2':
            kart_id = input("Kart ID girin: ")  # Kart ID'sini al
            kullanici = kart_id_ile_kullanici_bul(kart_id)  # Kart ID ile kullanıcıyı bul
            if kullanici:
                print(kullanici[1], "içeri girdi.")  # Kullanıcının içeri girdiğini yazdır
                log_kaydet(kullanici[0], 'giris')  # Giriş işlemini logla
            else:
                print("Kart ID tanınmadı.")  # Kart ID tanınmazsa hata mesajı yazdır

        elif secim == '3':
            kart_id = input("Kart ID girin: ")  # Kart ID'sini al
            kullanici = kart_id_ile_kullanici_bul(kart_id)  # Kart ID ile kullanıcıyı bul
            if kullanici:
                print(kullanici[1], "dışarı çıktı.")  # Kullanıcının dışarı çıktığını yazdır
                log_kaydet(kullanici[0], 'cikis')  # Çıkış işlemini logla
            else:
                print("Kart ID tanınmadı.")  # Kart ID tanınmazsa hata mesajı yazdır

        elif secim == '4':
            admin.tum_kullanicilari_goruntule()  # Tüm kullanıcıları görüntüle

        elif secim == '5':
            break  # Çıkış yap

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")  # Geçersiz seçim için hata mesajı yazdır

if __name__ == '__main__':
    ana()  # Ana fonksiyonu çalıştır
