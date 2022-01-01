listDokter = [
    {"nama": "Dr John"},
    {"nama": "Dr Paul"},
    {"nama": "Dr Ringo"}
]
listKlinik = [
    {
        "nama": "Klinik Gigi",
        "dokter": listDokter[0],
        "jadwal": [
            {
                "hari": "Senin",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Selasa",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Rabu",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Kamis",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Jumat",
                "mulai": "09:00",
                "selesai": "12:00"
            },
            {
                "hari": "Sabtu",
                "mulai": "13:00",
                "selesai": "18:00"
            },
            {
                "hari": "Minggu",
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
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Selasa",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Rabu",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Kamis",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Jumat",
                "mulai": "09:00",
                "selesai": "12:00"
            },
            {
                "hari": "Sabtu",
                "mulai": "13:00",
                "selesai": "18:00"
            },
            {
                "hari": "Minggu",
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
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Selasa",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Rabu",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Kamis",
                "mulai": "09:00",
                "selesai": "15:00"
            },
            {
                "hari": "Jumat",
                "mulai": "09:00",
                "selesai": "12:00"
            },
            {
                "hari": "Sabtu",
                "mulai": "13:00",
                "selesai": "18:00"
            },
            {
                "hari": "Minggu",
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
