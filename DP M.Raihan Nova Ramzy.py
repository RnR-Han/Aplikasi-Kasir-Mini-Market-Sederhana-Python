def menu():
    global jb,kb,bb
    print("Jenis Ke - ",i+1)
    jb = input("Masukan Jenis Barang :")
    jenis_barang.append(jb)
    kb = input("Kode Barang :")
    kode_barang.append(kb)
    bb = int(input("Banyak Barang :"))
    banyak_barang.append(bb)
    print(500*"-")
def kode():
    global ck
    ck = input("Tampil Kode Barang:")
    cek_kode.append(ck)
def halamenu():
    global sk
    sk = input("\t\t\tSilakan Input Tujuan anda :")
    tujuan.append(sk)
tujuan=[]
#code waktu
import datetime
saat_ini = datetime.datetime.now()
#append
jenis_barang=[]
kode_barang=[]
banyak_barang=[]
cek_kode=[]

def contact():
    print(6*"\t",10*"-","=* Kelompok 6 *=",10*"-","\n",
          "\t\t\t1.M.Raihan Nova Ramzy\n"
          "\t\t\t2.Dimas Prasetyo\n"
          "\t\t\t3.M.Ilham Almagribi\n"
          "\t\t\t4.Ridho Irawan\n"
          "\t\t\t6.Michael Stanley H Gultom\n")
    print(6*"\t","Call : 0812 1067 2585(Tlpn/Wa) \n",6*'\t',"email : juniormart@gmail.com")
    print("Saran Dan Masukan pendapat bisa dikirim melalui contack diatas, Sekian Dan terimakasih")
def help():
    print(5*"\t","Langkah-Langkah Mengunakan Aplikasi kasir\n"
          "1.Pertama-tama anda diarahkan ke halaman login,anda harus Memasukan Username Yang sudah di cantumkan oleh program,\n"
          "2.pastikan username anda benar jika salah anda akan keluar,\n"
          "3.setalah memasukan username anda harus memasukan password yang sudah dicantumkan oleh program,\n"
          '4.anda mendapat 3 kesempatan untuk memasukan password jika anda salah lebih dari itu anda akan terblokir dan harus mengulanggi dari langka pertama,\n'
          '5.setelah password sudah berhasil berarti anda sudah melawati tahap login,\n'
          '6.langka berikutnya pilihan menu pilih angka 1 untuk menuju ke aplikasi kasir,\n'
          '7.setalah itu anda dapat mengunakan aplikasi kasir berikut langkah-langkah menjalankannya,\n'
          '8.pertama anda akan diarahkan untuk melihat kode barang yang sudah dicantumkan oleh program contoh palanggan anda membeli makanan pastikan,\n'
            'mencetak urutan kode supaya anda tahu kode makanan tersebut, dengan cara menggetik angka 2 pada menu "tampilkan Kode"lanjut,\n'
          '9. Setelah itu Perhatikan Lagi Apakah Pembelanjaan pelanggan anda di jenis yang lain jika ada tampilkan menu untuk barang tersebut,Contoh sayuran ketik perintah 1 pada "tampilkan Kode",\n'
          '10.jika tidak atau mengakhiri Tampilan Kode anda harus mengetik angka "0" yang artinya mengakhiri dari perintah Tampilan Kode dan melanjuti tahap Pemesanan,\n'
          '11.setelah Tahap Tampilan Kode Selesai anda harus menjalani tahap pemesanan,\n'
          '12. dilangkah ini anda harus menghitung jumlah barang yang dibeli dari pelanggan di semua jenis barang contoh Banyak Varian Barang : 2 artinya anda memcantumkan 2 barang yang di beli pelanggan,\n'
          '13.setelah itu anda harus memasukan/menginput barang tersebut satu persatu pastikan anda sudah mengetahui kode barang tersebut dari tampilan kode yang anda perintahkan,\n'
           'Contoh : Barang Sayuran Anda Harus Memasukan angka pada Perintah "Jenis Barang"dengan Angka 1 lalu masukan kode barang tersebut misalkan cabai Merah Masukan Kode Barang:6,\n'
          'lalu banyak barang ? pada tampilan kode barang cabai merah di hitung secara (ons) misalkan pelanggan ingin membeli 1/2kg maka Anda harus mencantumkan 5 pada penginputan Banyak barang,\n'
          '14.setelah itu tahap pemesanan yang ke dua sama seperti tahap pemesanan pertama pastikan sudah Tampilan Kode sudah di Jalan kan Pada jenis Barang yang di pesan oleh pelanggan,\n'
          '15.selesai tahap pemesanan langsung ketahap pembayaran dangan membayar uang yang sudah di hitung oelh perogram dan tampilan struk yang sudah terlihat,\n'
          '16.pastikan masukan uang sesuai dengan perhitungan program atau lebih JIKA UANG KURANG MAKA PROGRAM AKAN MENAMPILKAN UANG ANDA KURANG DAN MENGAKHIRINYA,\n'
          '17.setelah itu program akan menghitung kembali uang anda dan rincian hemat anda,\n'
          '18.lalu program menkonfirmasikan lagi apakah anda ingin berbelanja lagi jika iya ketik y/Y jika tidak ketik T/t,\n'
          '19.jika anda ketik y maka program akan menjalankan nya lagi DENGAN KETERANGAN PAJAK DAN HEMAT HANYA DI HITUNG SEKALI dan uang dihitung bersama dengan pesanan yang pertama,\n'
          '20.setelah selesai maka program menampilkan nama admin pada pemasukan di username dan program selesai. ')


#Halaman Login
print(7*"\t","Selamat Datang dihalaman Login \n",8*"\t","Junior Mart\n")
nm = input("\t\t\t\t\t\t\tUsername :")
if nm=='raihan'or nm=='dimas'or nm=='ilham':
    print()
elif nm=='ridho'or nm=='michael':
    print()
else:
    print("Username Salah")
    exit()
salah = True
i = 0
while salah:
    jawaban = input("\t\t\t\t\t\t\tPassword : ")

    if jawaban == "juniormart"or jawaban=="jmart":
        salah = False
        break
    else:
        i+=1
        print("Password Anda Salah Jika 3 kali salah maka anda terblokir, Anda Sudah Mencoba Sebanyak : "+str(i))
        if i==3:
            print('Maaf anda terblokir silakan coba lagi nanti')
            exit()

print("\t\t\t\t\t\t\tLogin sucsesfull")
print(1000*"-")

#pembukaan
print(6 * "\t", 10 * "-", "=* halaman menu *=", 10 * "-", "\n")
print(8 * "\t", "1.Aplikasi Kasir\n",
      8 * "\t", "2.Bantuan\n",
      8 * "\t", "3.Contact\n",
      8 * "\t", "4.Check Code Item\n",
      8 * "\t", "5.Exit\n")
