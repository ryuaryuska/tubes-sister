import xmlrpc.client
import datetime
import getpass
from prettytable import PrettyTable
from pyfiglet import Figlet
import sys

p = xmlrpc.client.ServerProxy("http://localhost:8001/RPC2", allow_none=True)


def login():
    print("LOGIN")
    print("-----")
    username = input("Username: ")
    while username == "":
        username = input("Username: ")
    password = getpass.getpass()
    while password == "":
        password = getpass.getpass()
    data = p.Login(username, password)

    if data == False:
        print("Username/Password yang anda masukkan tidak sesuai")
        login()
    else:
        return data


def main():
    print("\nMENU")
    print("1. Lihat list antrian pasien")
    print("2. Selesaikan pasien saat ini")
    print("3. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        arr = p.LihatAntrian(klinik)

        t = PrettyTable(["No Antrian", "Nomor Rekam Medis", "Nama", "Umur"])
        for x in arr:
            t.add_row([x["antrian"], x["nrm"], x["name"], x["age"]])
        print(t)
    elif menu == "2":
        n = p.PasienSelesai(klinik)

        if len(n) > 0:
            t = PrettyTable(["No Antrian", "Nomor Rekam Medis", "Nama", "Umur"])
            t.add_row([n[0]["antrian"], n[0]["nrm"], n[0]["name"], n[0]["age"]])
    elif menu == "3":
        sys.exit()

    main()


if __name__ == "__main__":
    data = login()
    custom_fig = Figlet()
    if data["klinik"] == "KLINIK GIGI":
        klinik = "gigi"
    elif data["klinik"] == "KLINIK THT":
        klinik = "tht"
    else:
        klinik = "umum"

    print(custom_fig.renderText(data["klinik"]))

    print()
    main()
