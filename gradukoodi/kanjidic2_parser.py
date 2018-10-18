import xml.etree.ElementTree as ET

puu = ET.parse('kanjidic2.xml')
juuri = puu.getroot()

sanakirja = {}

def lisää_vetomaarat():
	with open ('ids_jooyoo+_chine.txt', 'r') as f:
		for rivi in f:
			avain = rivi.split()[0]
			sanakirja[avain] = 5.5

	for kanji in juuri.findall('character'):
		merkki = kanji.find('literal').text
		if merkki in sanakirja:
			vedot = kanji.find('misc').find('stroke_count').text
			sanakirja[merkki] = vedot

	with open ('vedot.txt', 'w') as f:
		for avain,arvo in sanakirja.items():
			f.write(avain + ' ' + str(arvo) + '\n')
			

kanit = []	
with open ('jarjestys_BCCWJ.txt', 'r') as f:
	for rivi in f:
		kanit.append(rivi.split()[0])

def luo_anki():
	'''luo ankille maistuvan txt-filun merkeistä ja niiden lukutavoista'''
	anki = {}
	'''kanit = []	
	with open ('jarjestys_BCCWJ.txt', 'r') as f:
		for rivi in f:
			kanit.append(rivi.split()[0])'''
			
	for kanji in kanit:
		lista = ''
		for entry in juuri.findall('character'):
			if kanji == entry.find('literal').text:
				try:
					enkut = entry.find('reading_meaning').find('rmgroup').findall('meaning')
					lista += '"'
					for enkku in enkut:
						if enkku.attrib == {}:
							lista += enkku.text + '\n'
					lista += '";'
				except AttributeError:
					lista += "Ei käännöstä;"
										
				lista += kanji + ";"	
					
				try: #kaikilla ei oo reading r_type="ja_on"
					lukutavat = entry.find('reading_meaning').find('rmgroup').findall('reading')
					lista += '"'
					for tapa in lukutavat:
						if tapa.attrib['r_type'] == 'ja_kun' or tapa.attrib['r_type'] == 'ja_on':
							lista += tapa.text + '\n'
					lista += '"'
				except AttributeError:
					lista += '"Ei lukutapoja"'
				lista += ";\n"
				#print(lista)
				
		anki[kanji] = lista
	print_anki(anki)
				
def print_anki(printattava):
	with open ('anki.txt', 'w') as f:
		for kanji in kanit:
			f.write(printattava[kanji])
				

def tulosta_fancysti():
	'''Tulostaa merkit siten, että ei jooyoo on värjätty ja enkkumerkitys mukana'''
	kanit = []
	lista = [0] * 2800 #taikaluku, vähän isompi kuin kanjien määrä
	loytyi = False
	with open ('jarjestys_BCCWJ.txt', 'r') as f:
		for rivi in f:
			kanit.append(rivi.split()[0])
			
	for kanji in kanit:
		for entry in juuri.findall('character'):
			if kanji == entry.find('literal').text: #jos on kanjidicissa
				loytyi = True
				grade = 9 #default siis ei-jooyoo
				enkku = "ei käännöstä" #default
				try: #kaikilla ei oo
					grade = entry.find('misc').find('grade').text
				except AttributeError:
					pass
					#print(kanji, 'no grade')
				try: #kaikilla ei oo
					enkku = entry.find('reading_meaning').find('rmgroup').find('meaning').text #eka enkku
				except AttributeError:
					pass
					#print(kanji, 'no translation')
				if int(grade) < 7 or int(grade) == 8: #on jooyoo-kani
					lista.insert(kanit.index(kanji), kanji + ' ' + enkku + '</br>')
				else: #harmaaksi jos ei jooyoo
					lista.insert(kanit.index(kanji), '<span style="color:DarkGrey">' + kanji + ' ' + enkku + '</span></br>')
		if not loytyi:
			#harmaaksi jos ei jooyoo
			lista.insert(kanit.index(kanji), '<span style="color:DarkGrey">' + kanji + ' ei käännöstä' + '</span></br>')	
		loytyi = False
	
	with open ('fancy_lista.html', 'w') as f:
		for rivi in lista:
			if ('0' or 0) not in rivi: #ei kirjoiteta vikaa riviä 
				f.write(str(rivi))
				


'''
pääohjelma alkaa
'''

#tulosta_fancysti()

luo_anki()

#__________________

#print(juuri.tag)
'''
for lapsi in juuri:
	#if lapsi.attrib
	for sisalto in lapsi:
		#print(sisalto.tag, sisalto.attrib) #printtaa 1. tason kenttien nimet
		for sis in sisalto:
			print(sis.tag, sis.tostring())


lista = []
lista.append('本')

#print(ET.tostring(juuri, encoding='utf8').decode('utf8')) #printtaa kaiken

#tämä on se oikeasti hyödyllinen asia
for juttu in juuri.iter('literal'):
	if juttu.text in lista:
		print('jee')
	#print(juttu.text)
									
for juttu in juuri.findall("./character/radical[@cp_value='672c']"): #ei toimi, koska ??
	print('moimoi')
	print(juttu.text)

#jos halutaan printata vanhempi	niin ...
#for movie in root.findall("./genre/decade/movie/format[@multiple='Yes']..."):
#    print(movie.attrib)

'''
