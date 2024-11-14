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
        zoom 0.3
    
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
    
    show nenek 1 at left:
        zoom 0.3
    
    show anindira 1 at right:
        zoom 0.3
        
    show cecep 1 at Position(xpos=350,ypos=220) behind anindira:
        zoom 0.3
        
    
    nenek "Nuhun ya, Neng, Kang. Moga rezeki kalian dilancarkan, apa-apanya dimudahkan"
        
    anindira "Makasih ya, Bu. Moga dagangan ibu juga laris."
    
    cecep "aamiinn..."
    
    "Setelah berpamitan, mereka pun berpisah."
    hide nenek with dissolve
    hide anindira with dissolve
    hide cecep with dissolve
    
    "Melihat suasana di Jalan Braga, Anindira tertarik buat berhenti dan jalan-jalan sebentar di daerah itu."
    
    show anindira 1 at left with moveinleft:
        zoom 0.3
    
    #ekspresi excited
    anindira "Mas, mampir dulu yak!"
    
    show cecep 1 at right with moveinright:
        zoom 0.4
    
    cecep "Aduh, males banget atuh, Teh. Rame pisan euy."
    
    anindira "Aku traktir deh nanti"
    
    #ekspresi senyum tipis
    cecep "Gas!"
    
    scene black
    with dissolve
    
    scene braga
    
    "Anindira membeli banyak jajanan kuliner Bandung seperti Batagor, Awug, dan Baso Tahu. Sedangkan Cecep menikmati apa pun yang Anindira tawarkan."
    
    show anindira 1 at left:
        zoom 0.3
        
    #ekspresi excited
    anindira "Wahh. Enak banget jajanan Bandung!"
    
    show cecep 1 at right with moveinright:
        zoom 0.4
        
    #ekspresi senyum tipis
    cecep "Apalagi kalau ditraktir, hehe"
    
    anindira "Menurut Mas Cecep, paling suka kuliner apa?"
    
    
    menu:
        "Awug":
            #ekspresi berpikir
            anindira "hmm setuju sih, manisan enak banget, banyak banget kelapanya, saya jadi tau perpaduan kelapa dan gula merah seenak ini"
        
        "Batagor":
            #ekspresi excited
            anindira "SETUJU BANGET, apalagi saus kacangnya, mantap!!!"
        
        "Baso Tahu":
            #ekspresi kecewa
            anindira "Oke sih menurut saya, cuman saya gak suka paria-nya karena terlalu pait"
   
  
    "Setelah makan dan berbincang tentang kuliner mereka pun melanjutkan perjalanannya menuju alun-alun bandung" 
    
    scene black
    with dissolve
    
    scene dalamangkot
    
    "Hari semakin larut suasana hangat kini bersapaan dengan sejuknya warna ungu disaat sore menjelang malam, mereka melaju dengan keheningan karena sudah lumayan lelah."
    "Sedangkan Anindira, masih sibuk melihat foto-foto yang sudah dia ambil."
    "Dalam perjalanan, Cecep melihat seorang kakek yang melambaikan tangan kearah angkotnya. Melihat itu, Cecep menepikan angkotnya, membuat Anindira kebingungan dan menaruh kameranya."
    
    show anindira 1 at left:
        zoom 0.3
    
    anindira "Kenapa, Mas?"
    
    show cecep 1 at right:
        zoom 0.4
        
    cecep "Kakek itu ngelambaiin tangannya tadi, barangkali butuh bantuan. Gaapa kan, Teh?"
    
    anindira "...."
    
    "Anindira tampak terheran melihat Cecep yang tiba-tiba peduli sama orang yang memintanya untuk menepi, padahal sedari siang tadi, dia selalu mengabaikan orang yang minta tumpangan di jalan."
    
    cecep "Gapapa kan"
    
    anindira "Eh, Ah, iya gaapa, Mas. Tambah senang saya dengernya."
    
    cecep "Oke."
    
    scene dalamangkot
    
    "Setelah berdiskusi dengan Anindira, Cecep menghampiri Kakek tua itu. Ia menggunakan peci dengan kemeja batik dan"
    extend "celana hitam longgar, serta tongkat untuknya berdiri."
    
    show cecep 1 at left:
        zoom 0.3
    
    cecep "Kunaon, Pak?\n(Kenapa, Pak?)"
    
    show kakek 1 at left:
        zoom 0.4
    
    kakek "Bade ngiring ka Masjid raya tiasa teu?\n(Mau ikut ke Masjid Raya bisa gak?)"
    
    "Cecep dan Anindira bertukar tatapan, dilanjut dengan anggukan Anindira menyetujui permintaan kakek itu."

    cecep "Muhun, mangga, Pak.\n(Boleh, silahkan, Pak.)"
    
    kakek "Mayar na sabaraha\n(Bayarnya berapa?)"
    
    cecep "Eh teu kedah, Pak. Sekalian abdi gè badè kaditu\n(Eh gausah, Pak. Sekalian saya juga mau kesana)"
    
    hide cecep with dissolve
    
    scene dalamangkot
    
    "Kakek tua kemudian dibantu oleh Anindira untuk memasuki Angkot. Kemudian, mereka melanjutkan perjalanan."
    "Selama perjalanan, keheningan diisi dengan storytelling milik Kakek itu. Energi kakek itu membuat Anindira terpukau dan membuatnya mendengarnya dengan penuh ketertarikan." 
    "Mengetahui Anindira tidak bisa memakai bahasa sunda akhirnya kakek tua itu bercerita menggunakan bahasa Indonesia."

        
    show kakek 1 at left:
        zoom 0.4

    kakek "Omong-omong, tumben ada angkot di sekitar sini?"
    
    
    show cecep 1 at right:
        zoom 0.3
    #ekspresi senyum tipis
    cecep "Hehe, soal itu tanya aja toh sama mbaknya, Pak."
    hide cecep with dissolve
    
    show anindira 1 at right:
        zoom 0.3
    
    #excited
    anindira "Iya, Pak. Saya yang minta Mas Cecep buat nganterin saya keliling Bandung naik angkot. Jadi ya, keluar jalur."
    
    kakek "Oh, gitu toh."
    extend "Hmm..."
    
    #yapping
    kakek "Omong-omong, saya itu pecinta angkot sepuh atuh, Neng."
    
    #excited
    anindira "Wah, kenapa, Kek?"
    
    #yapping
    kakek "Ohya, panggil Pak Asep aja atuh, Neng. Meski muka kriput, jiwa masih muda, haha."
    
    #excited
    anindira "Siap, Pak! (Ada-ada aja orang tua jaman sekarang)"
    
    kakek "Ohya, soal angkot, dulu waktu saya masih muda itu kalo mau sekolah, kerja, bahkan waktu udah rumah tangga sekalipun, naiknya ya angkot."
    kakek "Tapi, makin tua, udah jarang keluar, apalagi jalan-jalan naik angkot."
    kakek "Tadi kebetulan aja lihat ada angkot lewat, saya stop deh"
    
    #yapping
    kakek "Jiwa saya langsung tergugah ngelihat angkot lewat"
    
    #excited
    anindira "Wah, seru banget ya keliatannya!"
    
    #yapping
    kakek "Ya, dong."
    
    "Mereka melanjutkan perjalanan sambil melihat-lihat suasana di Jalan Braga."
    
    kakek "Dulu mah, di sini teh gaada yang kayak gini. Apa yang anak muda suka bilang? Instagramable?"
    kakek "Pokoknya eta. Makin kesini tempat - tempat disini bukan orang bandung yang terlihat, tapi orang Jakarta. Jadi we macet pisan."
    
    "Jalanan mulai menjadi sangat padat terutama di wilayah Museum Asia Afrika. Pak Asep tidak melewatkan kenangannya dengan museum itu"
    
    #Menampilkan Latar Belakang, Museum KAA, di dalam Angkot
    
    scene museumKAA

    show kakek 1 at left:
        zoom 0.3
    
    kakek "Menurut kalian barudak, mengapa di Bandung loba gedung gedung bersejarah?"
    
    show anindira 1 at right:
        zoom 0.3
    
    #ekspresi berpikir
    anindira "Karena dulu kota Bandung awalnya mau dijadikan kota Batavia?"
    
    kakek "Nah, betul"
    
    "Pak Asep berpaling dan menatap ke arah Cecep."

    #yapping
    kakek "Naha pinter awèwè gening? Lalaki na teu nyaho ieu tèh?\n(Kenapa pinter yang perempuan? Laki-lakinya gak tau ini teh?)"
    
    "Cecep memalingkan wajah sambil tersenyum malu karena memang dia tidak tahu apa apa mengenai sejarah."
    
    kakek "Dibangunnya gedung-gedung bersejarah, karena dulu pemerintah Hindia Belanda yang pengen pindah ke Bandung gagal karena adanya"
    kakek "perang dunia ke dua. Jadi, mereka teh gak mampu meneruskan pembanguannya." 
    kakek "Nah setelah perang dunia, berkumpul lah negara negara lain disini, Indonesia sebagai tuan rumah."
    
    "Kemudian, mereka melanjutkan perjalanannya menuju Alun-Alun Bandung, sambil membahas apapun yang mereka lihat."
    hide kakek with dissolve
    
    scene alunalunbandung
    
    "Sesampainya di Alun-Alun Bandung, Pak Asep dan kedua lainnya ikut turun. Ketika Pak Asep hendak membungkuk dan berterima kasih, "
    "Cecep langsung meluruskan posisi Pak Asep dan meyakinkan dia untuk tidak perlu berterima kasih."
    "Kemudian, Pak Asep meninggalkan mereka dan perlahan semakin menyusut dari pandangan Cecep dan Anindira"
    
    anindira "Kakek yang penuh energi untuk seumuran itu!"
    
    
    show cecep 1 at left:
        zoom 0.3
    
    "Cecep tertawa kecil menanggapinya."
    
    #senyum tipis
    cecep "Kau benar. Semoga usianya diperpanjang dan dapat menginspirasi pemuda jaman sekarang"
    
    "Anindira tersenyum hangat memandang Cecep"
    
    #anindira senyum
    
    #senyum tipis
    
    
    
    #excited
    anindira "Okeh. Ayo keliling di sekitar sini, Mas Cep!"
    
    cecep "Orang satu ini juga gak ada capeknya dah."
    
    hide anindira with dissolve
    hide cecep with dissolve
    
    #Menampilkan Latar Belakang, Alun-Alun Bandung
    
    "Mereka berkeliling menelusuri Alun-alun Bandung berdampingan, suasana riuh namun sejuk, warna warni lampu sudah mulai bermunculan untuk menyambut kegelapan malam hari."
    "Di sana, mereka juga menjumpai beberapa musisi dan pelukis jalanan. Mereka menikmati suasana disana"
    
    show anindira 1 at left:
        zoom 0.37
        
    show cecep 1 at right:
        zoom 0.37
    
    anindira "Enak banget ya, Bandung. Tempat kek gini aja kerasa nyaman."
    
    cecep "Iya, Teh. Jujur aja kalo gak ketemu teteh, saya gak bakal ngerasain Bandung kek gini."
    cecep "Gak ada waktu rasanya buat ngenikmatin kota ini. Pingin kaya teteh saya, bisa keliling-keliling antar kota."
    
    #sedih
    anindira "Saya sebenernya juga lagi lari sih, Mas"
    
    cecep "Lari? Dari apa?"
    
    #sedih
    anindira "Dari rumah."
    anindira "Keluarga di rumah gak pernah berenti buat ribut. Penelitian buat skripsi mah cuman alibi saya biar bisa keluar dari rumah."
    
    "Cecep merasa iba dengan cerita Anindira. Ia jadi teringat dengan masalahnya sendiri"
    " Ia merasa memiliki kesamaan dengan Anindira, meski memiliki masalah yang berbeda."

    #default
    anindira "Well. Tapi mau gimana lagi ya, Mas. Hidup gak pernah berhenti berjalan, jadi kita juga harus tetep berjalan."

    "Cecep hanya terdiam mendengarkan cerita dari Anindira."

    #excited
    anindira "Ahhh, malah jadi cerita gini. Mas Cecep sih!"

    #senyum tipis
    cecep "Lah, kok malah saya."

    anindira "Yaudah, lanjut keliling yuk, Mas Cecep."
    
    "Belum aja mereka mulai berjalan, tiba-tiba terdengar alarm dari handphone Anindira"
    "yang mengingatkan akan pemberangkatan keretanya 2 jam lagi"
    
    #terkejut
    cecep "Loh, mbaknya mau pergi lagi?"
    
    anindira "Iya, Mas Cep, hampir lupa saya. Saya udah mau balik ke Yogyakarta jam 8 nanti. Dah cukup lama saya berpergian"

    #terkejut
    cecep "Jam 8? Loh, bentar lagi dong? Yaudah ayo kita berangkat kalo gitu."

    "Cecep dan Anindira bergegas untuk kembali ke angkotnya. Namun, setibanya di angkot, sudah ada seorang ibu yang menggendong seorang bayi."
    
    show ibu 1 at left:
        zoom 0.3
    
    ibu "Mohon maaf, Nak, ibu boleh ikut gak ya? Ibu dari tadi nunggu ojek tapi gak datang-datang."
    
    show cecep 1 at right:
        zoom 0.37
    
    cecep "Aduh, Bu. Mohon maaf saya lagi buru-buru."
    
    #worried
    ibu "Tolong ya, Nak. Anak saya lagi sakit, jadi harus buru-buru."
    
    cecep "Duh, gimana ya. \n(Menatap ke arah Anindira)"
    
    show anindira 1 at Position(xpos=350,ypos=220) behind cecep:
        zoom 0.3
    
    anindira "Gak apa, Mas. Biarin ibunya ikut. Harusnya sempet."
    
    cecep "Bentar, ibunya mau ke mana?"
    
    #worried
    ibu "RSIA Limijati, Nak."
    
    cecep "Oke, aman kelihatannya. Baik, Bu, ayo masuk aja."
    
    ibu "Makasih ya, Nak."
    
    "Setelah berbincang, akhirnya Ibu dan anaknya itu diperbolehkan Cecep untuk ikut masuk."
    "Mereka pun melanjutkan perjalanan menuju RSIA Limijati."
    
    
    scene black
    with dissolve
    jump scene5
    
