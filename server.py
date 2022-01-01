# import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCServer

# import SimpleXMLRPCRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler
import random
import datetime
from prettytable import PrettyTable
import data


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Buat server
with SimpleXMLRPCServer(('localhost', 8001,),
                        requestHandler=RequestHandler) as server:

    class Pasien:
        def __init__(self, name, birthDate, gender):
            self.gender = gender
            self.name = name
            self.nrm = "130119" + str(random.randint(1000, 9999))
            self.birthDate = birthDate
            # self.birthDate = datetime.strptime(
            #     birthDate, "%Y-%m-%d").date()
            self.antrian = 0

            today = datetime.date.today()
            self.age = today.year - self.birthDate.year - \
                ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))

    def GetWaktuAntrian(nrm, array):
        n = 0
        for x in array:
            if x.nrm == nrm:
                n = n + 15
                break
        hours_added = datetime.timedelta(hours=hours)
        future_date_and_time = current_date_and_time + hours_added
        return future_date_and_time.strftime('%H:%M')

    listPasien = []

    antrianGigi = []
    antrianTHT = []
    antrianUmum = []

    def CheckNRM(nrm):
        for x in listPasien:
            if x["nrm"] == nrm:
                return x
            return False

    def GetTotalAntrian(klinik):
        if klinik == "gigi":
            return len(antrianGigi)
        elif klinik == "tht":
            return len(antrianTHT)
        elif klinik == "umum":
            return len(antrianUmum)

    def RegisPasien(name, birthDate, gender):
        print("masuk")

        tgl = datetime.datetime.strptime(
            birthDate, "%Y-%m-%d").date()
        pasien = Pasien(name, tgl, gender)
        data = {
            "name": pasien.name,
            "birthDate": birthDate,
            "gender": pasien.gender,
            "age": pasien.age,
            "nrm": pasien.nrm,
            "antrian": pasien.antrian
        }
        listPasien.append(data)
        return data

    def TambahAntrian(klinik, pasien):
        if klinik == "gigi":
            antrianGigi.append(pasien)
            pasien["antrian"] = GetTotalAntrian("gigi")
        elif klinik == "tht":
            antrianTHT.append(pasien)
            pasien["antrian"] = GetTotalAntrian("tht")
        elif klinik == "umum":
            antrianUmum.append(pasien)
            pasien["antrian"] = GetTotalAntrian("umum")
        return pasien

    def PasienSelesai(klinik, antrian):
        if klinik == "gigi":
            antrianGigi.pop(0)
        elif klinik == "tht":
            antrianTHT.pop(0)
        elif klinik == "umum":
            antrianUmum.pop(0)

    def LihatAntrian(klinik):
        t = PrettyTable(['No Antrian', 'Nomor Rekam Medis', 'Nama', 'Umur'])

        def listAntrian(arr):
            for x in arr:
                t.add_row([x.antrian, x.nrm, x.namem, x.age])
            print(t)

        if klinik == "gigi":
            listAntrian(antrianGigi)
        elif klinik == "tht":
            listAntrian(antrianTHT)
        elif klinik == "umum":
            listAntrian(antrianUmum)

    def GetListKlinik():
        return data.Klinik()

    def GetListDokter():
        return data.Dokter()

    def GetWaktuDatang(klinik, nrm):
        menit = 15
        i = 0
        if klinik == "gigi":
            for x in antrianGigi:
                if x['nrm'] != nrm:
                    i = i + 1
                else:
                    break
        elif klinik == "tht":
            for x in antrianTHT:
                if x['nrm'] != nrm:
                    i = i + 1
                else:
                    break
        elif klinik == "umum":
            for x in antrianUmum:
                if x['nrm'] != nrm:
                    i = i + 1
                else:
                    break

    server.register_function(CheckNRM)
    server.register_function(TambahAntrian)
    server.register_function(PasienSelesai)
    server.register_function(GetTotalAntrian)
    server.register_function(LihatAntrian)
    server.register_function(RegisPasien)
    server.register_function(GetListKlinik)
    server.register_function(GetListDokter)

    print("SERVER RUNNING...")
    # Jalankan server
    server.serve_forever()