for i in range(5):
    halamenu()
    if tujuan[i] == 1 or tujuan[i] == '1':
        print()
        break
    elif tujuan[i] == 2 or tujuan[i] == '2':
        help()

    elif tujuan[i] == 3 or tujuan[i] == '3':
        contact()

    elif tujuan[i] == 4 or tujuan[i] == '4':
        print("Jenis Barang :\n0.balik ke halaman menu 1.sayuran & Umbi-umbian(1/62) 2.Makanan(1/107) 3.Minuman(1/53) 4.Peralatan mandi(1/24) 5.Kosmetik(1/27)\n "
            "6.Kebersihan(1/28) 7.Keperluan dapur(1/30) 8.Buah-buahan(1/25) 9.Daging,ayam,sosis,ikan(1/28) 10.Obat-Obatan(1/35) 11.Lainnya")
        for i in range(11):
            kode()
            if cek_kode[i] == '0':
                cek=''
                break
            elif cek_kode[i] == '1':
                cek='\t\t\t\t Nomor Kode barang Sayuran\t\t\t (ons)kilogram/(pck)ikat/(pct)satuan\nPart 1\n' \
            '[1].Bawang Merah(ons)  [6].Cabai Rawit Merah(ons) [11].Sousin(pck)   [16].Labu Siam(pct)   [21].Kacang Panjang(pck) [26].Singkong(ons)      [31].Jeruk lemon(pct)  [36].Selada Keriting(ons) [41].Paprika Merah(pct)\n'\
            '[2].Bawang Putih(ons)  [7].Bayam(pck)             [12].Touge(ons)    [17].Pare(pct)        [22].Petai(pck)          [27].Kentang(ons)       [32].Sawi Hijau(ons)   [37].Selada Air(ons)      [42].Paprika Hijau(pct)\n'\
            '[3].Bawang Bombay(ons) [8].Bayam Merah(pck)       [13].Brocolli(ons) [18].Jagung(pct)      [23].Jengkol(ons)        [28].Kentang Somai(ons) [33].Jeruk Limo(ons)   [38].Sawi Putih(ons)      [43].Paprika Kuning(pct)\n'\
            '[4].Cabai Merah(ons)   [9].Kangkung(pck)          [14].Wortel(ons)   [19].Jagung Acar(pct) [24].Ubi(ons)            [29].Poccoi(pck)        [34].Timun(ons)        [39].Daun Bawang(ons)     [44].Jeruk Nipis(ons)\n'\
            '[5].Cabai Rawit(ons)   [10].Kangkung Merah(pck)   [15].Labu(pct)     [20].Tomat(ons)       [25].Ubi Merah(ons)      [30].Buncis(pck)        [35].Timun Jepang(Ons) [40].Terong Ungu(ons)     [45].Kol(ons)\nPart 2\n'\
            '[46].Seledri(pck)     [49].Jamur Merang(pct) [52].Labu Parang(pct)   [55].Jahe(ons)       [58].Kunyit(ons)      [61].Daun Jeruk(pck)\n'  \
            '[47].Kembang kol(ons) [50].Kemiri(ons)       [53].Daun Singkong(pck) [56].Jahe Merah(ons) [59].Nangka Muda(ons) [62].Daun Salam(pck\n' \
            '[48].Lobak(ons)       [51].Daun Katuk(pck)   [54].Daun Pandan(pck)   [57].Kencur(ons)     [60].Sereh(pck)'
            elif cek_kode[i] == '2':
                cek='\t\t\t\t Nomor Kode Barang Makanan\n' \
            '[1].frozz permen mint org 15gr         [21].TAO KAE NOI CRISPY 4GR             [41].MIE SEDAP GERENG CUP SERIES 85GR  [61].BATTER VANILA BOX               [81].TANGO WAFER POUCH 115GR SERIES        [101].DISNEY LOCO WHOLEMEAL\n'\
            '[2].FROZZ PERMEN CHERRY 15GR           [22].LAYS 55g                           [42].MIE SEDAP KUAH CUP SERIES 77GR    [62].REGAL MARIE 230GR SERIES        [82].KHONG GUAN WAFER 160GR                [102].DISNEY MILK LOF\n' \
            '[3].FISHERMANS FREIND HONEY LEMON 25GR [23].KUSUKA SNACK JAGUNG 180GR          [43].POPMIE KUAH SERIES 75GR           [63].REGAL MARIE TIN 550GR SERIES    [83].KHONG GUAN CLASIC 280GR               [103].DISNEY BIG SUGAR LOFT\n' \
            '[4].Mentos Pure Papermint 35GR         [24].DUA KELINCI GARNIC NUT 200GR       [44].POPMIE GORENG SERIES 75GR         [64].REGAL MARIE 1000GR              [84].KHONG GUAN MINI TIN 650GR             [104].DISNEY FAMILY WHITE BREAD\n' \
            '[5].MINT FRUIT CHERRYMINT 115GR        [25].DUA KELINCI 75GR                   [45].LAFONTE 450GR                     [65].HELLO PANDA 45GR                [85].KHONG GUAN SEGI TIN 1600GR            [105].KAYA PILLOW BREAD\n' \
            '[6].MINT FRUIT GRAPEMINT 115GR         [26].REBO KUACI MATAHARI 70GR           [46].BAKMI MEWAH 110GR                 [66].FITBAR COKLAT 25GR              [86].SELAMAT WAFER 60GR SERIES             [106].MEXICO PILLOW BREAD\n' \
            '[7].RELAXA PERMEN BARLEY MINT 125GR    [27].CHEETOS TWIST 75GR                 [47].SARIMI ISI 2 GORENG SERIES 125GR  [67].MONDE GENJI PIE 70GR            [87].SELAMAT WAFER 198GR SERIES            [107].BURGER BUN\n' \
            '[8].MENTOS FRUIT BAG 121,5GR           [28].CHITATO 85GR                       [48].SARIMI ISI 2 KUAH SERIES 115GR    [68].MONDE RAISIN PIE 85GR           [88].SELAMAT WAFER TIN 440GR SERIES\n' \
            '[9].MINT MOJIZ DUO MINT 112,5GR        [29].GARUDA KACANG KULIT 200GR          [49].ABC MIE GORENG SERIES 70GR        [69].MONDE SARENA ROLL BICKUIT 60GR  [89].NISSIN WAFER 110GR SERIES\n' \
            '[10].KISS APPLE PEACH 125GR            [30].PINGLES POT SNACK 107GR            [50].ABC MIE KUAH SERIES 65GR          [70].OREO 95GR SERIES                [90].NISSIN WAFER COKLAT MINI TIN 200GR SERIES\n' \
            '[11].KISS CHERRY MINT 125GR            [31].INDOMIE GORENG SERIES 75GR         [51].SILVER QUEEN MINI 30GR SERIES     [71].OREO SANDWICT 133GR SERIES      [91].NISSIN WAFER COKLAT TIN 570GR SERIES\n' \
            '[12].YUPI STROWBERRY KISS 110GR        [32].INDOMIE JUMBO GORENG SERIES 125GR  [52].SILVER QUEEN BITES ALMOND 40GR    [72].OREO MINI 67GR SERIES           [92].ROMA WAFER CAN 336GR SERIES\n' \
            '[13].YUPI FUN GUM 120GR                [33].INDOMIE KUAH SERIES 75GR           [53].SILVER QUEEN 68GR SERIES          [73].ROMA MALKIST TRAMISU 120GR      [93].SARI ROTI SANDWICH SERIES\n' \
            '[14].CHUPA CHUPS ASSORTED CANDY        [34].INDOMIE KARI SERIES 72GR           [54].SILVER QUEEN CHUNKY BAR 100GR     [74].ROMA MALKIST ABON 240GR         [94].SARI ROTI ISI SERIES\n' \
            '[15].SUGUS STIK STR 30GR               [35].INDOMIE GORENG KTN SERIES          [55].DAILY MILK 30GR                   [75].ROMA MARIE 115GR                [95].SARI ROTI TAWAR GANDUM\n' \
            '[16].SUGUS STIK BLACK CURRANT 30GR     [36].INDOMIE KUAH KTN SERIES            [56].DAILY MILK 65GR                   [76].ROMA FESTIVE 765GR              [96].SARI ROTI TAWAR\n' \
            '[17].BIG BABOL STR STICK 24GR          [37].INDOMIE KARI KTN SERIES            [57].KINDER JOY 20GR                   [77].SLAI OLAI 240GR SERIES          [97].SARI ROTI TAWAR KUPAS\n' \
            '[18].DORITOS TORTILLA 160GR            [38].SEDAP MIE KARI SERIES 72GR         [58].DELFI COKLAT 55GR                 [78].TANGO WAFER 78GR SERIES         [98].SARI ROTI KRIM\n' \
            '[19].OISHI SPOGE CRUNCH 120GR          [39].SEDAP MIE KUAH SERIES 75GR         [59].DELFI COKLAT 155GR                [79].TANGO WAFER 145GR SERIES        [99].SARI ROTI SOBEK 2 RASA\n' \
            '[20].PILUS GARUDA 95GR                 [40].SEDAP MIE GORENG SERIES 75GR       [60].BENG-BENG MAX                     [80].TANGO WAFER 176GR SERIES        [100].DISNEY TAWAR KUPAS\n' \
            '\nuntuk Makanan uratan:permen(1/15)-chiki(16/30)-mieinstan(31/50)-coklat(51/60)biskuit(61/77)-wafer(78/92)-roti(93/107)'
            elif cek_kode[i]=='3':
                cek = '\t\t\t\t Nomor Kode Barang Minuman\n'\
            '[1].sprite botol 250ml     [10].TEBS             [19].le mineral galon 15lt [28].nescafe 450ml    [37].bear bland             [46].sgm 1/3 1000gr\n' \
            '[2].sprite botol 500ml     [11].big cola 500ml   [20].prima 500ml           [29].kopiko 78 500ml  [38].hilo 550ml             [47].sgm 3/6 1000gr\n' \
            '[3].sprite botol 1lt       [12].big cola 1lt     [21].prima 1500ml          [30].yogurt drink     [39].frisian flag klg 230ml [48].sgm soya 1000gr\n' \
            '[4].coca cola botol 250ml  [13].big cola 2lt     [22].cleo 300ml            [31].yakult 1 pack    [40].milo 500ml             [49].dancow 0/1 900gr\n' \
            '[5].coca cola botol 500ml  [14].aqua 500ml       [23].cleo 500ml            [32].pulpy 550ml      [41].fresh milk 1lt         [50].dancow 1/3 900gr\n' \
            '[6].coca cola botol 1lt    [15].aqua 1500ml      [24].crystaline 500ml      [33].floridina 350ml  [42].bebelac 0/1 800gr      [51].dancow 3/6 900gr\n' \
            '[7].Fanta botol 250ml      [16].aqua 19lt        [25].ades 500ml            [34].indomilk 250ml   [43].bebelac 1/3 800gr      [52].frisian flag 123 1000gr\n' \
            '[8].Fanta botol 500ml      [17].le mineral 500ml [26].vit 500ml             [35].indomilk 550ml   [44].bebelac 3/6 800gr      [53].frisian flag 456 1000gr\n' \
            '[9].Fanta botol 1lt        [18].le mineral1500ml [27].naraya 500ml          [36].indomilk 1lt     [45].sgm 0/1 1000gr\n' \
            'untuk minuman urutan : soda(1/13),air mineral(14/26),kopi(27/29),yogurt(30/31),jeruk(32/33),susu(34/53)'
            elif cek_kode[i]=='4':
                cek = '\t\t\t\t Kode Barang Peralatan Mandi Mandi\n' \
            '[1].sabun batang lifebouy            [5].sahmpoo sunsilk hijab 340ml           [9].pepsodent 75 gr    [13].onda hand shower so  250   [17].sikat cuci pring stainles [21].ember besar\n' \
            '[2].zwitsal baby baath natural       [6].head & shoulder anti hair fall shampoo[10].bak mandi anak    [14].selang air stainless       [18].sikat cuci baju           [22].ember jumbo\n' \
            '[3].shampoo lifebouy 170ml           [7].pepsodent sensitive expert enamel     [11].handuk jumbo      [15].onda keran air A 812 cis   [19].bak mandi                 [23].sabun cuci\n' \
            '[4].sahmpoo sunsilk soft&smoot 170ml [8].sendsodyen original 100gr             [12].lion star gayung  [16].sikat gigi 1pcs            [20].ember kecil               [24].gantungan baju dan handuk\n' \
            'untuk alat mandi(1/24)urutan: SSP(1/9),alat mandi(10/24)'
            elif cek_kode[i]=='5':
                cek = '\t\t\t\t Kode Barang Kosmetik\n' \
              '[1].Acnes                [5].Viva Skin Food Cream [9].Clear     [13].Revlon  [17].Rejoice    [21].Dove       [25].Vaseline UV\n' \
              '[2].Ponds                [6].Garnier              [10].Lifebuoy [14].Nature  [18].Zinc       [22].Purbasari  [26].Sari Ayu\n' \
              '[3].Wardah Lips          [7].Romano               [11].Elips    [15].Emeron  [19].Pantene    [23].Citra      [27].Fairy N Pink\n' \
              '[4].Olay Regenerist Night[8].Headshoulder         [12].Loreal   [16].Sunsilk [20].Nuvo       [24].Nivea\n' \
              'untuk kosmetik (1/27)'
            elif cek_kode[i]=='6':
                cek = '\t\t\t\t Kode Barang Kebersihan\n' \
              '[1].Beyclin              [5].Procline White Crystal  [9].Reckitt Benckiser      [13].Downi Deterjen  [17].Boom Wing     [21].Mr Muscle Axi Triguna   [25].Vixal\n' \
              '[2].So Klin Pemutih      [6].NEOhaus White Up        [10].Rinso Molto Deterjen  [14].Molto Deterjen  [18].S.O.S         [22].Wipol Ultra Protection  [26].Harpic\n' \
              '[3].Vanish               [7].Seven G C Free Bleach   [11].So Klin Deterjen      [15].Daia Deterjen   [19].SuperPell     [23].Dettol Pembersih Lantai [27].WPC\n' \
              '[4].Clorox Bleach Pen Gel[8].Tide Plus Bleach A L L  [12].Jaz1 Deterjen         [16].Attack Easy     [20].So Klin Lantai[24].Porstex                 [28].Wipol Cair\n' \
              'untuk kebersihan: pemutih (1/9), deterjen (10/17),Pembersih Lantai (18/23),Pembersih WC (24/28)'
            elif cek_kode[i]=='7':
                cek = '\t\t\t\t Kode Barang Keperluan Dapur\n' \
              '[1].teplon maxim     [6].sendok 1 set [11].isi gas elpiji 5 kg     [16].bango kecap manis 550ml     [21].ABC sarden besar 425gr      [26].fortune 2lt.\n' \
              '[2].wajan            [7].gelas 6 pcs  [12].kompor miyako           [17].ABC sambal terasi 180 g     [22].tepung terigu kunci biru 1kg[27].sania 2lt.\n' \
              '[3].lion star talenan[8].piring 1 pcs [13].sasa santan bubuk 500gr [18].ladaku merica bubuk 100gr   [23].desaku ketumbar bubuk 1rcg  [28].filma 2lt minyak jagung.\n' \
              '[4].rak piring       [9].baskom 1pcs  [14].sasa penyedap 1kg       [19].saori saos teriyaki 10sachet[24].royko 1kg                   [29].bimoli 1lt.\n' \
              '[5].pengocok telur   [10].cobek       [15].sasa tepung bumbu 850 gr[20].saus ABC botol 335ml        [25].bimoli 2lt                  [30].tropikal 1lt.\n' \
              'untuk keperluan dapur (1/30)urutan:alatmasak(1/12),bumbudapur(13/24),minyak(25/30)'
            elif cek_kode[i]=='8':
                cek = '\t\t\t\t Kode Barang Buah-buahan\n' \
              '[1].pir madu    [6].duku      [11].buah naga[16].alpukat   [21].nangka\n' \
              '[2].anggur merah[7].rambutan  [12].ceri     [17].bengkuang [22].durian\n' \
              '[3].nanas       [8].lemon     [13].kurma    [18].kelengkeng[23].pepaya\n' \
              '[4].apel        [9].jeruk     [14].melon    [19].mangga    [24].salak\n' \
              '[5].semangka    [10].blueberry[15].jambu air[20].manggis   [25].stowberry\n' \
              'untuk Buah-buahan (kg)'
            elif cek_kode[i]=='9':
                cek = '\t\t\t\t Kode Barang Daging,ayam,dan ikan\n' \
              '[1].Ayam Parting Frozen 1 kg   [6].Fiesta Paha Bawah 1 kg          [11].Fiesta Happy Star 500 g       [16].Champ Nugget ABC 500 g       [21].Champ Sosis 150 g               [26].Ikan Tuna  500 gr\n' \
              '[2].Fiesta Ayam Flt Dd TTK 1 kg[7].Fiesta Chicken Nugget 500 g     [12].Fiesta Nugget Cheese 123 500 g[17].Fiesta Sausage 300 g         [22].Daging Sapi Beku Import Aus 1 kg[27].Ikan Salmon 1 kg\n' \
              '[3].Fiesta Ayam Flt Dd TTK 1 kg[8].Fiesta Stikie 500 g             [13].Champ Nugget 500 g            [18].Fiesta  Sosis Bratwurst 300 g[23].Daging Sapi Paha 1 kg           [28].Ikan Tenggiri Giling 1 kg\n' \
              '[4].Fiesta Paha Utuh 1 kg      [9].Fiesta Golden Chicken Ring 500 g[14].Champ Nugget Coin 500 g       [19].Fiesta Sosis Keju 300 g      [24].Ikan Dori 1 kg\n' \
              '[5].Fiesta Paha Atas 1 kg      [10].Fiesta Nugget Zoo 500 g        [15].Champ Nugget Stick 500 g      [20].Champ Sosis 375 g            [25].Ikan Tenggiri Jumbo 500 gr\n' \
              'untuk Daging,Ayam,dan Ikan(1/28):dagingayam(1/6),nuggetayam(7/16),sosisayam(17/21),dagingsapi(22/23)dagingikan(24/28)'
            elif cek_kode[i]=='10':
                cek = '\t\t\t\t Kode Barang Obat-Obatan\npart1\n' \
              '[1].Siladex Batuk Pilek 30ml        [6].OBH Combi Anak Rasa Jeruk 60ml[11].Anakonidin OBH 60ml         [16].Vicks Formula 44 Anak 54ml.\n' \
              '[2].Siladex Batuk Pilek 60ml        [7].OBH Combi Anak Rasa Madu 60ml [12].SanaFlu Plus Batuk Tablet   [17].Bodrex Flu & Batuk Berdahak PE Tablet.\n' \
              '[3].Triaminic Batuk Syr 60ml        [8].AnaKonidin 30ml               [13].Bodrex Flu & Batuk PE Tablet[18].Benadryl Batuk Berdahak Syr 50ml.\n' \
              '[4].OBH Combi Dewasa Rasa Jahe 100ml[9].AnaKonidin 60ml               [14].Bodrexin Flu & B PE S 56ml  [19].OBH Combi Batuk Berdahak Rasa M 100ml.\n' \
              '[5].OBH Combi Dewasa Rasa Madu 100ml[10].Anakonidin OBH 30ml          [15].Mixagrip Flu & Batuk Tablet [20].Bodrexin Flu & Batuk Berdahak PES56ml.\npart2\n' \
              '[21].Bodrexin Demam 60ml            [26].Ultraflu 4 Strip             [31].Paramex Tab 4 Strip' \
              '[22].Siantan Demam Berdarah Tablet  [27].Panadol Syrup 60ml           [32].Sanmol Drop 15ml' \
              '[23].Sari Kurma Sahara              [28].Panadol Biru Tablet 10 tab   [33].Rohto Fever Patch 2S' \
              '[24].Pimtrakol kids D & B Str       [29].Panadol Cold Flu Hju T10 tab [34].Panadol Anak Tab' \
              '[25].Procold Flu 6 Strip            [30].Panadol Extra Merah 10 tab   [35].Decolgen tab 4 str' \
              'untuk Obat-obatan (1/35):Fludanbatuk(1/20),demam(21/35)'
            else:
                halamenu()

            print(cek)
    elif tujuan[i] == 5 or tujuan[i] =='5':
        exit()
    else:
        print('anda salah input')
