# 'kullanici_yonetimi' modülünden 'kart_id_ile_kullanici_bul' fonksiyonunu içe aktarıyoruz.
# Bu fonksiyon, kart ID'ye göre kullanıcı bilgilerini getirir.
from kullanici_yonetimi import kart_id_ile_kullanici_bul

# 'log_yonetimi' modülünden 'log_kaydet' fonksiyonunu içe aktarıyoruz.
# Bu fonksiyon, giriş ve çıkış işlemlerinin log kayıtlarını tutar.
from log_yonetimi import log_kaydet

def kullanici_giris(kart_id):
    """
    Verilen kart ID'ye göre kullanıcı girişi yapar.
    Kart ID'si tanınırsa giriş log kaydı oluşturur ve kullanıcıya bilgi verir.
    Tanınmazsa kullanıcıya kart ID'sinin tanınmadığını bildirir.
    
    Args:
        kart_id (str): Kullanıcının kart ID'si.
    
    Returns:
        str: Giriş işleminin sonucunu belirten mesaj.
    """
    # Kart ID'ye göre kullanıcıyı buluyoruz.
    kullanici = kart_id_ile_kullanici_bul(kart_id)
    if kullanici:
        # Kullanıcı bulunduysa giriş log kaydı oluşturuyoruz.
        log_kaydet(kullanici[0], 'giris')
        # Kullanıcının içeri girdiğini belirten mesaj döndürüyoruz.
        return f"{kullanici[1]} içeri girdi."
    else:
        # Kullanıcı bulunamadıysa kart ID'sinin tanınmadığını belirten mesaj döndürüyoruz.
        return "Kart ID tanınmadı."

def kullanici_cikis(kart_id):
    """
    Verilen kart ID'ye göre kullanıcı çıkışı yapar.
    Kart ID'si tanınırsa çıkış log kaydı oluşturur ve kullanıcıya bilgi verir.
    Tanınmazsa kullanıcıya kart ID'sinin tanınmadığını bildirir.
    
    Args:
        kart_id (str): Kullanıcının kart ID'si.
    
    Returns:
        str: Çıkış işleminin sonucunu belirten mesaj.
    """
    # Kart ID'ye göre kullanıcıyı buluyoruz.
    kullanici = kart_id_ile_kullanici_bul(kart_id)
    if kullanici:
        # Kullanıcı bulunduysa çıkış log kaydı oluşturuyoruz.
        log_kaydet(kullanici[0], 'cikis')
        # Kullanıcının dışarı çıktığını belirten mesaj döndürüyoruz.
        return f"{kullanici[1]} dışarı çıktı."
    else:
        # Kullanıcı bulunamadıysa kart ID'sinin tanınmadığını belirten mesaj döndürüyoruz.
        return "Kart ID tanınmadı."

if __name__ == '__main__':
    # Test senaryoları için örnek kullanıcı giriş ve çıkışı yapıyoruz.
    # '123456' kart ID'si ile kullanıcı girişi yapıyoruz ve sonucu yazdırıyoruz.
    print(kullanici_giris('123456'))
    # '123456' kart ID'si ile kullanıcı çıkışı yapıyoruz ve sonucu yazdırıyoruz.
    print(kullanici_cikis('123456'))
