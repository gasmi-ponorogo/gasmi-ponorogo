import qrcode
from qrcode.image.pil import PilImage
import os
from typing import List, Dict

# Konfigurasi
BASE_URL = "https://gasmi.id/cari-murid.html"
OUTPUT_FOLDER = "qr-codes"

# Data siswa (sesuai format)
SISWA_DATA: List[Dict[str, str]] = [
   {
    "nomor_induk": "03352 - 19 - 09",
    "nama": "DEWI NOVITAYENI",
    "ttl": "Trenggalek, 23 Agustus 2005",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMK FATHUL MUNA",
    "orangtua": "Mesnan / Dati",
    "alamat": "Botoputih, Bendungan, Trenggalek"
  },
  {
    "nomor_induk": "03353 - 19 - 09",
    "nama": "AFNAN GHOZI MAYRIA ASEGAF",
    "ttl": "Ponorogo, 20 Mei 2008",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS.AL - JAWARIYAH",
    "orangtua": "Agus Riyadi / Siti Maysaroh",
    "alamat": "Grogol, Sawoo Ponorogo"
  },
  {
    "nomor_induk": "3354 - 19 - 09",
    "nama": "FARA SURYARENATA",
    "ttl": "Ponorogo, 07 Juni 2011",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTSN 1 JETIS",
    "orangtua": "Suryadi / Sri Turini",
    "alamat": "Campurejo, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3355 - 19 - 09",
    "nama": "DENIS YOGA PRATAMA",
    "ttl": "Oku, 06 September 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMP FATHUL MUNA",
    "orangtua": "Jarman / Surati",
    "alamat": "Kurungan Nyawa II, Buay Madang, Oku Timur"
  },
  {
    "nomor_induk": "3356 - 19 - 09",
    "nama": "ANISA DWI YANA PUTRI",
    "ttl": "Ponorogo, 18 Februari 2012",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTSN 1 JETIS",
    "orangtua": "Edi Sunaryanto / Srika Dwi Yana Anjani",
    "alamat": "Campurejo, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3357 - 19 - 09",
    "nama": "SEPTIAN TRIANI YOGA ADHITAMA",
    "ttl": "Ponorogo, 06 September 2006",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MA MAARIF KRATON MOJO KEDIRI",
    "orangtua": "Parni / Jemitri",
    "alamat": "Grogol, Sawoo Ponorogo"
  },
  {
    "nomor_induk": "3358 - 19 - 09",
    "nama": "FAIREL ATHARIZZ CALIEF LEE",
    "ttl": "Ponorogo, 08 Januari 2014",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDN 1 KEMUNING",
    "orangtua": "Nur Ali / Priyanti",
    "alamat": "Wringinanom, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3359 - 19 - 09",
    "nama": "RIYAN NUR HANDIKA PRASETYO",
    "ttl": "Blora, 11 Juli 2007",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMK PGRI 2 PONOROGO",
    "orangtua": "Bonangin / Sriwahyuni",
    "alamat": "Sedarat, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3360 - 19 - 09",
    "nama": "AFIZA SITI ARIYANTI",
    "ttl": "Pekalongan, 09 Juni 2013",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMP FATHUL MUNA",
    "orangtua": "Agus Giyanto / Aris Karisna",
    "alamat": "Prantaan, Bogorejo, Blora"
  },
  {
    "nomor_induk": "3361 - 19 - 09",
    "nama": "ZAHWA NADIA IZZATI",
    "ttl": "Ponorogo, 30 Oktober 2007",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMK MUHAMMADIYAH DORO",
    "orangtua": "Maroto / Fitriyah",
    "alamat": "Pandak, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3362 - 19 - 09",
    "nama": "SITI NURROSIDAH",
    "ttl": "Ponorogo, 22 Agustus 2009",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMAN 1 SLAHUNG",
    "orangtua": "Sarnianto / Sri Suparmi",
    "alamat": "Baosan Kidul, Ngrayun, Ponorogo"
  },
  {
    "nomor_induk": "3363 - 19 - 09",
    "nama": "MUHAMMAD SYAHRUL MUNIB",
    "ttl": "Cilacap, 10 Juni 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMP FATHUL MUNA",
    "orangtua": "Suyono / Katri",
    "alamat": "Wagir Kidul, Pulung, Ponorogo"
  },
  {
    "nomor_induk": "3364 - 19 - 09",
    "nama": "AHMAD HAETI",
    "ttl": "Ponorogo, 19 Agustus 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMK FATHUL MUNA",
    "orangtua": "Turijan / Siti Halimatus Sadiyah",
    "alamat": "Labangka, Babulu, Penajam Paser Utara"
  },
  {
    "nomor_induk": "3365 - 19 - 09",
    "nama": "IKHDA WARDATUL ANNISA'",
    "ttl": "Ponorogo, 17 Juli 2008",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MA AL-ISLAM",
    "orangtua": "Sumari / Puriyah",
    "alamat": "Kutu Wetan, Jetis, Ponorogo"
  },
  {
    "nomor_induk": "3366 - 19 - 09",
    "nama": "MIRDAYANI AGUSTINA",
    "ttl": "Ponorogo, 22 Agustus 2008",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTS. MA'ARIF AL - ISHLAH",
    "orangtua": "Suryono / Tutik Kholistiana",
    "alamat": "Bungu, Bungkal, Ponorogo"
  },
  {
    "nomor_induk": "3367 - 19 - 09",
    "nama": "LUTFI NUFITA ASFA'I",
    "ttl": "Ponorogo, 22 November 2007",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTS MA'ARIF AL ISLAH",
    "orangtua": "Imam Safi'i / Sriyatin",
    "alamat": "Munggu, Bungkal, Ponorogo"
  },
  {
    "nomor_induk": "3368 - 19 - 09",
    "nama": "RIZKI KURNIAWAN",
    "ttl": "Ponorogo, 10 Agustus 2006",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS MA'ARIF AL ISLAH",
    "orangtua": "Kateno / Mesti",
    "alamat": "Wringinanom, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3369 - 19 - 09",
    "nama": "VANES RYAN SAPUTRA",
    "ttl": "Ponorogo, 24 Januari 2007",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMKN 1 JENANGAN",
    "orangtua": "Yani / Turini",
    "alamat": "Ketro, Sawoo, Ponorogo"
  },
  {
    "nomor_induk": "3370 - 19 - 09",
    "nama": "KEVIN ANDREAN PUTRA",
    "ttl": "Madiun, 24 Maret 2009",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 2 SAMBIT",
    "orangtua": "Sutoyo / Yuliani",
    "alamat": "Ketro, Sawoo, Ponorogo"
  },
  {
    "nomor_induk": "3371 - 19 - 09",
    "nama": "LARAS INDAH ANUNGRAHITA SURGAWI",
    "ttl": "Ponorogo, 17 Mei 2009",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTS AL-ISLAM JORESAN",
    "orangtua": "Edhi Prastyo / Sri Kusuma Rahayu",
    "alamat": "Nglewan, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3372 - 19 - 09",
    "nama": "FATHUROHIM AULIA",
    "ttl": "Ponorogo, 20 Juli 2008",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMP FATHUL MUNA",
    "orangtua": "Imam Sukirno",
    "alamat": "Baosan Kidul, Ngrayun, Ponorogo"
  },
  {
    "nomor_induk": "3373 - 19 - 09",
    "nama": "NADHIFA RAHMA DEWANTI",
    "ttl": "Ponorogo, 23 Juli 2007",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMKN 1 SLAHUNG",
    "orangtua": "Sumari / Misinem",
    "alamat": "Singkil, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3374 - 19 - 09",
    "nama": "MUH.RIFAI AINURSALAM",
    "ttl": "Ponorogo, 04 Mei 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDN 8 BAOSAN LOR",
    "orangtua": "Nurwahid / Seniati",
    "alamat": "Baosan Kidul, Ngrayun, Ponorogo"
  },
  {
    "nomor_induk": "3375 - 19 - 09",
    "nama": "AYUNDA CHINTIYA FIRDA SARI NING TIYAS",
    "ttl": "Ponorogo, 20 November 2011",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SDN 4 BAOSAN LOR",
    "orangtua": "Riyanto / Subinti",
    "alamat": "Baosan Lor, Ngrayun, Ponorogo"
  },
  {
    "nomor_induk": "3376 - 19 - 09",
    "nama": "ZASKIA ALTHOFUNISA",
    "ttl": "Ponorogo, 23 Mei 2012",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MI MA'RIF AL - FAQIH",
    "orangtua": "Trimawan / Erna Rahmawati",
    "alamat": "Wringinanom, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3377 - 19 - 09",
    "nama": "FAJAR APRIAN ALI MUSYAFA",
    "ttl": "Pacitan, 06 Juni 2013",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDIT AL-MAWADDAH COPER",
    "orangtua": "Supriono / Siti Nurul Solikah",
    "alamat": "Wringinanom, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3378 - 19 - 09",
    "nama": "DIAN WAHYU PUTRI",
    "ttl": "Pacitan, 06 November 2008",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMPN 5 TAGALOMBO",
    "orangtua": "Miswan / Suprihatun",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3379 - 19 - 09",
    "nama": "AMELIA RAHMAWATI",
    "ttl": "Pacitan, 05 Agustus 2009",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMPN 5 TAGALOMBO",
    "orangtua": "Sukatno / Tutik Susanti",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3380 - 19 - 09",
    "nama": "MIFTAHUL MUDTAQIN",
    "ttl": "Pacitan, 23 Juni 2009",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS AL FATTAH TAHUNAN",
    "orangtua": "Mahmud Jiono / Paryati",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3381 - 19 - 09",
    "nama": "ANDIKA PUTRA FERDIANSA",
    "ttl": "Pacitan, 06 Juli 2007",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MA AL FATTAH TAHUNAN",
    "orangtua": "Sugianto / Murtini",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3382 - 19 - 09",
    "nama": "SELVIRA JULIA INDRIANA SARI",
    "ttl": "Pacitan, 31 Juli 2009",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMPN 5 TAGALOMBO",
    "orangtua": "Jarno / Misti",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3383 - 19 - 09",
    "nama": "NATHAN ADI PRATAMA",
    "ttl": "Pacitan, 12 Agustus 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMKN 1 BANDAR PACITAN",
    "orangtua": "Nur Handoko / Wiwid Widiani",
    "alamat": "Kledung, Bandar, Pacitan"
  },
  {
    "nomor_induk": "3384 - 19 - 09",
    "nama": "RIZKI ALFIAN NUGROHO",
    "ttl": "Pacitan, 18 November 2009",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 1 BANDAR PACITAN",
    "orangtua": "Suparno / Suwarti",
    "alamat": "Kledung, Bandar, Pacitan"
  },
  {
    "nomor_induk": "3385 - 19 - 09",
    "nama": "DELTA AYU SAFIRA",
    "ttl": "Pacitan, 30 Desember 2010",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTS. AL - FATTAH TAHUNAN",
    "orangtua": "Meseri / Wiwin Winarti",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3386 - 19 - 09",
    "nama": "ARSYAVIN MORGAN DIESTA HAIYKAL",
    "ttl": "Ponorogo, 13 Desember 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDN 2 TAHUNAN BARU TEGALOMBO",
    "orangtua": "Didik Budi Santoso / Ika Yuliana",
    "alamat": "Ngilo-Ilo, Slahung, Ponorogo"
  },
  {
    "nomor_induk": "3387 - 19 - 09",
    "nama": "FAHRIS IMRON KHOIRI",
    "ttl": "Ponorogo, 12 Mei 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDN 2 TAHUNAN BARU TEGALOMBO",
    "orangtua": "Wagiyanto / Sri Purwati",
    "alamat": "Ngilo-Ilo, Slahung, Ponorogo"
  },
  {
    "nomor_induk": "3388 - 19 - 09",
    "nama": "AHMAD NUR HASAN",
    "ttl": "Ponorogo, 11 Maret 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDN 2 TAHUNAN BARU TEGALOMBO",
    "orangtua": "Jari Nur Said / Sri Lestari",
    "alamat": "Ngilo-Ilo, Slahung, Ponorogo"
  },
  {
    "nomor_induk": "3389 - 19 - 09",
    "nama": "JAHAROH IZZAH FADZILAH",
    "ttl": "Ponorogo, 09 Desember 2011",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTS. AL - HIKMAH NGRAYUN",
    "orangtua": "Lamiyo / Tulastri",
    "alamat": "Baosan Kidul, Ngrayun, Ponorogo"
  },
  {
    "nomor_induk": "3390 - 19 - 09",
    "nama": "ADITYA RAHMAT WIDYANTO",
    "ttl": "Ponorogo, 26 Juni 2009",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MA. AL - HIKMAH NGRAYUN",
    "orangtua": "Tato / Widya Supartin",
    "alamat": "Baosan Lor, Ngrayun, Ponorogo"
  },
  {
    "nomor_induk": "3391 - 19 - 09",
    "nama": "MIFTAHUL HIDAYAH ISMAIL",
    "ttl": "Ponorogo, 21 Mei 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - HIKMAH NGRAYUN",
    "orangtua": "Imam Mutakin / Siti Rukayah",
    "alamat": "Mrayan, Ngrayun, Ponorogo"
  },
  {
    "nomor_induk": "3392 - 19 - 09",
    "nama": "BRAMA ECHA PRASETYA",
    "ttl": "Pacitan, 19 Desember 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 2 GEMAHARJO",
    "orangtua": "Arif Setyo Darmanto / Duwi Ekasari",
    "alamat": "Tahunan Baru, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3393 - 19 - 09",
    "nama": "AHMAD JENDRA ALHAFIDL",
    "ttl": "Pacitan, 13 Oktober 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 2 GEMAHARJO",
    "orangtua": "Budiono / Dewi Agustina",
    "alamat": "Tahunan Baru, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3394 - 19 - 09",
    "nama": "EVI YUNITA ANGGRAINI",
    "ttl": "Pacitan, 08 Juni 2011",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MA. AL - FATTAH TAHUNAN",
    "orangtua": "Darmanto / Maryam",
    "alamat": "Tahunan Baru, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3395 - 19 - 09",
    "nama": "NADIYA SEPTIA MAHARANI",
    "ttl": "Pacitan, 24 September 2010",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MA. AL - FATTAH TAHUNAN",
    "orangtua": "Hendrik Kurniawan / Surati",
    "alamat": "Tahunan Baru, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3396 - 19 - 09",
    "nama": "FATHYA ALVINATUL RISKI",
    "ttl": "Pacitan, 30 Desember 2006",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMK. AL - FATTAH TAHUNAN",
    "orangtua": "Marjito / Partini",
    "alamat": "Tahunan Baru, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3397 - 19 - 09",
    "nama": "ADITIYA PRADANA PUTRA",
    "ttl": "Pacitan, 03 Mei 2007",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDN 1 GEMAHARJO",
    "orangtua": "Sukadi / Suhartini",
    "alamat": "Tahunan Baru, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3398 - 19 - 09",
    "nama": "ZION ALFA SATIAGRAHA",
    "ttl": "Pacitan, 29 Juni 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. MUHAMMADIYAH BANDAR",
    "orangtua": "Kaseri / Mesiyem",
    "alamat": "Kledung, Bandar, Pacitan"
  },
  {
    "nomor_induk": "3399 - 19 - 09",
    "nama": "ABDUL AZIS KHOIRY",
    "ttl": "Pacitan, 05 Februari 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMKN BANDAR",
    "orangtua": "Tumirin / Sri Utami",
    "alamat": "Kledung, Bandar, Pacitan"
  },
  {
    "nomor_induk": "3400 - 19 - 09",
    "nama": "KURNIA NASIROH",
    "ttl": "Pacitan, 20 Februari 2013",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMPN 1 BANDAR",
    "orangtua": "Suparno / Suwarti",
    "alamat": "Kledung, Bandar, Pacitan"
  },
  {
    "nomor_induk": "3401 - 19 - 09",
    "nama": "FARIS AL GOZHI",
    "ttl": "Pacitan, 06 Juli 2008",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 1 BANDAR",
    "orangtua": "Eko Ferianto / Karsini",
    "alamat": "Mangunharjo, Arjosari, Pacitan"
  },
  {
    "nomor_induk": "3402 - 19 - 09",
    "nama": "YOGI FIRNANDA",
    "ttl": "Pacitan, 26 Agustus 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 5 TEGALOMBO",
    "orangtua": "Mulyono / Rani Febrianti",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3403 - 19 - 09",
    "nama": "AGUS FRIANTO",
    "ttl": "Pacitan, 02 Agustus 2013",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SDN 2 PLOSO",
    "orangtua": "Mispan / Lasmini",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3404 - 19 - 09",
    "nama": "MELFIN RIFA'I",
    "ttl": "Pacitan, 02 November 2011",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 5 TEGALOMBO",
    "orangtua": "Wasit / Tumini",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3405 - 19 - 09",
    "nama": "RISKI ALFIAN",
    "ttl": "Pacitan, 15 Februari 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 5 TEGALOMBO",
    "orangtua": "Giyanto / Etik Ernawati",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3406 - 19 - 09",
    "nama": "ANGGIA RESTU INVANI",
    "ttl": "Pacitan, 03 September 2010",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMKN BANDAR",
    "orangtua": "Adi Aulia Ardiansah / Surati",
    "alamat": "Kledung, Bandar, Pacitan"
  },
  {
    "nomor_induk": "3407 - 19 - 09",
    "nama": "EDI TRIATMOKO",
    "ttl": "Pacitan, 24 Mei 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 5 TEGALOMBO",
    "orangtua": "Soiman / Sujiati",
    "alamat": "Ploso, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3408 - 19 - 09",
    "nama": "ANANG SETIYAWAN",
    "ttl": "Pacitan, 22 Juli 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMKN BANDAR",
    "orangtua": "Teguh Wiyono / Trismiatin",
    "alamat": "Mangunharjo, Arjosari, Pacitan"
  },
  {
    "nomor_induk": "3409 - 19 - 09",
    "nama": "WILDAN ALRUZAIN",
    "ttl": "Pacitan, 16 April 2012",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 2 TEGALOMBO",
    "orangtua": "Paniran / Warsiyem",
    "alamat": "Gemaharjo, Tegalombo, Pacitan"
  },
  {
    "nomor_induk": "3410 - 19 - 09",
    "nama": "ANANDA RIO RISKI SAPUTRA",
    "ttl": "Pacitan, 26 Mei 2000",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMAN 1 TEGALOMBO",
    "orangtua": "Mujiran / Sri Handayani",
    "alamat": "Margahayu, Loa Kulu"
  },
  {
    "nomor_induk": "3411 - 19 - 09",
    "nama": "FANI AFNAN NURHAFIZAH",
    "ttl": "Banjarnegara, 23 April 2010",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MA DARUL ISTIQOMAH",
    "orangtua": "Mohamad Khoirul Anifin / Siti Mukharomah",
    "alamat": "Winong, Bawang, Banjarnegara"
  },
  {
    "nomor_induk": "3412 - 19 - 09",
    "nama": "MOHAMMAD MAFTUH FADLI",
    "ttl": "Ponorogo, 10 Februari 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MA DARUL ISTIQOMAH",
    "orangtua": "Kani / Sumiati",
    "alamat": "Semanding, Kauman, Ponorogo"
  },
  {
    "nomor_induk": "3413 - 19 - 09",
    "nama": "MUROBBI EKA ADITYA",
    "ttl": "Ponorogo, 05 Maret 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MA DARUL ISTIQOMAH",
    "orangtua": "Poniran / Yati",
    "alamat": "Semanding, Kauman, Ponorogo"
  },
  {
    "nomor_induk": "3414 - 19 - 09",
    "nama": "SYNTIA 'ULYA KHUSNITA",
    "ttl": "Ponorogo, 24 Juli 2009",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MA DARUL ISTIQOMAH",
    "orangtua": "Parni / Parti",
    "alamat": "Dadapan, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3415 - 19 - 09",
    "nama": "MUHAMMAD AMHAR MUMTAZ",
    "ttl": "Ponorogo, 20 Juni 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. DARUL ISTIQOMAH",
    "orangtua": "Kusno, S.Pd.I / Ema Wardati, S.Pd.I",
    "alamat": "Ngumpul, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3416 - 19 - 09",
    "nama": "IJAT FAHEM BADIUL ALAM",
    "ttl": "Ponorogo, 08 November 2011",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. DARUL ISTIQOMAH",
    "orangtua": "Sunarno / Dwi Erni Widiastuti",
    "alamat": "Ngumpul, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3417 - 19 - 09",
    "nama": "MUHAMMAD ZAKARIYA NURROHMAN",
    "ttl": "Ponorogo, 13 Oktober 2011",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. DARUL ISTIQOMAH",
    "orangtua": "Prianto / Sunarti",
    "alamat": "Pandak, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3418 - 19 - 09",
    "nama": "MUHAMAD ALDY NURSALAM",
    "ttl": "Nganjuk, 12 Desember 2011",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. DARUL ISTIQOMAH",
    "orangtua": "Ali Jafar Shodiq / Parmiatun",
    "alamat": "Ngumpul, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3419 - 19 - 09",
    "nama": "NABIL ZAKI IBRAHIM",
    "ttl": "Tangerang, 19 November 2008",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Casmudi / Hesti Setiarini",
    "alamat": "Tambakrejo, Pemalang, Jawa Tengah"
  },
  {
    "nomor_induk": "3420 - 19 - 09",
    "nama": "ULUL ALBAB",
    "ttl": "Sukamulya, 16 September 2008",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Supriyanto / Sri Haryati",
    "alamat": "Rawamangun, Pulogadung, Jakarta Timur"
  },
  {
    "nomor_induk": "3421 - 19 - 09",
    "nama": "AHMAD WILDAN ROMDLONI",
    "ttl": "Ponorogo, 22 Agustus 2011",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Samsuri / Wiji Utami",
    "alamat": "Joresan, Mlarak, Ponorogo"
  },
  {
    "nomor_induk": "3422 - 19 - 09",
    "nama": "MUHAMMAD RIDHO SAPUTRA",
    "ttl": "Surabaya, 30 Mei 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Suparman / Sumarpi",
    "alamat": "Bajang, Mlarak, Ponorogo"
  },
  {
    "nomor_induk": "3423 - 19 - 09",
    "nama": "MUHAMMAD ROHMAN",
    "ttl": "Jakarta, 23 Oktober 2009",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Alm. Anen Priyatna / Suginem",
    "alamat": "Tangen, Sragen, Jawa Tengah"
  },
  {
    "nomor_induk": "3424 - 19 - 09",
    "nama": "ZAYANA FAWAZARSYA RUWAIDAH",
    "ttl": "Ponorogo, 17 Juli 2005",
    "jenis_kelamin": "Perempuan",
    "sekolah": "UIN PONOROGO",
    "orangtua": "Syamsudin / Siti Arini",
    "alamat": "Joresan, Mlarak, Ponorogo"
  },
  {
    "nomor_induk": "3425 - 19 - 09",
    "nama": "AHMAD MUSYAFA NASYWATUL WAFFA",
    "ttl": "Lamongan, 13 Maret 2009",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Latief Ali Zahrowi / Zaitul Erni",
    "alamat": "Kariangau, Balikpapan Barat, Kaltim"
  },
  {
    "nomor_induk": "3426 - 19 - 09",
    "nama": "AHMAD SABHAL LATHAF",
    "ttl": "Ponorogo, 23 Februari 2008",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Rohmat Fadeli / Mursini",
    "alamat": "Bulu, Sambit, Ponorogo"
  },
  {
    "nomor_induk": "3427 - 19 - 09",
    "nama": "DWI PUTRA PRAYOGO",
    "ttl": "Magetan, 30 Maret 2010",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Komarudin / Susilawati",
    "alamat": "Dukuh, Lembeyan, Magetan"
  },
  {
    "nomor_induk": "3428 - 19 - 09",
    "nama": "ISMA FAIZATUL MUNA",
    "ttl": "Ponorogo, 18 Januari 2004",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTS. AL - ISLAM JORESAN",
    "orangtua": "Muhrodji / Siti Solekah",
    "alamat": "Joresan, Mlarak, Ponorogo"
  },
  {
    "nomor_induk": "3429 - 19 - 09",
    "nama": "ARSYA RIZKY AL MUBAROK",
    "ttl": "Ponorogo, 14 Juni 2013",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTs. MIFTAHUL ULUM NGRAKET",
    "orangtua": "Tukimun / Sutini",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3430 - 19 - 09",
    "nama": "STEVEN ORVA ROLANDA",
    "ttl": "Ponorogo, 12 Juni 2014",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "PP. DARUL HUDA MAYAK",
    "orangtua": "Muh. Heri Purwanto / Renita Tri Oktapia Dewi",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3431 - 19 - 09",
    "nama": "KELVIN RAMDANI SAPUTRA",
    "ttl": "Ponorogo, 02 Februari 2013",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 2 BALONG",
    "orangtua": "Trimo / Nanik Minasri",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3432 - 19 - 09",
    "nama": "NADIA HASNA SAKHI",
    "ttl": "Ponorogo, 25 Juli 2012",
    "jenis_kelamin": "Perempuan",
    "sekolah": "MTs. MIFTAHUL ULUM NGRAKET",
    "orangtua": "Sarju / Robit Tahtul Asadah",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3433 - 19 - 09",
    "nama": "NATHANIA AYU EVELINNA",
    "ttl": "Ponorogo, 18 Desember 2009",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMK KESEHATAN PONOROGO",
    "orangtua": "Bambang Maulana Maheswara / Fitri Yuliana",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3434 - 19 - 09",
    "nama": "FRISKA LAURENZIA LIDIA SABELLA",
    "ttl": "Ponorogo, 04 Maret 2011",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMAN 1 BADEGAN",
    "orangtua": "Mudjiono / Ria Dewi Yuliati",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3435 - 19 - 09",
    "nama": "ERLIA NUR HIDAYAH",
    "ttl": "Ponorogo, 16 Februari 2011",
    "jenis_kelamin": "Perempuan",
    "sekolah": "SMK KESEHATAN BIMPO",
    "orangtua": "Sugito / Umi Andarwati",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3436 - 19 - 09",
    "nama": "JOSHUA DAREN PRATAMA",
    "ttl": "Ponorogo, 06 Januari 2014",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "MTs. MIFTAHUL ULUM NGRAKET",
    "orangtua": "Panji Asmoro / Katemi",
    "alamat": "Jonggol, Jambon, Ponorogo"
  },
  {
    "nomor_induk": "3437 - 19 - 09",
    "nama": "ARDAN ZHAFRAN DWI MAHADIKA",
    "ttl": "Ponorogo, 20 Maret 2013",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 1 BALONG",
    "orangtua": "Agus Supriyono / Puji Lestari",
    "alamat": "Ngampel, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3438 - 19 - 09",
    "nama": "DAFFA FIRDAUS FIRJATULLAH",
    "ttl": "Ponorogo, 19 November 2009",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMK PGRI 2 PONOROGO",
    "orangtua": "Hariyanto / Wijayanti",
    "alamat": "Ngampel, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3439 - 19 - 09",
    "nama": "DIMAS ADHYASTHA BAGUS PAMBUDI",
    "ttl": "Ponorogo, 23 Januari 2013",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 1 BALONG",
    "orangtua": "Pambudi / Uswatun Hasanah",
    "alamat": "Ngampel, Balong, Ponorogo"
  },
  {
    "nomor_induk": "3440 - 19 - 09",
    "nama": "ANGGA BRIANTAMA",
    "ttl": "Ponorogo, 10 November 2011",
    "jenis_kelamin": "Laki-Laki",
    "sekolah": "SMPN 1 JETIS",
   
    # Tambahkan data siswa lainnya di sini dengan format yang sama
]

def generate_qr_code(student: Dict[str, str]) -> str:
    """Buat QR Code untuk satu siswa & simpan sebagai PNG"""
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # URL yang akan tertanam di QR -> sesuai sistem pencarian Gasmi
    qr_url = f"{BASE_URL}?nomor_induk={student['nomor_induk']}"
    
    # Konfigurasi tampilan QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url)
    qr.make(fit=True)
    
    img = qr.make_image(
        image_factory=PilImage,
        fill_color="black",
        back_color="white"
    ).resize((300, 300))
    
    # Simpan file
    filename = f"{OUTPUT_FOLDER}/{student['nomor_induk']}.png"
    img.save(filename)
    print(f"✅ Dibuat: {filename} → {qr_url}")
    return filename

def generate_all() -> None:
    """Buat QR untuk semua siswa"""
    print(f"Memproses {len(SISWA_DATA)} QR Code...")
    for siswa in SISWA_DATA:
        generate_qr_code(siswa)
    print("Selesai! Semua QR tersimpan di folder:", OUTPUT_FOLDER)

if __name__ == "__main__":
    generate_all()

