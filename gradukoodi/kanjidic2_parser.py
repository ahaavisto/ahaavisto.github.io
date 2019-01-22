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
with open ('tuloksia/jarjestys_BCCWJ_alku.txt', 'r') as f: #atm ottaa vain alun
	for rivi in f:
		kanit.append(rivi.split()[0])

def add_enkku(entry):
	juttu = ""
	try:
		enkut = entry.find('reading_meaning').find('rmgroup').findall('meaning')
		juttu += '"'
		for enkku in enkut:
			if enkku.attrib == {}:
				juttu += enkku.text + ', '
		juttu += '";'
	except AttributeError:
		juttu += "Ei tunnettuja käännöksiä;"
	return juttu
	
def add_lukutavat(entry):
	juttu = ""
	try:
		yomit = entry.find('reading_meaning').find('rmgroup').findall('reading')
		juttu += '"'
		for yomi in yomit:
			if yomi.attrib['r_type'] == 'ja_kun' or yomi.attrib['r_type'] == 'ja_on':
				juttu += yomi.text + '\n'
		juttu = juttu[:-2] #pois vika enter
		juttu += '";'
	except AttributeError:
		juttu += "Ei tunnettuja ääntämyksiä;"
	return juttu

	
sanasto = []
with open ('yhdyssanat_hira.txt', 'r') as f:
	for rivi in f:
		sanasto.append(rivi)

hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"	
katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
hiraganaksi = str.maketrans(katakana, hiragana)

def valkkaa_sanastoa(kanji):
	'''kaivaa viisi yleisintä sanaa, joissa kys. kanji esiintyy''' #TODO pois tuplat kun samalla sanalla useampi POS = useampi entry?
	ret = '"'
	setti = ("Ei tunnettuja yleisiä sanoja","","0")
	lista_sanoja = list()
	for rivi in sanasto:
		if kanji in rivi.split()[0]:
			setti = (rivi.split()[0], rivi.split()[1], int(rivi.split()[3]))
			lista_sanoja.append(setti)
	lista_sanoja = sorted(lista_sanoja, key=lambda setti: setti[2]) #yleisyysjärkkään yhdyssanat
	i = 0
	for sana in lista_sanoja:
		ret += sana[0] + "[" + sana[1] + "] (" + str(sana[2]) + ")\n"
		#kanjisana ja hakasulkuihin sen ääntämys, koska ankin furiganakomento. Perään frekvenssi.
		ret += etsi_esimerkkilauseet(sana[0]) + '\n'
		i += 1
		if i > 4: #lisätään max viisi yleisintä
			break
	return ret + '"'
	
'''Tatoeba-tietokannasta ekat lauseet, joissa kanjisana esiintyy'''
def etsi_esimerkkilauseet(sana):
	i = 0
	lauseet = ""
	with open ('kaannokset.tsv', 'r') as f:
		for rivi in f:
			if sana in rivi:
				i += 1
				lauseet += rivi
				if i == 3: #kuinka monta lausetta halutaan
					return lauseet
	return "Tietokannasta ei löytynyt esimerkkilauseita"

'''Haetaan esimerkkilauseet ja sitten lainausmerkit ympärille'''
def esimerkkilauseet(merkki):
	lista = etsi_esimerkkilauseet(merkki)
	string = ';"'
	for entry in lista:
		string += entry
	string += '";'
	return string
	
#luetaan komponenttilista sanakirjaksi
komp_sanakirja = {}
with open ('ids_jooyoo+_chine_muokattu.txt', 'r') as f:
	for rivi in f:
		komp_sanakirja[rivi.split(' ')[0]] = rivi.split(' ')[1]
	
'''Lisää lista merkin komponenteista'''
def etsi_komponentit(merkki):
	if merkki in komp_sanakirja:
		return " Komponentit: " + komp_sanakirja[merkki] + ";"
	else:
		return "Ei tunnettuja komponentteja, jossain on siis bugi;"

def luo_anki():
	'''luo ankille maistuvan txt-filun merkeistä ja niiden lukutavoista'''
	anki = {}
			
	for kanji in kanit:
		lista = ''
		for entry in juuri.findall('character'):		
			if kanji == entry.find('literal').text:
				lista += kanji + ";"
				lista += etsi_komponentit(kanji)
				lista += add_enkku(entry)
				lista += add_lukutavat(entry)
				lista += valkkaa_sanastoa(kanji)
				lista += "\n"
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
	with open ('tuloksia/jarjestys_BCCWJ.txt', 'r') as f:
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
		f.write('<meta charset="UTF-8"> ') #merkistökoodaus kuntoon
		for rivi in lista:
			if ('0' or 0) not in rivi: #ei kirjoiteta vikaa riviä 
				f.write(str(rivi))
				

def katakana_hiraganaksi():
	hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"	
	katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
	hiraganaksi = str.maketrans(katakana, hiragana)
	kirjoitettava = ""
	with open ('yhdyssanat1.txt', 'r') as f:
		for rivi in f:
			rivi = rivi.translate(hiraganaksi)
			kirjoitettava += str(rivi)
	with open ('yhdyssanat_hira.txt', 'w') as f:
		f.write(kirjoitettava)

KANJI_DIV = '<div class="panel panel-info">\n'
COMPONENT_DIV = '<div class="panel panel-warning">\n'
HEADER_DIV = '<div class="panel-heading">\n'
BODY_DIV = '<div class="panel-body">\n'
DIV_CLOSE = '</div>\n'

def luo_html():
	html = ""
	for kanji in kanit:
			lista = ''
			for entry in juuri.findall('character'):		
				if kanji == entry.find('literal').text:
					lista += KANJI_DIV + HEADER_DIV + kanji + DIV_CLOSE
					lista += BODY_DIV + etsi_komponentit(kanji)
					lista += add_enkku(entry)
					lista += add_lukutavat(entry)
					lista += valkkaa_sanastoa(kanji)
					lista += DIV_CLOSE + DIV_CLOSE
					lista = lista.replace(';', '')
					#lista = lista.replace('\n', '\n<br>')
			for rivi in lista.split('\n'):
				html += rivi + '<br>\n'
	print(html)
		
'''
pääohjelma alkaa
'''

#tulosta_fancysti()

#katakana_hiraganaksi()

#luo_anki()

luo_html()

#__________________

#print(juuri.tag)
