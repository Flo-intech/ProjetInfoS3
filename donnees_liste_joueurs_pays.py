
def liste_joueurss():
    d=["Huitièmes de finale","Quarts de finale", "Demi-finales","Finale"]

    liste_joueurs_baseball_colombie={"Pitchers":['Ángel Vílchez','Carlos Mario Díaz','Dewin Pérez','Ezequiel Zabaleta','Hernán Guzmán','Hernando Chiquillo','Jaider Rocha','José Calero','Luis Yendis','Luis Barrios','Luis Ortega','Randy Consuegra'],
        "Catchers":['Álvaro Noriega [es]','Christian Correa','Jair Camargo [es]'],'Infielders':['Derwin Pomare [es]','Héctor Acuña','Milton Ramos','Reynaldo Rodriguez','Samir Caraballo','Sneider Batista'],
        'Outfielders':[
'Efrain Contreras',
'Jonathan Lozada',
'Steve Brown']}
    liste_joueurs_football_colombie={"gb":["1 david ospina", 
        "22 eder chaux",
        "12 aldair quintana"],
        "df":["2 jhon lucumi",
        "13 yerry Mina",
        "4 santiago arias",
        "6 william tesillo",
        "2 stefan medina",
        "17 frank fabra ",
        "23 davinson sanchez",
        "3 jeison murillo"],
        "ml":["18 stiven mendoza",
        "5 mateus uribe",
        "10 james rodriguez",
        "11 juan guillermo cuadrado",
        "8 yairo moreno",
        "14 luis diaz",
        "16 jefferson lerma"],
        "at":["10 steven alzate",
        "20 roger martinez",
        "9 alfredo morelos",
        "21 luis muriel"]}
    liste_joueurs_basketball_USA={"1/2":["4	Derrick White"],	
"2/1":['5	Donovan Mitchell'],	
"2/3":['6	Joe Harris',
'9	Jaylen Brown'],	
"2":['7	Marcus Smart'],	
"3/4":['8	Harrison Barnes'],	
"3":['10	Jayson Tatum',
'14	Khris Middleton'],	
"4/5":['11	Mason Plumlee'],	
"5":['12	Myles Turner',	
'13	Brook Lopez'],
"1":["15	Kemba Walker"]}

    liste_joueurs_baseball_USA={"Pitchers":[
' 3 Clayton Andrews',
'32 Brandon Dickson',
'29 Parker Dunshee',
'27 J. P. Feyereisen',
'43 Brian Flynn',
'31 Tanner Houck',
'-- Spencer Howard',
'29 Tyler Johnson',
'36 Wyatt Mills',
' 8 Penn Murfee',
'44 Cody Ponce',
'50 Brooks Pounders',
'38 Clayton Richard',
'-- Connor Seabold',
'37 Noah Song',
'16 Caleb Thielbar',
"33 Daniel Tillo"],'Catchers':[
'17 Taylor Gushue',
'14 Erik Kratz',
'10 Daulton Varsho'],'Infielders':[
'23 Alec Bohm',
' 2 C. J. Chatham',
' 1 Jake Cronenworth',
'15 Bobby Dalbec',
' 5 Xavier Edwards',
'12 Andrew Vaughn'],'Outfielders':[
'22 Jo Adell',
' 4 Mark Payton',
'35 Brent Rooker',
'11 Drew Waters'] }
    liste_joueurs_football_japon={"gb":
['Masaaki Higashiguchi',	
'Eiji Kawashima',
'Daniel Schmidt'],
"df":['Wataru Endo',
'Tomoaki Makino',	
'Yasuyuki Konno',
'Yuto Nagatomo',	
'Gotoku Sakai',	
'Genta Miura',	
'Hiroki Sakai',	
'Gen Shoji',	
'Maya Yoshida'],	
"ml":['Yosuke Ideguchi',	
'Shinji Kagawa',	
'Takashi Inui',	
'Takefusa Kubo', 
'Makoto Hasebe',	
'Hotaru Yamaguchi'],	
"at":['Genki Haraguchi',	
'Takuma Asano',	
'Keisuke Honda',	
'Yuya Kubo',	
'Shinji Okazaki',	
'Yuya Osako'
]}
    liste_joueurs_football_france={
"g":["16 Steve Mandada",
"1	Alphonse Areola",	
"23	Mike Maignan"],	
"d":["2	Benjamin Pavard",	
"21	Léo Dubois",	
"4	Raphaël Varane", 
"3	Presnel Kimpembe",	
"5	Clément Lenglet",	
"15	Kurt Zouma",	
"19	Lucas Digne",	
"22	Benjamin Mendy"],	
"m":["17	Moussa Sissoko",	
"13	N'Golo Kanté",	
"12	Corentin Tolisso",	
"6	Tanguy Ndombele",	
"14	Mattéo Guendouzi"],	
"at":["8	Thomas Lemar",	
"9	Olivier Giroud",	
"7	Antoine Griezmann",	
"10	Kylian Mbappé",	
"18	Nabil Fekir",	
"20	Wissam Ben Yedder"
]}
    liste_joueurs_handball_france={
"gb":["12	Vincent Gérard",	
"24	Wesley Pardin"],	
"ALG":[
"15	Mathieu Grébille",	
"21	Michaël Guigou"],
"ALD":[	
"19	Luc Abalo",	
"28	Valentin Porte"],
"ARD":[	
"5	Nedim Remili",	
"10	Dika Mem"],
"DEF":[	
"27	Adrien Dipanda"],
"ARG":[	
"7	Romain Lagarde",	
"8	Elohim Prandi"],
"DC":[	
"9	Melvyn Richardson",	
"13	Nikola Karabatic"],	
"P":[
"20	Cédric Sorhaindo", 	
"23	Ludovic Fabregas",	
"30	Nicolas Tournat"	
]}
    liste_joueurs_football_australie={
"G":[
"1	Mathew Ryan",	
"12	Adam Federici",	
"18	Andrew Redmayne"],
"D":[	
"2	Miloš Degenek",	
"3	Brad Smith",	
"4	Rhyan Grant",
"8	Bailey Wright",	
"16	Aziz Behich",
"17	Josh Risdon",
"19	Harry Souttar",	
"20	Trent Sainsbury"],
"M":[	
"5	Kenneth Dougall",	
"6	James Jeggo",
"11	Ajdin Hrustic",	
"13	Aaron Mooy",
"22	Jackson Irvine",	
"23	Tom Rogić"],
"A":[
"7	Craig Goodwin",	
"9	Martin Boyle",
"10	Adam Taggart",	
"14	Brandon Borrello",	
"15	Mitchell Duke",
"21	Awer Mabil"
]}
    liste_joueurs_football_algerie={
"G":[
"1	Azzedine Doukha",	
"16	Alexandre Oukidja",	
"23	Raïs M'Bolhi"],	
"D":[
"2	Aïssa Mandi",	
"3	Mehdi Tahrat",	
"4	Djamel Benlamri",	
"5	Ayoub Abdellaoui",	
"6	Maxime Spano-Rahou",	
"12	Réda Halaïmia",
"20	Youcef Atal",
"21	Ramy Bensebaini"],	
"M":[
"7	Riyad Mahrez", 
"8	Youcef Belaïli",	
"10	Sofiane Feghouli",	
"14	Haris Belkebla",
"17	Adlène Guedioura",	
"18	Adem Zorgane",
"19	Mehdi Abeid",
"22	Ismaël Bennacer"],	
"A":[
"9	Baghdad Bounedjah",	
"11	Andy Delort",
"13	Islam Slimani",	
"15	El Arabi Hilal Soudani"
]}
    #USA,Colombie,France,Japon
    competition_football_20ans={
       0: "competition de football mondial des -20ans 2019",
       d[0]:[
 "Colombie 1 5",#1
 "New_Zealand 1 4",#1		
 "Ukraine 4",#1
 "Panama	1",#1	
 	
 "Italy 1",#1
 "Poland 0",#1	

 "Argentina 2 4",#1
 "Mali 2 5",#1

 "France 2",#1	
 "United States 3",#1	

 "Uruguay 1",#1
 "Ecuador 3",#1	

 "Japan 0",#1
 "South Korea 1",#1	

 "Senegal 2",#1
 "Nigeria 1"],#1
 d[1]:[
 "Colombia 0",#2
 "Ukraine 1",#2
  "Italy 4",#2 
 "Mali 2",#2
 "United States 1",#2
"Ecuador 2",#2
"South Korea 3 3",#2
"Senegal 3 2"],#2
d[2]:[
"Ukraine 1",#3
"Italy 0",#3
"Ecuador 0",#3
"South Korea 1"],#3
d[3]:[
"Ukraine 3",#4
"South Korea 1"]}#4
 #colombie,france,Japon
    competition_football_mondial_2018={
    0:"competition de football du mondial 2018",
   d[0]:[
    " Uruguay 2",#1
 	" Portugal 1",	#1 
 	" France	4",#1
 	" Argentine	3",#1	 
 	" Brésil	2",#1
 	" Mexique 0",#1
 	" Belgique 3",#1
 	" Japon 2",#1	 
 	" Espagne 1 3",#1
 	" Russie	1 4",#1	 
 	" Croatie 1 3",#1
 	" Danemark 1 2",#1	 
 	" Suède 1",#1
 	" Suisse 0",#1
 	" Colombie 1 3",#1
 	" Angleterre 1 4"],#1
    d[1]:[
    " Uruguay 0",#2
 	" France	2",#2
    	" Brésil	1",#2
 	" Belgique 2",#2
     	" Russie	2 3",#2
 	" Croatie 2 4",#2
     	" Suède	0",#2
 	" Angleterre 2"],#2
    d[2]:[
     	" France	1",#3
 	" Belgique 0",#3
     	"Croatie	2",#3
 	" Angleterre 1"],#3
    d[3]:[
     	" France	4",#4
 	" Croatie 2"]}#4
    competition_football_australie=[
        "Australie : A-League 2019",
        "Vendredi 06 décembre 2019",
"09:30	Terminé	Melbourne HeartMelbourne Heart0 - 3Perth GloryPerth Glory",	 
"Samedi 07 décembre 2019",
"07:00	Terminé	Wellington PhoenixWellington Phoenix2 - 1Western Sydney WanderersWestern Sydney Wanderers",	 
"09:30	Terminé	SydneySydney5 - 1Brisbane RoarBrisbane Roar",
"Dimanche 08 décembre 2019",
"06:00	Terminé	Western UnitedWestern United3 - 1Melbourne VictoryMelbourne Victory",	 
"08:00	Terminé	Adelaide UnitedAdelaide United2 - 1Newcastle JetsNewcastle Jets",	 
"Australie : National Youth League - Classement"
    ]
    competition_football_algerie=[
        "algerie division 1 2019",
        "Samedi 07 décembre 2019",
"15:00	Terminé	NA Hussein DeyNA Hussein Dey0 - 1NC MagraNC Magra",	 
"15:00	Terminé	CR BelouizdadCR Belouizdad1 - 0JS SaouraJS Saoura",	 
"15:00	Terminé	USM Bel AbbèsUSM Bel Abbès3 - 1MC AlgerMC Alger", 
"15:00	Terminé	ES SétifES Sétif4 - 0AS Aïn M'lilaAS Aïn M'lila",	 
"16:00	Terminé	US BiskraUS Biskra0 - 0CA Bordj Bou ArreridjCA Bordj Bou Arreridj"

    ]
    competition_handball_2017={
    0:"competition handball 2017",
    "Huitièmes de finale":[
    " Espagne 28",#1
    " Brésil 27",#1
    " Égypte 19",#1
 	" Croatie 21",#1
 	
    " Macédoine	24",#1
 	" Norvège 34",#1
    " Danemark	25",#1
 	" Hongrie 27",#1
    " France 31",#1
 	 
 	" Islande 25",#1
    " Suède 41",#1
 	" Biélorussie 22",#1
    " Slovénie	32",#1
 	" Russie 26",#1
    " Allemagne 20",#1	 
 	" Qatar	21"],#1	 	
 	
    "Quarts de finale":[	
    "Espagne 29",#2
    "Croatie 30",#2
    "Norvège 31",#2
 	"Hongrie 28",#2 
 	
    "France 33",#2
 	"Suède 30",#2 
 	"Slovénie 32",#2
 	"Qatar 30"],#2
    
    "Demi-finales":[ 
 	"Croatie 25",#3
 	"Norvège 28",#3
    "France 31",#3
 	"Slovénie 25"],#3
 	
    "Finale":[	 
 	"Norvège 26",#4
 	"France 33"],#4
    "Troisième place":[
 	"Croatie 30",#4	
    "Slovénie 31"]} #4 
  

    return {'Colombie':{'baseball':liste_joueurs_baseball_colombie,'football':liste_joueurs_football_colombie,"competition_football":[competition_football_20ans,competition_football_mondial_2018],"competition_baseball":[]},
    'USA':{'baseball':liste_joueurs_baseball_USA,'basketball':liste_joueurs_basketball_USA,"competition_football":[competition_football_20ans],"competition_basketball":[],"competition_baseball":[]},
    'Japon':{'football':liste_joueurs_football_japon,"competition_football":[competition_football_20ans,competition_football_mondial_2018]},
    'France':{'football':liste_joueurs_football_france,'handball':liste_joueurs_handball_france,"competition_football":[competition_football_mondial_2018,competition_football_20ans],"competition_handball":[competition_handball_2017]},
    'Australie':{'football':liste_joueurs_football_australie,"competition_football":[competition_football_australie]},
    'Algérie':{'football':liste_joueurs_football_algerie,"competition_football":[competition_football_algerie]}}