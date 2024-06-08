import personel


class Hemsire(personel.Personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def __str__(self):
        return (f'\nHemşire Bilgileri'
                f'\nÇalisma Saatleri: {self.__calisma_saati}'
                f'\nSeritifka: {self.__sertifika}'
                f'\nHastane: {self.__hastane}')

    def __repr__(self):
        return self.__str__()

    def get_calisma_saati(self):
        return self.__calisma_saati

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def get_sertifika(self):
        return self.__sertifika

    def set_seritifka(self, sertifika):
        self.__sertifika = sertifika

    def get_hastane(self):
        return self.__hastane

    def set_hastane(self, hastane):
        self.__hastane = hastane
