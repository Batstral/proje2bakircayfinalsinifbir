# Gerekli kütüphanelerin import edilmesi
import pandas as pd
import personel
import doktor
import hemsire
import hasta

# Kodu çalıştırınca tüm satırın gözükmesi için gerekli kod satırı
pd.set_option('display.max_columns', None)


def main():
    print("Hastane Yönetim Sistemine Hoşgeldiniz.")

    # Dataframe için hazırlık
    data = []
    sutunlar = ['personel_no', 'ad',
                'soyad', 'departman', 'maas', 'uzmanlik', 'deneyim_yili', 'hastane', 'calisma_saati', 'sertifika',
                'hasta_no', 'dogum_tarihi', 'hastalik', 'tedavi']
    df = pd.DataFrame(data, columns=sutunlar)

    # Hazır nesnelerin oluşturulması
    hpersonel1 = personel.Personel(1, "Renas", "Taş", "Hasta Kabul", 17002)
    hpersonel2 = personel.Personel(2, "Ahmet Hasan", "Uçar", "İstatistik", 19530)
    hdoktor1 = doktor.Doktor(100, "Muhammed Can", "Arıca", "Cerrahi Departmanı",
                             53000, "Genel Cerrah", 20, "Malatya Eğitim ve Araştırma Hastanesi")
    hdoktor2 = doktor.Doktor(101, "Seray", "Fırıncıoğulları", "Kadın Hastalıkları", 37000,
                             "Psikoloji", 6, "Antakya Devlet Hastanesi")
    hdoktor3 = doktor.Doktor(102, "Batuhan", "Parıltı", "Nöroloji", 83032,
                             "Nöroinfeksiyon", 31, "Bursa Şehir Hastanesi")
    hhemsire1 = hemsire.Hemsire(200, "Zeynep Sude", "Kuru", "Nöroloji", 62120, 72,
                                "Sertifikalı Nörobilim Kayıtlı Hemşire (CNRN)", "Bursa Şehir Hastanesi")
    hhemsire2 = hemsire.Hemsire(201, "Emirhan", "Oğuz", "Cerrahi Hemşirelik", 32500,
                                60, "İleri Kardiyak Yaşam Desteği (ACLS)", "Malatya Eğitim ve Araştırma Hastanesi")
    hhemsire3 = hemsire.Hemsire(202, "Seçil", "Taş", "Kadın Sağlığı ve Doğum Hemşireliği",
                                20054, 48, "Laktasyon Danışmanlığı Sertifikası (IBCLC)", "Antakya Devlet Hastanesi")
    hhasta1 = hasta.Hasta(1, "Mehmet Akif", "Duman", "30-03-2004", "Kolorektal Hastalıklar", "Cerrahi Müdahale")
    hhasta2 = hasta.Hasta(2, "Muhammet Faik", "Duman", "23-03-2004", "Nörosifiliz", "Kortikosteroid")
    hhasta3 = hasta.Hasta(3, "Gülten", "Gülenç", "01-11-2005", "Menopoz ve Postmenopozal Sağlık", "Medikal Tedavi")

    # Boş listelerin açılması (sadece hazır personelleri içeren)
    hemsireler = [hhemsire1, hhemsire2, hhemsire3]
    doktorlar = [hdoktor1, hdoktor2, hdoktor3]
    hastalar = [hhasta1, hhasta2, hhasta3]
    personeller = [hpersonel1, hpersonel2]

    for insan in doktorlar:
        yeni_satir = pd.DataFrame([{'personel_no': insan.get_personel_no,
                                    'ad': insan.get_ad,
                                    'soyad': insan.get_soyad,
                                    'departman': insan.get_departman,
                                    'maas': insan.get_maas,
                                    'uzmanlik': insan.get_uzmanlik,
                                    'deneyim_yili': insan.get_deneyim_yili,
                                    'hastane': insan.get_hastane,
                                    'calisma_saati': None,
                                    'sertifika': None,
                                    'hasta_no': None,
                                    'dogum_tarihi': None,
                                    'hastalik': None,
                                    'tedavi': None}])
        df = pd.concat([df, yeni_satir], ignore_index=True)

    for insan in hemsireler:
        yeni_satir = pd.DataFrame([{'personel_no': insan.get_personel_no,
                                    'ad': insan.get_ad,
                                    'soyad': insan.get_soyad,
                                    'departman': insan.get_departman,
                                    'maas': insan.get_maas,
                                    'uzmanlik': None,
                                    'deneyim_yili': None,
                                    'hastane': insan.get_hastane,
                                    'calisma_saati': insan.get_calisma_saati,
                                    'sertifika': insan.get_sertifika,
                                    'hasta_no': None,
                                    'dogum_tarihi': None,
                                    'hastalik': None,
                                    'tedavi': None}])
        df = pd.concat([df, yeni_satir], ignore_index=True)

    for insan in personeller:
        yeni_satir = pd.DataFrame([{'personel_no': insan.get_personel_no,
                                    'ad': insan.get_ad,
                                    'soyad': insan.get_soyad,
                                    'departman': insan.get_departman,
                                    'maas': insan.get_maas,
                                    'uzmanlik': None,
                                    'deneyim_yili': None,
                                    'hastane': None,
                                    'calisma_saati': None,
                                    'sertifika': None,
                                    'hasta_no': None,
                                    'dogum_tarihi': None,
                                    'hastalik': None,
                                    'tedavi': None}])
        df = pd.concat([df, yeni_satir], ignore_index=True)

    for insan in hastalar:
        yeni_satir = pd.DataFrame([{'personel_no': None,
                                    'ad': insan.get_ad,
                                    'soyad': insan.get_soyad,
                                    'departman': None,
                                    'maas': None,
                                    'uzmanlik': None,
                                    'deneyim_yili': None,
                                    'hastane': None,
                                    'calisma_saati': None,
                                    'sertifika': None,
                                    'hasta_no': insan.get_hasta_no,
                                    'dogum_tarihi': insan.get_dogum_tarihi,
                                    'hastalik': insan.get_hastalik,
                                    'tedavi': insan.get_tedavi}])
        df = pd.concat([df, yeni_satir], ignore_index=True)

    while True:
        print("Yapmak istediğiniz işlemi"
              "\n(1)Hazır Nesneleri Kullan"
              "\n2) Yeni Nesneleri Ata"
              "\n3) Çıkış Yap)")
        sec = int(input("giriniz: "))
        if sec == 1:
            print(df)

        elif sec == 2:
            print("Yapmak istediğiniz işlemi"
                  "\n(1) Personel Ata"
                  "\n2) Doktor Ata"
                  "\n3) Hemşire Ata"
                  "\n4) Hasta Ata"
                  "\n9) Çıkış Yap)")
            secim = int(input("giriniz: "))

            if secim == 1:
                pno = int(input("Personel No: "))
                pad = input("Personel Adı: ")
                psoyad = input("Personel Soyad: ")
                pdepartman = input("Personel Departman: ")
                pmaas = int(input("Personel Maaş: "))
                yeni_personel = personel.Personel(pno, pad, psoyad, pdepartman, pmaas)
                personeller.append(yeni_personel)
                yeni_satir = pd.DataFrame([{'personel_no': pno, 'ad': pad, 'soyad': psoyad, 'departman': pdepartman,
                                            'maas': pmaas}])
                df = pd.concat([df, yeni_satir], ignore_index=True)

            elif secim == 2:
                pno = int(input("Personel No: "))
                pad = input("Personel Adı: ")
                psoyad = input("Personel Soyad: ")
                pdepartman = input("Personel Departman: ")
                pmaas = int(input("Personel Maaş: "))
                duz = input("Doktor Uzmanlığı: ")
                ddy = int(input("Doktor Deneyim Yılı: "))
                dh = input("Doktor Çalıştığı Hastane: ")
                yeni_doktor = doktor.Doktor(pno, pad, psoyad, pdepartman, pmaas, duz, ddy, dh)
                doktorlar.append(yeni_doktor)
                yeni_satir = pd.DataFrame([{'personel_no': pno, 'ad': pad, 'soyad': psoyad, 'departman': pdepartman,
                                            'maas': pmaas, 'uzmanlık': duz, 'deneyim_yili': ddy, 'hastane': dh}])
                df = pd.concat([df, yeni_satir], ignore_index=True)

            elif secim == 3:
                pno = int(input("Personel No: "))
                pad = input("Personel Adı: ")
                psoyad = input("Personel Soyad: ")
                pdepartman = input("Personel Departman: ")
                pmaas = int(input("Personel Maaş: "))
                hecs = int(input("Hemşire Çalışma Saati: "))
                hes = input("Hemşire Sertifikası: ")
                heh = input("Hemşire Çalıştığı Hastane: ")
                yeni_hemsire = hemsire.Hemsire(pno, pad, psoyad, pdepartman, pmaas, hecs, hes, heh)
                hemsireler.append(yeni_hemsire)
                yeni_satir = pd.DataFrame([{'personel_no': pno, 'ad': pad, 'soyad': psoyad, 'departman': pdepartman,
                                            'maas': pmaas, 'calisma_saati': hecs, 'sertifika': hes, 'hastane': heh}])
                df = pd.concat([df, yeni_satir], ignore_index=True)

            elif secim == 4:
                hano = int(input("Hasta No: "))
                haad = input("Hasta Adı: ")
                haso = input("Hasta Soyadı: ")
                hadt = input("Hasta Doğum Tarihi: ")
                haha = input("Hasta Hastalığı: ")
                hate = input("Hasta Tedavisi: ")
                yeni_hasta = hasta.Hasta(hano, haad, haso, hadt, haha, hate)
                hastalar.append(yeni_hasta)
                yeni_satir = pd.DataFrame(
                    [{'hasta_no': hano, 'ad': haad, 'soyad': haso, 'dogum_tarihi': hadt, 'hastalik': haha,
                      'tedavi': hate}])
                df = pd.concat([df, yeni_satir], ignore_index=True)

            elif secim == 9:
                break

            else:
                print("Yanlış girdi verdiniz. Başa dönülüyor.")
                continue

        elif sec == 3:
            break

        else:
            print("Yanlış girdi verdiniz. Başa dönülüyor.")
            continue


if __name__ == "__main__":
    main()
