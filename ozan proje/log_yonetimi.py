import pandas as pd
from openpyxl import load_workbook
from datetime import datetime
import os

# Log kaydetme fonksiyonu
def log_kaydet(kullanici_id, islem):
    try:
        tarih = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Geçerli tarih ve saati al
        log_df = pd.DataFrame({'Tarih': [tarih], 'Kullanici_ID': [kullanici_id], 'Islem': [islem]})  # Yeni log verisini oluştur

        if not os.path.exists('log_kayitlari.xlsx'):  # Log dosyası yoksa
            log_df.to_excel('log_kayitlari.xlsx', index=False)  # Yeni log dosyası oluştur ve logları yaz
        else:
            mevcut_loglar = pd.read_excel('log_kayitlari.xlsx')  # Mevcut log dosyasını oku
            yeni_loglar = pd.concat([mevcut_loglar, log_df], ignore_index=True)  # Yeni logları mevcut loglara ekle
            yeni_loglar.to_excel('log_kayitlari.xlsx', index=False)  # Güncellenmiş logları dosyaya yaz
        
    except Exception as e:
        print(f'Hata: {e}')  # Hata durumunda hata mesajını yazdır

# Logları görüntüleme fonksiyonu
def loglari_goruntule():
    try:
        if os.path.exists('log_kayitlari.xlsx'):  # Log dosyası varsa
            loglar = pd.read_excel('log_kayitlari.xlsx')  # Log dosyasını oku
            print(loglar)  # Logları yazdır
        else:
            print("Log kaydı bulunamadı.")  # Log dosyası yoksa mesaj yazdır
    except Exception as e:
        print(f'Hata: {e}')  # Hata durumunda hata mesajını yazdır