#aplikasi Kasir
print("\t\t\t\t\t\t\tSelamat Datang \n\t\t\t\t\t\tDi Aplikasi Kasir Junior Mart")
print("Jenis Barang :\n0.Tanpa kode 1.sayuran & Umbi-umbian(1/62) 2.Makanan(1/107) 3.Minuman(1/53) 4.Peralatan mandi(1/24) 5.Kosmetik(1/27)\n "
       "6.Kebersihan(1/28) 7.Keperluan dapur(1/30) 8.Buah-buahan(1/25) 9.Daging,ayam,sosis,ikan(1/28) 10.Obat-Obatan(1/35) 11.Lainnya")
#detail code
for i in range(11):
    kode()
    if cek_kode[i] == '0':
        cek=''
        break
    elif cek_kode[i] == '1':
        cek='\t\t\t\t Nomor Kode barang Sayuran\t\t\t (ons)kilogram/(pck)ikat/(pct)satuan\nPart 1\n' \
            '[1].Bawang Merah(ons)  [6].Cabai Rawit Merah(ons) [11].Sousin(pck)   [16].Labu Siam(pct)   [21].Kacang Panjang(pck) [26].Singkong(ons)      [31].Jeruk lemon(pct)  [36].Selada Keriting(ons) [41].Paprika Merah(pct)\n'\
            '[2].Bawang Putih(ons)  [7].Bayam(pck)             [12].Touge(ons)    [17].Pare(pct)        [22].Petai(pck)          [27].Kentang(ons)       [32].Sawi Hijau(ons)   [37].Selada Air(ons)      [42].Paprika Hijau(pct)\n'\
            '[3].Bawang Bombay(ons) [8].Bayam Merah(pck)       [13].Brocolli(ons) [18].Jagung(pct)      [23].Jengkol(ons)        [28].Kentang Somai(ons) [33].Jeruk Limo(ons)   [38].Sawi Putih(ons)      [43].Paprika Kuning(pct)\n'\
            '[4].Cabai Merah(ons)   [9].Kangkung(pck)          [14].Wortel(ons)   [19].Jagung Acar(pct) [24].Ubi(ons)            [29].Poccoi(pck)        [34].Timun(ons)        [39].Daun Bawang(ons)     [44].Jeruk Nipis(ons)\n'\
            '[5].Cabai Rawit(ons)   [10].Kangkung Merah(pck)   [15].Labu(pct)     [20].Tomat(ons)       [25].Ubi Merah(ons)      [30].Buncis(pck)        [35].Timun Jepang(Ons) [40].Terong Ungu(ons)     [45].Kol(ons)\nPart 2\n'\
            '[46].Seledri(pck)     [49].Jamur Merang(pct) [52].Labu Parang(pct)   [55].Jahe(ons)       [58].Kunyit(ons)      [61].Daun Jeruk(pck)\n'  \
            '[47].Kembang kol(ons) [50].Kemiri(ons)       [53].Daun Singkong(pck) [56].Jahe Merah(ons) [59].Nangka Muda(ons) [62].Daun Salam(pck\n' \
            '[48].Lobak(ons)       [51].Daun Katuk(pck)   [54].Daun Pandan(pck)   [57].Kencur(ons)     [60].Sereh(pck)'
    elif cek_kode[i] == '2':
        cek='\t\t\t\t Nomor Kode Barang Makanan\n' \
            '[1].frozz permen mint org 15gr         [21].TAO KAE NOI CRISPY 4GR             [41].MIE SEDAP GERENG CUP SERIES 85GR  [61].BATTER VANILA BOX               [81].TANGO WAFER POUCH 115GR SERIES        [101].DISNEY LOCO WHOLEMEAL\n'\
            '[2].FROZZ PERMEN CHERRY 15GR           [22].LAYS 55g                           [42].MIE SEDAP KUAH CUP SERIES 77GR    [62].REGAL MARIE 230GR SERIES        [82].KHONG GUAN WAFER 160GR                [102].DISNEY MILK LOF\n' \
            '[3].FISHERMANS FREIND HONEY LEMON 25GR [23].KUSUKA SNACK JAGUNG 180GR          [43].POPMIE KUAH SERIES 75GR           [63].REGAL MARIE TIN 550GR SERIES    [83].KHONG GUAN CLASIC 280GR               [103].DISNEY BIG SUGAR LOFT\n' \
            '[4].Mentos Pure Papermint 35GR         [24].DUA KELINCI GARNIC NUT 200GR       [44].POPMIE GORENG SERIES 75GR         [64].REGAL MARIE 1000GR              [84].KHONG GUAN MINI TIN 650GR             [104].DISNEY FAMILY WHITE BREAD\n' \
            '[5].MINT FRUIT CHERRYMINT 115GR        [25].DUA KELINCI 75GR                   [45].LAFONTE 450GR                     [65].HELLO PANDA 45GR                [85].KHONG GUAN SEGI TIN 1600GR            [105].KAYA PILLOW BREAD\n' \
            '[6].MINT FRUIT GRAPEMINT 115GR         [26].REBO KUACI MATAHARI 70GR           [46].BAKMI MEWAH 110GR                 [66].FITBAR COKLAT 25GR              [86].SELAMAT WAFER 60GR SERIES             [106].MEXICO PILLOW BREAD\n' \
            '[7].RELAXA PERMEN BARLEY MINT 125GR    [27].CHEETOS TWIST 75GR                 [47].SARIMI ISI 2 GORENG SERIES 125GR  [67].MONDE GENJI PIE 70GR            [87].SELAMAT WAFER 198GR SERIES            [107].BURGER BUN\n' \
            '[8].MENTOS FRUIT BAG 121,5GR           [28].CHITATO 85GR                       [48].SARIMI ISI 2 KUAH SERIES 115GR    [68].MONDE RAISIN PIE 85GR           [88].SELAMAT WAFER TIN 440GR SERIES\n' \
            '[9].MINT MOJIZ DUO MINT 112,5GR        [29].GARUDA KACANG KULIT 200GR          [49].ABC MIE GORENG SERIES 70GR        [69].MONDE SARENA ROLL BICKUIT 60GR  [89].NISSIN WAFER 110GR SERIES\n' \
            '[10].KISS APPLE PEACH 125GR            [30].PINGLES POT SNACK 107GR            [50].ABC MIE KUAH SERIES 65GR          [70].OREO 95GR SERIES                [90].NISSIN WAFER COKLAT MINI TIN 200GR SERIES\n' \
            '[11].KISS CHERRY MINT 125GR            [31].INDOMIE GORENG SERIES 75GR         [51].SILVER QUEEN MINI 30GR SERIES     [71].OREO SANDWICT 133GR SERIES      [91].NISSIN WAFER COKLAT TIN 570GR SERIES\n' \
            '[12].YUPI STROWBERRY KISS 110GR        [32].INDOMIE JUMBO GORENG SERIES 125GR  [52].SILVER QUEEN BITES ALMOND 40GR    [72].OREO MINI 67GR SERIES           [92].ROMA WAFER CAN 336GR SERIES\n' \
            '[13].YUPI FUN GUM 120GR                [33].INDOMIE KUAH SERIES 75GR           [53].SILVER QUEEN 68GR SERIES          [73].ROMA MALKIST TRAMISU 120GR      [93].SARI ROTI SANDWICH SERIES\n' \
            '[14].CHUPA CHUPS ASSORTED CANDY        [34].INDOMIE KARI SERIES 72GR           [54].SILVER QUEEN CHUNKY BAR 100GR     [74].ROMA MALKIST ABON 240GR         [94].SARI ROTI ISI SERIES\n' \
            '[15].SUGUS STIK STR 30GR               [35].INDOMIE GORENG KTN SERIES          [55].DAILY MILK 30GR                   [75].ROMA MARIE 115GR                [95].SARI ROTI TAWAR GANDUM\n' \
            '[16].SUGUS STIK BLACK CURRANT 30GR     [36].INDOMIE KUAH KTN SERIES            [56].DAILY MILK 65GR                   [76].ROMA FESTIVE 765GR              [96].SARI ROTI TAWAR\n' \
            '[17].BIG BABOL STR STICK 24GR          [37].INDOMIE KARI KTN SERIES            [57].KINDER JOY 20GR                   [77].SLAI OLAI 240GR SERIES          [97].SARI ROTI TAWAR KUPAS\n' \
            '[18].DORITOS TORTILLA 160GR            [38].SEDAP MIE KARI SERIES 72GR         [58].DELFI COKLAT 55GR                 [78].TANGO WAFER 78GR SERIES         [98].SARI ROTI KRIM\n' \
            '[19].OISHI SPOGE CRUNCH 120GR          [39].SEDAP MIE KUAH SERIES 75GR         [59].DELFI COKLAT 155GR                [79].TANGO WAFER 145GR SERIES        [99].SARI ROTI SOBEK 2 RASA\n' \
            '[20].PILUS GARUDA 95GR                 [40].SEDAP MIE GORENG SERIES 75GR       [60].BENG-BENG MAX                     [80].TANGO WAFER 176GR SERIES        [100].DISNEY TAWAR KUPAS\n' \
            '\nuntuk Makanan uratan:permen(1/15)-chiki(16/30)-mieinstan(31/50)-coklat(51/60)biskuit(61/77)-wafer(78/92)-roti(93/107)'
    elif cek_kode[i]=='3':
        cek = '\t\t\t\t Nomor Kode Barang Minuman\n'\
            '[1].sprite botol 250ml     [10].TEBS             [19].le mineral galon 15lt [28].nescafe 450ml    [37].bear bland             [46].sgm 1/3 1000gr\n' \
            '[2].sprite botol 500ml     [11].big cola 500ml   [20].prima 500ml           [29].kopiko 78 500ml  [38].hilo 550ml             [47].sgm 3/6 1000gr\n' \
            '[3].sprite botol 1lt       [12].big cola 1lt     [21].prima 1500ml          [30].yogurt drink     [39].frisian flag klg 230ml [48].sgm soya 1000gr\n' \
            '[4].coca cola botol 250ml  [13].big cola 2lt     [22].cleo 300ml            [31].yakult 1 pack    [40].milo 500ml             [49].dancow 0/1 900gr\n' \
            '[5].coca cola botol 500ml  [14].aqua 500ml       [23].cleo 500ml            [32].pulpy 550ml      [41].fresh milk 1lt         [50].dancow 1/3 900gr\n' \
            '[6].coca cola botol 1lt    [15].aqua 1500ml      [24].crystaline 500ml      [33].floridina 350ml  [42].bebelac 0/1 800gr      [51].dancow 3/6 900gr\n' \
            '[7].Fanta botol 250ml      [16].aqua 19lt        [25].ades 500ml            [34].indomilk 250ml   [43].bebelac 1/3 800gr      [52].frisian flag 123 1000gr\n' \
            '[8].Fanta botol 500ml      [17].le mineral 500ml [26].vit 500ml             [35].indomilk 550ml   [44].bebelac 3/6 800gr      [53].frisian flag 456 1000gr\n' \
            '[9].Fanta botol 1lt        [18].le mineral1500ml [27].naraya 500ml          [36].indomilk 1lt     [45].sgm 0/1 1000gr\n' \
            'untuk minuman urutan : soda(1/13),air mineral(14/26),kopi(27/29),yogurt(30/31),jeruk(32/33),susu(34/53)'
    elif cek_kode[i]=='4':
        cek = '\t\t\t\t Kode Barang Peralatan Mandi Mandi\n' \
            '[1].sabun batang lifebouy            [5].sahmpoo sunsilk hijab 340ml           [9].pepsodent 75 gr    [13].onda hand shower so  250   [17].sikat cuci pring stainles [21].ember besar\n' \
            '[2].zwitsal baby baath natural       [6].head & shoulder anti hair fall shampoo[10].bak mandi anak    [14].selang air stainless       [18].sikat cuci baju           [22].ember jumbo\n' \
            '[3].shampoo lifebouy 170ml           [7].pepsodent sensitive expert enamel     [11].handuk jumbo      [15].onda keran air A 812 cis   [19].bak mandi                 [23].sabun cuci\n' \
            '[4].sahmpoo sunsilk soft&smoot 170ml [8].sendsodyen original 100gr             [12].lion star gayung  [16].sikat gigi 1pcs            [20].ember kecil               [24].gantungan baju dan handuk\n' \
            'untuk alat mandi(1/24)urutan: SSP(1/9),alat mandi(10/24)'
    elif cek_kode[i]=='5':
        cek = '\t\t\t\t Kode Barang Kosmetik\n' \
              '[1].Acnes                [5].Viva Skin Food Cream [9].Clear     [13].Revlon  [17].Rejoice    [21].Dove       [25].Vaseline UV\n' \
              '[2].Ponds                [6].Garnier              [10].Lifebuoy [14].Nature  [18].Zinc       [22].Purbasari  [26].Sari Ayu\n' \
              '[3].Wardah Lips          [7].Romano               [11].Elips    [15].Emeron  [19].Pantene    [23].Citra      [27].Fairy N Pink\n' \
              '[4].Olay Regenerist Night[8].Headshoulder         [12].Loreal   [16].Sunsilk [20].Nuvo       [24].Nivea\n' \
              'untuk kosmetik (1/27)'
    elif cek_kode[i]=='6':
        cek = '\t\t\t\t Kode Barang Kebersihan\n' \
              '[1].Beyclin              [5].Procline White Crystal  [9].Reckitt Benckiser      [13].Downi Deterjen  [17].Boom Wing     [21].Mr Muscle Axi Triguna   [25].Vixal\n' \
              '[2].So Klin Pemutih      [6].NEOhaus White Up        [10].Rinso Molto Deterjen  [14].Molto Deterjen  [18].S.O.S         [22].Wipol Ultra Protection  [26].Harpic\n' \
              '[3].Vanish               [7].Seven G C Free Bleach   [11].So Klin Deterjen      [15].Daia Deterjen   [19].SuperPell     [23].Dettol Pembersih Lantai [27].WPC\n' \
              '[4].Clorox Bleach Pen Gel[8].Tide Plus Bleach A L L  [12].Jaz1 Deterjen         [16].Attack Easy     [20].So Klin Lantai[24].Porstex                 [28].Wipol Cair\n' \
              'untuk kebersihan: pemutih (1/9), deterjen (10/17),Pembersih Lantai (18/23),Pembersih WC (24/28)'
    elif cek_kode[i]=='7':
        cek = '\t\t\t\t Kode Barang Keperluan Dapur\n' \
              '[1].teplon maxim     [6].sendok 1 set [11].isi gas elpiji 5 kg     [16].bango kecap manis 550ml     [21].ABC sarden besar 425gr      [26].fortune 2lt.\n' \
              '[2].wajan            [7].gelas 6 pcs  [12].kompor miyako           [17].ABC sambal terasi 180 g     [22].tepung terigu kunci biru 1kg[27].sania 2lt.\n' \
              '[3].lion star talenan[8].piring 1 pcs [13].sasa santan bubuk 500gr [18].ladaku merica bubuk 100gr   [23].desaku ketumbar bubuk 1rcg  [28].filma 2lt minyak jagung.\n' \
              '[4].rak piring       [9].baskom 1pcs  [14].sasa penyedap 1kg       [19].saori saos teriyaki 10sachet[24].royko 1kg                   [29].bimoli 1lt.\n' \
              '[5].pengocok telur   [10].cobek       [15].sasa tepung bumbu 850 gr[20].saus ABC botol 335ml        [25].bimoli 2lt                  [30].tropikal 1lt.\n' \
              'untuk keperluan dapur (1/30)urutan:alatmasak(1/12),bumbudapur(13/24),minyak(25/30)'
    elif cek_kode[i]=='8':
        cek = '\t\t\t\t Kode Barang Buah-buahan\n' \
              '[1].pir madu    [6].duku      [11].buah naga[16].alpukat   [21].nangka\n' \
              '[2].anggur merah[7].rambutan  [12].ceri     [17].bengkuang [22].durian\n' \
              '[3].nanas       [8].lemon     [13].kurma    [18].kelengkeng[23].pepaya\n' \
              '[4].apel        [9].jeruk     [14].melon    [19].mangga    [24].salak\n' \
              '[5].semangka    [10].blueberry[15].jambu air[20].manggis   [25].stowberry\n' \
              'untuk Buah-buahan (kg)'
    elif cek_kode[i]=='9':
        cek = '\t\t\t\t Kode Barang Daging,ayam,dan ikan\n' \
              '[1].Ayam Parting Frozen 1 kg   [6].Fiesta Paha Bawah 1 kg          [11].Fiesta Happy Star 500 g       [16].Champ Nugget ABC 500 g       [21].Champ Sosis 150 g               [26].Ikan Tuna  500 gr\n' \
              '[2].Fiesta Ayam Flt Dd TTK 1 kg[7].Fiesta Chicken Nugget 500 g     [12].Fiesta Nugget Cheese 123 500 g[17].Fiesta Sausage 300 g         [22].Daging Sapi Beku Import Aus 1 kg[27].Ikan Salmon 1 kg\n' \
              '[3].Fiesta Ayam Flt Dd TTK 1 kg[8].Fiesta Stikie 500 g             [13].Champ Nugget 500 g            [18].Fiesta  Sosis Bratwurst 300 g[23].Daging Sapi Paha 1 kg           [28].Ikan Tenggiri Giling 1 kg\n' \
              '[4].Fiesta Paha Utuh 1 kg      [9].Fiesta Golden Chicken Ring 500 g[14].Champ Nugget Coin 500 g       [19].Fiesta Sosis Keju 300 g      [24].Ikan Dori 1 kg\n' \
              '[5].Fiesta Paha Atas 1 kg      [10].Fiesta Nugget Zoo 500 g        [15].Champ Nugget Stick 500 g      [20].Champ Sosis 375 g            [25].Ikan Tenggiri Jumbo 500 gr\n' \
              'untuk Daging,Ayam,dan Ikan(1/28):dagingayam(1/6),nuggetayam(7/16),sosisayam(17/21),dagingsapi(22/23)dagingikan(24/28)'
    elif cek_kode[i]=='10':
        cek = '\t\t\t\t Kode Barang Obat-Obatan\npart1\n' \
              '[1].Siladex Batuk Pilek 30ml        [6].OBH Combi Anak Rasa Jeruk 60ml[11].Anakonidin OBH 60ml         [16].Vicks Formula 44 Anak 54ml.\n' \
              '[2].Siladex Batuk Pilek 60ml        [7].OBH Combi Anak Rasa Madu 60ml [12].SanaFlu Plus Batuk Tablet   [17].Bodrex Flu & Batuk Berdahak PE Tablet.\n' \
              '[3].Triaminic Batuk Syr 60ml        [8].AnaKonidin 30ml               [13].Bodrex Flu & Batuk PE Tablet[18].Benadryl Batuk Berdahak Syr 50ml.\n' \
              '[4].OBH Combi Dewasa Rasa Jahe 100ml[9].AnaKonidin 60ml               [14].Bodrexin Flu & B PE S 56ml  [19].OBH Combi Batuk Berdahak Rasa M 100ml.\n' \
              '[5].OBH Combi Dewasa Rasa Madu 100ml[10].Anakonidin OBH 30ml          [15].Mixagrip Flu & Batuk Tablet [20].Bodrexin Flu & Batuk Berdahak PES56ml.\npart2\n' \
              '[21].Bodrexin Demam 60ml            [26].Ultraflu 4 Strip             [31].Paramex Tab 4 Strip' \
              '[22].Siantan Demam Berdarah Tablet  [27].Panadol Syrup 60ml           [32].Sanmol Drop 15ml' \
              '[23].Sari Kurma Sahara              [28].Panadol Biru Tablet 10 tab   [33].Rohto Fever Patch 2S' \
              '[24].Pimtrakol kids D & B Str       [29].Panadol Cold Flu Hju T10 tab [34].Panadol Anak Tab' \
              '[25].Procold Flu 6 Strip            [30].Panadol Extra Merah 10 tab   [35].Decolgen tab 4 str' \
              'untuk Obat-obatan (1/35):Fludanbatuk(1/20),demam(21/35)'
    else:
        exit()
    print(cek)
