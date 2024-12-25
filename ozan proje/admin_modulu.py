# Kullanıcı yönetimi ve log yönetimi modüllerinden gerekli fonksiyonları içe aktarıyoruz
from kullanici_yonetimi import kullanici_ekle, tum_kullanicilari_getir
from log_yonetimi import loglari_goruntule

# Admin girişi fonksiyonu
def admin_giris():
    admin_sifre = input("Admin şifresini girin: ")  # Admin şifresi kullanıcıdan istenir
    if admin_sifre == 'admin123':  # Şifre kontrolü yapılır
        return True  # Şifre doğru ise True döner
    else:
        print("Admin şifresi yanlış!")  # Şifre yanlış ise hata mesajı verir
        return False  # Yanlış şifre için False döner

# Yeni kullanıcı ekleme fonksiyonu
def yeni_kullanici_ekle():
    if admin_giris():  # Admin girişi başarılı ise
        isim = input("İsim girin: ")  # Kullanıcının ismi istenir
        rol = input("Rol girin: ")  # Kullanıcının rolü istenir
        kullanici_ekle(isim, rol)  # Yeni kullanıcı eklenir

# Tüm kullanıcıları görüntüleme fonksiyonu
def tum_kullanicilari_goruntule():
    if admin_giris():  # Admin girişi başarılı ise
        kullanicilar = tum_kullanicilari_getir()  # Tüm kullanıcılar getirilir
        for kullanici in kullanicilar:  # Her bir kullanıcı için
            print(kullanici)  # Kullanıcı bilgileri yazdırılır
