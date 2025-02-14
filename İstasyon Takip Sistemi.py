class İstasyon () :
    def __init__(self,istasyon_adı,istasyon_adresi):
        self.istasyon_adı = istasyon_adı
        self.istasyon_adresi = istasyon_adresi

    def bilgilerigöster (self) :
        print("""
        istasyon Adı: {}
        İstasyon Adresi : {}

        """.format(self.istasyon_adı, self.istasyon_adresi))

class Pompa () :
    def __init__(self,pompa_numarası, yakıt_türü , yakıt_miktarı , pompa_durumu):
        self.pompa_numarası = pompa_numarası
        self.yakıt_türü = yakıt_türü
        self.yakıt_miktarı = yakıt_miktarı
        self.pompa_durumu = pompa_durumu

    def bilgilerigöster (self) :
        print("""
        Pompa Numarası : {}
        Yakıt Türü : {}
        Yakıt Miktarı : {}
        Pompa Durumu : {}     

        """.format(self.pompa_numarası, self.yakıt_türü, self.yakıt_miktarı, self.pompa_durumu))

    def azalma (self,miktar) :
        if miktar > self.yakıt_miktarı :
            print("Yeterli yakıt yoktur....")

        else :
            self.yakıt_miktarı -= miktar
            print("Alınan yakıt miktarı : {} dır. Kalan Yakıt Miktarı :{}".format(miktar,self.yakıt_miktarı))


    def ekleme (self,miktar) :
        self.yakıt_miktarı +=miktar
        print("Eklenen yakıt miktarı : {} dir. Yeni yakıt Miktarı : {}".format(miktar,self.yakıt_miktarı))


istasyon = İstasyon ("Aytemizler","Malatya")

pompalar = {"1" : Pompa (1,"Benzin",100,"Çalışıyor"),
            "2" : Pompa (2,"LPG",200,"Çalışıyor")
            }

while True:
    print("""

    İşlem Seçiniz :

    1.İstasyon Bilgilerini Göster
    2.Pompa Bilgilerini Göster
    3.Benzin alma
    4.Benzin depolama
    5.Sistemden Çıkış

    """)

    işlem = int(input("İşlem Seçiniz : "))

    if işlem == 1 :
        istasyon.bilgilerigöster()

    elif işlem == 2 :
        pompa_numarası = input("Pompa numarasını giriniz :")

        if pompa_numarası in pompalar :
            pompalar[pompa_numarası].bilgilerigöster()

        else :
            print("Pompa Bulunamadı...")

    elif işlem == 3 :
        pompa_numarası = input("Pompa numarasını giriniz :")
        if pompa_numarası in pompalar :
            miktar = int(input("Alınacak Yakıt Miktarını Giriniz :"))
            pompalar[pompa_numarası].azalma(miktar)

        else :
            print("Geçersin pompa numarası....")

    elif işlem == 4 :
        pompa_numarası = input("Pompa numarasını giriniz :")
        if pompa_numarası in pompalar:
            miktar = int(input("Eklenecek yakıt miktarını giriniz :"))
            pompalar[pompa_numarası].ekleme(miktar)


    elif işlem == 5 :
        print("Sistemden çıkılıyor...")

    else :
        print("Geçersin işlem")