print(500*"-")
bj = int(input("Banyak Varian Barang :"))

#perulangan
for i in range(bj):
    menu()

#tampilan struk dan rincian kode
print("\t\t\t\t\t\tJunior Mart", "\n", 499 * "=")
print("Belanja Kebutuhan Sehari-hari cuma ada di Junior Mart\n\t\t\tLengkap Dan Terjangkau")
print("\t\t\tJl.Kp.Melayu Timur KEl Kp.Melayu Timur \n\t\t\t\tKec. TELUKNAGA,Kab.Tangerang")
print(500 * "-", "\nPembelanjaan Anda : ")
total_beli=0
#check Condition
for i in range(bj):
    if jenis_barang[i]=="1" or jenis_barang[i]=="I":#untuk sayuran barang yang kiloan di hitung ons & hitung satuan bagi sayuran yang per ikat
        if kode_barang[i]=="1":
            jenis = "Bawang Merah"
            harga = 4500
        elif kode_barang[i]=="2":
            jenis = "Bawang Putih"
            harga = 4000
        elif kode_barang[i]=="3":
            jenis = "Bawang Bombay"
            harga = 4000
        elif kode_barang[i]=="4":
            jenis = "Cabai Merah"
            harga = 7000
        elif kode_barang[i]=="5":
            jenis = "Cabai Rawit"
            harga = 5000
        elif kode_barang[i]=="6":
            jenis = "Cabai Rawit Merah"
            harga = 8000
        elif kode_barang[i]=="7":
            jenis = "Bayam"
            harga = 5000
        elif kode_barang[i]=="8":
            jenis = "Bayam Merah"
            harga = 8000
        elif kode_barang[i]=="9":
            jenis = "Kangkung"
            harga = 5000
        elif kode_barang[i]=="10":
            jenis = "Kangkung Merah"
            harga = 8000
        elif kode_barang[i]=="11":
            jenis = "Sousin"
            harga = 5000
        elif kode_barang[i]=="12":
            jenis = "Touge"
            harga = 1000
        elif kode_barang[i]=="13":
            jenis = "Brocoli"
            harga = 2000
        elif kode_barang[i]=="14":
            jenis = "Wortel"
            harga = 2000
        elif kode_barang[i]=="15":
            jenis = "labu"
            harga = 1500
        elif kode_barang[i] == "16":
            jenis = "labu siam"
            harga = 2000
        elif kode_barang[i] == "17":
            jenis = "pare"
            harga = 1000
        elif kode_barang[i] == "18":
            jenis = "jagung"
            harga = 5000
        elif kode_barang[i] == "19":
            jenis = "jagung acar"
            harga = 500
        elif kode_barang[i] == "20":
            jenis = "Tomat"
            harga = 2000
        elif kode_barang[i] == "21":
            jenis = "Kacang Panjang"
            harga = 1500
        elif kode_barang[i] == "22":
            jenis = "Petai"
            harga = 1500
        elif kode_barang[i] == "23":
            jenis = "Jengkol"
            harga = 5000
        elif kode_barang[i] == "24":
            jenis = "Ubi"
            harga = 500
        elif kode_barang[i] == "25":
            jenis = "Ubi Merah"
            harga = 800
        elif kode_barang[i] == "26":
            jenis = "Singkong"
            harga = 500
        elif kode_barang[i] == "27":
            jenis = "Kentang"
            harga = 1500
        elif kode_barang[i] == "28":
            jenis = "Kentang Somay"
            harga = 1000
        elif kode_barang[i] == "29":
            jenis = "poccoy"
            harga = 2000
        elif kode_barang[i] == "30":
            jenis = "Buncis"
            harga = 5000
        elif kode_barang[i] == "31":
            jenis = "Jeruk Lemon"
            harga = 5000
        elif kode_barang[i] == "32":
            jenis = "Sawi Hijau"
            harga = 500
        elif kode_barang[i] == "33":
            jenis = "Jeruk limo"
            harga = 2000
        elif kode_barang[i] == "34":
            jenis = "Timun"
            harga = 3000
        elif kode_barang[i] == "35":
            jenis = "Timun Jepang"
            harga = 600
        elif kode_barang[i] == "36":
            jenis = "Selada Keriting"
            harga = 2000
        elif kode_barang[i] == "37":
            jenis = "Selada air"
            harga = 2000
        elif kode_barang[i] == "38":
            jenis = "Sawi Putih"
            harga = 1500
        elif kode_barang[i] == "39":
            jenis = "Daun Bawang"
            harga = 1000
        elif kode_barang[i] == "40":
            jenis = "Terong Ungu"
            harga = 2000
        elif kode_barang[i] == "41":
            jenis = "Paprika Merah"
            harga = 5000
        elif kode_barang[i] == "42":
            jenis = "Paprika Hijau"
            harga = 5000
        elif kode_barang[i] == "43":
            jenis = "Paprika Kuning"
            harga = 5000
        elif kode_barang[i] == "44":
            jenis = "Jeruk nipis"
            harga = 2000
        elif kode_barang[i] == "45":
            jenis = "kol"
            harga = 1500
        elif kode_barang[i] == "46":
            jenis = "Seledri"
            harga = 1500
        elif kode_barang[i] == "47":
            jenis = "Kembang Kol"
            harga = 1800
        elif kode_barang[i] == "48":
            jenis = "Lobak"
            harga = 1500
        elif kode_barang[i] == "49":
            jenis = "Jamur Merang"
            harga = 2000
        elif kode_barang[i] == "50":
            jenis = "Kemeri"
            harga = 2500
        elif kode_barang[i] == "51":
            jenis = "Daun Katuk"
            harga = 1000
        elif kode_barang[i] == "52":
            jenis = "labu parang"
            harga = 2000
        elif kode_barang[i] == "53":
            jenis = "Daun Singkong"
            harga = 3000
        elif kode_barang[i] == "54":
            jenis = "Daun Pandan"
            harga = 3000
        elif kode_barang[i] == "55":
            jenis = "Jahe"
            harga = 3000
        elif kode_barang[i] == "56":
            jenis = "Jahe Merah"
            harga = 5000
        elif kode_barang[i] == "57":
            jenis = "kencur"
            harga = 2000
        elif kode_barang[i] == "58":
            jenis = "Kunyit"
            harga = 3000
        elif kode_barang[i] == "59":
            jenis = "Nangka Muda"
            harga = 2400
        elif kode_barang[i] == "60":
            jenis = "Sereh"
            harga = 5000
        elif kode_barang[i] == "61":
            jenis = "Daun Jeruk"
            harga = 2000
        elif kode_barang[i] == "62":
            jenis = "Daun salam"
            harga = 2000
        else:
            jenis = "Kode Sampai 62 Saja"
            harga = 0

    elif jenis_barang[i]=="2" or jenis_barang[i]=="II": #untuk Makanan uratan:permen(1/15)-chiki(16/30)-mieinstan(31/50)-coklat(51/60)
        # -biskuit(61/77)-wafer(78/92)-roti(93/105)
        #candy start
        if kode_barang[i]=="1":
            jenis = "FROZZ permen mint org 15GR"
            harga = 9550
        elif kode_barang[i] == "2":
            jenis = "FROZZ PERMEN CHERRY 15GR"
            harga = 9550
        elif kode_barang[i]=="3":
            jenis = "FISHERMANS FREIND HONEY LEMON 25GR"
            harga = 17850
        elif kode_barang[i]=="4":
            jenis = "Mentos Pure Papermint 35GR"
            harga = 19890
        elif kode_barang[i]=="5":
            jenis = "MINT FRUIT CHERRYMINT 115GR "
            harga = 7290
        elif kode_barang[i]=="6":
            jenis = "MINT FRUIT GRAPEMINT 115GR"
            harga = 7290
        elif kode_barang[i]=="7":
            jenis = "RELAXA PERMEN BARLEY MINT 125GR"
            harga = 8380
        elif kode_barang[i]=="8":
            jenis = "MENTOS FRUIT BAG 121,5GR"
            harga = 7590
        elif kode_barang[i]=="9":
            jenis = "MINT MOJIZ DUO MINT 112,5GR"
            harga = 7350
        elif kode_barang[i]=="10":
            jenis = "KISS APPLE PEACH 125GR"
            harga = 8450
        elif kode_barang[i]=="11":
            jenis = "KISS CHERRY MINT 125GR"
            harga = 8450
        elif kode_barang[i]=="12":
            jenis = "YUPI STROWBERRY KISS 110GR"
            harga = 10490
        elif kode_barang[i]=="13":
            jenis = "YUPI FUN GUM 120GR"
            harga = 12200
        elif kode_barang[i]=="14":
            jenis = "CHUPA CHUPS ASSORTED CANDY"
            harga = 1550
        elif kode_barang[i]=="15":
            jenis = "SUGUS STIK STR 30GR"
            harga = 3200
        elif kode_barang[i] == "16":
            jenis = "SUGUS STIK BLACK CURRANT 30GR"
            harga = 3200
        elif kode_barang[i] == "17":
            jenis = "BIG BABOL STR STICK 24GR"
            harga = 3290
        #finist Candy
        #start chiki
        elif kode_barang[i] == "18":
            jenis = "DORITOS TORTILLA 160GR"
            harga = 11200
        elif kode_barang[i] == "19":
            jenis = "OISHI SPOGE CRUNCH 120GR"
            harga = 11500
        elif kode_barang[i] == "20":
            jenis = "PILUS GARUDA 95GR"
            harga = 5590
        elif kode_barang[i] == "21":
            jenis = "TAO KAE NOI CRISPY 4GR"
            harga = 5500
        elif kode_barang[i] == "22":
            jenis = "LAY'S 55GR"
            harga = 8900
        elif kode_barang[i] == "23":
            jenis = "KUSUKA SNACK JAGUNG 180GR"
            harga = 15990
        elif kode_barang[i] == "24":
            jenis = "DUA KELINCI GARNIC NUT 200GR"
            harga = 20900
        elif kode_barang[i] == "25":
            jenis = "DUA KELINCI 75GR"
            harga = 11500
        elif kode_barang[i] == "26":
            jenis = "REBO KUACI MATAHARI 70GR"
            harga = 8250
        elif kode_barang[i] == "27":
            jenis = "CHEETOS TWIST 75GR"
            harga = 6800
        elif kode_barang[i] == "28":
            jenis = "CHITATO 85GR"
            harga = 9800
        elif kode_barang[i] == "29":
            jenis = "GARUDA KACANG KULIT 200GR"
            harga = 16500
        elif kode_barang[i] == "30":
            jenis = "PINGLES POT SNACK 107GR"
            harga = 21850
        #finist chiki
        #start mie instan
        elif kode_barang[i] == "31":
            jenis = "INDOMIE GORENG SERIES 75GR"
            harga = 2490
        elif kode_barang[i] == "32":
            jenis = "INDOMIE JUMBO GORENG SERIES 125GR "
            harga = 3290
        elif kode_barang[i] == "33":
            jenis = "INDOMIE KUAH SERIES 75GR"
            harga = 2350
        elif kode_barang[i] == "34":
            jenis = "INDOMIE KARI SERIES 72GR"
            harga = 2480
        elif kode_barang[i] == "35":
            jenis = "INDOMIE GORENG KTN SERIES"
            harga = 99600
        elif kode_barang[i] == "36":
            jenis = "INDOMIE KUAH KTN SERIES"
            harga = 90200
        elif kode_barang[i] == "37":
            jenis = "INDOMIE KARI KTN SERIES"
            harga = 98000
        elif kode_barang[i] == "38":
            jenis = "SEDAP MIE KARI SERIES 72GR"
            harga = 2450
        elif kode_barang[i] == "39":
            jenis = "SEDAP MIE KUAH SERIES 75GR"
            harga = 2390
        elif kode_barang[i] == "40":
            jenis = "SEDAP MIE GORENG SERIES 75GR"
            harga = 2490
        elif kode_barang[i] == "41":
            jenis = "MIE SEDAP GERENG CUP SERIES 85GR"
            harga = 4650
        elif kode_barang[i] == "42":
            jenis = "MIE SEDAP KUAH CUP SERIES 77GR"
            harga = 4450
        elif kode_barang[i] == "43":
            jenis = "POPMIE KUAH SERIES 75GR"
            harga = 4350
        elif kode_barang[i] == "44":
            jenis = "POPMIE GORENG SERIES 75GR"
            harga = 4590
        elif kode_barang[i] == "45":
            jenis = "LAFONTE 450GR"
            harga = 15600
        elif kode_barang[i] == "46":
            jenis = "BAKMI MEWAH 110GR"
            harga = 10800
        elif kode_barang[i] == "47":
            jenis = "SARIMI ISI 2 GORENG SERIES 125GR"
            harga = 3500
        elif kode_barang[i] == "48":
            jenis = "SARIMI ISI 2 KUAH SERIES 115GR"
            harga = 3300
        elif kode_barang[i] == "49":
            jenis = "ABC MIE GORENG SERIES 70GR"
            harga = 1900
        elif kode_barang[i] == "50":
            jenis = "ABC MIE KUAH SERIES 65GR"
            harga = 1520
        #finist mie instan
        #start coklat
        elif kode_barang[i] == "51":
            jenis = "SILVER QUEEN MINI 30GR SERIES"
            harga = 9150
        elif kode_barang[i] == "52":
            jenis = "SILVER QUEEN BITES ALMOND 40GR"
            harga = 9890
        elif kode_barang[i] == "53":
            jenis = "SILVER QUEEN 68GR SERIES"
            harga = 16250
        elif kode_barang[i] == "54":
            jenis = "SILVER QUEEN CHUNKY BAR 100GR"
            harga = 24590
        elif kode_barang[i] == "55":
            jenis = "DAILY MILK 30GR"
            harga = 9150
        elif kode_barang[i] == "56":
            jenis = "DAILY MILK 65GR"
            harga = 16150
        elif kode_barang[i] == "57":
            jenis = "KINDER JOY 20GR"
            harga = 12050
        elif kode_barang[i] == "58":
            jenis = "DELFI COKLAT 55GR"
            harga = 14200
        elif kode_barang[i] == "59":
            jenis = "DELFI COKLAT 155GR"
            harga = 32200
        elif kode_barang[i] == "60":
            jenis = "BENG-BENG MAX"
            harga = 3450
        #finist coklat
        #startbiskuit
        elif kode_barang[i] == "61":
            jenis = "BATTER VANILA BOX"
            harga = 5350
        elif kode_barang[i] == "62":
            jenis = "REGAL MARIE 230GR SERIES"
            harga = 19550
        elif kode_barang[i] == "63":
            jenis = "REGAL MARIE TIN 550GR SERIES"
            harga = 63990
        elif kode_barang[i] == "64":
            jenis = "REGAL MARIE 1000GR"
            harga = 148550
        elif kode_barang[i] == "65":
            jenis = "HELLO PANDA 45GR"
            harga = 9150
        elif kode_barang[i] == "66":
            jenis = "FITBAR COKLAT 25GR"
            harga = 5150
        elif kode_barang[i] == "67":
            jenis = "MONDE GENJI PIE 70GR"
            harga = 9750
        elif kode_barang[i] == "68":
            jenis = "MONDE RAISIN PIE 85GR"
            harga = 9750
        elif kode_barang[i] == "69":
            jenis = "MONDE SARENA ROLL BICKUIT 60GR "
            harga = 9150
        elif kode_barang[i] == "70":
            jenis = "OREO 95GR SERIES"
            harga = 10750
        elif kode_barang[i] == "71":
            jenis = "OREO SANDWICT 133GR SERIES"
            harga = 7890
        elif kode_barang[i] == "72":
            jenis = "OREO MINI 67GR SERIES"
            harga = 8750
        elif kode_barang[i] == "73":
            jenis = "ROMA MALKIST TRAMISU 120GR"
            harga = 6200
        elif kode_barang[i] == "74":
            jenis = "ROMA MALKIST ABON 240GR"
            harga = 10150
        elif kode_barang[i] == "75":
            jenis = "ROMA MARIE 115GR"
            harga = 5500
        elif kode_barang[i] == "76":
            jenis = "ROMA FESTIVE 765GR"
            harga = 95550
        elif kode_barang[i] == "77":
            jenis = "SLAI OLAI 240GR SERIES"
            harga = 10500
        #FINIST BISKUIT
        #START WAFER
        elif kode_barang[i] == "78":
            jenis = "TANGO WAFER 78GR SERIES"
            harga = 5800
        elif kode_barang[i] == "79":
            jenis = "TANGO WAFER 145GR SERIES"
            harga = 5400
        elif kode_barang[i] == "80":
            jenis = "TANGO WAFER 176GR SERIES"
            harga = 12250
        elif kode_barang[i] == "81":
            jenis = "TANGO WAFER POUCH 115GR SERIES"
            harga = 8900
        elif kode_barang[i] == "82":
            jenis = "KHONG GUAN WAFER 160GR"
            harga = 13800
        elif kode_barang[i] == "83":
            jenis = "KHONG GUAN CLASIC 280GR"
            harga = 20300
        elif kode_barang[i] == "84":
            jenis = "KHONG GUAN MINI TIN 650GR"
            harga = 45890
        elif kode_barang[i] == "85":
            jenis = "KHONG GUAN SEGI TIN 1600GR"
            harga = 80000
        elif kode_barang[i] == "86":
            jenis = "SELAMAT WAFER 60GR SERIES"
            harga = 5750
        elif kode_barang[i] == "87":
            jenis = "SELAMAT WAFER 198GR SERIES"
            harga = 12980
        elif kode_barang[i] == "88":
            jenis = "SELAMAT WAFER TIN 440GR SERIES"
            harga = 37800
        elif kode_barang[i] == "89":
            jenis = "NISSIN WAFER 110GR SERIES"
            harga = 7200
        elif kode_barang[i] == "90":
            jenis = "NISSIN WAFER COKLAT MINI TIN 200GR SERIES"
            harga = 24590
        elif kode_barang[i] == "91":
            jenis = "NISSIN WAFER COKLAT TIN 570GR SERIES"
            harga = 51450
        elif kode_barang[i] == "92":
            jenis = "ROMA WAFER CAN 336GR SERIES"
            harga = 33800
        #FINIST WAFER
        #START ROTI
        elif kode_barang[i] == "93":
            jenis = "SARI ROTI SANDWICH SERIES"
            harga = 4650
        elif kode_barang[i] == "94":
            jenis = "SARI ROTI ISI SERIES"
            harga = 5900
        elif kode_barang[i] == "95":
            jenis = "SARI ROTI TAWAR GANDUM"
            harga = 18550
        elif kode_barang[i] == "96":
            jenis = "SARI ROTI TAWAR "
            harga = 12700
        elif kode_barang[i] == "97":
            jenis = "SARI ROTI TAWAR KUPAS"
            harga = 14500
        elif kode_barang[i] == "98":
            jenis = "SARI ROTI KRIM"
            harga = 5000
        elif kode_barang[i] == "99":
            jenis = "SARI ROTI SOBEK 2 RASA"
            harga = 15500
        elif kode_barang[i] == "100":
            jenis = "DISNEY TAWAR KUPAS"
            harga = 14500
        elif kode_barang[i] == "101":
            jenis = "DISNEY LOCO WHOLEMEAL"
            harga = 33500
        elif kode_barang[i] == "102":
            jenis = "DISNEY MILK LOF"
            harga = 16500
        elif kode_barang[i] == "103":
            jenis = "DISNEY BIG SUGAR LOFT"
            harga = 20000
        elif kode_barang[i] == "104":
            jenis = "DISNEY FAMILY WHITE BREAD"
            harga = 12700
        elif kode_barang[i] == "105":
            jenis = "KAYA PILLOW BREAD"
            harga = 19500
        elif kode_barang[i] == "106":
            jenis = "MEXICO PILLOW BREAD"
            harga = 19500
        elif kode_barang[i] == "107":
            jenis = "BURGER BUN"
            harga = 11590
        else:
            jenis = 'kode sampai 107 saja'
            harga = 0
    elif jenis_barang[i]=="3" or jenis_barang[i]=="III" : #untuk minuman urutan : soda(1/13),air mineral(14/26),kopi(27/29),yogurt(30/31),jeruk(32/33),susu(34/53)
        #start soda
        if kode_barang[i]=="1":
            jenis = "sprite botol 250ml"
            harga = 1950
        elif kode_barang[i]=="2":
            jenis = "sprite botol 500ml"
            harga = 5200
        elif kode_barang[i]=="3":
            jenis = "sprite botol 1lt"
            harga = 9950
        elif kode_barang[i]=="4":
            jenis = "coca cola botol 250ml"
            harga = 1950
        elif kode_barang[i]=="5":
            jenis = "coca cola botol 500ml"
            harga = 5200
        elif kode_barang[i] == "6":
            jenis = "coca cola botol 1lt"
            harga = 9950
        elif kode_barang[i] == "7":
            jenis = "Fanta botol 250ml"
            harga = 1950
        elif kode_barang[i] == "8":
            jenis = "Fanta botol 500ml"
            harga = 5200
        elif kode_barang[i] == "9":
            jenis = "Fanta botol 1lt"
            harga = 9950
        elif kode_barang[i] == "10":
            jenis = "TEBS"
            harga = 6000
        elif kode_barang[i] == "11":
            jenis = "big cola 500ml"
            harga = 3500
        elif kode_barang[i] == "12":
            jenis = "big cola 1lt"
            harga = 6700
        elif kode_barang[i] == "13":
            jenis = "big cola 2lt"
            harga = 13050
        #finist soda
        #start air mineral
        elif kode_barang[i] == "14":
            jenis = "aqua 500ml"
            harga = 4000
        elif kode_barang[i] == "15":
            jenis = "aqua 1500ml"
            harga = 6200
        elif kode_barang[i] == "16":
            jenis = "aqua 19lt"
            harga = 19500
        elif kode_barang[i] == "17":
            jenis = "le mineral 500ml"
            harga = 3000
        elif kode_barang[i] == "18":
            jenis = "le mineral 1500ml"
            harga = 5700
        elif kode_barang[i] == "19":
            jenis = "le mineral galon 15lt"
            harga = 18000
        elif kode_barang[i] == "20":
            jenis = "prima 500ml"
            harga = 2800
        elif kode_barang[i] == "21":
            jenis = "prima 1500ml"
            harga = 5400
        elif kode_barang[i] == "22":
            jenis = "cleo 300ml"
            harga = 1800
        elif kode_barang[i] == "23":
            jenis = "cleo 500ml"
            harga = 2800
        elif kode_barang[i] == "24":
            jenis = "crystaline 500ml"
            harga = 2000
        elif kode_barang[i] == "25":
            jenis = "ades 500ml"
            harga = 3500
        elif kode_barang[i] == "26":
            jenis = "vit 500ml"
            harga = 4000
        #finist air mineral
        #start kopi
        elif kode_barang[i] == "27":
            jenis = "naraya 500ml"
            harga = 6500
        elif kode_barang[i] == "28":
            jenis = "nescafe 450ml"
            harga = 5000
        elif kode_barang[i] == "29":
            jenis = "kopiko 78 500ml"
            harga = 6000
        #finist kopi
        #strat yogurt
        elif kode_barang[i] == "30":
            jenis = "yogurt drink "
            harga = 8500
        elif kode_barang[i] == "31":
            jenis = "yakult 1 pack"
            harga = 9000
        #finist Yogurt
        #start jeruk
        elif kode_barang[i] == "32":
            jenis = "pulpy 550ml"
            harga = 7500
        elif kode_barang[i] == "33":
            jenis = "floridina 350ml"
            harga = 2500
        #finist jeruk
        #start susu
        elif kode_barang[i] == "34":
            jenis = "indomilk 250ml"
            harga = 2900
        elif kode_barang[i] == "35":
            jenis = "indomilk 550ml"
            harga = 5500
        elif kode_barang[i] == "36":
            jenis = "indomilk 1lt"
            harga = 13500
        elif kode_barang[i] == "37":
            jenis = "bear bland"
            harga = 11000
        elif kode_barang[i] == "38":
            jenis = "hilo 550ml"
            harga = 6000
        elif kode_barang[i] == "39":
            jenis = "frisian flag klg 230ml"
            harga = 12000
        elif kode_barang[i] == "40":
            jenis = "milo 500ml"
            harga = 5500
        elif kode_barang[i] == "41":
            jenis = "fresh milk 1lt"
            harga = 19500
        elif kode_barang[i] == "42":
            jenis = "bebelac 0/1 800gr"
            harga = 100000
        elif kode_barang[i] == "43":
            jenis = "bebelac 1/3 800gr"
            harga = 120000
        elif kode_barang[i] == "44":
            jenis = "bebelac 3/6 800gr"
            harga = 150000
        elif kode_barang[i] == "45":
            jenis = "sgm 0/1 1000gr"
            harga = 50000
        elif kode_barang[i] == "46":
            jenis = "sgm 1/3 1000gr"
            harga = 60000
        elif kode_barang[i] == "47":
            jenis = "sgm 3/6 1000gr"
            harga = 70000
        elif kode_barang[i] == "48":
            jenis = "sgm soya 1000gr"
            harga = 90000
        elif kode_barang[i] == "49":
            jenis = "dancow 0/1 900gr"
            harga = 70000
        elif kode_barang[i] == "50":
            jenis = "dancow 1/3 900gr"
            harga = 80000
        elif kode_barang[i] == "51":
            jenis = "dancow 3/6 900gr "
            harga = 90000
        elif kode_barang[i] == "52":
            jenis = "frisian flag 123 1000gr"
            harga = 70000
        elif kode_barang[i] == '53':
            jenis = "frisian flag 456 1000gr"
            harga = 85000
        else:
            jenis = 'kode sampai 53 saja'
            harga = 0
       #finist minuman
    elif jenis_barang[i]=="4" or jenis_barang[i]=="IV":#untuk alat mandi(1/24)urutan: SSP(1/9),alat mandi(10/24)
        #start alat mandi
        if kode_barang[i]=="1":
            jenis = "sabun batang lifebouy"
            harga = 2000
        elif kode_barang[i]=="2":
            jenis = "zwitsal baby baath natural "
            harga = 26000
        elif kode_barang[i]=="3":
            jenis = "shampoo lifebouy 170ml"
            harga = 18000
        elif kode_barang[i]=="4":
            jenis = "sahmpoo sunsilk soft&smoot 170ml"
            harga = 28000
        elif kode_barang[i]=="5":
            jenis = "sahmpoo sunsilk hijab 340ml"
            harga = 31000
        elif kode_barang[i]=="6":
            jenis = "head & shoulder anti hair fall shampoo"
            harga = 40000
        elif kode_barang[i]=="7":
            jenis = "pepsodent sensitive expert enamel"
            harga = 30000
        elif kode_barang[i]=="8":
            jenis = "sendsodyen original 100gr"
            harga = 31000
        elif kode_barang[i]=="9":
            jenis = "pepsodent 75 gr"
            harga = 5000
        elif kode_barang[i]=="10":
            jenis = "bak mandi anak"
            harga = 17900
        elif kode_barang[i]=="11":
            jenis = "handuk jumbo"
            harga = 43000
        elif kode_barang[i]=="12":
            jenis = "lion star gayung"
            harga = 35000
        elif kode_barang[i]=="13":
            jenis = "onda hand shower so  250"
            harga = 115000
        elif kode_barang[i]=="14":
            jenis = "selang air stainless "
            harga = 150000
        elif kode_barang[i]=="15":
            jenis = "onda keran air A 812 cis"
            harga = 48000
        elif kode_barang[i] == "16":
            jenis = "sikat gigi 1pcs"
            harga = 6000
        elif kode_barang[i] == "17":
            jenis = "sikat cuci pring stainles"
            harga = 4000
        elif kode_barang[i] == "18":
            jenis = "sikat cuci baju"
            harga = 4000
        elif kode_barang[i] == "19":
            jenis = "bak mandi"
            harga = 25000
        elif kode_barang[i] == "20":
            jenis = "ember kecil"
            harga = 5000
        elif kode_barang[i] == "21":
            jenis = "ember besar"
            harga = 15000
        elif kode_barang[i] == "22":
            jenis = "ember jumbo"
            harga = 25000
        elif kode_barang[i] == "23":
            jenis = "sabun cuci"
            harga = 2000
        elif kode_barang[i] == '24':
            jenis = "gantungan baju dan handuk"
            harga = 15000
        else:
            jenis = 'kode sampai 24 saja'
            harga = 0
        #finist alat mandi
    elif jenis_barang[i]=="5" or jenis_barang[i]=="V":#untuk kosmetik (1/27)
        #start kosmetik
        if kode_barang[i]=="1":
            jenis = "Acnes"
            harga = 40000
        elif kode_barang[i]=="2":
            jenis = "Ponds"
            harga = 30000
        elif kode_barang[i]=="3":
            jenis = "Wardah Lips "
            harga = 70000
        elif kode_barang[i]=="4":
            jenis = "Olay Regenerist Night "
            harga = 198000
        elif kode_barang[i]=="5":
            jenis = "Viva Skin Food Cream"
            harga = 15000
        elif kode_barang[i]=="6":
            jenis = "Garnier"
            harga = 40000
        elif kode_barang[i]=="7":
            jenis = "Romano"
            harga = 47500
        elif kode_barang[i]=="8":
            jenis = "Headshoulder"
            harga = 53000
        elif kode_barang[i]=="9":
            jenis = "Clear"
            harga = 52500
        elif kode_barang[i]=="10":
            jenis = "Lifebuoy"
            harga = 46000
        elif kode_barang[i]=="11":
            jenis = "Elips"
            harga = 57000
        elif kode_barang[i]=="12":
            jenis = "Loreal"
            harga = 44000
        elif kode_barang[i]=="13":
            jenis = "Revlon"
            harga = 110000
        elif kode_barang[i]=="14":
            jenis = "Nature"
            harga = 99000
        elif kode_barang[i]=="15":
            jenis = "Emeron"
            harga = 66000
        elif kode_barang[i] == "16":
            jenis = "Sunsilk"
            harga = 55000
        elif kode_barang[i] == "17":
            jenis = "Rejoice"
            harga = 52000
        elif kode_barang[i] == "18":
            jenis = "Zinc"
            harga = 42000
        elif kode_barang[i] == "19":
            jenis = "Pantene"
            harga = 43500
        elif kode_barang[i] == "20":
            jenis = "Nuvo"
            harga = 45000
        elif kode_barang[i] == "21":
            jenis = "Dove"
            harga = 62000
        elif kode_barang[i] == "22":
            jenis = "Purbasari"
            harga = 52800
        elif kode_barang[i] == "23":
            jenis = "Citra"
            harga = 20500
        elif kode_barang[i] == "24":
            jenis = "Nivea"
            harga = 32500
        elif kode_barang[i] == "25":
            jenis = "Vaseline UV"
            harga = 40000
        elif kode_barang[i] == "26":
            jenis = "Sari Ayu"
            harga = 19000
        elif kode_barang[i] == '27':
            jenis = "Fairy N Pink"
            harga = 100000
        else:
            jenis = 'kode sampai 27 saja'
            harga = 0
        #finist kosmetik
    elif jenis_barang[i]=="6" or jenis_barang[i]=="VI":#untuk kebersihan (1/28)
        #start kebersihan
        #start pemutih
        if kode_barang[i]=="1":
            jenis = "Beyclin"
            harga = 16500
        elif kode_barang[i]=="2":
            jenis = "So Klin Pemutih"
            harga = 15000
        elif kode_barang[i]=="3":
            jenis = "Vanish"
            harga = 19000
        elif kode_barang[i]=="4":
            jenis = "Clorox Bleach Pen Gel"
            harga = 11000
        elif kode_barang[i]=="5":
            jenis = "Procline White Crystal"
            harga = 19500
        elif kode_barang[i]=="6":
            jenis = "NEOhaus White Up"
            harga = 14880
        elif kode_barang[i]=="7":
            jenis = "Seven Generation Chlorine Free Bleach"
            harga = 17500
        elif kode_barang[i]=="8":
            jenis = "Tide Plus Bleach Alternative Liquid Laundry Detergent"
            harga = 38500
        elif kode_barang[i]=="9":
            jenis = "Reckitt Benckiser"
            harga = 39000
        #finist pemutih
        #start deterjen
        elif kode_barang[i]=="10":
            jenis = "Rinso Molto Deterjen"
            harga = 70000
        elif kode_barang[i]=="11":
            jenis = "So Klin Deterjen"
            harga = 59000
        elif kode_barang[i]=="12":
            jenis = "Jaz1 Deterjen"
            harga = 60000
        elif kode_barang[i]=="13":
            jenis = "Downi Deterjen"
            harga = 72000
        elif kode_barang[i]=="14":
            jenis = "Molto Deterjen"
            harga = 38000
        elif kode_barang[i]=="15":
            jenis = "Daia Deterjen"
            harga = 38000
        elif kode_barang[i] == "16":
            jenis = "Attack Easy"
            harga = 72000
        elif kode_barang[i] == "17":
            jenis = "Boom Wing"
            harga = 53000
        #finist deterjen
        #start pembersih lantai
        elif kode_barang[i] == "18":
            jenis = "S.O.S"
            harga = 11700
        elif kode_barang[i] == "19":
            jenis = "SuperPell"
            harga = 11500
        elif kode_barang[i] == "20":
            jenis = "So Klin Lantai"
            harga = 11000
        elif kode_barang[i] == "21":
            jenis = "Mr Muscle Axi Triguna"
            harga = 12000
        elif kode_barang[i] == "22":
            jenis = "Wipol Ultra Protection"
            harga = 31000
        elif kode_barang[i] == "23":
            jenis = "Dettol Pembersih Lantai"
            harga = 21000
        #Finist pembersih lantai
        #start pembersih wc
        elif kode_barang[i] == "24":
            jenis = "Porstex"
            harga = 18500
        elif kode_barang[i] == "25":
            jenis = "Vixal"
            harga = 16500
        elif kode_barang[i] == "26":
            jenis = "Harpic"
            harga = 21000
        elif kode_barang[i] == "27":
            jenis = "WPC"
            harga = 14300
        elif kode_barang[i] == '28':
            jenis = "Wipol Cair"
            harga = 11000
        else:
            jenis = 'kode sampai 28 saja'
            harga = 0
        #finist pembersih lantai kebersihan
    elif jenis_barang[i]=="7" or jenis_barang[i]=="VII":#untuk keperluan dapur (1/30)urutan:alatmasak(1/12),bumbudapur(13/24),minyak(25/30)
        #start keperluan dapur
        #start alat masak
        if kode_barang[i]=="1":
            jenis = "teplon maxim"
            harga = 60000
        elif kode_barang[i]=="2":
            jenis = "wajan"
            harga = 52000
        elif kode_barang[i]=="3":
            jenis = "lion star talenan"
            harga = 45000
        elif kode_barang[i]=="4":
            jenis = "rak piring"
            harga = 237000
        elif kode_barang[i]=="5":
            jenis = "pengocok telur"
            harga = 96000
        elif kode_barang[i]=="6":
            jenis = "sendok 1 set"
            harga = 75000
        elif kode_barang[i]=="7":
            jenis = "gelas 6 pcs"
            harga = 30000
        elif kode_barang[i]=="8":
            jenis = "piring 1 pcs"
            harga = 5000
        elif kode_barang[i]=="9":
            jenis = "baskom 1pcs"
            harga = 5000
        elif kode_barang[i]=="10":
            jenis = "cobek"
            harga = 35000
        elif kode_barang[i]=="11":
            jenis = "isi gas elpiji 5 kg"
            harga = 20000
        elif kode_barang[i]=="12":
            jenis = "kompor miyako"
            harga = 124000
        #finist alat masak
        #start bumbu dapur
        elif kode_barang[i]=="13":
            jenis = "sasa santan bubuk 500gr"
            harga = 40000
        elif kode_barang[i]=="14":
            jenis = "sasa penyedap 1kg "
            harga = 35000
        elif kode_barang[i]=="15":
            jenis = "sasa tepung bumbu 850 gr"
            harga = 40000
        elif kode_barang[i] == "16":
            jenis = "bango kecap manis 550ml"
            harga = 18000
        elif kode_barang[i] == "17":
            jenis = "ABC sambal terasi 180 g"
            harga = 30000
        elif kode_barang[i] == "18":
            jenis = "ladaku merica bubuk 100gr"
            harga = 35000
        elif kode_barang[i] == "19":
            jenis = "saori saos teriyaki 10sachet"
            harga = 30000
        elif kode_barang[i] == "20":
            jenis = "saus ABC botol 335ml"
            harga = 35000
        elif kode_barang[i] == "21":
            jenis = "ABC sarden besar 425gr"
            harga = 50000
        elif kode_barang[i] == "22":
            jenis = "tepung terigu kunci biru 1kg"
            harga = 14000
        elif kode_barang[i] == "23":
            jenis = "desaku ketumbar bubuk 1rcg"
            harga = 12000
        elif kode_barang[i] == "24":
            jenis = "royko 1kg"
            harga = 41000
        #finist bumbu dapur
        #start minyak
        elif kode_barang[i] == "25":
            jenis = "bimoli 2lt"
            harga = 25000
        elif kode_barang[i] == "26":
            jenis = "fortune 2lt"
            harga = 26000
        elif kode_barang[i] == "27":
            jenis = "sania 2lt"
            harga = 24800
        elif kode_barang[i] == "28":
            jenis = "filma 2lt minyak jagung"
            harga = 31000
        elif kode_barang[i] == "29":
            jenis = "bimoli 1lt"
            harga = 15000
        elif kode_barang[i] == '30':
            jenis = "tropikal 1lt"
            harga = 16000
        else:
            jenis = 'kode sampai 30 saja'
            harga = 0
        #finist minyak keperluan dapur
    elif jenis_barang[i]=="8" or jenis_barang[i]=="VIII":#untuk buah buahan(1/25) harga perkilo
        #start buah
        if kode_barang[i]=="1":
            jenis = "pir madu"
            harga = 35000
        elif kode_barang[i]=="2":
            jenis = "anggur merah"
            harga = 22000
        elif kode_barang[i]=="3":
            jenis = "nanas"
            harga = 18000
        elif kode_barang[i]=="4":
            jenis = "apel"
            harga = 30000
        elif kode_barang[i]=="5":
            jenis = "semangka"
            harga = 20000
        elif kode_barang[i]=="6":
            jenis = "duku"
            harga = 25000
        elif kode_barang[i]=="7":
            jenis = "rambutan"
            harga = 30000
        elif kode_barang[i]=="8":
            jenis = "lemon "
            harga = 65000
        elif kode_barang[i]=="9":
            jenis = "jeruk"
            harga = 30000
        elif kode_barang[i]=="10":
            jenis = "blueberry"
            harga = 85000
        elif kode_barang[i]=="11":
            jenis = "buah naga"
            harga = 18500
        elif kode_barang[i]=="12":
            jenis = "ceri"
            harga = 75000
        elif kode_barang[i]=="13":
            jenis = "kurma"
            harga = 100000
        elif kode_barang[i]=="14":
            jenis = "melon"
            harga = 15000
        elif kode_barang[i]=="15":
            jenis = "jambu air"
            harga = 16000
        elif kode_barang[i] == "16":
            jenis = "alpukat"
            harga = 20000
        elif kode_barang[i] == "17":
            jenis = "bengkuang"
            harga = 12000
        elif kode_barang[i] == "18":
            jenis = "kelengkeng"
            harga = 45000
        elif kode_barang[i] == "19":
            jenis = "mangga"
            harga = 15000
        elif kode_barang[i] == "20":
            jenis = "manggis"
            harga = 17000
        elif kode_barang[i] == "21":
            jenis = "nangka"
            harga = 16000
        elif kode_barang[i] == "22":
            jenis = "durian"
            harga = 47000
        elif kode_barang[i] == "23":
            jenis = "pepaya"
            harga = 23500
        elif kode_barang[i] == "24":
            jenis = "salak"
            harga = 20000
        elif kode_barang[i] == "25":
            jenis = "stowberry"
            harga = 50000
        else:
            jenis = 'kode sampai 25 saja'
            harga = 0
        #finist buah
    elif jenis_barang[i]=="9" or jenis_barang[i]=="IX":#untuk daging,ayam,ikan urutan:dagingayam(1/6),nuggetayam(7/16),sosisayam(17/21)
        # ,dagingsapi(22/23)dagingikan(24/28)
        #start daging ayam
        if kode_barang[i]=="1":
            jenis = "Ayam Parting Frozen 1 kg"
            harga = 41000
        elif kode_barang[i]=="2":
            jenis = "Fiesta Ayam Fillet Dada Tanpa Tulang dan Kulit 1 kg"
            harga = 65000
        elif kode_barang[i]=="3":
            jenis = "Fiesta Ayam Fillet Dada Tanpa Tulang dan Kulit 1 kg"
            harga = 63000
        elif kode_barang[i]=="4":
            jenis = "Fiesta Paha Utuh 1 kg"
            harga = 45000
        elif kode_barang[i]=="5":
            jenis = "Fiesta Paha Atas 1 kg"
            harga = 48000
        elif kode_barang[i]=="6":
            jenis = "Fiesta Paha Bawah 1 kg"
            harga = 46000
        #finist daging ayam
        #start nugget ayam
        elif kode_barang[i]=="7":
            jenis = "Fiesta Chicken Nugget 500 g"
            harga = 22500
        elif kode_barang[i]=="8":
            jenis = "Fiesta Stikie 500 g"
            harga = 22500
        elif kode_barang[i]=="9":
            jenis = "Fiesta Golden Chicken Ring 500 g"
            harga = 47500
        elif kode_barang[i]=="10":
            jenis = "Fiesta Nugget Zoo 500 g"
            harga = 40500
        elif kode_barang[i]=="11":
            jenis = "Fiesta Happy Star 500 g"
            harga = 23000
        elif kode_barang[i]=="12":
            jenis = "Fiesta Nugget Cheese 123 500 g"
            harga = 40500
        elif kode_barang[i]=="13":
            jenis = "Champ Nugget 500 g"
            harga = 33000
        elif kode_barang[i]=="14":
            jenis = "Champ Nugget Coin 500 g"
            harga = 30500
        elif kode_barang[i]=="15":
            jenis = "Champ Nugget Stick 500 g"
            harga = 33000
        elif kode_barang[i] == "16":
            jenis = "Champ Nugget ABC 500 g"
            harga = 30500
        #finist nugget ayam
        #start sosis ayam
        elif kode_barang[i] == "17":
            jenis = "Fiesta Sausage 300 g"
            harga = 23500
        elif kode_barang[i] == "18":
            jenis = "Fiesta  Sosis Bratwurst 300 g"
            harga = 32000
        elif kode_barang[i] == "19":
            jenis = "Fiesta Sosis Keju 300 g"
            harga = 34000
        elif kode_barang[i] == "20":
            jenis = "Champ Sosis 375 g"
            harga = 29500
        elif kode_barang[i] == "21":
            jenis = "Champ Sosis 150 g"
            harga = 7500
        #finist sosis ayam
        #start daging sapi
        elif kode_barang[i] == "22":
            jenis = "Daging Sapi Beku Import Aus 1 kg"
            harga = 85000
        elif kode_barang[i] == "23":
            jenis = "Daging Sapi Paha 1 kg"
            harga = 81500
        #finist daging sapi
        #start daging ikan
        elif kode_barang[i] == "24":
            jenis = "Ikan Dori 1 kg"
            harga = 44000
        elif kode_barang[i] == "25":
            jenis = "Ikan Tenggiri Jumbo 500 gr"
            harga = 48000
        elif kode_barang[i] == "26":
            jenis = "Ikan Tuna  500 gr"
            harga = 45000
        elif kode_barang[i] == "27":
            jenis = "Ikan Salmon 1 kg"
            harga = 255000
        elif kode_barang[i] == '28':
            jenis = "Ikan Tenggiri Giling 1 kg"
            harga = 100000
        else:
            jenis = 'kode sampai 28 saja'
            harga = 0
        #finist daging ikan dagingayamikan
    elif jenis_barang[i]=="10" or jenis_barang[i]=="X":
        if kode_barang[i]=="1":
            jenis = "Siladex Batuk Pilek 30ml"
            harga = 8500
        elif kode_barang[i]=="2":
            jenis = "Siladex Batuk Pilek 60ml"
            harga = 20000
        elif kode_barang[i]=="3":
            jenis = "Triaminic Batuk Syr 60ml"
            harga = 25000
        elif kode_barang[i]=="4":
            jenis = "OBH Combi Dewasa Rasa Jahe 100ml"
            harga = 17000
        elif kode_barang[i]=="5":
            jenis = "OBH Combi Dewasa Rasa Madu 100ml"
            harga = 18000
        elif kode_barang[i]=="6":
            jenis = "OBH Combi Anak Rasa Jeruk 60ml"
            harga = 15000
        elif kode_barang[i]=="7":
            jenis = "OBH Combi Anak Rasa Madu 60ml"
            harga = 16000
        elif kode_barang[i]=="8":
            jenis = "AnaKonidin 30ml"
            harga = 8000
        elif kode_barang[i]=="9":
            jenis = "AnaKonidin 60ml"
            harga = 13000
        elif kode_barang[i]=="10":
            jenis = "Anakonidin OBH 30ml"
            harga = 9000
        elif kode_barang[i]=="11":
            jenis = "Anakonidin OBH 60ml"
            harga = 14000
        elif kode_barang[i]=="12":
            jenis = "SanaFlu Plus Batuk Tablet"
            harga = 5000
        elif kode_barang[i]=="13":
            jenis = "Bodrex Flu & Batuk PE Tablet"
            harga = 6000
        elif kode_barang[i]=="14":
            jenis = "Bodrexin Flu & Batuk PE Syrup 56ml"
            harga = 12000
        elif kode_barang[i]=="15":
            jenis = "Mixagrip Flu & Batuk Tablet"
            harga = 8000
        elif kode_barang[i] == "16":
            jenis = "Vicks Formula 44 Anak 54ml"
            harga = 18000
        elif kode_barang[i] == "17":
            jenis = "Bodrex Flu & Batuk Berdahak PE Tablet"
            harga = 10000
        elif kode_barang[i] == "18":
            jenis = "Benadryl Batuk Berdahak Syr 50ml"
            harga = 24000
        elif kode_barang[i] == "19":
            jenis = "OBH Combi Batuk Berdahak Rasa Mint 100ml"
            harga = 18000
        elif kode_barang[i] == "20":
            jenis = "Bodrexin Flu & Batuk Berdahak PE Syrup 56ml"
            harga = 12000
        #finist flu&batuk berdahak
        #start demam
        elif kode_barang[i] == "21":
            jenis = "Bodrexin Demam 60ml"
            harga = 12000
        elif kode_barang[i] == "22":
            jenis = "Siantan Demam Berdarah Tablet"
            harga = 37000
        elif kode_barang[i] == "23":
            jenis = "Sari Kurma Sahara"
            harga = 31000
        elif kode_barang[i] == "24":
            jenis = "Pimtrakol kids Demam & Batuk Strawberry"
            harga = 13000
        elif kode_barang[i] == "25":
            jenis = "Procold Flu 6 Strip"
            harga = 4000
        elif kode_barang[i] == "26":
            jenis = "Ultraflu 4 Strip"
            harga = 3500
        elif kode_barang[i] == "27":
            jenis = "Panadol Syrup 60ml"
            harga = 54000
        elif kode_barang[i] == "28":
            jenis = "Panadol Biru Tablet 10 tab"
            harga = 10000
        elif kode_barang[i] == "29":
            jenis = "Panadol Cold Flu Hijau Tablet 10 tab"
            harga = 15000
        elif kode_barang[i] == "30":
            jenis = "Panadol Extra Merah 10 tab"
            harga = 12000
        elif kode_barang[i] == "31":
            jenis = "Paramex Tab 4 Strip"
            harga = 3000
        elif kode_barang[i] == "32":
            jenis = "Sanmol Drop 15ml"
            harga = 22000
        elif kode_barang[i] == "33":
            jenis = "Rohto Fever Patch 2S"
            harga = 13000
        elif kode_barang[i] == "34":
            jenis = "Panadol Anak Tab"
            harga = 14000
        elif kode_barang[i] == '35':
            jenis = "Decolgen tab 4 str"
            harga = 5000
        else:
            jenis = 'kode sampai 35 saja'
            harga = 0
    else:
        jenis = "kode belum update"
        harga = 0


    total= harga * banyak_barang[i]
    total_beli+=total

    print(i+1, jenis,"\n    ", harga,"x",banyak_barang[i],"\t    Rp.",total)

