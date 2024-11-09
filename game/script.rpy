# Declare characters used by this game. The color argument colorizes the name of the character.
define cecep = Character("Cecep", color="#CD6247", who_bold=True, who_outlines=[(1, "#000")])
define sudirman = Character("Sudirman", color="#F8DC71", who_bold=True, who_outlines=[(1, "#000")])
define penumpang = Character("Penumpang", color="#EF6C3A", who_bold=True, who_outlines=[(1, "#000")])
define mahasiswa = Character("Mahasiswa", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define anindira = Character("Anindira", color="#B6AAA6", who_bold=True, who_outlines=[(1, "#000")])
define nenek = Character("Nenek Tua", color="#F8DC71", who_bold=True, who_outlines=[(1, "#000")])
define kakek = Character("Kakek Tua", color="#EF6C3A", who_bold=True, who_outlines=[(1, "#000")])
define ibu = Character("Ibu-ibu", color="#FCE52B", who_bold=True, who_outlines=[(1, "#000")])
define suster = Character("Suster",color="#CD6247", who_bold=True, who_outlines=[(1, "#000")])
define dokter = Character("Dokter", color="#B6AAA6", who_bold=True, who_outlines=[(1, "#000")])


style screentext:
    color "#5A4730"
    size 18

label splashscreen:
    scene yellow
    $renpy.pause(1.0, hard=True)
    show splash with dissolve:
        xalign 0.5
        yalign 0.5
    $renpy.pause(3.0, hard=True)
    hide splash with dissolve
    $renpy.pause(2.0, hard=True)
    return

# The game starts here.
label start:
    show screen judul_cerita1
    $ renpy.pause(5.0, hard=True) # Durasi tampilan screen
    hide screen judul_cerita1
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene rumahsakit
    "Terik matahari yang di pagi hari tidak dapat menyelinap masuk area rumah sakit yang tertutup rapat meskipun begitu cahaya disana sangat terang."
    "Tembok putih, aroma herbal yang begitu kuat dan suara jentikan jam bagaikan jantung yang berdebar."
    "Itu semua tidak dapat mencairkan suasana dari ayah dan anak yang kini sedang memiliki suasana yang tegang."
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    screen black
    with dissolve
    jump scene1


label scene1:

    scene rumahsakit
        
    show sudirman 1 at right:
        zoom 0.35
    
    sudirman "Bapa teh geus lemes kieu atuh teu kedah narik Cèp, ai nu ngajagaan bapa saha?\n(Bapak udah lemah gini gausah narik(angkot), Cep. Siapa yang mau ngejaga bapa?)"
    
    show cecep 11 at left:
        zoom 0.35
        
    cecep "Eh atuh apan ekonomi arurang te kieu pa, Lainna ti baheula nèangan gawè nu gajina gedè?\n(Tapi kan ekonomi kita lagi gini, Kenapa gak dari dulucari kerja yang gajihnya besar?)"
 
    sudirman "Tong kitu atuh ka kolot tèh, kieu-kieu gè da artosna halal\n(Jangan gitu ke orang tua, gini-gini juga uangnya halal)" 
    
    cecep "Era abdi tèh, Pak! babaturan mah geus boga usaha gedè, ngan abdi hungkul nu jadi sopir angkot\n(malu saya, Pak, temen temen udah punya usaha besar, cuman saya doang yang jadi supir angkot)" 
       
    "Mendengar perkataan pemuda itu, pria tua yang kini sedang berbaring lemah dihadapannya terlihat berkaca-kaca, meski begitu pemuda itu sama sekali tidak terlihat bersalah akan apa yang telah ia ucapkan." 
    
    show sudirman 1 at right:
        zoom 0.37
    
    sudirman "Acan rejekina, Cèp.\n(Belum rezekinya, Cep)"
    
    show cecep 11 at left:
        zoom 0.37
    
    menu:
        "Males":
            cecep "Hayoh wè lain rezeki! lain rezeki! Geus bilang wèh GAGAL, males pisan ngomong jeung bapa\n(Selalu saja bukan rezeki bukan rezeki, udah aja bilang gagal, males bicara sama bapa)"
            "Sebelum sang ayah mengeluarkan kata-kata cecep langsung mengambil kunci mobil angkot lalu menutup pintu dengan keras dan pergi"
            
        "Alesan":
            cecep "Halah alesan bapak wèh èta mah, matakna mun teu tiasa nèangan duit nu loba tong boga budak! Abdi ayeuna nu hèsè neraskeun ieu gawè!\n(Halah alasan bapak aja itu mah, makanya kalau gak bisa cari uang yang banyak gausah punya anak, sekarang saya yang susah nerusin pekerjaan ini)"
            sudirman "Astagfirullah cèp,"
            "Ketukan pintu terdengar dari luar, sepertinya suster yang biasa menjaga Sudirman. Tanpa melihat reaksi ayahnya, Cecep keluar tanpa bersalaman dengan ayahnya"
        
        "Nya enggeus lah!!!\n(Yaudah iya)":
            "Cecep langsung mengambil kunci mobil dengan amarah didalam benaknya lalu keluar tanpa memberi salam"
    scene black
    with dissolve
    jump scene2
    
label scene2:
    show screen judul_cerita2
    $ renpy.pause(5.0, hard=True)
    hide screen judul_cerita2
    
    scene dalamangkot
    
    "Emosi yang menyelimuti hati Cecep tidak mengubah fakta bahwa pagi ini sangat terang bagaikan langit yang tidak mendukung kondisi Cecep saat ini."
    "Ditambah Cecep tidak terlalu mengenal jalanan yang ada di Bandung yang memperburuk suasana hatinya."
    "Perlahan dia mencoba menghembuskan nafas dan memadamkan emosi dengan melupakan ayahnya yang masih panas dalam hatinya dan memulai perjalanannya."
    
    show cecep 1 at right:
        zoom 0.4
    
    cecep "Bisa lah bisa"
    
    # HALAMAN TUTORIAL / PANDUAN MINIGAMES
    
    #lanjutan cerita
    
    "Menit berlalu , beberapa penumpang menaiki angkotnya. Karena raut wajah Cecep yang memancarkan hawa amarah beberapa penumpang segan dan menanyakan kondisinya."
    
    scene dalamangkot
    
    show penumpang 1 at left with moveinleft:
        zoom 0.4
    
    penumpang "Leu badè narik kang? (Ini bakal narik mas?)"
    
    "Cecep mungkin tidak sengaja tapi intonasi suaranya terdengar ketus"
    
    cecep "Muhun (iya)"
    
    "setelah penumpang lainnya naik, Cecep memulai mengemudi."
    
    #MINI GAMES 1

    scene halte
    "Seorang mahasiswa diam di Halte, terlihat earphone ditelinganya teriknya matahari secara tidak sengaja memperlihatkan tekstur wajahnya."    
    "Gayanya seperti mahasiswa pada umumnya. Di tangannya terbuka sebuah buku bertulisan bahasa asing."
    "Mungkin karena terlalu fokus pada bukunya Cecep kebingungan dia mau naik atau engga."
     
    menu:
        "Bunyi klakson":
            "Tersentak, Mahasiswa itu menjatuhkan bukunya dan dengan buru-buru membuka kedua earphonenya, tangannya berada didadanya dan nafasnya tak karuan."
            "Memalingkan wajahnya ke kanan dan kekiri dan akhirnya bertuju pada angkot hijau didepan matanya"
        
        "Memanggil sambil teriak":
            show cecep 1 at left:
                zoom 0.4
        
            cecep "punten, kang (permisi, Mas)"
        
            show mahasiswa 1 at right:
                zoom 0.4
        
            mahasiswa "......."
            
            "Mahasiswa itu masih hanyut dalam dunianya sendiri, Cecep mencoba menaikkan suaranya."
        
            cecep "Kang!"

            mahasiswa "...."
            
            "Tidak bergerak sama sekali, Cecep sedikit kesal dan mulai berteriak"
            
            cecep "Woi!!"
            
            "akhirnya mahasiswa itu meluruskan pandangannya dan mulai melepas earphonenya"
        
        "Lempar dengan kertas remuk":
            "Cecep meremukan kertas kecil yang tidak terpakai dan melemparkannya pada mahasiswa itu."
            "Kertas itu mendarat di bahunya. Mahasiswa itu tersentak dan kaget dan *GUBRAKK* dia terjatuh lalu langsung bangun dengan wajah yang mulai memerah karena malu."
            
    scene halte
        
    show cecep 1 at left:
            zoom 0.4
                
    cecep "Hampura Kang, badè naik?\n(Permisi Mas, mau naik?)"
        
    show mahasiswa 1 at right:
            zoom 0.4
        
    mahasiswa "Oh, iya."
            
    "Mahasiswa itu membereskan barangnya lalu mulai menaiki angkotnya dengan perasaan malu, apalagi di dalam angkot menjadi tontonan penumpang lainnya"
    "Penumpang lain menanyakan mengapa dia tetap kuliah pada hari minggu dan ternyata mahasiswa itu sedang ikut acara seminar yang diadakan oleh dosennya"
    "Sepanjang perjalanan mahasiswa itu kalem dan tidak berekspresi namun sesekali melihat keluar jendela, ekspresinya berubah saat melewati beberapa tempat dan mulai memfotonya dengan kameranya. Sisa perjalanan dia larut pada buku dan earphonenya."
    "Angkot mulai melewati kampus dengan bangunan orange yang begitu terang, kampus Itenas."
        
    show mahasiswa 1 at left:
        zoom 0.4
            
    mahasiswa "KIRI"
        
    "Cecep meminggirkan angkotnya dan mahasiswa itupun turun. Karena respon mahasiswa itu sepertinya tidak terlalu menggunakan bahasa sunda akhirnya Cecep menggunakan bahasa Indonesia"

    show cecep 1 at right:
        zoom 0.4
            
    cecep "lain kali mah jangan baca buku kalau lagi nunggu angkot."
        
    mahasiswa "Eh,, iya, Kang"
        
    "sembari malu, mahasiswa itu memasuki gerbang kampus dengan wajah yang memerah karena kejadian yang mungkin tidak akan dia lupakan"
    
    #minigames 2  
    
    scene terminal
    
    "Terik matahari sudah tidak memancarkan kehangatan namun sudah bagaikan tusukan yang menyengat. Langit berwarna biru dan awan yang hanya sedikit sulit untuk menutupi matahari."
    "Jalanan semakin riuh tak karuan, suara tanpa irama sudah layaknya teriakan yang menguras energi."
    "Saat ini Cecep berada di terminal Cicaheum, dia bersender di angkotnya. Sebotol air putih yang kini sudah terkuras setengahnya. "
    "Keringatnya kini membasahi wajah dan rambutnya. Sesekali dia mengibaskan benda tipis apapun di depan lehernya untuk menyejukan suhu tubuhnya."
    "Cecep sudah lelah dan hendak tidur sejenak sampai akhirnya ada suara perempuan yang memanggil, awalnya dia kira bukan bertuju padanya sampai akhirnya wanita itu menghampirinya."
    
    show anindira 1 at left with moveinleft:
        zoom 0.4
    
    anindira "Selamat siang, Mas"
    
    "Dari logatnya cecep sudah tau dia buka asli dari Bandung"
    
    show cecep 1 at right:
        zoom 0.4
        
    menu:
       "Siang, ada apa, Teh?":
            cecep "Siang, ada apa, Mba?"
       "Hah?":
            cecep "Hah?"   
       "Kenapa?":        
            cecep "Kenapa?"
    
    show anindira 1 at left:
        zoom 0.4
        
    anindira "Sebelumnya perkenalkan saya Anindira. Jadi gini, Mas. Saya kebetulan baru pertama kali ke Bandung dan sangat asing sama jalanan dan tempat-tempatnya." 
    anindira "Masnya berkenan gak nganter saya selagi masnya narik penumpang?"
    
    show cecep 1 at right:
        zoom 0.4
    
    cecep "Oh, gak bisa, Teh. Angkot di sini mah punya rutenya masing-masing, yang berbeda-beda. Paling nanti teteh turun di mana terus lanjut naik angkot lain yang rutenya berbeda."
    cecep "Nanti Teteh tinggal bedain aja warna angkot sama nomer angkotnya"
    
    anindira "Hmm... Tapi saya kan gak tau harus turun dimananya, Mas."
    anindira "Yaudah gimana kalau gini aja, saya bayar khusus deh, asal Masnya mau nganter saya keliling Bandung. Gimana?"
    
    "Belum sempat menyelesaikan kalimatnya, Anindir mengambil dompetnya dan mengeluarkan selembar uang kertas merah."
    
    anindira "Nanti kalau perjalanannya lebih jauh dari perkiraan, saya tambah lagi deh"
    
    menu:
    
       "Hayu lah, Gas!":
           cecep "Hayu lah, Gas!"
       "Boleh aja kalo gini, Teh.":
            cecep "Boleh teh"    
       "Bisa banget atuh euy kalau gitu mah":        
            cecep "Bisa banget atuh euy kalau gitu mah."
    
    scene terminal
    
    "Andira pun menaiki angkotnya dan Cecep dengan semangat mengemudikan angkotnya untuk melanjutkan perjalanannya tanpa peduli dengan rute angkotnya dan memulai berkeliling Bandung."
    
    scene black
    with dissolve
    jump scene3
    
label scene3:
    show screen judul_cerita3
    $ renpy.pause(5.0, hard=True)
    hide screen judul_cerita3
    
    scene dalamangkot

    #minigames 3
    
    #lanjut cerita
    
    "Selama perjalanan keheningan menyelemuti mereka, meskipun suara dari jalanan menaburkan bising yang tidak enak pun tidak mampu melepaskan keheningan mereka"
    "Akhirnya meskipun Cecep males untuk melakukan konversasi tapi karena sudah dibayar akhirnya Cecep-pun memecahkan keheningan itu."
    
    show cecep 1 at right:
        zoom 0.4
    
    cecep "Masih sekolah, Teh? Atau udah kerja?"
    
    show anindira 1 at left:
        zoom 0.4
    
    anindira "Kuliah, Mas"
    
    cecep "Ooh, kuliah dimana"
    
    anindira "di ISI, Mas. Yogyakarta"
    
    cecep "ELEUH SIA MENI TEBIH, KADIEU SORANGAN?"
    
    "Tidak mendengar jawaban, Cecep sekejap menengok kearah Anindira dan wajahnya terlihat mengerucutkan dahinya, akhirnya Cecep sadar saking kagetnya dia tidak sadar dia menggunakan bahasa Sunda."
    
    cecep "Eh maaf, Teh. Maksudnya, jauh banget, Teh, kesini sendiri?"
    
    anindira "Iya, Mas. Kebetulan sekalian buat cari referensi untuk skripsi saya"
    
    cecep "Waduh hebat, dari jurusan apa emang, Teh?"
    
    anindira "Seni murni, mas"
    
    cecep "Ohh anak seni ya. Hebat-hebat."
    cecep "Kalau saya sih engga bisa kayak gitu, punya bapak bukannya nyari uang buat bayar sekolah saya malah keasikan jadi supir angkot, jadi uangnya kurang buat sekolah."
    cecep "Teteh mah pasti ayahnya ngedukung ya?"
    
    "mendengar omongan cecèp ekspresi Anindira menjadi kecut, Cecep sadar kalau dia salah ngomong"
    
    "Akhirnya keadaan kembali menjadi canggung. Untuk keluar dari suasana tidak enak ini, cecèp kembali dengan topik yang berbeda."
    
    menu:
        "Mau coba ke jalan sini, Teh?":
            anindira "Jalan kesitu kemana ya?"
        
        "Mau mulai dari mana dulu ini?":
            anindira "Menurut, Mas, enaknya dari mana dulu? Saya belum tau jalan sama sekali"
        
        "Teteh ada rekomendasi tempat?":
            anindira "Gak tau sih, Mas. Masnya ada rekomendasi tempat yang bagus?"
            
    cecep "Ke jalan sana banyak tempat museum-museum, Teh, tadi kebetulan ada mahasiswa suka foto-foto pas ngelewat kesana, mungkin tetehnya bakal tertarik"
    anindira "Oh, boleh deh, Mas."
            
    "Cecep mengendarai angkotnya menuju jalan DipenogorO."
    "Tiba di Jalan Diponegoro, kondisi disana macet karena ramainya tempat wisata, akhirnya mereka berhenti dulu untuk melihat lapangan Gasibu."
    
    scene lapangangasibu
    #suasana riuh
    
    "Disana terlihat lapangan lari yang sangat luas, diwarnai biru muda dan biru tua. Ditengah-tengah lapangan ada bendera Indonesia yang berkibaran."
    "Di pinggir lapangan terdapat banyak pohon dan tempat duduk untuk beristirahat. Adapun perpustakaan tertutup di bagian atas"
    
    show cecep 1 at left with moveinleft:
        zoom 0.4
    
    cecep "Ini lapangan Gasibu, Teh, kalau pagi mah disini penuh pisan. Orang dari daerah yang jauh juga banyak yang kesini buat olahraga pagi. Sering juga dijadikan wisata sama anak sekolahan."
    
    show anindira 1 at right with moveinright:
        zoom 0.4
    
    anindira "Ohh gitu ya, Mas. Lumayan luas ya lapangannya."
    
    "Anindira berjalan sambil memfoto sekitaran dengan kegirangan, kamera ditangannya terlihat berat namun karena pemandangan lapangan begitu indah, ia tetap terlihat gesit."
    
    anindira "Wah, saya suka banget tempatnya."
    
    anindira "(Tempat kek gini apa bagusnya coba.)"
    
    "Setelah mengambil banyak foto, Anindira mengajak Cecep ke tempat lainnya."
    
    anindira "Ayo pindah ke bangunan situ, Mas!"
    
    "Mereka pindah ke area Gedung Sate"
    
    scene gedungsate
    
    show cecep 1 at left with moveinleft:
        zoom 0.4
        
    cecep "Ini mah tau lah ya, Teh? Kalau ada Bandung pasti di gambarinnya bangunan ini, Gedung sate."
    cecep "Namanya kok gitu ya, apa cuman gegara atapnya kayak sate ya? Itu ada berapa tusuk lagi"
    
    show anindira 1 at right with moveinright:
        zoom 0.4
    
    anindira "Ada 6 tusuk tuh, Mas!"
    
    anindira "6 tusuk sate ini melambangkan 6 juta Gulden yang dipakai untuk membangun gedung ini waktu tahun 1920-an."
    
    anindira "Bangunannya dibuat sebagai pusat administrasi pemerintahan Hindia Belanda dengan nama Gouvernements Bedrijven yang berarti Kantor Pemerintahan Daerah."
    anindira "Gaya arsiteknya juga memiliki unsur art deco!"
    
    "Cecep terdiam terpukau"
    
    menu:
        "Wah, saya kalah sama orang luar Bandung":
            cecep "Wah, saya kalah sama orang luar Bandung"
        "Waduh, tau banyak ya, Teh? Saya jadi malu orang Bandung asli tapi gak tau, hehe. Makasih infonya, Teh.":
            cecep "Waduh, tau banyak ya, Teh? Saya jadi malu orang Bandung asli tapi gak tau, hehe. Makasih infonya, Teh"
        "Oh gitu ya. Maaf malah jadi teteh yang jelasin.":
            cecep "Oh gitu ya. Maaf malah jadi teteh yang jelasin."
        
    anindira "Hehe, gapapa dong, Mas. Sama-sama belajar!"
    
    scene gedungsate
    
    "Setelah bercerita lebih banyak, Anindira meminta Cecep untuk menfotonya di depan gedung tersebut,"
    "Karena suasana lumayan ramai sedikit susah untuk berfoto tanpa ada orang lain yang ikut terfoto."
    
    "Matahari makin menyengat namun hal itu tidak mengkuras semangat Anindira untuk berjalan."
    "Tak jauh dari Gedung sate Cecep mengajak Anindira untuk pergi ke Museum Pos Indonesia, suasana selama perjalanan kesana agak sedikit sejuk karena dikerumuni banyak pepohonan."
    "Setelah jalan beberapa saat, terlihatlah gedung museum pos namun ada beberapa penjaga di gerbangnya membuat Anindira ragu-ragu untuk mendekatinya."    
    
    scene museumpos
    
    show cecep 1 at left with moveinleft:
        zoom 0.4
        
    cecep "Oh iya, ini hari Minggu ya. Kalau hari Minggu tutup ini, Teh. Kalau mau ke sini hari kerja aja, gratis"
    
    show anindira 1 at right:
        zoom 0.4
    
    anindira "Yahh, padahal mau lihat barang-barang antiknya, saya baca dari buku katanya museum ini awalnya memang kantor pos asli dan pertama tahun 1884."
   
    anindira "Tapi, seiring berjalannya waktu kantor ini beralih fungsi jadi kantor telekomunikasi Hindi Belanda, dan setelah merdeka kantor ini diambil alih lagi oleh pemerintah Indonesia."
   
    anindira "Kalau dilihat dari gaya bangunannya sih, punya gaya arsitektur Indische Empire yang khas dengan ciri khas bangunan kolonial Belanda."
    
    anindira "ya kan mas?"
   
    menu:
       "Ya mana saya tau, kok tanya saya":
         cecep "Ya mana saya tau, kok tanya saya"
       "i-iya\n(bohong)":
         cecep "i-iya\n(bohong)"
     
    "Karena terlalu larut dengan bangunannya, Anindira tidak memperdulikan jawabannya Cecep"   
    "Mereka tidak lama berada di Museum Pos karena tutup, mereka melanjutkan perjalanannya menuju Museum Geologi namun ada yang menarik perhatian Anindira"    
    
    scene tamanlansia
    
    "Terpaku pada nama Lansia, Anindira tidak melihat satupun pengunjung lanjut usia didalamnya, disamping itu hawanya sangat sejuk karena saking banyaknya pepohonan dan tumbuhan bahkan mataharipun sulit untuk menyelinap kedalamnya."
    "Di dalamnya ada banyak tempat duduk, ada juga sungai kecil dihiasi dengan jembatan. Ada segerombolan anak sekolahan ada juga pengunjung berbagai umur."
    "Lokasi nya dikelilingi oleh pedagang kaki lika dengan aneka khas kuliner Indonesia, kebanyakan dari Bandung."
    
    show anindira 1 at right with moveinright:
        zoom 0.4
        
    show cecep 1 at left:
        zoom 0.4
        
    anindira "Ini yang bukan lanjut usia juga boleh masuk, Mas?"

    cecep "Setau saya memang dibuat untuk orang-orang yang lanjut usia. Tapi banyak juga yang datang buat dijadikan wisata."
    
    "Mereka memasuki Taman Lansia"    
    
    anindira "Sejuk banget disini, istirahat dulu disini kali ya, Mas?"
    
    cecep "Boleh, Teh."
    
    "Setelah duduk-duduk sebentar, Anindira gantian memulai percakapan dengan Cecep."
    
    anindira "Ohya, Mas. Daritadi masnya belum ngasi tau namanya?"
    
    cecep "Oh, bener juga. Nama saya, Cecep, Teh."
    
    anindira "Ah, Mas Cecep ya. Bandung banget namanya, hehe."
    
    cecep "Ya gimana lagi atuh, Teh. Orang asli Bandung."
    
    anindira "Hehe... Ohya, Mas Cep. Mau Cendol gak? Saya belikan?"
    
    menu:
        "Boleh deh kalau gitu, makasih ya":
            cecep " Boleh deh kalau gitu, makasih ya"
        "Hehe, kalau ga ngerepotin mah gaskeun aja.":
            cecep "Hehe, kalau ga ngerepotin mah gaskeun aja."
            
    "Setelah itu Anindira pergi ke pedagang cendol di dekat taman. Dari dulu ia penasaran dengan rasanya Cendol"
    "Setelah itu mereka berteduh di salah satu dudukan di dalam Taman Lansia."
    
    anindira "Akhh, dah lama banget saya pingin minum ini. Ternyata seenak itu ya."

    cecep "Iya dong, apalagi kalau gratis, hehe."
    
    "20 menit telah berlalu minuman merekapun telah habis. Kemudian, dari depan pandangan mereka, mereka melihat bis yang parkir di depan Museum Geologi"
    "Anindira agak heran karena banyak sekali bis yang berparkir di parkirannya bahkan ada di pinggir trotoar."
    
    show anindira 1 at right:
        zoom 0.4
    
    anindira "Itu ada acara apa ya, Mas Cep?"
    
    show cecep 1 at left:
        zoom 0.4
    
    cecep "Oh, itu mah dah biasa, Teh. Banyak anak sekolahan yang study tour di sana. Banyak juga keluarga rombongan yang ke sana."
    
    anindira "Aduh, kayaknya penuh banget ya. Mana bayar lagi."
    
    cecep "Iya, Teh. Maklum hari Minggu"

    "Meskipun Anindira ingin sekali masuk kesana, dia tidak terlalu menyukai keramaian karena hal itu membuatnya tidak fokus untuk melihat keindahan museum tersebut."
    
    anindira "Yaudah deh, lihat dari sini aja."
    
    anindira "Dilihat-lihat, bangunan bersejarah memang beda ya sensasinya walaupun sudah sering direnovasi"
    
    anindira "Nuansa Art Deconya kerasa banget, saya lihat dari buku museum ini diarsiteki oleh Ir Menalda van Schouwenburg."
    
    cecep "Emang dulunya museum itu dipakai untuk apa, Teh?"
    
    "Anindira tersenyum kearah Cecep karena dia tau Cecep sudah mulai tertarik dan antusias dalam mengetahui sejarah."
    
    anindira "Pada masa Hindia Belanda sekitar Tahun 1929 sebuah dinas pertambangan menginginkan sebuah tempat untuk menyimpan hasil penyelidikan pertambangan yang mereka lakukan."
    anindira "Namun, pada Perang dunia ke II tempat ini dijadikan markas angkatan udara dan semua koleksi dipindahkan ke Gedung Dwiwarma."
    anindira "Akhirnya, pada kemerdekaan Indonesia gedung ini diambil oleh pengelolaan Djwatan Tambang dan Geologi."

    cecep "Wah. Epices saya."
    
    anindira "Haha, speechless toh maksudnya?"
    
    cecep "Iya, itu, hehe."
    
    "Anindira terlihat senang dan bangga karena bisa bercerita banyak ke Cecep."
    "Setelah beberapa menit, akhirnya mereka kembali menaiki angkot untuk melanjutkan perjalanan."

    scene black
    with dissolve
    jump scene4
    
label scene4:
    show screen judul_cerita4
    $ renpy.pause(5.0, hard=True)
    hide screen judul_cerita4
    
    scene dalamangkot
    #suasana normal
    
    "Saat hendak berangkat, terdapat seorang wanita yang sudah lanjut usia menghampiri mereka"
    "Wanita itu mengenakan Kebaya simpel dengan selendang yang ditalikan pada barang bawaan dipunggungnya. Wanita itu agak membungkuk dan disebelah tangan kanannya membawa ember kosong."
    
    show nenek 1 at left with moveinleft:
        zoom 0.4
        
    nenek "Punten kasèp geulis, tiasa ngiring sakedap teu nya? Abdi badè ka Braga. \n(Permisi ganteng dan cantik, bisa ikut sebentar tidak? Saya mau ke braga)"
    
    show cecep 1 at right:
        zoom 0.4
    
    cecep "Eh aya naon kitu, Bu?\n(Eh, Ada apa, Bu?)"
    
    nenek "Abdi bade icalan diditu, loba jelema ti Jakarta, bisi lakuna di ditu, tulungan ibunya, Kasep.\n(Saya mau jualan disana, banyak orang dari Jakarta, mungkin aja bisa laku disana, tolong ibu ya?)"
       
    "Tak tega dengan wanita itu, Cecep berdiskusi dulu kepada Anindira. Dia dengan senang hati membolehkan ibu itu untuk ikut menumpang pada perjalanan."
    
    cecep "Mangga bu, asup wè.\n(Silakan, Bu. masuk aja.)"
    
    nenek "Hatur nuhun pisan nya, Kasèp... Geulis....\n(Makasih banyak ya, ganteng... cantik....)"
    
    scene dalamangkot
    
    "Cecep membantu memasukan barang ibu itu yang lumayan berat ke dalam angkot. Kemudian, Anindira menyadari"
    "Yang dibawah ibu itu adalah minuman kuliner berupa jamu yang saat ini sudah jarang ditemukan."
    
    show anindira 1 at right:
        zoom 0.4
    
    anindira "Eh, itu jamu, Bu?"
    
    show nenek 1 at left:
        zoom 0.4
    
    nenek "Iya, Neng. Mau coba?"
    
    anindira "Wah. Boleh, Bu. Penasaran sama rasa jamu di Bandung"
   
    "Anindira meminum segelas jamu pemberian wanita tua itu dan merasa sangat puas dengan rasanya."
    
    anindira "Enak, Bu. Gak beda jauh ya ternyata dari yang ada di Jogja."
    
    nenek "Iya atuh, Neng. Namanya juga jamu. Neng dari Jogja ta?"
    
    anindira "Iya atuh, Neng. Namanya juga jamu. Neng dari Jogja ta?"
    
    anindira "Omong-omong, Bu. Ibu namanya siapa?"
    
    nenek "Nama ibu, Aida, Neng"
    
    anindira "Ah… Salam kenal ya, Bu."
    
    "Setelah berkenalan dengan wanita tua itu, mereka pun melanjutkan perjalanannya menuju Braga."
    
    #MINIGAMES 4
    
    "Matahari mulai mereda, namun hangatnya suasana pada sebuah angkot berwarna hijau terasa seakan tidak akan pernah mereda, banyak tawa dan candaan yang mereka keluarkan."
    
    "Sebatas perbedaan bahasa daerah tidak menjadi halangan bagi mereka untuk akur sepanjang perjalanan macam-macam bahasan mereka obrolkan mulai dari kisah penuh tawa sampai penuh kesedihan."
   
    scene dalamangkot
    
    show nenek 1 at left:
        zoom 0.4
    
    nenek "Meni hèsè nèangan artos di jaman ayeuna tèh, warga tèh geus teu hayang jeung dahareun nu tradisional tèh, padahal mah dahareun tradisional jauh leuwih sehat.\n((Susah sekali mencari uang di jaman sekarang, warga udah gak mau sama makanan tradisional, padahal jauh lebih sehat.)"

    #ekspresi sedih
    nenek "Ungga dinten meni sepi dagangan abdi teh. \n (Tiap hari sepi dagangan saya.)"    
    
    show cecep 1 at right:
        zoom 0.4
    
    cecep "Nya rèk kumaha deui atuh, Bu, jaman leuwih resep ka dahareun ti kulon.\n (Ya mau gimana lagi atuh, Bu, jaman sekarang mah banyak yang suka makanan dari barat.)"

    #ekspresi sedih
    nenek "He eh jabaning pangaosna meuni awis jiga kunyit keur ngolah jamu abdi.\n (Iya ditambah harganya sangat mahal kayak kunyit buat ngolah jamu saya)"    
    
    hide nenek
    with dissolve
    
    "Sedih dengan keadaan ekonomi wanita tua itu, Cecep sekejap mengingat ayahnya. Namun hal itu langsung dipudarkan oleh suara Anindira yang kegirangan melihat sebuah bangunan."
    "Anidira menunjukan jarinya pada bangunan putih bertulisan De Driekleu"
    
    show anindira 1 at right:
        zoom 0.4
        
    #ekspresi terkejut
    anindira "Berhenti dulu, Mas Cecep!"
 #Menampilkan latar belakang, Gedung Tiga Warna, di dalam Angkot
    
    scene gedungtigawarna
    
    show cecep 1 at left:
        zoom 0.4
    
    #ekspresi terkejut
    cecep "Naon, Teh!"
    
    "Cecep dan Bu Aida terlihat sama-sama penasaran, karena Anindira terlihat sangat senang mendengar pertanyaan dari Cecep"
    
    show anindira 1 at Position(xpos=350,ypos=220) behind nenek:
        zoom 0.4
    
    #ekspresi excited
    anindira "Ini Gedung De Driekleur, atau sering disebut Gedung tiga warna"
    
    #ekspresi berpikir
    anindira "Dulu ini gedung buat nyebarin berita proklamasi kantor berita Domei yang awalnya milik Jepang, tapi diambil alih sama pejuang proklamasi dari Bandung."
    
    #ekspresi bingung
    cecep "Oh, jadi berita kemerdekaan disebarkan pake gedung ini?"
    
    #ekspresi excited
    anindira "Benar sekali!"
    
    "Anindiri menjawab sambil memfoto bangunan itu dengan buru-buru karena mereka akan memulai perjalanannya kembali."

    #ekspresi default
    anindira "Okehh, udah. Maaf ya, Mas Cecep, Bu Aida. Hehe."    
    
    "Kemudian, mereka memulai perjalanan kembali. Anindira banyak sekali membicarakan bangunan-bangunan yang mereka lewati."
    
    #ekspresi berpikir
    anindira "Oh, itu tadi kita ngelewatin Taman Sejarah Bandung ya?"
    
    #ekspresi default
    cecep "Iya, Neng. Kok tau?"
    
    #ekspresi excited
    anindira "Tau dong! Kalau gak salah itu dulu parkiran DPRD Bandung kan? Cuman oleh Ridwan Kamil dijadiin taman 2017 kemarin."
    
    #ekspresi bingung
    cecep "(Eh, emang iya? Kok aku gak tau ya.)"
    
    scene taman
    
    show anindira 1 at right:
        zoom 0.4
    
    #ekspresi terkejut
    anindira "Eh, itu tadi Taman Balai Kota Bandung, ya? Duh, kenapa nggak berhenti, Mas!"
    
    show cecep 1 at left:
        zoom 0.4
    
    #ekspresi default
    cecep "Mana saya tau atuh, Neng..."
    
    anindira "Taman tadi itu taman paling indah menurut saya. Tamannya kayak labirin, ditambah ada patung Dewi Sartika, dan penampilannya yang-"
    
    show nenek 1 at Position(xpos=350,ypos=220) behind cecep:
        zoom 0.4
    
    "Perkataan Anindira terpotong karena tersadar dengan tatapan kedua orang didepannya. Dia sadar dari tadi dia berbicara dengan keasikan dunianya sendiri"
    "Tanpa memikirkan kerisihan yang mungkin dirasakan oleh Cecep dan wanita tua itu. Namun pemikiran negatif itu tersingkirkan oleh perkataan wanita tua itu"
    
    #ekspresi default
    nenek "Masyaallah geulis, meuni pinter pisan\n(Masyaallah, Cantik, sangat pintar sekali.)"
    nenek "Nyaho kabèh gedung jeung tempat ti Bandung, arurang urang Bandung gè teu tiasa jiga ènèng\n(Semua gedung dan tempat di Bandung hafal, kita orang Bandung juga gak bisa kayak mbak)"
    
    "Malu dengan pujian Bu Aida, Anindira pun tersipu malu. Wajahnya merah layaknya sebuah tomat"
    
    #ekspresi senyum tipis
    cecep "Neng. Tuker kepala yok!"
    
    #ekspresi malu
    anindira "Diam gak kamu, Mas!"
    
    "Setelah itu, Anindira menjadi agak pendiam, karena terlanjur malu dengan pujian dua orang itu."
    "Hingga tak terasa, mereka tiba di Braga."
    
    scene black
    with dissolve
    
    scene braga
    #suasana riuh
    
    "Setelah perjalanan yang lumayan panjang sampai juga di Braga yang akhirnya wanita tua itu meminta untuk turun dan berterima kasih. Mereka pun berpisah dengan damai."
    "Matahari sudah semakin tenggelam dan pandangan warna menjadi warna sore yang hangat. Anindira mengajak Cecep untuk berkeliling braga yang sangat ramai."
    "Awalnya cecep menolak karena tidak punya uang untuk jajan disana, namun karena Anindira bersikeras untuk mengajaknya dengan tawaran akan mentraktir akhirnya Cecep pun ikut."
    "Anindira membeli banyak jajanan kuliner Bandung seperti Batagor, Awug, dan baso tahu. Sedangkan Cecep menikmati apa pun yang Anindira tawarkan"
    
    show anindira 1 at left:
        zoom 0.4
        
    anindira "Mas, paling suka kuliner apa?"
    
    show cecep 1 at right with moveinright:
        zoom 0.4
    
    menu:
        "Awug":
            anindira "hmm setuju sih, manisan enak banget, banyak banget kelapanya, saya jadi tau perpaduan kelapa dan gula merah seenak ini"
        
        "Batagor":
            anindira "SETUJU BANGET, apalagi saus kacangnya, mantap!!!"
        
        "Baso Tahu":
            anindira "Oke sih menurut saya, cuman saya gak suka paria-nya karena terlalu pait"
   
  
    "Setelah makan dan berbincang tentang kuliner mereka pun melanjutkan perjalanannya menuju alun-alun bandung" 
    
    scene black
    with dissolve
    jump scene12
    
label scene12:
    
    scene dalamangkot
    
    "Hari semakin larut suasana hangan kini bersapaan dengan sejuknya warna ungu disaat sore menjelang malam, mereka melaju dengan keheningan karena sudah lumayan lelah, Anindira sibuk melihat foto-foto yang sudah dia ambil."
    "suatu saat diperjalanan cecep melihat seorang kakek yang melambaikan tangan kearah angkotnya, cecepun mengemudikan angkotnya kepinggir dan berhenti membuat Anindira kebingungan dan menaruh kameranya."
    "Berdirilah seorang kakek tua. Dia memakai peci dengan pakaian kemeja batik dan celana hitam yang longgar, dia menggunakan tongkat untuk membantunya berdiri"
    
    show cecep 1 at right:
        zoom 0.4
        
    cecep "Kunaon pak?\n(kenapa pakk?)"
    
    show kakek 1 at left:
        zoom 0.4
    
    kakek "Mayar na sabaraha\n(Bayarnya berapa?)"
    
    cecep "eh teu kedah pak, sakalian abdi gè badè kaditu\n(eh gausah pak, sekalian saya juga mau kesana)"
    hide cecep with dissolve
    
    show dalamangkot
    
    "Kakek tua itupun dibantu dengan Anindira untuk memasuki angkot tersebut."
    "Selama perjalanan keheningan diisi denga storytelling milik Kakek tua itu, ternyata kakek tua ini meskipun terlihat sudah lemah tapi energi dalam berceritanya seperti kembali pada masa mudanya yang penuh energi sampai Anindira pun terpukau dan mendengarnya dengan penuh ketertarikan." 
    "Mengetahui Anindira tidak bisa memakai bahasa sunda akhirnya kakek tua itu bercerita menggunakan bahasa Indonesia"
    
    show kakek 1 at left:
        zoom 0.4
        
    kakek "dulu mah disini teh gaada yang kayak gini apa yang anak muda suka bilang? Instagramable? Pokoknya eta. Makin kesini tempat - tempat disini bukan orang bandung yang terlihat, tapi orang jakarta jadi we macet pisan."
    
    "Jalanan mulai menjadi sangat padat terutama diwilayah Museum Asia Afrika, Kakek tua itu tidak melewatkan kenangannya dengan museum itu"
    
    kakek "menurut kalian barudak, mengapa di Bandung loba gedung gedung bersejarah?"
    
    show anindira 1 at right:
        zoom 0.4
    
    anindira "karena dulu kota Bandung awalnya mau dijadikan kota Batavia?"
    
    kakek "Nah betul"
    
    scene dalamangkot
    
    "Kakek tua itu berpaling dan menatap cecep"
    
    show kakek 1 at left:
        zoom 0.4
    
    kakek "naha pinter awèwè gening, lalaki na teu nyaho ieu tèh?\n(kenapa pinter yang perempuan? Laki-lakinya gak tau ini teh?)"

    "Cecep memalingkan wajah sambil tersenyum malu karena memang dia tidak tahu apa apa mengenai sejarah"    
    
    kakek "dibangunnya gedung gedung bersejarah karena dulu pemerintah Hindia Belanda yang pengen pindah ke Bandung cuman gagal karena adanya perang dunia ke dua jadi mereka teh gak mampu meneruskan pembanguannya"
    kakek "Nah setelah perang dunia, berkumpul lah negara negara lain disini, Indonesia sebagai tuan rumah"
    
    scene black
    with dissolve
    jump scene13
    
label scene13:
    
    scene alunalunbandung
    #suasana sejuk(menjelang malam hari)
    
    "Setelah sesampainya di Alun-alun Bandung Kakek tua itu dan kedua lainnya ikut turun, sebelum kakek tu itu turun dia membungkuk dan berterima kasih"
    "Cecep langsung meluruskan posisi kakek tua itu dan meyakinkan Kakek tua itu untuk tidak berterima kasih dan hanya ingin membantu. Mereka memandangi Kakek tua itu yang semakin menyusut dari pandangan."
    
    show anindira 1 at left with moveinleft:
        zoom 0.4
        
    anindira "Kakek yang penuh energi untuk seumuran itu"
    
    "Cecep tertawa kecil menanggapinya"
    
    show cecep 1 at right:
        zoom 0.4
    
    cecep "Kau benar, semoga usianya dipanjangkan dan dapat menginspirasi pemuda era sekarang"
    
    "Anindira tersenyum hangat memandang Cecep"
    
    anindira "waw, saya tidak tahu mas segitu menghormatinya, apakah beliau mengingatkanmu pada seseorang?"
    
    "Seketika senyuman Cecep memudar dan ingatan seseorang yang tidak mau dia ingatpun muncul dalam benaknya, segera ia menepisnya."
    
    cecep "Sudahlah, mari berkeliling"
    
    scene alunalunbandung
    
    "Merekapun berkeliling menelusuri Alun-alun Bandung berdampingan, suasana riuh namun sejuk, warna warni lampu sudah mulai bermunculan untuk menyambut kegelapan malam hari,"
    "disana mereka menjumpai beberapa musisi dan pelukis jalanan dan menikmati suasana disana."
    
    show anindira 1 at left:
        zoom 0.4
    
    anindira "eh mas kayaknya kita sudah harus pulang, saya harus balik ke stasiun jam 8 malam"
    
    show cecep 1 at right:
        zoom 0.4

    cecep "Waduh, ayok atuh cepetan supaya gak telat"
    
    "mereka berlahir kearah dimana mereka memarkirkan angkotnya. Tiba tiba ada seorang ibu yang sedang menggendong seorang bayi mengetuk jendela pintu Cecep."
    "Cecep dengan keadaan sedang terburu-buru membuka kaca jendelanya"
    
    scene alunalunbandung
    
    show ibu 1 at left:
        zoom 0.4
        
    ibu "Mohon maaf nak, ibu boleh ikut gak ya? Ibu dari tadi nunggu angkot tapi gaada yang lewat sekalinya ada yang lewat malah penuh."
    
    show cecep 1 at right:
        zoom 0.4
        
    cecep "aduh bu mohon maaf saya lagi buru buru"
    
    ibu "tolong lah nak, anak saya sakit, saya harus buru-buru"
    
    show anindira 1 at Position(xpos=500, ypos=220) behind ibu:
        xzoom -1.0
        zoom 0.4
        
    anindira "Gak apa pa mas, biarin ibunya ikut"
    
    "dengan paksaan Anindira akhirnya ibu itu diperbolehkan untuk masuk"
    
    scene black
    with dissolve
    jump scene14
    
label scene14:

    scene dalamangkot
    #suasana tergesa-gesa
    
    "Kegelapan menyelimuti jalanan, rembulan malam hiasan langit terlihat menyendiri. perlahan mereka memasuki area penuh dengan lampu warna-warni memperlihatkan kesejukan kota Bandung pada malam hari."
    "Cecep fokus pada jalanan sementara Anindira membantu ibu tersebut untuk menenangkan bayinya dengan memperlihatkan kota bandung dan ilmu ilmu yang dia ketahui tentang kota Bandung, membuat ibu tersebut terpukau"

    show ibu 1 at left:
        zoom 0.4
        
    ibu "Kakak pinter banget, sudah pinter baik lagi, pasti orang tuanya membesarkan kakak dengan baik"
    
    show anindira 1 at right:
        zoom 0.4
        
    anindira "hehe"
    
    "Anindira menundukan kepalanya dengan fakta bahwa sebenarnya orang tuanya tidak peduli dan keras dengannya, itulah mengapa dia sendirian ke Kota Bandung."
    
    scene black
    with dissolve
    jump scene15
    
    #DIALOG BABAK 4
label scene15:
    
    scene rslimijati
    #suasana normal
    
    "Setiba di rumah sakit, Ibu itu berpamitan dengan mereka. Anaknya terlihat sangat menyukai Anindira sampai dia tidak mau melepas tangan Anindira namun karena waktu ibu itu melepas paksa tangannya yang membuat Anindira berasa tidak enak."
    "Sedikit rasa cemburu pada mereka, andaikan Anindira memiliki ibu yang rela berkorban deminya"
    "Selesainya perpisahan mereka. Kini mereka kembali fokus untuk menuju ke Stasiun Bandung. Mereka kembali ke Angkot dan berangkat menuju Stasiun."
    
    scene black
    with dissolve
    jump scene16
    
label scene16:
    
    scene dalamangkot
    #suasana tercengang
    
    "Keheningan Kembali menemani mereka diperjalanan menuju Stasiun Bandung. Keduanya sama-sama lelah karena perjalanan sepanjang hari, namun cecep tidak menyesal dan malah tersenyum mengingat semua hal yang telah terjadi"
    "Senyumannya pudar ketika handphonenya bergetar dan terpapang nama RSUP DR.HASAN Anindira pun ikut tersentak dan bertanya-tanya"
    "Firasat Cecep entah mengapa semakin buruk. Dengan tangan bergetar Cecep langsung menekan tombol warna hijau."
    
    show cecep 1 at left:
        zoom 0.4
    
    cecep "Halo?"
    
    scene rumahsakit
    
    show suster 1 at right:
        zoom 0.4
    
    suster "halo, mas Cecep tolong segera kesini, bapaknya sedang kritis dan segera untuk dioperasi"
    
    scene dalamangkot
    
    "Hati Cecep bagaikan kulit yang sedang disayat. Disayat oleh kenyataan."
    
    show cecep 1 at left:
        zoom 0.4
    
    cecep "B-bapak saya akan baik baik saja kan ?"
    
    "Tangan cecep bergetar, suaranya menahan isakan, Anindira melihatnya dengan khawatir"
    
    scene rumahsakit 
    
    show suster 1 at right:
        zoom 0.4
    
    suster "saya belum tau pasti mas, yang penting mas tolong cepat kesini ya-"
    
    scene dalamangkot
    
    "Terdengar suara ambrukan keluar dari handphonenya Cecep, sepertinya sesuatu telah terjadi di rumah sakit saat itu. Dan tiba-tiba telepon putus."
    "Cecep mencoba menelpon kembali rumah sakit tapi tidak ada jawaban. Kini Cecep menjatuhkan handphonenya dan merosot pada kursinya"
    "Dunianya yang telah berubah pandangan dan berdiri kokoh karena pengalaman hari ini dengan sekejap runtuh dan berubah mejadi sayatan tajam"
    "Anindira tidak tega melihatnya mengeluarkan sebotol air putih dan mencoba menenangkan Cecep"
    "beberapa detik kemudian Cecep sedikit lebih tenang dan melihat wajah Anindira, dia lupa kalau masih ada 1 lagi yang harus diantarkan, namun suasana hati Cecep sudah tidak bisa bangun dan ingin segera ke rumah sakit sekarang juga."
    
    show cecep 1 at left:
        zoom 0.4
    
    cecep "ak-"
    
    show anindira 1 at right:
        zoom 0.4
    
    anindira "tidak usah memaksakan, cepat arahkan kemudinya pada tempat ayah mas berada"
    
    show dalamangkot
    
    "terlalu lemah untuk menolak, Cecep menganggukan kepalanya lalu menekan gas menuju rumah sakit dimana tempat ayahnya berada"
    "sepanjang perjalanan Cecep menceritakan kisahnya termasuk kejadian tadi pagi kepada Anindira sambil menahan isakan. Anindira yang mendengar semuanya, dia tidak tahu harus"
    "bagaimana karena kondisi dia dengan orang tuanya pun tidak kalah buruknya. Tapi saat ini dia hanya bisa menyemangati Cecep bahwa semuanya akan baik-baik saja meskipun dia sangat tahu itu dari semua cerita Cecep bahwa semua tidak akan baik baik saja."
    
    scene black
    with dissolve
    jump scene18
    
#label scene17
     #final mini games


label scene18:
    
    scene rsulin
    #suasana panik
    
    "Sesampainya dirumah sakit keduanya pun turun, Anindira langsung membuka Handphonenya lalu memesan ojeg oline. sebelum berpisah Cecep mengeluarkan uangnya"    
    "Anindira dengan niat sebagai kompensasi karena tidak dapat mengantarnya ke stasiun namun Anindira memegang tangannya dan menghentikannya."

    show anindira 1 at left:
        zoom 0.4
    
    anindira "Apa yang sedang mas lakukan disini? Cepat temui ayah mas!"
    
    show cecep 1 at right:
        zoom 0.4
    
    "wajah merasa bersalah terpampang diwajahnya tak tega meninggalkan perempuan ini sendirian namun ada hal yang lebih penting."
    "Cecep mengangguk dan langsung berlari menuju Lobby rumah sakit"

    scene black
    with dissolve
    jump scene19
    
label scene19:

    scene rumahsakit
    #suasana penyesalan,kesedihan
    
    "Cecep berlarian kelorong rumah sakit demi menemukan ruangan ayahnya seperti orang gila, dia tidak peduli dengan tatapan dari pasien lain, yang di otaknya saat ini hanya satu hal. Keluarga satu satunya yang dimiliki."
    "Sampai akhirnya dia menemukan lorong dimana kamar operasi berada namun suasana disana sedang riuh, petugas rumah sakit keluar masuk dengan panik,"
    "salah satunya suster dengan membawa keranjang yang di dalamnya merupakan kain dengan penuh darah. Suster itulah yang menelponnya tadi."
    "Baru saja mau melewati, Suster itu menyadari keberadaan Cecep dan menyuruh cecep untuk tenang dan menunggunya diluar."
    "Namun hati cecep bagaikan api yang membara diselimuti rasa khawatir yang hebat. Akhirnya kaki cecep bergerak dan berlaju menuju kamar itu, "
    "suster itu langsung memanggil penjaga dan menghentikan Cecep untuk masuk ke ruang operasi."
    
    "Beberapa jam berlalu dan tidak ada gerak gerik dari kamar operasi. Deretan memori bertebaran layaknya air terjun di ingatan Cecep saat ini. Air mata perlahan mengalir dipipinya."
    "Dijam berikutnya dokter pun keluar dari ruang operasi. Cecep langsung berdiri dan berlari kearahnya"
    
    show cecep 1 at left:
        zoom 0.4
    
    cecep "Dok..."
    
    "kasihan terhadap cecep, Dokter itu menggelengkan kepalanya"
    
    show dokter 1 at right:
        zoom 0.4
    
    dokter "Mohon maaf..."
    
    cecep "Tidak... TIDAK"
    
    "Cecep memasuki ruang operasi dan horror menempel pada wajahnya, darah berserakan dimana mana dan ditengahnya berbaring lah seorang lelaki yang selama ini dia sebenarnya sayangin tanpa ia sadari."
    "Tidak peduli dengan apapun cecep berlari kepadanya dan memeluknya."
    
    cecep "Maafin cecep pak, cecep salah, cecep anak durhakan, maafin cecep. Cecep menyesal. Maafin Cecep"

    scene black
    with dissolve
    jump scene20
    
label scene20:

    scene black
    

label scene21:
 #epilog
    scene dalamangkot
    
    "Cecep kembali ke angkotnya dengan tatapan kosong, wajahnya basah oleh tangisan. Ia menatap angkot yang menjadi bukti kerja keras ayahnya."
    "dan bodohnya dia tidak menyadari itu. setelah memasuki angkot Cecep menyadari ada secarik kertas tertempel di kemudi bertuliskan"
    
    show cecep 1 at left:
        zoom 0.4
    
    show anindira 2 at Position(xpos=900,ypos=400)
     
    anindira "Halo mas cecep, saya pamit untuk pulang, terimakasih atas tumpangannya hari ini saya sangat menikmatinya, ingatlah kalau mas sudah menyelamatkan banyak orang hari ini termasuk saya, jadi apapun yang terjadi Mas pasti kuat, mas pasti" 
    anindira "bisa melewatinya, dan mas tidak sendiri, semua orang yang telah mas selamatkan akan medoa'kan mas selalu, sehat selalu semoga dipertemuan selanjutnya kita lebih memiliki banyak waktu”"
    anindira "Salam, Anindira                  082 xxx xxx xxx"
    
label scene22:
    
    scene black
    
    "END"
    # This ends the game.
    return
