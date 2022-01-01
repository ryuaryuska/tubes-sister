from datetime import date
from datetime import datetime
import random


class Pasien:

    def __init__(self, name, birthDate):
        self.name = name
        self.nrm = "130119"
        self.birthDate = datetime.strptime(
            birthDate, ("%Y-%m-%d")).date()
        self.antrian = 0

        today = date.today()
        self.age = today.year - self.birthDate.year - \
            ((today.month, today.day) <
             (self.birthDate.month, self.birthDate.day))

        def Registrasi(self, array):
            array.append(self)
            self.antrian = array.index(self) + 1
            return self

    # def CheckNRM(nrm, array):
    #     for x in array:
    #         if x.nrm == nrm:
    #             return x
    #         else:
    #             return False

    # listPasien = []
    # listDokter = []
    # listKlinik = []

    # antrianGigi = []
    # antrianTHT = []
    # antrianUmum = []

    # def TambahAntrian(klinik, pasien):
    #     if klinik == "gigi":
    #         antrianGigi.append(pasien)
    #     else if klinik == "tht":
    #         antrianTHT.append(pasien)
    #     else if klinik == "umum":
    #         antrianUmum.append(pasien)

    # def PasienSelesai(klinik, antrian):
    #     if klinik == "gigi":
    #         antrianGigi.pop(0)
    #     else if klinik == "tht":
    #         antrianTHT.pop(0)
    #     else if klinik == "umum":
    #         antrianUmum.pop(0)

    # def LihatAntrian(klinik):
    #     t = PrettyTable(['No Antrian', 'Nomor Rekam Medis', 'Nama', 'Umur'])

    #     def listAntrian(arr):
    #         for x in arr:
    #             t.add_row([x.antrian, x.nrm, x.namem x.age])
    #         print(t)

    #     if klinik == "gigi":
    #         listAntrian(antrianGigi)
    #     else if klinik == "tht":
    #         listAntrian(antrianTHT)
    #     else if klinik == "umum":
    #         listAntrian(antrianUmum)


p = Pasien("ryu", "2001-02-02")

print(p.birthDate)
