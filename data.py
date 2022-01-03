listDokter = [
    {"nama": "Dr John", "username": "john", "pass": "123", "klinik": "KLINIK GIGI"},
    {"nama": "Dr Paul", "username": "paul", "pass": "123", "klinik": "KLINIK THT"},
    {"nama": "Dr Ringo", "username": "ringo",
        "pass": "123", "klinik": "KLINIK UMUM"}
]


listKlinik = [
    {
        "nama": "Klinik Gigi",
        "dokter": listDokter[0],
        "jadwal": [
            {
                "hari": "Senin",
                "day": 0,
                "mulai": "09:00",
                "selesai": "23:59"
            },
            {
                "hari": "Selasa",
                "day": 1,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Rabu",
                "day": 2,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Kamis",
                "day": 3,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Jumat",
                "day": 4,
                "mulai": "09:00",
                "selesai": "12:00"
            },
            {
                "hari": "Sabtu",
                "day": 5,
                "mulai": "13:00",
                "selesai": "18:00"
            },
            {
                "hari": "Minggu",
                "day": 6,
                "mulai": "13:00",
                "selesai": "18:00"
            },
        ]
    },
    {
        "nama": "Klinik THT",
        "dokter": listDokter[1],
        "jadwal": [
            {
                "hari": "Senin",
                "day": 0,
                "mulai": "09:00",
                "selesai": "23:59"
            },
            {
                "hari": "Selasa",
                "day": 1,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Rabu",
                "day": 2,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Kamis",
                "day": 3,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Jumat",
                "day": 4,
                "mulai": "09:00",
                "selesai": "12:00"
            },
            {
                "hari": "Sabtu",
                "day": 5,
                "mulai": "13:00",
                "selesai": "18:00"
            },
            {
                "hari": "Minggu",
                "day": 6,
                "mulai": "13:00",
                "selesai": "18:00"
            },
        ]
    },
    {
        "nama": "Klinik Umum",
        "dokter": listDokter[2],
        "jadwal": [
            {
                "hari": "Senin",
                "day": 0,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Selasa",
                "day": 1,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Rabu",
                "day": 2,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Kamis",
                "day": 3,
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Jumat",
                "day": 4,
                "mulai": "09:00",
                "selesai": "12:00"
            },
            {
                "hari": "Sabtu",
                "day": 5,
                "mulai": "13:00",
                "selesai": "18:00"
            },
            {
                "hari": "Minggu",
                "day": 6,
                "mulai": "13:00",
                "selesai": "18:00"
            },
        ]
    }
]


def Klinik():
    return listKlinik


def Dokter():
    return listDokter
