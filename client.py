import xmlrpc.client
import datetime
from prettytable import PrettyTable
import sys

p = xmlrpc.client.ServerProxy("http://localhost:8001/RPC2", allow_none=True)


def validateDate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def registrasiNama():
    nama = input("Nama Lengkap: ")
    if nama == "0":
        main()
    while nama == "":
        print("data tidak boleh kosong")
        nama = registrasiNama()
    return str(nama)


def registrasiTglLahir():
    print("Tanggal Lahir:   ")
    tahun = input(" Tahun:  ")
    while tahun == "":
        print("data tidak boleh kosong")
        tahun = input(" Tahun:  ")
    bulan = input(" Bulan:  ")
    while bulan == "":
        print("data tidak boleh kosong")
        bulan = input("  Bulan:   ")
    tgl = input("  Hari:   ")
    while tgl == "":
        print("data tidak boleh kosong")
        tgl = input("  Hari:   ")
    tglLahir = tahun + "-" + bulan + "-" + tgl
    return str(tglLahir)


def registrasiGender():
    getGender = input("Laki-Laki / Perempuan (l/p): ")
    gender = ""
    while getGender == "":
        print("data tidak boleh kosong")
        getGender = registrasiGender()

    if getGender == "l":
        gender = "laki-laki"
    elif getGender == "p":
        gender = "perempuan"
    else:
        print("data tidak valid")
        while getGender != "laki-laki" and getGender != "perempuan":
            getGender = registrasiGender()
    return str(gender)


def checkNRM():
    nrm = input("Masukkan Nomor Rekam Medis anda: ")
    pasien = p.CheckNRM(nrm)


def regisAntrian():
    klinikGigi = p.GetTotalAntrian("gigi")
    klinikTHT = p.GetTotalAntrian("tht")
    klinikUmum = p.GetTotalAntrian("umum")

    t = PrettyTable(["No", "Nama", "Antrian"])
    t.add_row(["1", "Klinik Gigi", klinikGigi])
    t.add_row(["2", "Klinik THT", klinikTHT])
    t.add_row(["3", "Klinik Umum", klinikUmum])
    print(t)
    klinik = input("Pilih Klinik: ")

    if klinik == "0":
        main()

    if klinik == "1":
        klinik = "gigi"
    elif klinik == "2":
        klinik = "tht"
    elif klinik == "3":
        klinik = "umum"
    else:
        print("data yang anda masukkan tidak valid")
        regisAntrian()
    nrm = input("Masukkan Nomor Rekam Medis anda: ")
    pasien = p.CheckNRM(nrm)

    checkAntrian = p.CheckAntrian(nrm)
    if checkAntrian != False:
        print("Nomor Pasien " + nrm + " telah terdaftar pada antrian yang lain")
        main()

    if pasien == False:
        print("Data tidak ditemukan!")
        main()
    else:
        data = p.TambahAntrian(klinik, pasien)
        waktuDatang = p.GetWaktuDatang(klinik, pasien["nrm"])
        if waktuDatang == "":
            print(
                "Mohon maaf antrian sudah pada batas maksimum, silakan daftar keesokan hari")
        else:
            print("Daftar antrian berhasil, nomor antrian anda: (" +
                  str(data['antrian']) + ")\n Silakan datang pada jam " + waktuDatang)


def main():
    print("MENU")
    print("1. REGISTRASI PASIEN")
    print("2. REGISTRASI ANTRIAN")
    print("3. LIHAT DATA DIRI")
    print("4. LIHAT KLINIK YANG TERSEDIA")
    print("5. LIHAT INFO ANTRIAN")
    print("6. Keluar")

    menu = input("Pilih Menu:   ")
    if menu == "1":
        nama = registrasiNama()
        gender = registrasiGender()
        tglLahir = registrasiTglLahir()
        dataBaru = p.RegisPasien(nama, tglLahir, gender)
        print("Registrasi berhasi Nomor Rekam Medis Anda: " + dataBaru["nrm"])
    elif menu == "3":
        nrm = input("Masukkan Nomor Rekam Medis Anda: ")
        data = p.CheckNRM(nrm)

        if data == False:
            print("Data tidak ditemukan!")
        else:
            t = PrettyTable(['Nomor Rekam Medis', 'Nama', 'Umur',
                            'Tanggal Lahir', "Jenis Kelamin"])
            t.add_row([data['nrm'], data['name'], data['age'],
                       data['birthDate'], data['gender']])
            print(t)
    elif menu == "4":
        klinik = p.GetListKlinik()
        t = PrettyTable(["Nama", "Dokter", "Jadwal"])
        for x in klinik:
            jadwal = ""
            for y in x["jadwal"]:
                jadwal += y["hari"] + " " + \
                    y["mulai"] + " - " + \
                    y["selesai"] + "\n"
            t.add_row([x['nama'], x['dokter']['nama'], jadwal])
        print(t)
    elif menu == "2":
        regisAntrian()
    elif menu == "5":
        nrm = input("Masukkan Nomor Rekam Medis Anda: ")
        data = p.CheckAntrian(nrm)
        if data == False:
            print("Data tidak ditemukan!")
        else:
            t = PrettyTable(['Nomor Rekam Medis', 'Nama',
                            "Waktu Datang", "Nomor Antrian", "Klinik"])
            t.add_row([data['nrm'], data['name'],
                      data['waktuDatang'], data['antrian'], data['klinik']])
            print(t)
    elif menu == "6":
        sys.exit()
    main()


if __name__ == "__main__":
    main()
