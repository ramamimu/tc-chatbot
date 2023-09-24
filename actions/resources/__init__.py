from enum import Enum

file_resources = {
    "names": [
        "qna akademik kemahasiswaan IF",
        "kalender akademik ITS 2023 - 2024",
        "daftar mata kuliah IF",
        "Daftar Dosen IF",
        "Peraturan Akademik",
    ],
    "urls": [
        "https://itsacid-my.sharepoint.com/:x:/r/personal/ary_shiddiqi_if_its_ac_id/_layouts/15/Doc.aspx?sourcedoc=%7BF44B561E-C98D-449E-8809-D08862AD4D10%7D&file=Q%20dan%20A%20Akademik%20dan%20Kemahasiswaan%20-%20S1.xlsx&action=default&mobileredirect=true",
        "https://itsacid-my.sharepoint.com/:x:/r/personal/ary_shiddiqi_if_its_ac_id/_layouts/15/Doc.aspx?sourcedoc=%7BCC688BB5-9033-445B-A03D-D6218028550C%7D&file=Kalender%20Akademik%20ITS%202023-2024%20ver%20%201.xlsx&action=default&mobileredirect=true",
        "https://itsacid-my.sharepoint.com/:x:/r/personal/ary_shiddiqi_if_its_ac_id/_layouts/15/Doc.aspx?sourcedoc=%7B62B52BA4-007D-49E0-AD10-E1805382A5D3%7D&file=Daftar%20MK%20IF%20-%20wajib%20dan%20pilihan.xlsx&action=default&mobileredirect=true",
        "https://itsacid-my.sharepoint.com/:x:/r/personal/ary_shiddiqi_if_its_ac_id/_layouts/15/Doc.aspx?sourcedoc=%7B62B52BA4-007D-49E0-AD10-E1805382A5D3%7D&file=Daftar%20MK%20IF%20-%20wajib%20dan%20pilihan.xlsx&action=default&mobileredirect=true",
        "https://itsacid-my.sharepoint.com/personal/ary_shiddiqi_if_its_ac_id/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fary%5Fshiddiqi%5Fif%5Fits%5Fac%5Fid%2FDocuments%2FITS%2FMANAGEMENT%2FPERKULIAHAN%2FRESOURCE%20AKADEMIK%20DAN%20KEMAHASISWAAN%2FPeraturan%20Akademik%202018%2Epdf&parent=%2Fpersonal%2Fary%5Fshiddiqi%5Fif%5Fits%5Fac%5Fid%2FDocuments%2FITS%2FMANAGEMENT%2FPERKULIAHAN%2FRESOURCE%20AKADEMIK%20DAN%20KEMAHASISWAAN",
    ],
    "intents_name": ["qna_file", "kalender_file", "dahIUH23", "daftar_dosen_file"],
}


class IndexTopic(Enum):
    QNA_AKADEMIK: 0
    KALENDER_AKADEMIK: 1
    DAFTAR_MATA_KULIAH: 2
    DAFTAR_DOSEN: 3
    PERATURAN_AKADEMIK: 4