label scene5:
    show screen judul_cerita5
    $ renpy.pause(5.0, hard=True)
    hide screen judul_cerita5
    
    scene dalamangkot
    
    "Kegelapan menyelimuti jalanan, rembulan malam hiasan langit terlihat menyendiri. perlahan mereka memasuki area penuh dengan"
    "lampu warna-warni memperlihatkan kesejukan kota Bandung pada malam hari."
    "Cecep fokus pada jalanan sementara Anindira membantu ibu tersebut untuk menenangkan bayinya dengan"
    "memperlihatkan kota bandung dan ilmu ilmu yang dia ketahui tentang kota Bandung, membuat ibu tersebut terpukau."
    
    show ibu 1 at left:
        zoom 0.3
    
    show anindira 1 at right:
        zoom 0.3
    
    #bahagia
    ibu "Eneng pinter banget. Sudah pinter baik lagi, pasti orang tuanya membesarkan eneng dengan baik."
    
    #malu
    anindira "Hehe, Ibu bisa aja."
    
    "Anindira menundukan kepalanya dengan fakta bahwa sebenarnya orang tuanya tidak"
    "peduli dan keras dengannya, itulah mengapa dia sendirian ke Kota Bandung."
    
    anindira "Omong-omong, adiknya namanya siapa, Bu?"
    
    ibu "Oh, ini namanya Cipung. Kalo saya Bu Endah"
    
    #excited
    anindira "Cipung! Lucu banget namanya."
    
    #bahagia
    ibu "Iya, dong. Ayahnya dulu yang namain dia gini."
    
    #berpikir
    anindira "Emang dek Cipung sakit apa, Bu?"
    
    #worried
    ibu "Gak tau sih, Neng. Dari kemaren dia ini muntah-muntah mulu. BAB nya juga susah"
    
    "Cecep yang dari tadi hanya fokus menyetir, tiba-tiba ikut menyahut dengan nada yang agak ketus"
    
    show cecep 1 at Position(xpos=350,ypos=220) behind anindira:
        zoom 0.3
    
    cecep "Emang ayahnya ke mana, Bu?"
    
    #marah
    cecep "Udah tahu anaknya sakit, kok ngilang."
 
    ibu "Oh. Ayahnya lagi kerja di luar kota."
    
    ibu "Awalnya saya minta dia buat kerja di deket-deket sini aja, biar bisa deket sama si Cipung. Tapi katanya gaji di luar lebih gede dari yang ada di sini"   
    
    cecep "Bukanya lebih baik gitu ya, Bu? Biar Si Cipung juga bakal ada tabungannya nanti."
    
    ibu "Hmm. Nggak salah sih."
    
    #worried
    ibu "Tapi jujur aja, di usia anak yang masih kecil gini, mereka juga butuh dampingan kedua orang tuanya."
    
    ibu "Uang mah bisa dicari kapan-kapan lagi, tapi momen sama keluarga ini yang gak bisa diulang."
  
    #marah
    cecep "Tapi kan-"
    
    "Melihat Cecep yang tampak lebih tegang, Anindira memotong ucapan Cecep."
    
    anindira "Semoga rezeki ibu dan sekeluarga dilancarkan ya, Bu. Semoga juga Si Cipung bisa segera sembuh."
    
    ibu "Iya. Makasih ya, Neng."
    
    "Suasana perjalanan itu menjadi lebih dingin, seiringan dengan kota Bandung yang semakin gelap"
    
    
    scene rslimijati
    
    "Setiba di rumah sakit, Ibu itu berpamitan dengan mereka Anaknya terlihat sangat menyukai Anindira sampai dia tidak mau melepas tangan Anindira."
    
    show ibu 1 at left:
        zoom 0.3

    show anindira 1 at right:
        zoom 0.3
                
    ibu "Maaf ya, Neng. Si Cipung seneng banget ketemu sama Eneng."

    anindira "Duh, udah dulu ya, Cipung. Kapan-kapan kita main lagi, okey?"    
    
    "Setelah dibujuk oleh Bu Endang dan Anindira, akhirnya Si Cipung melepaskan tangan Anindira. Kemudian mereka pun berpamitan."
    "Anindira melihat ke arah mereka yang berjalan menuju ke arah Rumah Sakit."
    
    anindira "Sehat-sehat ya, Bu."
    
    hide ibu with dissolve
    
    #worried
    anindira "Beruntung banget Si Cipung punya ibu penyayang kaya Bu Endang."
    
    show cecep 1 at left:
        zoom 0.37
        
    cecep "...." 
    
    "Mereka saling berdiam melihat Bu Endang dan Cipung memasuki Rumah Sakit. Kemudian, Anindira melihat jam dan terkejut karena sudah tinggal 1 jam setengah keretanya akan berangkat."
    
    #terkejut
    anindira "Waduh, Mas Cep. Kita harus berangkat ke Stasiun sekarang."
    
    #terkejut
    cecep "Ohya. Sampe lupa saya."
    
    
    "Selesainya perpisahan mereka. Kini mereka kembali fokus untuk menuju ke Stasiun Bandung. Mereka masuk ke Angkot dan berangkat menuju Stasiun."
    "Keheningan Kembali menemani mereka di perjalanan menuju Stasiun Bandung. Keduanya sama-sama lelah karena perjalanan sepanjang hari ini."
    
    anindira "Omong-omong, kamu gapapa kan, Mas?"
    
    cecep "Eh, kenapa emang?"
    
    anindira "Tadi pas Bu Endang cerita soal suaminya. Masnya keliatan kek marah?"
    
    cecep "Emang keliatan, Teh?"
    
    anindira "Sedikit?"
    
    "Cecep tidak menanggapi Anindira dan fokus mengemudi. Meski demikian, Cecep menjadi kepikiran dengan apa yang Anindira katakan."
    
    cecep "Sebenernya, waktu teteh bilang lagi lari dari rumah, saya berasa ikut ngerasain apa yang teteh rasain."
    
    #worried
    anindira "Mas kenapa?"
    
    #sedih
    cecep "Hubungan saya sama ayah saya gak terlalu baik. Saya tau, ayah saya ngelakuin banyak hal buat saya setelah kematian ibu."
    cecep "Tapi… Rasanya kek gak pingin aja gitu ngelihat ayah saya ataupun rumah. Makannya, Teh, saya seneng banget nyari kerja srabutan, ngumpulin uang, biar bisa keluar dari kota ini."
    
    #sedih
    anindira "..."
    anindira "Maaf ya, Mas. Saya gak tau masalah berat apa yang Mas Cecep rasain."
    
    #senyum tipis
    cecep "Meski gitu, Teh. Sejak ketemu teteh dan orang-orang tadi, saya jadi lumayan seneng sama hidup ini."
    cecep "Ternyata, Teh. Ketemu sama orang-orang tu enak banget, saya nggak nyangka ngrasain perasaan campur aduk seperti yang saya rasain seharian ini."
    cecep "Makasih ya, Te-"
    
    "Belum sempat menyelesaikan kalimatnya, handphonenya bergetar. Terpapang nama “RSUP Dr. Hasan” di dalamnya. Cecep dan Anindira tersentak dan bertanya-tanya."
    "Firasat Cecep entah mengapa semakin buruk. Dengan tangan bergetar Cecep langsung menekan tombol warna hijau."
    
    hide anindira with dissolve
    
    #bingung
    cecep "Halo?"
    
    scene rumahsakit
    
    show suster 1 at right:
        zoom 0.4
    
    suster "Selamat siang, apa benar ini nomor telfon dari keluarga Pak Sudirman?"
    
    scene dalamangkot
    
    show cecep 1 at left:
        zoom 0.37
    
    cecep "Benar, saya Cecep, putra Pak Sudirman."
    
    scene rumahsakit
    
    show suster 1 at right:
        zoom 0.4
    
    suster "Selamat malam, Mas Cecep, mohon maaf mengganggu. Kami dari pihak rumah sakit ingin mengabarkan bahwa"
    extend "kondisi Bapak Sudirman saat ini dalam keadaan kritis dan memerlukan tindakan operasi segera."
    extend "Kami membutuhkan persetujuan dan kehadiran dari pihak keluarga untuk proses lebih lanjut. Kami mengerti bahwa ini kabar yang berat, dan kami akan melakukan yang terbaik untuk menangani situasi ini."
    
    scene dalamangkot
    
    show cecep 1 at left:
        zoom 0.37
    
    #terkejut
    cecep "Eh! Ayah saya kenapa?"
    
    #sedih
    cecep "..."
    cecep "Maaf, Mbak, saya masih berada di jalan. Saya akan segera datang ke Rumah Sakit."
    cecep "Namun, jika saya belum juga datang, sedangkan ayah saya segera butuh dioperasi, mohon langsung dioperasi saja ya, Mbak."
    
    scene rumahsakit
    
    show suster 1 at right:
        zoom 0.4
    
    suster "Baik, terima kasih Mas Cecep. Kami akan menunggu Mas Cecep beberapa menit terlebih dahulu sebelum menindaklanjutinya."
    
    scene dalamangkot
    
    show cecep 1 at left:
        zoom 0.37
        
    #sedih
    cecep "Terima kasih, Mbak. Saya akan segera tiba."
    
    "Cecep merasa sangat terkejut. Pengalaman berharganya hari ini dengan sekejap runtuh dan berubah mejadi sayatan tajam."
    "Anindira yang tidak tega melihatnya, mengeluarkan sebotol air putih dan mencoba menenangkan Cecep."
    "Beberapa detik kemudian, Cecep sedikit lebih tenang. Setelah melihat wajah Anindira, dia lupa kalau masih ada 1 lagi yang harus diantarkan, ia bingun apa yang harus ia lakukan."
    
    menu:
        "Antar Anindira":
            scene black
            with dissolve
            jump ending1

        "Kerumah sakit":
            scene black
            with dissolve
            jump ending2