pajak = .1 * total_beli
total_bayar = total_beli + pajak
if total_bayar>=100000:
    hemat = total_bayar * .2
else:
    hemat = total_bayar * 0
totba = total_bayar - hemat
print("Admin :",nm,"\n",499*"-")
print("\t\t Jumlah Bayar = Rp.",total_beli,"\n\t\t Pajak 10%    = Rp.",pajak,"\n\t\t Anda Hemat   = Rp.",hemat,"\n\t\t Total Bayar  = Rp.",totba)
print(500*"-")
#pembayaran
uang=int(input("Uang Anda   : "))
kembali=uang-totba
if uang<=totba:
    kembali = "MAAF UANG ANDA KURANG"
else :
    kembali = kembali

print("Kembali     :",kembali)
print(500*"-","\n\t\t\t",saat_ini,"\n",499*"-")
#Ulangilagi
lagi=input("Apakah Anda ingin Berbelanja Lagi :")
if lagi=="y"or lagi=="Y":
    bj = int(input("Banyak Varian Barang :"))
    print(
        "Jenis Barang :\n 1.sayuran & Umbi-umbian(1/62) 2.Makanan(1/107) 3.minuman(1/53) 4.alat mandi(1/24) 5.kosmetik(1/27)\n "
        "6.Kebersihan(1/28) 7.keperluan dapur(1/30) 8.buah-buahan(1/25) 9.daging,ayam,sosis,ikan(1/28) 10.Obat-Obatan(1/35) 11.Lainnya")
    for i in range(bj):
        menu()


    total= harga * banyak_barang[i]
    total_beli+=total

    print(i+1, jenis,"\n    ", harga,"x",banyak_barang[i],"\t    Rp.",total)

    pajak = .1 * total_beli
    total_bayar = total_beli + pajak
    if total_bayar>=100000:
        hemat = total_bayar * .2
    else:
        hemat = total_bayar * 0
    totba = total_bayar - hemat
    print("Admin :",nm,"\n",499*"-")
    print("\t\t Jumlah Bayar = Rp.",total_beli,"\n\t\t Pajak 10%    = Rp.",pajak,"\n\t\t Anda Hemat   = Rp.",hemat,"\n\t\t Total Bayar  = Rp.",totba)
    print(500*"-")
#pembayaran_ulang
    uang=int(input("Uang Anda   : "))
    kembali=uang-totba
    if uang<=totba:
        kembali = "MAAF UANG ANDA KURANG"
    else :
        kembali = kembali

    print("Kembali     :",kembali)

else:
    exit()
print(500*"-","\n\t\t\t",saat_ini,"\n",499*"-")
print("\t\t Terimakasih dan sampai Jumpa kembali\n\t\t\t\t\t Junior Mart")
print("\tLayanan Konsumen SMS 0812 1067 2585\nContact juniormart@gmail.com \nBarang Yang Sudah Di beli tidak Boleh Di Kembalikan")

# Kelopok 6
#1.M.Raihan Nova Ramzy
#2.Dimas Prasetyo
#3.Ridho Irawan
#4.M.Ilham magribi
#5.Michael S H Gultom
#Finist
