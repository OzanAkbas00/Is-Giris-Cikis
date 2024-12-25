# Giriş Çıkış Sistemi

## Proje Açıklaması
Bu proje, kullanıcıların giriş ve çıkışlarını yönetmek için tasarlanmış bir sistemdir. Sistemde yeni kullanıcılar eklenebilir, mevcut kullanıcıların giriş ve çıkışları kaydedilebilir ve log kayıtları görüntülenebilir. Sadece admin yetkisine sahip kullanıcılar yeni kullanıcı ekleyebilir, tüm kullanıcıları görüntüleyebilir ve log kayıtlarını inceleyebilir.

## Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.x
- Pandas
- Openpyxl
- Sqlite3

### Proje Dosyaları
- `kullanici_yonetimi.py`: Kullanıcı yönetimi işlemlerini içerir.
- `log_yonetimi.py`: Log yönetimi işlemlerini içerir.
- `veritabani.py`: Veritabanı bağlantısı ve tablo oluşturma işlemlerini içerir.
- `admin_modulu.py`: Admin yetkisi gerektiren işlemleri içerir.
- `main.py`: Ana çalışma dosyası.

### Kurulum
- Proje dosyalarını aynı dizine indirin.
- Gerekli Python paketlerini yükleyin:
  ```bash
  pip install pandas openpyxl

## Çalıştırma
* `main.py` dosyasını çalıştırın:
  ```bash
  python main.py
 ## Kullanım
 ## Ana Menü
1. Yeni Kullanıcı Ekle (Admin Yetkisi Gerektirir)
2. Kullanıcı Girişi
3. Kullanıcı Çıkışı
4. Tüm Kullanıcıları Görüntüle (Admin Yetkisi Gerektirir)
5. Çıkış

*   1.Yeni Kullanıcı Ekle: Admin yetkisi gerektirir. Kullanıcı adı ve rol bilgileri girilir.
*   2.Kullanıcı Girişi: Kullanıcı kart ID'si girilir ve giriş işlemi loglanır.
* 3.Kullanıcı Çıkışı: Kullanıcı kart ID'si girilir ve çıkış işlemi loglanır.
* 4.Tüm Kullanıcıları Görüntüle: Admin yetkisi gerektirir. Tüm kullanıcılar görüntülenir.
* 5.Çıkış: Sistemden çıkış yapılır.
## Fonksiyonlar
* `admin_giris()`: Admin girişi için şifre kontrolü yapar.
* `yeni_kullanici_ekle()`: Yeni kullanıcı ekleme işlemini gerçekleştirir.
* `tum_kullanicilari_goruntule()`: Tüm kullanıcıları görüntüler.
* `loglari_goruntule()`: Log kayıtlarını görüntüler.
* `rastgele_kart_id_olustur()`: Rastgele kart ID oluşturur.
* `kullanici_ekle(isim, rol)`: Yeni kullanıcı ekler.
* `kart_id_ile_kullanici_bul(kart_id)`: Kart ID ile kullanıcı bulur.
* `tum_kullanicilari_getir()`: Tüm kullanıcıları getirir.
* `log_kaydet(kullanici_id, islem)`: Log kaydı yapar.
#### Katkıda Bulunma
Katkıda bulunmak için pull request gönderebilir veya issue açabilirsiniz.
#### İletişim
Proje ile ilgili sorularınız için 202307105043@dogus.edu.tr adresinden iletişime geçebilirsiniz.
