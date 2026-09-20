import qrcode
import csv
import os

# Buat folder penyimpanan
output_folder = "QR_SISWA"
os.makedirs(output_folder, exist_ok=True)

# Data CSV
csv_data = """NO INDUK|Nama|Temp./Tgl. Lahir|Jenis Kelamin|Pendidikan|Orang Tua|Alamat
03352 - 19 - 09|DEWI NOVITAYENI|Trenggalek, 23 Agustus 2005|Perempuan|SMK FATHUL MUNA|Mesnan / Dati|Botoputih, Bendungan,Trenggalek
03353 - 19 - 09|AFNAN GHOZI MAYRIA ASEGAF|Ponorogo, 20 Mei 2008|Laki-Laki|MTS.AL - JAWARIYAH|Agus Riyadi / Siti Maysaroh|Grogol, Sawoo Ponorogo
3354 - 19 - 09|FARA SURYARENATA|Ponorogo, 07 Juni 2011|Perempuan|MTSN 1 JETIS|Suryadi / Sri Turini|Campurejo, Sambit, Ponorogo
3355 - 19 - 09|DENIS YOGA PRATAMA|Oku, 06 September 2012|Laki-Laki|SMP FATHUL MUNA|Jarman / Surati|Kurungan Nyawa Ii,Buay Madang,.Oku Timur
3356 - 19 - 09|ANISA DWI YANA PUTRI|Ponorogo, 18 Februari 2012|Perempuan|MTSN 1 JETIS|Edi Sunaryanto / Srika Dwi Yana Anjani|Campurejo, Sambit, Ponorogo
3357 - 19 - 09|SEPTIAN TRIANI YOGA ADHITAMA|Ponorogo, 06 September 2006|Laki-Laki|MA MAARIF KRATON MOJO KEDIRI|Parni / Jemitri|Grogol, Sawoo Ponorogo
3358 - 19 - 09|FAIREL ATHARIZZ CALIEF LEE|Ponorogo, 08 Januari 2014|Laki-Laki|SDN 1 KEMUNING|Nur Ali / Priyanti|Wringinanom, Sambit, Ponorogo
3359 - 19 - 09|RIYAN NUR HANDIKA PRASETYO|Blora, 11 Juli 2007|Laki-Laki|SMK PGRI 2 PONOROGO|Bonangin / Sriwahyuni|Sedarat, Balong, Ponorogo
3360 - 19 - 09|AFIZA SITI ARIYANTI|Pekalongan, 09 Juni 2013|Perempuan|SMP FATHUL MUNA|Agus Giyanto / Aris Karisna|Prantaan, Bogorejo, Blora
3361 - 19 - 09|ZAHWA NADIA IZZATI|Ponorogo, 30 Oktober 2007|Perempuan|SMK MUHAMMADIYAH DORO|Maroto / Fitriyah|Pandak, Balong, Ponorogo
3362 - 19 - 09|SITI NURROSIDAH|Ponorogo, 22 Agustus 2009|Perempuan|SMAN 1 SLAHUNG|Sarnianto / Sri Suparmi|Baosan Kidul, Ngrayun, Ponorogo
3363 - 19 - 09|MUHAMMAD SYAHRUL MUNIB|Cilacap, 10 Juni 2012|Laki-Laki|SMP FATHUL MUNA|Suyono / Katri|Wagir Kidul, Pulung, Ponorogo
3364 - 19 - 09|AHMAD HAETI|Ponorogo, 19 Agustus 2010|Laki-Laki|SMK FATHUL MUNA|Turijan / Siti Halimatus Sadiyah|Labangka, Babulu, Penajam Paser Utara
3365 - 19 - 09|IKHDA WARDATUL ANNISA'|Ponorogo, 17 Juli 2008|Perempuan|MA AL-ISLAM|Sumari / Puriyah|Kutu Wetan, Jetis, Ponorogo
3366 - 19 - 09|MIRDAYANI AGUSTINA|Ponorogo, 22 Agustus 2008|Perempuan|MTS. MA'ARIF AL - ISHLAH|Suryono / Tutik Kholistiana|Bungu, Bungkal, Ponorogo
3367 - 19 - 09|LUTFI NUFITA ASFA'I|Ponorogo, 22 November 2007|Perempuan|MTS MA'ARIF AL ISLAH|Imam Safi / Sriyatin|Munggu, Bungkal, Ponorogo
3368 - 19 - 09|RIZKI KURNIAWAN|Ponorogo, 10 Agustus 2006|Laki-Laki|MTS MA'ARIF AL ISLAH|Kateno / Mesti|Wringinanom, Sambit, Ponorogo
3369 - 19 - 09|VANES RYAN SAPUTRA|Ponorogo, 24 Januari 2007|Laki-Laki|SMKN 1 JENANGAN|Yani / Turini|Ketro, Sawoo, Ponorogo
3370 - 19 - 09|KEVIN ANDREAN PUTRA|Madiun, 24 Maret 2009|Laki-Laki|SMPN 2 SAMBIT|Sutoyo / Yuliani|Ketro, Sawoo, Ponorogo
3371 - 19 - 09|LARAS INDAH ANUNGRAHITA SURGAWI|Ponorogo, 17 Mei 2009|Perempuan|MTS AL-ISLAM JORESAN|Edhi Prastyo / Sri Kusuma Rahayu|Nglewan, Sambit, Ponorogo
3372 - 19 - 09|FATHUROHIM AULIA|Ponorogo, 20 Juli 2008|Laki-Laki|SMP FATHUL MUNA|Imam Sukirno|Baosan Kidul, Ngrayun, Ponorogo
3373 - 19 - 09|NADHIFA RAHMA DEWANTI|Ponorogo, 23 Juli 2007|Perempuan|SMKN 1 SLAHUNG|Sumari / Misinem|Singkil, Balong, Ponorogo
3374 - 19 - 09|MUH.RIFAI AINURSALAM|Ponorogo, 04 Mei 2012|Laki-Laki|SDN 8 BAOSAN LOR|Nurwahid / Seniati|Baosan Kidul, Ngrayun, Ponorogo
3375 - 19 - 09|AYUNDA CHINTIYA FIRDA SARI NING TIYAS|Ponorogo, 20 November 2011|Perempuan|SDN 4 BAOSAN LOR|Riyanto / Subinti|Baosan Lor, Ngrayun, Ponorogo
3376 - 19 - 09|ZASKIA ALTHOFUNISA|Ponorogo, 23 Mei 2012|Perempuan|MI MA'RIF AL - FAQIH|Trimawan / Erna Rahmawati|Wringinanom, Sambit, Ponorogo
3377 - 19 - 09|FAJAR APRIAN ALI MUSYAFA|Pacitan, 06 Juni 2013|Laki-Laki|SDIT AL-MAWADDAH COPER|Supriono / Siti Nurul Solikah|Wringinanom, Sambit, Ponorogo
3378 - 19 - 09|DIAN WAHYU PUTRI|Pacitan, 06 November 2008|Perempuan|SMPN 5 TAGALOMBO|Miswan / Suprihatun|Ploso, Tegalombo, Pacitan
3379 - 19 - 09|AMELIA RAHMAWATI|Pacitan, 05 Agustus 2009|Perempuan|SMPN 5 TAGALOMBO|Sukatno / Tutik Susanti|Ploso, Tegalombo, Pacitan
3380 - 19 - 09|MIFTAHUL MUDTAQIN|Pacitan, 23 Juni 2009|Laki-Laki|MTS AL FATTAH TAHUNAN|Mahmud Jiono / Paryati|Ploso, Tegalombo, Pacitan
3381 - 19 - 09|ANDIKA PUTRA FERDIANSA|Pacitan, 06 Juli 2007|Laki-Laki|MA AL FATTAH TAHUNAN|Sugianto / Murtini|Ploso, Tegalombo, Pacitan
3382 - 19 - 09|SELVIRA JULIA INDRIANA SARI|Pacitan, 31 Juli 2009|Perempuan|SMPN 5 TAGALOMBO|Jarno / Misti|Ploso, Tegalombo, Pacitan
3383 - 19 - 09|NATHAN ADI PRATAMA|Pacitan, 12 Agustus 2010|Laki-Laki|SMKN 1 BANDAR PACITAN|Nur Handoko/Wiwid Widiani|Kledung, Bandar, Pacitan
3384 - 19 - 09|RIZKI ALFIAN NUGROHO|Pacitan, 18 November 2009|Laki-Laki|SMPN 1 BANDAR PACITAN|Suparno/Suwarti|Kledung, Bandar, Pacitan
3385 - 19 - 09|DELTA AYU SAFIRA|Pacitan, 30 Desember 2010|Perempuan|MTS. AL - FATTAH TAHUNAN|Meseri/Wiwin Winarti|Ploso, Tegalombo, Pacitan
3386 - 19 - 09|ARSYAVIN MORGAN DIESTA HAIYKAL|Ponorogo, 13 Desember 2012|Laki-Laki|SDN 2 TAHUNAN BARU TEGALOMBO|Didik Budi Santoso / Ika Yuliana|Ngilo-Ilo, Slahung, Ponorogo
3387 - 19 - 09|FAHRIS IMRON KHOIRI|Ponorogo, 12 Mei 2012|Laki-Laki|SDN 2 TAHUNAN BARU TEGALOMBO|Wagiyanto / Sri Purwati|Ngilo-Ilo, Slahung, Ponorogo
3388 - 19 - 09|AHMAD NUR HASAN|Ponorogo, 11 Maret 2012|Laki-Laki|SDN 2 TAHUNAN BARU TEGALOMBO|Jari Nur Said / Sri Lestari|Ngilo-Ilo, Slahung, Ponorogo
3389 - 19 - 09|JAHAROH IZZAH FADZILAH|Ponorogo, 09 Desember 2011|Perempuan|MTS. AL - HIKMAH NGRAYUN|Lamiyo / Tulastri|Baosan Kidul, Ngrayun, Ponorogo
3390 - 19 - 09|ADITYA RAHMAT WIDYANTO|Ponorogo, 26 Juni 2009|Laki-Laki|MA. AL - HIKMAH NGRAYUN|Tato / Widya Supartin|Baosan Lor, Ngrayun, Ponorogo
3391 - 19 - 09|MIFTAHUL HIDAYAH ISMAIL|Ponorogo, 21 Mei 2012|Laki-Laki|MTS. AL - HIKMAH NGRAYUN|Imam Mutakin / Siti Rukayah|Mrayan, Ngrayun, Ponorogo
3392 - 19 - 09|BRAMA ECHA PRASETYA|Pacitan, 19 Desember 2012|Laki-Laki|SMPN 2 GEMAHARJO|Arif Setyo Darmanto / Duwi Ekasari|Tahunan Baru, Tegalombo, Pacitan
3393 - 19 - 09|AHMAD JENDRA ALHAFIDL|Pacitan, 13 Oktober 2012|Laki-Laki|SMPN 2 GEMAHARJO|Budiono / Dewi Agustina|Tahunan Baru, Tegalombo, Pacitan
3394 - 19 - 09|EVI YUNITA ANGGRAINI|Pacitan, 08 Juni 2011|Perempuan|MA. AL - FATTAH TAHUNAN|Darmanto / Maryam|Tahunan Baru, Tegalombo, Pacitan
3395 - 19 - 09|NADIYA SEPTIA MAHARANI|Pacitan, 24 September 2010|Perempuan|MA. AL - FATTAH TAHUNAN|Hendrik Kurniawan / Surati|Tahunan Baru, Tegalombo, Pacitan
3396 - 19 - 09|FATHYA ALVINATUL RISKI|Pacitan, 30 Desember 2006|Perempuan|SMK. AL - FATTAH TAHUNAN|Marjito / Partini|Tahunan Baru, Tegalombo, Pacitan
3397 - 19 - 09|ADITIYA PRADANA PUTRA|Pacitan, 03 Mei 2007|Laki-Laki|SDN 1 GEMAHARJO|Sukadi / Suhartini|Tahunan Baru, Tegalombo, Pacitan
3398 - 19 - 09|ZION ALFA SATIAGRAHA|Pacitan, 29 Juni 2010|Laki-Laki|MTS. MUHAMMDIYAH BANDAR|Kaseri / Mesiyem|Kledung, Bandar, Pacitan
3399 - 19 - 09|ABDUL AZIS KHOIRY|Pacitan, 05 Februari 2010|Laki-Laki|SMKN BANDAR|Tumirin / Sri Utami|Kledung, Bandar, Pacitan
3400 - 19 - 09|KURNIA NASIROH|Pacitan, 20 Februari 2013|Perempuan|SMPN 1 BANDAR|Suparno / Suwarti|Kledung, Bandar, Pacitan
3401 - 19 - 09|FARIS AL GOZHI|Pacitan, 06 Juli 2008|Laki-Laki|SMPN 1 BANDAR|Eko Ferianto / Karsini|Mangunharjo, Arjosari, Pacitan
3402 - 19 - 09|YOGI FIRNANDA|Pacitan, 26 Agustus 2012|Laki-Laki|SMPN 5 TEGALOMBO|Mulyono / Rani Febrianti|Ploso, Tegalombo, Pacitan
3403 - 19 - 09|AGUS FRIANTO|Pacitan, 02 Agustus 2013|Laki-Laki|SDN 2 PLOSO|Mispan / Lasmini|Ploso, Tegalombo, Pacitan
3404 - 19 - 09|MELFIN RIFA'I|Pacitan, 02 November 2011|Laki-Laki|SMPN 5 TEGALOMBO|Wasit / Tumini|Ploso, Tegalombo, Pacitan
3405 - 19 - 09|RISKI ALFIAN|Pacitan, 15 Februari 2010|Laki-Laki|SMPN 5 TEGALOMBO|Giyanto / Etik Ernawati|Ploso, Tegalombo, Pacitan
3406 - 19 - 09|ANGGIA RESTU INVANI|Pacitan, 03 September 2010|Perempuan|SMKN BANDAR|Adi Aulia Ardiansah / Surati|Kledung, Bandar, Pacitan
3407 - 19 - 09|EDI TRIATMOKO|Pacitan, 24 Mei 2012|Laki-Laki|SMPN 5 TEGALOMBO|Soiman / Sujiati|Ploso, Tegalombo, Pacitan
3408 - 19 - 09|ANANG SETIYAWAN|Pacitan, 22 Juli 2010|Laki-Laki|SMKN BANDAR|Teguh Wiyono / Trismiatin|Mangunharjo, Arjosari, Pacitan
3409 - 19 - 09|WILDAN ALRUZAIN|Pacitan, 16 April 2012|Laki-Laki|SMPN 2 TEGALOMBO|Paniran / Warsiyem|Gemaharjo, Tegalombo, Pacitan
3410 - 19 - 09|ANANDA RIO RISKI SAPUTRA|Pacitan, 26 Mei 2000|Laki-Laki|SMAN 1 TEGALOMBO|Mujiran / Sri Handayani|Margahayu, Loa Kulu
3411 - 19 - 09|FANI AFNAN NURHAFIZAH|Banjarnegara, 23 April 2010|Perempuan|MA DARUL ISTIQOMAH|Mohamad Khoirul Anifin / Siti Mukharomah|Winong, Bawang, Banjarnegara
3412 - 19 - 09|MOHAMMAD MAFTUH FADLI|Ponorogo, 10 Februari 2010|Laki-Laki|MA DARUL ISTIQOMAH|Kani / Sumiati|Semanding, Kauman, Ponorogo
3413 - 19 - 09|MUROBBI EKA ADITYA|Ponorogo, 05 Maret 2010|Laki-Laki|MA DARUL ISTIQOMAH|Poniran / Yati|Semanding, Kauman, Ponorogo
3414 - 19 - 09|SYNTIA 'ULYA KHUSNITA|Ponorogo, 24 Juli 2009|Perempuan|MA DARUL ISTIQOMAH|Parni / Parti|Dadapan, Balong, Ponorogo
3415 - 19 - 09|MUHAMMAD AMHAR MUMTAZ|Ponorogo, 20 Juni 2010|Laki-Laki|MTS. DARUL ISTIQOMAH|Kusno, S.Pd. I / Ema Wardati, S.Pd. I|Ngumpul, Jambon, Ponorogo
3416 - 19 - 09|IJAT FAHEM BADIUL ALAM|Ponorogo, 08 November 2011|Laki-Laki|MTS. DARUL ISTIQOMAH|Sunarno / Dwi Erni Widiastuti|Ngumpul, Jambon, Ponorogo
3417 - 19 - 09|MUHAMMAD ZAKARIYA NURROHMAN|Ponorogo, 13 Oktober 2011|Laki-Laki|MTS. DARUL ISTIQOMAH|Prianto / Sunarti|Pandak, Balong, Ponorogo
3418 - 19 - 09|MUHAMAD ALDY NURSALAM|Nganjuk, 12 Desember 2011|Laki-Laki|MTS. DARUL ISTIQOMAH|Ali Jafar Shodiq / Parmiatun|Ngumpul, Jambon, Ponorogo
3419 - 19 - 09|NABIL ZAKI IBRAHIM|Tangerang, 19 November 2008|Laki-Laki|MTS. AL - ISLAM JORESAN|Casmudi / Hesti Setiarini|Tambakrejo, Pemalang, Jawa Tengah
3420 - 19 - 09|ULUL ALBAB|Sukamulya, 16 September 2008|Laki-Laki|MTS. AL - ISLAM JORESAN|Supriyanto / Sri Haryati|Rawamangun, Pulogadung, Jakarta Timur
3421 - 19 - 09|AHMAD WILDAN ROMDLONI|Ponorogo, 22 Agustus 2011|Laki-Laki|MTS. AL - ISLAM JORESAN|Samsuri / Wiji Utami|Joresan, Mlarak, Ponorogo
3422 - 19 - 09|MUHAMMAD RIDHO SAPUTRA|Surabaya, 30 Mei 2010|Laki-Laki|MTS. AL - ISLAM JORESAN|Suparman / Sumarpi|Bajang, Mlarak, Ponorogo
3423 - 19 - 09|MUHAMMAD ROHMAN|Jakarta, 23 Oktober 2009|Laki-Laki|MTS. AL - ISLAM JORESAN|Alm Anen Priyatna / Suginem|Tangen, Sragen, Jawa Tengah
3424 - 19 - 09|ZAYANA FAWAZARSYA RUWAIDAH|Ponorogo, 17 Juli 2005|Perempuan|UIN PONOROGO|Syamsudin / Siti Arini|Joresan, Mlarak, Ponorogo
3425 - 19 - 09|AHMAD MUSYAFA NASYWATUL WAFFA|Lamongan, 13 Maret 2009|Laki-Laki|MTS. AL - ISLAM JORESAN|Latief Ali Zahrowi / Zaitul Erni|Kariangau, Balikpapan Barat, Kaltim
3426 - 19 - 09|AHMAD SABHAL LATHAF|Ponorogo, 23 Februari 2008|Laki-Laki|MTS. AL - ISLAM JORESAN|Rohmat Fadeli / Mursini|Bulu, Sambit, Ponorogo
3427 - 19 - 09|DWI PUTRA PRAYOGO|Magetan, 30 Maret 2010|Laki-Laki|MTS. AL - ISLAM JORESAN|Komarudin / Susilawati|Dukuh, Lembeyan, Magetan
3428 - 19 - 09|ISMA FAIZATUL MUNA|Ponorogo, 18 Januari 2004|Perempuan|MTS. AL - ISLAM JORESAN|Muhrodji / Siti Solekah|Joresan, Mlarak, Ponorogo
3429 - 19 - 09|ARSYA RIZKY AL MUBAROK|Ponorogo, 14 Juni 2013|Laki-Laki|MTs.MIFTAHUL ULUM NGRAKET|Tukimun / Sutini|Jonggol, Jambon, Ponorogo
3430 - 19 - 09|STEVEN ORVA ROLANDA|Ponorogo, 12 Juni 2014|Laki-Laki|PP.DARUL HUDA MAYAK|Muh Heri Purwanto / Renita Tri Oktapia Dewi|Jonggol, Jambon, Ponorogo
3431 - 19 - 09|KELVIN RAMDANI SAPUTRA|Ponorogo, 02 Februari 2013|Laki-Laki|SMPN 2 BALONG|Trimo / Nanik Minasri|Jonggol, Jambon, Ponorogo
3432 - 19 - 09|NADIA HASNA SAKHI|Ponorogo, 25 Juli 2012|Perempuan|MTs.MIFTAHUL ULUM NGRAKET|Sarju / Robit Tahtul Asadah|Jonggol, Jambon, Ponorogo
3433 - 19 - 09|NATHANIA AYU EVELINNA|Ponorogo, 18 Desember 2009|Perempuan|SMK KESEHATAN PONOROGO|Bambang Maulana Maheswara / Fitri Yuliana|Jonggol, Jambon, Ponorogo
3434 - 19 - 09|FRISKA LAURENZIA LIDIA SABELLA|Ponorogo, 04 Maret 2011|Perempuan|SMAN 1 BADEGAN|Mudjiono / Ria Dewi Yuliati|Jonggol, Jambon, Ponorogo
3435 - 19 - 09|ERLIA NUR HIDAYAH|Ponorogo, 16 Februari 2011|Perempuan|SMK KESEHATAN BIMPO|Sugito / Umi Andarwati|Jonggol, Jambon, Ponorogo
3436 - 19 - 09|JOSHUA DAREN PRATAMA|Ponorogo, 06 Januari 2014|Laki-Laki|MTs.MIFTAHUL ULUM NGRAKET|Panji Asmoro / Katemi|Jonggol, Jambon, Ponorogo
3437 - 19 - 09|ARDAN ZHAFRAN DWI MAHADIKA|Ponorogo, 20 Maret 2013|Laki-Laki|SMPN 1 BALONG|Agus Supriyono / Puji Lestari|Ngampel, Balong, Ponorogo
3438 - 19 - 09|DAFFA FIRDAUS FIRJATULLAH|Ponorogo, 19 November 2009|Laki-Laki|SMK PGRI 2 PONOROGO|Hariyanto / Wijayanti|Ngampel, Balong, Ponorogo
3439 - 19 - 09|DIMAS ADHYASTHA BAGUS PAMBUDI|Ponorogo, 23 Januari 2013|Laki-Laki|SMPN 1 BALONG|Pambudi / Uswatun Hasanah|Ngampel, Balong, Ponorogo
3440 - 19 - 09|ANGGA BRIANTAMA|Ponorogo, 10 November 2011|Laki-Laki|SMPN 1 JETIS|Zaenal Abidin / Suratmi|Ngampel, Balong, Ponorogo
3441 - 19 - 09|KARTIKA NUR LAILATUR ROHMAH|Pacitan, 03 Juli 2011|Perempuan|SMKN 1 SLAHUNG|Yuris Nur Kholid / Nurul Amin|Ngilo-Ilo, Slahung, Ponorogo
3442 - 19 - 09|ALEEZA ARUMADHANI KAYOON|Ponorogo, 10 Juli 2013|Perempuan|MTS. MIFTAHUS SALAM KAMBENG|Susilo / Titik Handayani|Ngilo-Ilo, Slahung, Ponorogo
3443 - 19 - 09|HUSAIN SHAHBAZ|Ponorogo, 27 Maret 2013|Laki-Laki|SMPN 2 BALONG|Giman / Sri Wahyuni|Ngasinan, Jetis, Ponorogo
3444 - 19 - 09|MUHAMMAD NAUFAL ALFA RIZKY|Ponorogo, 19 Maret 2012|Laki-Laki|MTSN 1 PONOROGO|Mohammad Toha / Siti Fatimah|Bajang, Balong, Ponorogo
3445 - 19 - 09|MUHAMMAD RIZAL AVID AIMAN|Ponorogo, 24 November 2012|Laki-Laki|SMPN 1 BALONG|Sukateman / Rina Kholifatus|Bajang, Balong, Ponorogo
3446 - 19 - 09|SHUMA 'ALIM MUHAMMAD SYAH|Ponorogo, 30 September 2006|Laki-Laki|UIN PONOROGO|Ma'shum Syah, S.Psi, M.Psi / Syaukati Karimah, S.Pd|Truneng, Slahung, Ponorogo
3447 - 19 - 09|PRASTYO ADI NUGROHO|Ponorogo, 30 Oktober 2008|Laki-Laki|SMKN SLAHUNG|Karlan / Sri Fatimah|Bungkal, Bungkal, Ponorogo
3448 - 19 - 09|ERFA'RAJ ALFARIZQY|Ponorogo, 11 Februari 2012|Laki-Laki|SMPN 2 BUNGKAL|Suryanto / Rulik Hartatik|Kupuk, Bungkal, Ponorogo
3449 - 19 - 09|EGAR RESTU URAFA|Ponorogo, 27 Mei 2012|Laki-Laki|SMPN 2 BUNGKAL|Soiran / Sri Suharni|Kupuk, Bungkal, Ponorogo
3450 - 19 - 09|SRI SUHARNI|Lampung Selatan, 19 Maret 1981|Perempuan|SMK MUHAMMADIYAH 1 KALIANDA|Solikhin / Toilah|Kupuk, Bungkal, Ponorogo
3451 - 19 - 09|SATRIA BINTANG BUMI|Ponorogo, 25 Februari 2013|Laki-Laki|SMPN 2 BUNGKAL|Soiran / Sri Suharni|Kupuk, Bungkal, Ponorogo
3452 - 19 - 09|LEONY PRIATMAYA|Ponorogo, 14 Januari 2013|Perempuan|SMPN 2 BALONG|Supriyadi / Maimunah|Ngendut, Balong, Ponorogo
3453 - 19 - 09|RAHMAT FAIZ NUR KHAMBALI|Ponorogo, 20 Agustus 2014|Laki-Laki|SDN 3 KARANG PATIHAN|Arif Ampil Maksum / Meti Antika|Ngendut, Balong, Ponorogo
3454 - 19 - 09|RADITYA FERENDRA HAIKAL IBRAHIM|Ponorogo, 01 September 2012|Laki-Laki|SMPN 2 BALONG|Nanang Siswanto / Susanti|Ngendut, Balong, Ponorogo
3455 - 19 - 09|RAMADHAN AKBAR PERDANA|Ponorogo, 18 Agustus 2012|Laki-Laki|SMPN 1 JETIS|Muhtadin / Srini|Karanggebang, Jetis, Ponorogo
3456 - 19 - 09|ADIB FARDAN AL FARIZI|Ponorogo, 29 Juli 2010|Laki-Laki|MTS. AL - ISLAM|Suyono / Anis Fatmawati|Karanggebang, Jetis, Ponorogo
3457 - 19 - 09|MUHAMMAD RIZKY SYAHREZA|Ponorogo, 04 November 2013|Laki-Laki|MI AL - JIHAD KARANGGEBANG|Subur / Nuroh|Karanggebang, Jetis, Ponorogo
3458 - 19 - 09|AHMAD RIZQI MUSTHOFA HABIBI|Ponorogo, 01 Januari 2011|Laki-Laki|SMPN 1 JETIS|Gianto / Rosanti|Karanggebang, Jetis, Ponorogo
3459 - 19 - 09|MOH.RIFQI MUNIRUL JANANI|Ponorogo, 11 Oktober 2009|Laki-Laki|MTS. JORESAN|Jemari / widarti|Karanggebang, Jetis, Ponorogo
3460 - 19 - 09|TAMA DWI WARDANA|Ponorogo, 26 Maret 2012|Laki-Laki|SMPN 1 JETIS|Dedi Dwi Wijaya / Ervi Fitrianingrum|Karanggebang, Jetis, Ponorogo
3461 - 19 - 09|FATIHA NAFIATUL HAMIDAH|Ponorogo, 04 Mei 2011|Perempuan|MTS. RONGGOWARSITO TEGALSARI|Khoirul Musthofa / Surati|Tegalsari, Jetis, Ponorogo
3462 - 19 - 09|ADIBA SAKILA ATMARINI|Ponorogo, 25 Desember 2015|Perempuan|MI AL - JIHAD KARANGGEBANG|Edi Prayitno / Irawati Isnaeni|Tegalsari, Jetis, Ponorogo
3463 - 19 - 09|MUHAMMAD ALIF NAUFAL AFKAR|Ponorogo, 21 November 2014|Laki-Laki|SDN TEGALSARI|Saiful anam / Sri Wulan Fitri|Tegalsari, Jetis, Ponorogo
3464 - 19 - 09|MUHAMMAD ALKAHFI IBRAHIMOVIC|Ponorogo, 20 Juni 2012|Laki-Laki|SMPN 1 JETIS|Mohamad Warno / Sutiani|Bedrug, Pulung, Ponorogo
3465 - 19 - 09|RAISYA PUTRI EKA NURGANTI|Ponorogo, 08 Agustus 2014|Perempuan|SDN TEGALSARI|Budi Santoso / Yeni Novita Eliana|Josari, Jetis, Ponorogo
3466 - 19 - 09|ALBERT ZIVEN MAHFUZH AMIRUDIN|Ponorogo, 21 Mei 2013|Laki-Laki|SMPN 2 BALONG|Samsuri / Nuraini Muyasaroh|Singkil, Balong, Ponorogo
3467 - 19 - 09|MAYA PUTRI ADZKIA QURROTUL FUADAH|Ponorogo, 25 Mei 2008|Perempuan|SMKN 2 PONOROGO|Imam Tohari / Dwi Ernawati|Singkil, Balong, Ponorogo
3468 - 19 - 09|PUPUT WAGI PUTRI|Ponorogo, 30 Juli 2009|Perempuan|SMPN 2 BALONG|Senen / Partin|Singkil, Balong, Ponorogo
3469 - 19 - 09|ALYA KHOIRUN NISA|Ponorogo, 08 April 2006|Perempuan|SMKN 1 SLAHUNG|Jamari / Marsiyem|Nailan, Slahung, Ponorogo
3470 - 19 - 09|AFID IHSAN KAROHMAN|Ponorogo, 12 September 2008|Laki-Laki|SMPN 2 BALONG|Hariyadi / Samitun|Sedarat, Balong, Ponorogo
3471 - 19 - 09|NAWAF GALEH PRASETYO|Ponorogo, 15 April 2010|Laki-Laki|SMPN 1 BALONG|Jemono / Mesinem|Singkil, Balong, Ponorogo
3472 - 19 - 09|SALSABILLA ALFIRJANNAH|Ponorogo, 14 September 2012|Perempuan|SMPN 2 BALONG|Edy Suprapto / Siti Hartatik|Balong, Balong, Ponorogo
3473 - 19 - 09|ADIS ARDIANSYAH APRILIO|Ponorogo, 23 April 2013|Laki-Laki|SMPN 1 BALONG|Sunardi / Narni|Singkil, Balong, Ponorogo
3474 - 19 - 09|RIDWAN DWI PRABOWO|Ponorogo, 12 Oktober 2008|Laki-Laki|SMPN 2 BALONG|semun / Suminem|Sedarat, Balong, Ponorogo
3475 - 19 - 09|ARY MUKTI|Ponorogo, 09 Januari 2005|Laki-Laki|MA MIFTAHUL ULUM|Tumiran / Sri Rahayu|Sedarat, Balong, Ponorogo
3476 - 19 - 09|NOVI WULAN NINGRUM WIJAYANTI|Ponorogo, 20 November 2008|Perempuan|MTs. MA'ARIF BALONG|Mujito / Siti Nur Janah|Singkil, Balong, Ponorogo
3477 - 19 - 09|AMIRA HANIN DZAKIYYAH|Ponorogo, 21 Juni 2012|Perempuan|SMPN 1 BALONG|Edi Cahyono / Eni Wijandari|Singkil, Balong, Ponorogo
3478 - 19 - 09|SHAM ZUMAR BADRANI|Ponorogo, 01 Juni 2011|Laki-Laki|MTs. MA'ARIF AL - ISHLAH BUNGKAL|Sarjono / Ummi Hasanatul Fadlilatin|Nambak, Bungkal, Ponorogo
3479 - 19 - 09|ANUGRAH RAMSA LAZUARDI|Ponorogo, 10 April 2011|Laki-Laki|SDN 1 BALONG|Slamet S.Sos / Nur Hidayah|Gombang, Slahung, Ponorogo
3480 - 19 - 09|NAYLA DAEFA PRATISTA|Ponorogo, 15 Mei 2014|Perempuan|SDN 4 MRAYAN|Edi Prasetyo / Wiwik Setiawati|Mrayan, Ngrayun, Ponorogo
3481 - 19 - 09|AFRILIANSYAH|Muara Bungo, 12 April 2010|Laki-Laki|MA DARUL ISTIQOMAH|Syafrizal / Amsakiati|Teluk Kembang Jambu, Tebo Ulu, Tebo, Jambi
3482 - 19 - 09|BILLY ALFA JUNIOR|Ponorogo, 05 Mei 2011|Laki-Laki|SDN JEBENG|Bambang Eko Hari Prasetyo / Sulipah|Jebeng, Slahung, Ponorogo
3483 - 19 - 09|ZIYANA FAWAZARSYA RUWAIDAH|Ponorogo, 17 Juli 2005|Perempuan|UIN PONOROGO|Syamsudin / Siti Arini|Joresan, Mlarak, Ponorogo
3484 - 19 - 09|MUHAMMAD ABID AQILA RAHMANI|Ponorogo, 20 Juni 2014|Laki-Laki|MI MA'ARIF GANDU MLARAK|Moch.In'am Rahmani / Husna Ni'matul Ulya|Gandu, Mlarak, Ponorogo
3485 - 19 - 09|AZRIEL BARIQ MURTAZA|Ponorogo, 17 Juli 2005|Laki-Laki|PONPES MR.BOB|UsmanYudi / Muhayyaroh|Gandu, Mlarak, Ponorogo
3486 - 19 - 09|DIANA PURIYATUL JANNAH|Ponorogo, 03 Februari 2014|Perempuan|SDN 2 SENEPO SLAHUNG|Sujarwanto / Jemitun|Senepo, Slahung, Ponorogo
3487 - 19 - 09|M.VIAN ERLANGGA SAPUTRA|Ponorogo, 24 Desember 2012|Laki-Laki|SDN 2 SENEPO SLAHUNG|Syahrul / Linda|Senepo, Slahung, Ponorogo
3488 - 19 - 09|ANDHIKA DWI FANGGARA PUTRA|Ponorogo, 21 September 2012|Laki-Laki|SDN 2 SENEPO SLAHUNG|Atim Iswahyudi / Tutiana|Senepo, Slahung, Ponorogo
3489 - 19 - 09|ADI MUHAMAD RIDWAN|Ponorogo, 17 Februari 2014|Laki-Laki|SDN 2 SENEPO SLAHUNG|Paniman / Istiana|Senepo, Slahung, Ponorogo
3490 - 19 - 09|ADELLIA DWI LESTARI|Ponorogo, 07 Desember 2011|Perempuan|SDN 2 SENEPO SLAHUNG|Margono / Wiji Lestari|Senepo, Slahung, Ponorogo
3491 - 19 - 09|RISKA AYU PUTRI WARDIANA|Ponorogo, 06 Agustus 2008|Perempuan|SMKN 1 SLAHUNG|Miswadi / Darnawati|Singkil, Balong, Ponorogo
3492 - 19 - 09|THOMA 'IZZUL UMAM|Ponorogo, 14 November 2011|Laki-Laki|MTS. AL - ISLAM JORESAN|Bahrudin / Emy Nur Hamibah|Karang Gebang, Jetis, Kab. Ponorogo
3493 - 19 - 09|WAHYU RAFIF APRILIO ALFARIZI|Ponorogo, 18 April 2015|Laki-Laki|SDN 2 TAHUNAN BARU TEGALOMBO|Edi sutrisno / Endang Sri Wahyuning|Ngilo-Ilo, Slahung, Ponorogo
3494 - 19 - 09|SEPTIAN TRIANI YOGA ADHITAMA|Ponorogo, 06 September 2006|Laki-Laki|MA MA'ARIF KRATON MOJO KEDIRI|Parni / Jemitri|Grogol, Sawoo Ponorogo
3495 - 19 - 09|AKBAR RAFI ANANDA|Trenggalek, 08 Desember 2009|Laki-Laki|SDN 2 SENEPO SLAHUNG|Hadi Sutrisno / Komarul Hidayah|Senepo, Slahung, Ponorogo
3496 - 19 - 09|ALIF EKA NURDIANSYAH|Ponorogo, 05 Mei 2011|Laki-Laki|SMPN 2 BALONG|Didik Purnomo / Winarsih|Karangpatihan, Balong, Ponorogo
3497 - 19 - 09|RAFEL ADINATA FANEZA|Ponorogo, 07 Mei 2013|Laki-Laki|MTS. MIFTAHUL ULUM NGRAKET|Soni / Ponirah|Pandak, Balong, Ponorogo
3498 - 19 - 09|SRI SUHARNI|Lampung Selatan, 19 Maret 1981|Perempuan|SMP MUHAMMADIYAH 1 KALIANDA|Sholikin / Toilah|Kupuk, Bungkal, Ponorogo
3499 - 19 - 09|LARAS INDAH ANUGRAHITA SURGAWI|Ponorogo, 17 Mei 2009|Perempuan|SMK PGRI 1 PONOROGO|Edhi Prastyo / Sri Kusuma Rahayu|Nglewan, Sambit, Ponorogo
3500 - 19 - 09|ELYAS REZA ALQHIFARI|Ponorogo, 27 Januari 2014|Laki-Laki|MIN 3 PONOROGO|Budi hartoyo / Patonah|Gombang, Slahung, Ponorogo
3501 - 19 - 09|NIKA PUTRI ANDINI|Ponorogo, 29 Agustus 2007|Perempuan|MA MA'ARIF BALONG|Katimun / Tumini|Singkil, Balong, Ponorogo
3502 - 19 - 09|REIHAN WIJAYA KUSUMA|Oku Timur, 13 November 2008|Laki-Laki|SMK MUHAMMADIYAH RAWA BENING|Salim / Siti Mukaromah|Suka Maju, Belitang Oku Timur, Sumsel
3503 - 19 - 09|RAFQY ADITYA AFFANI|Ponorogo, 08 September 2012|Laki-Laki|MTS. DARUL HUDA MAYAK|Bambang Pamuji / Nur Lailatul Mukaromah|Pandak, Balong, Ponorogo
3504 - 19 - 09|ALFI NUR DINA|Ponorogo, 30 April 2013|Perempuan|SMPN 2 BALONG|Sidik Yulianto / Enik Winartin|Pandak, Balong, Ponorogo
3505 - 19 - 09|DAVID SETYAWAN|Ponorogo, 29 September 2012|Laki-Laki|MTS. MIFTAHUL ULUM NGRAKET|Supriyadi / Boyati|Pandak, Balong, Ponorogo
3506 - 19 - 09|INDRI JULIANTI|Ponorogo, 22 Juli 2012|Perempuan|MTS. MIFTAHUL ULUM NGRAKET|Barno / Siti Munawaroh|Pandak, Balong, Ponorogo
3507 - 19 - 09|KAILA ASYIFATUR ROHMAH|Ponorogo, 10 November 2011|Perempuan|SMP N 2 BALONG|Jarwoto / Sulistyowati|Pandak, Balong, Ponorogo
3508 - 19 - 09|MUHAMMAD AFFIS|Jombang, 14 April 2008|Laki-Laki|MAN 2 PONOROGO|Misno / Aifa|Gombang, Slahung, Ponorogo
3509 - 19 - 09|EVAN PRIMA AUGUSTA|Ponorogo, 02 September 2011|Laki-Laki|SDN NGRAKET|Mislan / Yuliani|Ngraket, Balong, Ponorogo
3510 - 19 - 09|EFRENZO VIRGONATA RAMADHANY|Ponorogo, 25 Agustus 2009|Laki-Laki|MTs. MA'ARIF BALONG|Harianto / Elys Nuryati|Gombang, Slahung, Ponorogo
3511 - 19 - 09|EVAN SABRY DANENDRA|Ponorogo, 27 November 2014|Laki-Laki|SDN 1 BALONG|Harianto / Elys Nuryati|Gombang, Slahung, Ponorogo
3512 - 19 - 09|ANUGRAH RAMSA LAZUARDI|Ponorogo, 10 April 2011|Laki-Laki|SDN 1 BALONG|Slamet S.Sos / Nur Hidayah|Gombang, Slahung, Ponorogo
3513 - 19 - 09|SITI NORDIANA|Petaling Jaya, 18 Agustus 2005|Perempuan|MA MAARIF BALONG|Parno / Yumaroh|Gombang, Slahung, Ponorogo
3514 - 19 - 09|DAVID ANANDA CANDRAPRATAMA|Ponorogo, 09 Desember 2008|Laki-Laki|MTSN 1 PONOROGO|Agus Santoso / Sri Rejeki|Gombang, Slahung, Ponorogo
3515 - 19 - 09|ABU NASHR DA'I ROBBY|Ponorogo, 25 Juli 2008|Laki-Laki|MTs. MA'ARIF BALONG|Zaini / Catur Wulandari|Gombang, Slahung, Ponorogo
3516 - 19 - 09|FANDA ARIS HARIYANTO|Madiun, 11 Februari 2008|Laki-Laki|SMKN 1 GEGER MADIUN|Slamet Hariyono / Ariana|Klorogan, Geger, Madiun
3517 - 19 - 09|MAARIP|Tanjab Barat, 17 Juni 2003|Laki-Laki|MA WALISONGO KEBONSARI|Ahmadi / Umi Baikah|Margo Rukun, Senyerang, Tanjung Jabung Barat Jambi
3518 - 19 - 09|DWI ALFIANSAH|Ponorogo, 26 Juli 2009|Laki-Laki|MA WALISONGO KEBONSARI|Samuji / Marini|Ngebel, Ngebel, Ponorogo
3519 - 19 - 09|ARIF FUADI|Muara Bungo, 03 Oktober 2003|Laki-Laki|MA WALISONGO KEBONSARI|Yanto Muhammad Amrullah / Siti Samsiyah|Suka Damai, Rimbo Ulu, Tebo Jambi
3520 - 19 - 09|LAFIF AKMAL MAHIR MUAWIM|Madiun, 12 Februari 2004|Laki-Laki|MA WALISONGO KEBONSARI|Sarno / Purniasih|Candi Mulyo, Dolopo, Madiun
3521 - 19 - 09|HARDIYANTI INDAH SAPUTRI|Magelang, 14 Agustus 2015|Perempuan|SDN 1 BANGUNSARI DOLOPO|Hariyadi / Nur Azizah|Dolopo, Dolopo, Madiun
3522 - 19 - 09|REVALDO ISKANDAR ZULKARNAEN|Madiun, 22 Juli 2009|Laki-Laki|MAN 1 MADIUN|Nur Sanderi / Nurul Ambarwati|Klorogan, Geger, Madiun
3523 - 19 - 09|M.IQBAL HASANUDDIN|Madiun, 14 April 2007|Laki-Laki|MA WALISONGO KEBONSARI|Mustofa / Nanik Purwati|Prambon, Dagangan, Madiun
3524 - 19 - 09|ANDIKA KHAMIM JAZULI|Rembang, 18 Juni 2007|Laki-Laki|MA WALISONGO KEBONSARI|Sukoco / Siti Khalifah|Logung, Sumber, Rembang
3525 - 19 - 09|MUHAMMAD ULIL ALBAB|Madiun, 30 Mei 2011|Laki-Laki|MTSN 1 DOLOPO|Suparno / Marfuah|Kelingan, Dolopo, Madiun
3526 - 19 - 09|ACMAD ROCKY AMIRUDIN|Madiun, 23 Januari 2010|Laki-Laki|SMK PGRI 2 PONOROGO|Choirul Anam / Marini|Cacingan, Dolopo, Madiun
3527 - 19 - 09|IRFAN MAULANA FAIRUZZANI|Madiun, 21 Februari 2010|Laki-Laki|MAN 3 DOLOPO|Misnan / Sutiyah|Dolopo, Dolopo, Madiun
3528 - 19 - 09|ANDIKA SATRIA PRADANA|Madiun, 22 Juli 2008|Laki-Laki|MAN 3 DOLOPO|Sarji / Ratna Wati|Sirah Nogo, Dolopo, Madiun
3529 - 19 - 09|DEVA NAUFALA ZZAM|Ponorogo, 31 Mei 2013|Laki-Laki|SMPN 3 DOLOPO|Didik Prasetio / Karmini|Ngebel, Ngebel, Ponorogo
3530 - 19 - 09|AMIRA LU'LUATUL HAFIDZA|Ponorogo, 31 Mei 2010|Perempuan|SMAN 1 DOLOPO|Suroso / Indah Wahyuni|Mlilir, Dolopo, Madiun
3531 - 19 - 09|SAMARA DITAWANTI SHOLIHAH|Madiun, 03 Maret 2010|Perempuan|MAN 3 DOLOPO|Edy Gunawan / Suprapti|Suluk, Dolopo, Madiun
3532 - 19 - 09|NAURA MELATI|Padang, 12 Maret 2025|Perempuan|SMPN 1 MLARAK|Sugito / Anik Yuliani|Mojorejo, Jetis, Kab. Ponorogo
3533 - 19 - 09|AFIFA NIKMATUL MA'RIFAH|Malang, 23 Juli 2013|Perempuan|MI SABILUL MUTTAQIN NAMBAK|Harun Nurosit / Lilik Widiya Wati|Nambak, Bungkal, Kab. Ponorogo
3534 - 19 - 09|HUWAIDA AZ-SHAKINA QOTRUNNADA|Ponorogo, 07 Oktober 2013|Perempuan|MI MA'ARIF SABILUL MUTTAQIN NAMBAK BUNGKAL|Muhamad Bharul Ulum / Aning Eka Widiastuti|Nambak, Bungkal, Kab. Ponorogo
3535 - 19 - 09|HUMAYRA ZAHRATUL ALIYAH|Ponorogo, 12 Juni 2012|Perempuan|SMPN 2 BALONG|Sudarmaji / Rodatul Chasanah|Pandak, Balong, Kab. Ponorogo
3536 - 19 - 09|PUTRI AMALIA DWI ASTUTI|Pacitan, 24 April 2012|Perempuan|MTS MA'ARIF BALONG PONOROGO|Muclhlisin / Titin Khasanah|Ngilo-Ilo, Slahung, Kab. Ponorogo
3537 - 19 - 09|KELVY GUS MAULANA|Ponorogo, 06 Februari 2012|Laki-Laki|PONDOK PESANTREN DARUL FIKRI|Miskun / Sulami|Pandak, Balong, Kab. Ponorogo
3538 - 19 - 09|ZASKIA AL THOFUN NISA|Ponorogo, 23 Mei 2012|Perempuan|MI MA'ARIF AL-FAQIH|Trimawan / Erna Rahmawati|Wringinanom, Sambit, Kab. Ponorogo
3539 - 19 - 09|FAJAR APRIAN ALI MUSYAFA|Ponorogo, 06 Juni 2013|Laki-Laki|SDIT AL-MAWADDAH COPER|Supriono / Siti Nurul Solikah|Wringinanom, Sambit, Kab. Ponorogo
3540 - 19 - 09|AKMALOVA AIHAM SYIFA IHROMI|Ponorogo, 10 Juli 2013|Perempuan|MI MA'ARIF SABILUL MUTTAQIN|Mikdar Ihromi / Siti Mariyam|Bekare, Bungkal, Kab. Ponorogo
3541 - 19 - 09|LOVELYNE AYSILLA ZAHRA|Ponorogo, 27 November 2012|Perempuan|SDN BRINGINAN|Warno / Sri Yatmini|Bringinan, Jambon, Kab. Ponorogo
3542 - 19 - 09|NICKO ADITYA YUDA PRATAMA|Ponorogo, 30 April 2013|Laki-Laki|SDN 1 TEGALOMBO|Eko Purnomo / Ninik Irawati|Tegalombo, Kauman, Kab. Ponorogo
3543 - 19 - 09|ARIANDIKA REZA PUTRA PRATAMA|Ponorogo, 04 Januari 2012|Laki-Laki|MTSN 1 PONOROGO|Eko Setiawan / Elis Nur Afita|Mojorejo, Jetis, Kab. Ponorogo
3544 - 19 - 09|AHMAD HAIDAR FARCHI AS-SYA'BANI|Ponorogo, 28 Juni 2012|Laki-Laki|SMP NEGERI 1 JETIS|Imam Maliki / Andriana|Tegalsari, Jetis, Kab. Ponorogo
3545 - 19 - 09|MUHAMMAD DZAKWAN FAHMIYANTO|Ponorogo, 20 November 2011|Laki-Laki|MTSN 1 JETIS|Suyanto / Catur Liana Safitri|Kutu Kulon, Jetis, Kab. Ponorogo
3546 - 19 - 09|CHARELL DEAFA SAPUTRA|Ponorogo, 29 Desember 2011|Laki-Laki|SMP NEGERI 1 JETIS|Aan Khoirul Fauzi / Veti Delia Martiana|Tegalsari, Jetis, Kab. Ponorogo
3547 - 19 - 09|DAFA' RAMADHAN AZHAR|Ponorogo, 30 Juli 2012|Laki-Laki|SDN TEGALSARI|Hartoyo / Asna Arifanti|Tegalsari, Jetis, Kab. Ponorogo
3548 - 19 - 09|DAVID SETYAWAN|Ponorogo, 29 Juli 2012|Laki-Laki|MTS MIFTAHUL ULUM NGRAKET BALONG PONOROGO|Supriyadi / Boyati|Pandak, Balong, Kab. Ponorogo
3549 - 19 - 09|KAILA ASYIFATUR ROHMAH|Ponorogo, 10 November 2011|Perempuan|SMPN 2 BALONG|Jarwoto / Sulistyowati|Pandak, Babadan, Kab. Ponorogo
3550 - 19 - 09|AHMAT RAFA IRFAN PRATAMA|Ponorogo, 08 Maret 2012|Laki-Laki|SMPN 2 BALONG PONOROGO|Wanto / Ika Wahyuni|Pandak, Balong, Kab. Ponorogo
3551 - 19 - 09|ADINDA RISKA SAPUTRI|Ponorogo, 26 November 2013|Perempuan|MI MA'ARIF SABILUL MUTAQQIN|Misnadi / Erti Purirahayu|Ketonggo, Bungkal, Kab. Ponorogo
3552 - 19 - 09|AYUNDA CHINTIYA FIRDA SARI NING TIYAS|Ponorogo, 20 November 2011|Perempuan|SDN 4 BAOSAN LOR|Riyanto / Subinti|Baosan Lor, Ngrayun, Kab. Ponorogo
3553 - 19 - 09|MUHAMMAD RIFA'I AINURSALAM|Ponorogo, 04 Mei 2012|Laki-Laki|SDN 8 BAOSAN LOR|Nurwahid / Seniati|Baosan Lor, Ngrayun, Kab. Ponorogo
3554 - 19 - 09|MUHAMMAD KAFA RENALDI|Ponorogo, 15 Desember 2011|Laki-Laki|MI MA'ARIF MOJOREJO|Mulyono / Kutomah|Mojorejo, Jetis, Kab. Ponorogo
3555 - 19 - 09|MUHAMMAD YUSUP KURNIAWAN|Garut, 08 April 2012|Laki-Laki|MI MA'ARIF MOJOREJO|Muhtadin / Sri Maryati|Mojorejo, Jetis, Kab. Ponorogo
3556 - 19 - 09|FIONA ESTANYDA HADI DESVICCA|Ponorogo, 29 Desember 2012|Perempuan|MI KANZUL HUDA|Hadi Siswanto / Sri Wati|Jebeng, Slahung, Kab. Ponorogo
3557 - 19 - 09|MUHAMMAD IRSYAD NUR FAQIH|Ponorogo, 29 April 2014|Laki-Laki|MI MIFTAHUS SALAM KAMBENG|Sunarto / Siti Umilatin|Jebeng, Slahung, Kab. Ponorogo
3558 - 19 - 09|ALFI NUR DINA|Ponorogo, 30 April 2013|Perempuan|SDN 2 PANDAK BALONG|Sidik Yulianto / Enik Winartin|Pandak, Balong, Kab. Ponorogo
3559 - 19 - 09|RAFQY ADITYA AFFANI|Ponorogo, 08 September 2012|Laki-Laki|MIN 3 PONOROGO|Bambang Pamuji / Nur Lailatul Mukaromah|Pandak, Balong, Kab. Ponorogo
3560 - 19 - 09|DARIS AVANDA WAHYUDA|Ponorogo, 17 Juni 2012|Laki-Laki|MTS DARUL ISTIQOMAH|Sutrisno / Sudarti|Pandak, Balong, Kab. Ponorogo
3561 - 19 - 09|NADIL ULUM HANAFIS|Ponorogo, 30 April 2013|Laki-Laki|SDN 2 PANDAK|Puguh Suparno / Khumaidah|Pandak, Balong, Kab. Ponorogo
3562 - 19 - 09|AS-SYIFA SHOFWATUL LAILY|Ponorogo, 02 Desember 2011|Perempuan|MTS DARUL ISTIQOMAH|Marwan / Dahliar|Ngasinan, Jetis, Kab. Ponorogo
3563 - 19 - 09|YUSUF|Ponorogo, 27 Desember 2011|Laki-Laki|SDN 1 BAOSAN KIDUL|Sali / Sarmini|Baosan Kidul, Ngrayun, Kab. Ponorogo
3564 - 19 - 09|ARGA ENJANG WAHDANA|Ponorogo, 20 Februari 2012|Laki-Laki|SDN 1 BAOSAN KIDUL|Deni Eko Santoso / Atik Diani|Baosan Kidul, Ngrayun, Kab. Ponorogo
3565 - 19 - 09|CINDY AULIA IZAHTI|Ponorogo, 08 September 2012|Perempuan|SDN 1 BAOSAN KIDUL|Slamet / Wahyu Jarwati|Baosan Kidul, Ngrayun, Kab. Ponorogo
3566 - 19 - 09|YUSUF RAHMAD RIFAI|Ponorogo, 02 November 2012|Laki-Laki|SDN 4 MRAYAN|Sumarno / Riyani|Mrayan, Ngrayun, Kab. Ponorogo
3567 - 19 - 09|SALSABELA MELIYATUL CHASANAH|Ponorogo, 08 Januari 2013|Perempuan|MI DARUL ISTIQOMAH NGUMPUL BALONG|Bangkit Syafrudin Athhari / Wahdiyatul Bariyah|Mojomati, Jetis, Kab. Ponorogo
3568 - 19 - 09|ABDUL MALIK IKHSAN|Bungo, 20 Februari 2014|Laki-Laki|SDN TURI JETIS|Suhaimi / Ririn Widiastuti|Bedaro, Muko-muko Batin VII, Kab. Bungo
3569 - 19 - 09|IZZA NUR QOYYUM|Ponorogo, 14 Mei 2014|Laki-Laki|SDN TEGALSARI|Teguh Widadi / Nur Aini|Tegalsari, Jetis, Kab. Ponorogo
3570 - 19 - 09|MUHAMMAD HANIF ANDIKA|Ponorogo, 19 Maret 2012|Laki-Laki|SMPN 1 JETIS|Sunoto / Uswatun Chasanah|Tegalsari, Jetis, Ponorogo
3571 - 19 - 09|AHMAD HAIDAR FARCHI AS-SYA'BANI|Ponorogo, 28 Juni 2012|Laki-Laki|SMPN 1 JETIS|Imam Malik / Andriana|Tegalsari, Jetis, Ponorogo
3572 - 19 - 09|DAFA' RAMADHAN AZHAR|Ponorogo, 30 Juli 2012|Laki-Laki|SMPN 1 JETIS|Hartono / Asna Arifanti|Tegalsari, Jetis, Ponorogo
3573 - 19 - 09|ROID DZAKIYYUN NASHIF AL-FAWAIZ|Ponorogo, 16 Oktober 2011|Laki-Laki|MTS AL-ISLAM JORESAN|Agus Susilo / Surati|Karanggebang, Jetis, Ponorogo
3574 - 19 - 09|MOHAMMAD HASAN RIFAI|Ponorogo, 09 Maret 1999|Laki-Laki|S-1 UIN PONOROGO|Slamet / Anik Murosidah|Tegalsari, Jetis, Ponorogo
3575 - 19 - 09|GALANG AULIA HANDOYO|Ponorogo, 25 Februari 2011|Laki-Laki|SMAN 3 PONOROGO|Yudi Handoyo / Tri Ratmini|Singkil, Balong, Ponorogo
3576 - 19 - 09|ANI NADEVA|Ponorogo, 08 Agustus 2008|Perempuan|MA NGRAYUN|Temon / Ngrayun, Ponorogo|Ngrayun, Ponorogo
3577 - 19 - 09|LUCKY AHMAD SYAIFULLOH|Ponorogo, 06 Februari 2012|Laki-Laki|MTs NGRAYUN|Sendang / Ngrayun, Ponorogo|Ngrayun, Ponorogo
3578 - 19 - 09|FAREL MAULANA|Ponorogo, 26 Mei 2013|Laki-Laki|SDN NGRAYUN|Sambi / Ngrayun, Ponorogo|Ngrayun, Ponorogo
3579 - 19 - 09|SHILVIYA DWI RATNASARI|Ponorogo, 13 Oktober 2011|Perempuan|SDN NGRAYUN|Sambi / Ngrayun, Ponorogo|Ngrayun, Ponorogo
3580 - 19 - 09|RIKA ANDINI SETIA NINGSIH|Ponorogo, 03 Juli 2009|Perempuan|MA NGRAYUN|Sambi / Ngrayun, Ponorogo|Ngrayun, Ponorogo
3581 - 19 - 09|MAULANA IBRAHIM|Oku Timur, 23 Januari 2011|Laki-Laki|SMP FATHUL MUNA|Palembang Sumatera Selatan|Oku Timur
3582 - 19 - 09|ALFIN TSALIS DELFARINDA|Ponorogo, 17 Agustus 2011|Perempuan|MI MAARIF AL FAQIH|Wringinanom, Sambit, Ponorogo|Sambit, Ponorogo
