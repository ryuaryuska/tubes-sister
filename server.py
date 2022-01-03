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
with SimpleXMLRPCServer(('localhost', 8001), requestHandler=RequestHandler, allow_none=True) as server:

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

    listPasien = [
    ]

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
        pasien["antriAt"] = datetime.datetime.now()
        if klinik == "gigi":
            antrianGigi.append(pasien)
            if len(antrianGigi) == 0:
                pasien["antrian"] = GetTotalAntrian("gigi")
            else:
                pasien["antrian"] = antrianGigi[antrianGigi.index(
                    pasien) - 1]['antrian'] + 1
        elif klinik == "tht":
            antrianTHT.append(pasien)
            if len(antrianTHT) == 0:
                pasien["antrian"] = GetTotalAntrian("gigi")
            else:
                pasien["antrian"] = antrianTHT[antrianTHT.index(
                    pasien) - 1]['antrian'] + 1
        elif klinik == "umum":
            antrianUmum.append(pasien)
            if len(antrianUmum) == 0:
                pasien["antrian"] = GetTotalAntrian("gigi")
            else:
                pasien["antrian"] = antrianUmum[antrianUmum.index(
                    pasien) - 1]['antrian'] + 1
        return pasien

    def PasienSelesai(klinik):
        if klinik == "gigi":
            antrianGigi.pop(0)
            return antrianGigi

        elif klinik == "tht":
            antrianTHT.pop(0)
            return antrianTHT

        elif klinik == "umum":
            antrianUmum.pop(0)
            return antrianUmum

    def LihatAntrian(klinik):
        if klinik == "gigi":
            return antrianGigi
        elif klinik == "tht":
            return antrianTHT
        elif klinik == "umum":
            return antrianUmum

    def GetListKlinik():
        return data.Klinik()

    def GetListDokter():
        return data.Dokter()

    def GetWaktuDatang(klinik, nrm):
        print("KLINIK " + klinik)
        if klinik == "gigi":
            for x in antrianGigi:
                if x['nrm'] == nrm:
                    pasien = x
                    break
            listPasien = antrianGigi
            getJadwal = data.Klinik(
            )[0]["jadwal"][datetime.date.today().weekday()]
        elif klinik == "tht":
            for x in antrianTHT:
                if x['nrm'] == nrm:
                    pasien = x
                    break
            listPasien = antrianTHT
            getJadwal = data.Klinik(
            )[1]["jadwal"][datetime.date.today().weekday()]
        elif klinik == "umum":
            for x in antrianUmum:
                if x['nrm'] == nrm:
                    pasien = x
                    break
            listPasien = antrianUmum
            getJadwal = data.Klinik(
            )[2]["jadwal"][datetime.date.today().weekday()]

        waktuMulai = datetime.datetime.strptime(
            getJadwal["mulai"], "%H:%M")
        waktuSelesai = datetime.datetime.strptime(
            getJadwal["selesai"], "%H:%M")

        if pasien["antriAt"].time() < waktuMulai.time():
            if len(listPasien) == 1:
                return waktuMulai.strftime("%H:%M")
            else:
                return (waktuMulai + datetime.timedelta(minutes=listPasien.index(pasien) * 15)).strftime("%H:%M")
        elif pasien["antriAt"].time() > waktuSelesai.time():
            print(pasien["antriAt"].time())
            print(waktuSelesai.time())
            listPasien.pop(listPasien.index(pasien))
            return ""
        else:
            if len(pasien) == 1:
                return (datetime.datetime.now() + datetime.timedelta(minutes=15)).strftime("%H:%M")
            return (listPasien[listPasien.index(pasien)-1]["antriAt"] + datetime.timedelta(minutes=15)).strftime("%H:%M")

    def Login(user, password):
        for x in data.Dokter():
            if x["username"] == user and x["pass"] == password:
                return x
        return False

    server.register_function(CheckNRM)
    server.register_function(TambahAntrian)
    server.register_function(PasienSelesai)
    server.register_function(GetTotalAntrian)
    server.register_function(LihatAntrian)
    server.register_function(RegisPasien)
    server.register_function(GetListKlinik)
    server.register_function(GetListDokter)
    server.register_function(GetWaktuDatang)
    server.register_function(Login)

    print("SERVER RUNNING...")
    # Jalankan server
    server.serve_forever()