label ending1:

            scene dalamangkot

            show cecep 1 at left:
                zoom 0.3

                cecep "Teh. Saya antar ke Stasiun sekarang ya."
            show anindira 1 at right:
                zoom 0.3
            
            #wooried
            anindira "Eh, saya gapapa, Mas. Apa mending nggak ke Ayah Mas aj-"
            
            #marah
            cecep "Udah, gaapa, Teh! Tanggung jawab saya nganter teteh ke Stasiun."
            "Anindira tersentak dan langsung terdiam. Mereka pun melanjutkan perjalanan menuju Stasiun Bandung."
            "Suasana menjadi sangat tegang di sepanjang jalan menuju stasiun."
            
            scene black
            #with dissolve
            #jump minigames5
            "Sesampainya di Stasiun Bandung, Anindira langsung turun dan berpamitan dengan Cecep."
            "Cecep langsung menancapkan gasnya dan segera menuju ke Rumah Sakit."
            "Namun, ia terlalu lama pergi menuju ke rumah sakit. Hingga pihak rumah sakit pun sudah mulai melakukan operasi kepada ayahnya."
            
            scene rumahsakit
            "Cecep berlarian ke lorong rumah sakit demi menemukan ruangan ayahnya dioperasi. Ia berlarian seperti orang gila, sambil bertanya dengan orang-orang di sana."
            "Sampai akhirnya, dia menemukan lorong di mana ayahnya dioperasi. Namun, suasana disana sedang riuh, petugas rumah sakit keluar masuk dengan panik, salah satunya suster dengan membawa keranjang yang di dalamnya merupakan kain dengan penuh darah."
            "Beberapa jam berlalu dan tidak ada gerak gerik dari kamar operasi. Deretan memori bertebaran layaknya air terjun. Air mata pun perlahan mengalir di pipinya."
            "Di jam berikutnya, dokter pun keluar dari ruang operasi. Cecep langsung berdiri dan berlari kearahnya."

            show cecep 1 at left:
                zoom 0.3
            #menyesal
            cecep "Dok..."
            cecep "Bagaimana hasil operasinya?"

            "Kasihan terhadap Cecep. Doketer itu hanya menggelengkan kepalanya sambil menepuk bahu Cecep."'

            cecep "Dok..."

            "Tersentak dengan berita yang ia terima, Cecep terjatuh dengan hati yang terasa seperti tertikam."
            "Kemudian, Cecep memasuki ruang operasi dan horror menempel pada wajahnya. Darah berserakan dan di tengahnya berbaring seorang pria tua yang selama ini tanpa sadar ia sayangi begitu dalam."
            "Dengan hati yang semakin tersayat-sayat, Cecep berlari ke arahnya dan mengenggam erat tangannya."

            #menyesal
            cecep "Maafin Cecep, Pak. Cecep salah. Cecep durhaka sama bapak. Maafin Cecep, Pak. Pak…"

            scene black

            "Perasaan yang kerap ia rasakan terhadap ayahnya. Kebenciannya kepadanya. Tidak sebanding dengan apa yang ia rasakan saat ini. Tidak pernah dalam hidupnya merasa sangat menyesal seperti ini."
            "Ia tidak menyangka, justru ucapan kasar darinya yang terakhir ayahnya dengar."
            "Hidup Cecep dipenuhi dengan kekecewaan terhadap dirinya sendiri dan hidupnya dipenuhi dengan penyesalan."
            "Cerita berakhir"
            
            scene black
            with dissolve
            jump end
    
