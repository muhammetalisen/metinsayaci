from collections import Counter

def kelime_sayaci(metin):
    # Metni küçük harfe çevir ve boşlukları temizle
    kelimeler = metin.lower().split()
    # Kelimelerin frekansını hesapla
    frekans = Counter(kelimeler)
    return frekans

def kelime_sayaci_uygulamasi():
    metin = input("Bir metin girin: ")
    frekans = kelime_sayaci(metin)
    print("Kelime frekansları:")
    for kelime, miktar in frekans.items():
        print(f"'{kelime}': {miktar}")

kelime_sayaci_uygulamasi()