label ending2:

            scene dalamangkot

            show cecep 1 at left:
                zoom 0.3
            cecep "Teh. Ak-"

            show anindira 1 at right:
                zoom 0.3
            anindira "Gak usah maksain, cepet arahkan kemudinya ke tempat ayah mas dirawat."

            "Terlalu lemah untuk menolak, Cecep menganggukan kepalanya lalu menekan gas menuju rumah sakit dimana tempat ayahnya berada."
            #minigames 5

            "Sesampainya di Rumah Saki,t keduanya segera turun dari Angkot. Seketika, Anindira langsung membuka Handphonenya dan memesan ojek online."
            "Sebelum berpisah, Cecep mengeluarkan uang Anindira dengan niat sebagai"
            "kompensasi karena tidak dapat mengantarnya ke stasiun. Namun, Anindira memegang tangannya dan menghentikannya."

            #worried
            anindira "Apa yang mas tunggu? Cepet temuin ayah, Mas."

            "Wajah merasa bersalah terpampang di wajah Cecep, karena tak tega meninggalkan perempuan itu sendirian."
            "Namun, karena ia harus segera menemui ayahnya, ia pun langsung meninggalkan Anindira dan berlari memasuki Rumah Sakit."

            #sedih
            cecep "Maaf ya, Teh. Saya tinggal."

            #sedih
            anindira "Iya, Mas. Semoga ayah Mas Cecep tidak apa-apa."
            hide anindira with dissolve

            "Memasuki rumah sakit, Cecep langsung berlari menuju ruangan ayahnya di rawat."

            scene rumahsakit

            "Ia beruntung, ayahnya masih belum dioperasi."

            #sedih
            show cecep 1 at left:
                zoom 0.3

            #sedih
            cecep "Bapa... bapa..."

            "Pak Sudirman hanya terbaring, tanpa membalas panggilan Cecep. Kemudian, Cecep memegang tangannya dan menangis sambil mengenggam tangannya."

            #menyesal
            cecep "Bapa... Hapunten Cecep, Pa. Cecep geus salah pisan ka Bapa. Cecep sadar Bapa geus usaha seueur pisan pikeun Cecep, tapi Cecep masih kénéh teu bersyukur."
            extend "(Bapak… Maafin Cecep ya, Pak. Cecep udah jahat banget sama Bapak. Cecep sadar bapak udah berusaha banyak banget buat Cecep, tapi Cecep masih aja nggak bersyukur. )"

            "Pak Sudirman masih terdiam.Hal itu membuat Cecep semakin menangis sambil menggenggam tangan ayahnya."

            show sudirman at right:
                zoom 0.3

            sudirman "Cep..."

            #sedih
            cecep "Pa? \n(Pak..?)"

            sudirman "Kumaha narikna, cep? \n (Gimana nariknya, Cep?)"

            #sedih
            cecep "Geus, Pak. Teu kedah kuwatirkeun Cecep. Bapak kumaha kaayaanana\n (Udah, Pak. Gausah khawatirin Cecep. Bapak gimana keadaanya.)"

            sudirman "Teu nanaon, Cep. Nupenting mah tiasa ningali budak bapa didieu gè geus bagja pisan bapa mah. \n (Aman kok, Cep. Yang penting bisa ngelihat anak bapak di sini dah seneng banget Bapak.)"

            #menyesal
            cecep "Ya Allah, Pa... \n (Ya Allah, Pak...)"

            sudirman "Cep... ulah keras ka kahirupan anjeun nya. Sing sabar. Sing tabah \n (Nak… Jangan keras-keras ya sama hidupmu. Yang sabar. Yang tabah. )"
            sudirman "Cecep tèh kuat, Bapa nyaho èta. Malah, teu aya nu leuwih kuat ti Cecep tina loba jalma nu Bapa tepung.\n (Cecep kuat, Bapak tau itu. Malahan, gak ada yang lebih kuat dari Cecep dari banyaknya orang yang bapak temuin.)"
            sudirman "Sing jadi budak Cageur nya, Cep. \n (Sehat-sehat ya, Nak.)"

            #menyesal
            cecep "Pa. Hampura Cecep nya, pa. Cecep tos kalepatan. \n (Pak. Maafin Cecep ya, Pak. Cecep selama ini salah.)"
            
            sudirman "Teu, Cep. Teu nanaon. Bapa nu salah, geus gagal salaku jadi kolot. \n (Nggak, Cep. Nggak. Bapak ngerti kok. Bapak yang salah, gagal jadi orang tua.)"

            #menyesal
            cecep "Ya Allah, henteu, Pa. Bapa geus ngalakukeun loba hal pikeun Cecep. Hatur nuhun pisan, Pak. \n (Ya Allah, nggak, Pak. Bapak sudah ngelakuin banyak hal buat Cecep. Makasih banyak ya, Pak.) "

            "Muka Cecep dipenuhi dengan air mata, ditambah ketika petugas rumah sakit mulai masuk dan membawa Pak Sudirman menuju ruang operasi."

            #menyesal
            cecep "Pa...geura cageur nya, Pa.. \n (Pak… Sembuh ya, Pak…)"

            "Cecep menangisi ayahnya di sepanjang jalan menuju Ruang Operasi. Ayahnya sudah tidak menjawab ucapan Cecep apapun."

            #menyesal
            cecep "Pa... Cecep nyaah ka Bapa. Ulah ninggalkeun Cecep heula, Pa. \n (Pak… Cecep sayang sama, Bapak. Jangan tinggalin Cecep dulu ya, Pak.)"

            "Setelah air mata Cecep memenuhi sepanjang lorong rumah sakit, ayahnya pun tiba di ruangan operasi untuk memulai operasinya."

            show screen ending2
            $ renpy.pause(5.0, hard=True) # Durasi tampilan screen
            hide screen ending2

            scene bandung

            show cecep 1 at left:
                zoom 0.3
            cecep "Geus sataun nya, Pa. Teu karasa \n (Udah setahun ya, Pak. Gak berasa.)"

            cecep "..."

            #sedih
            cecep "Cecep sono pisan ka Bapa. \n (Cecep kangen banget sama Bapak.)"

            "Sudah satu tahun sejak kematian Pak Sudirman, ayahnya Cecep. Setelah kematian ayahnya, Cecep menjadi orang yang berbeda dari sebelumnya. Cecep menjadi orang yang lebih penyabar dan ramah kepada orang-orang."
            "Ia meneruskan usaha angkot ayahnya sambil menjadi seorang Tour Guide untuk wisatawan-wisatawan setiap ada wisatawan yang memerlukannnya."

            cecep "Ah iya, Anindira gimana kabarnya ya? Kalo gak salah dia ninggalin surat dulu."

            show anindira 1 at left:
                zoom 0.3
            "Cecep mencari surat yang pernah ditinggalkan Anindira di hari kematian ayahnya, di dalam angkotnya."

            cecep "Oh, ini"

            "Melihat surat itu, Cecep membaca kembali isi surat itu."

            show anindira 1 at Position(xpos=900,ypos=400)
     
            anindira "Halo, Mas Cecep. Saya pamit untuk pulang, terimakasih atas tumpangannya hari ini, saya sangat menikmatinya!" 
            anindira "Ingatlah kalau Mas Cecep udah menyelamatkan banyak orang hari ini. Termasuk saya."
            anindira "Jadi, apapun yang terjadi, Mas pasti bisa melewatinya. Mas kuat!"
            anindira "Ingat juga ya, Mas. Mas nggak sendiri. Semua orang yang udah mas selamatkan akan mendoakan mas selalu."
            anindira "Sehat selalu ya, Mas Cecep. Semoga, di pertemuan selanjutnya kita bisa lebih memiliki banyak waktu."
            anindira "Salam, Anindira."
            cecep "Haha. Makasih ya, Teh. Saya juga gak bakal ngelupain teteh."

            "Melihat nomor di balik surat itu, Cecep mencatat nomor itu dan menyimpannya di ponsel barunya."
            "Hidup penuh dengan warna-warni kehidupan. Akan ada banyak lintasan cerita, baik cerita yang kita inginkan ataupun yang tidak kita harapkan."
            "Satu hal yang pasti, kita hanya bisa terus berjalan, mengikuti rute yang ada, sesekali berhenti, dan memilih tempat berhenti yang tepat."
            "Seperti sebuah angkot dan lintasannya."
            "Cerita Berakhir"
            
            scene black
            with dissolve
            jump end

label end:
    
    scene black
    
    "END"
    # This ends the game.
    return
