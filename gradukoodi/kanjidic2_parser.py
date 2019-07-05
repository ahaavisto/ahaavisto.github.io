import xml.etree.ElementTree as ET

puu = ET.parse('kanjidic2.xml')
juuri = puu.getroot()

sanakirja = {}

#SOURCE_FILE = 'tuloksia/jarjestys_BCCWJ.txt'
#SOURCE_FILE = 'tuloksia/jarjestys_BCCWJ_alku.txt'
SOURCE_FILE = 'tuloksia/muokattu_opiskelujarjestys.txt'
TSV_FILE = 'kirja/tuloste.tsv'

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

def get_vetomaara(entry):
	return entry.find('misc').find('stroke_count').text

kanit = []	
with open (SOURCE_FILE, 'r') as f:
	for rivi in f:
		kanit.append(rivi.split()[0])

def add_enkku(entry):
	juttu = ""
	try:
		enkut = entry.find('reading_meaning').find('rmgroup').findall('meaning')
		juttu += 'Kanjin merkityksiä englanniksi: '
		for enkku in enkut:
			if enkku.attrib == {}:
				juttu += enkku.text + ', '
		juttu = juttu.strip(" ")
		juttu = juttu.strip(",")
		juttu += ';'
	except AttributeError:
		juttu += "Ei tunnettuja englanninnoksia;"
	return juttu
	
def add_lukutavat(entry):
	lukutavat = []
	try:
		yomit = entry.find('reading_meaning').find('rmgroup').findall('reading')
		for yomi in yomit:
			if yomi.attrib['r_type'] == 'ja_kun' or yomi.attrib['r_type'] == 'ja_on':
				lukutavat.append(yomi.text)
	except AttributeError:
		lukutavat.append("Ei tunnettuja ääntämyksiä;")
	return lukutavat
	
sanasto = []
with open ('yhdyssanat_hira.txt', 'r') as f:
	for rivi in f:
		sanasto.append(rivi)

hiragana = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"	
katakana = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
hiraganaksi = str.maketrans(katakana, hiragana)

def valkkaa_sanastoa(kanji, tuleeko_lauseita):
	'''kaivaa viisi yleisintä sanaa, joissa kys. kanji esiintyy''' #TODO pois tuplat kun samalla sanalla useampi POS = useampi entry?
	ret = []
	setti = ("Ei tunnettuja yleisiä sanoja","","0")
	lista_sanoja = list()
	for rivi in sanasto:
		if kanji in rivi.split()[0]:
			setti = (rivi.split()[0], rivi.split()[1], int(rivi.split()[3]))
			lista_sanoja.append(setti)
	lista_sanoja = sorted(lista_sanoja, key=lambda setti: setti[2]) #yleisyysjärkkään yhdyssanat
	i = 0
	for sana in lista_sanoja:
		ret.append(sana[0] + "[" + sana[1] + "] (" + 'yleisyys: ' + str(sana[2]) + ".)")
		#kanjisana ja hakasulkuihin sen ääntämys, koska ankin furiganakomento. Perään frekvenssi.
		if tuleeko_lauseita: ret.append(etsi_esimerkkilauseet(sana[0]) + '\n')
		i += 1
		if i > 4: #lisätään max viisi yleisintä
			break
	return ret
	
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
		komp_sanakirja[rivi.split(' ')[0]] = rivi.split(' ')[1][:-1]
		
'''Lisää lista merkin komponenteista'''
def etsi_komponentit(merkki):
	if merkki in komp_sanakirja:
		return komp_sanakirja[merkki]
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
				lista += "Komponentit: " + etsi_komponentit(kanji) + ";"
				lista += add_enkku(entry)
				lista += '\n'.join(add_lukutavat(entry))
				lista += '"' + ', '.join(valkkaa_sanastoa(kanji, False)) + '"\n'
				lista += "\n\n"
		anki[kanji] = lista
	print_anki(anki)
				
def print_anki(printattava):
	with open ('anki_uusi.txt', 'w') as f:
		for kanji in kanit:
			f.write(printattava[kanji])
				
def tulosta_vain_jooyoo():
	kanit = []
	lista = ""
	with open (SOURCE_FILE, 'r') as f:
		for rivi in f:
			kanit.append(rivi.split()[0])
	for kanji in kanit:
		for entry in juuri.findall('character'):
			if kanji == entry.find('literal').text:
				if onko_jooyoo(entry):
					lista += kanji + '\n'
	with open ('muok_listan_jooyoo_kanjit.txt', 'w') as f:
		f.write(lista)

def tulosta_fancysti():
	'''Tulostaa merkit siten, että ei jooyoo on värjätty ja enkkumerkitys mukana'''
	kanit = []
	lista = [0] * 2700 #taikaluku, vähän isompi kuin kanjien määrä
	loytyi = False
	with open (SOURCE_FILE, 'r') as f:
		for rivi in f:
			kanit.append(rivi.split()[0])
			
	for kanji in kanit:
		for entry in juuri.findall('character'):
			if kanji == entry.find('literal').text: #jos on kanjidicissa
				loytyi = True
				enkku = "ei käännöstä" #default
				try: #kaikilla ei oo
					enkku = entry.find('reading_meaning').find('rmgroup').find('meaning').text #eka enkku
				except AttributeError:
					pass
				if onko_jooyoo(entry):
					lista.insert(kanit.index(kanji), kanji + ' ' + enkku + '</br>')
				else: #harmaaksi jos ei jooyoo
					lista.insert(kanit.index(kanji), '<span style="color:DarkGrey">' + kanji + ' ' + enkku + '</span></br>')
		if not loytyi:
			#harmaaksi jos ei jooyoo
			lista.insert(kanit.index(kanji), '<span style="color:DarkGrey">' + kanji + ' ei käännöstä' + '</span></br>')	
		loytyi = False
	
	with open ('tuloksia/fancy_lista.html', 'w') as f:
		f.write('<meta charset="UTF-8"> ') #merkistökoodaus kuntoon
		for rivi in lista:
		    f.write(str(rivi))
			#if ('0' or 0) not in rivi: #ei kirjoiteta vikaa riviä 
			#	f.write(str(rivi))
				

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

def onko_jooyoo(entry):
	try: #kaikilla ei oo
		grade = entry.find('misc').find('grade').text
	except AttributeError:
		grade = 9 #oletetaan, että ei-jooyoo
	if int(grade) < 7 or int(grade) == 8: #on jooyoo-kani
		return True
	else:
		return False

#wikimedia commonsin kuvat mukaan. Alustava toteutus ...joka toimii huonosti
def vetojarjestys(kanji):
	img_alku = '<img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/'
	img_loppu = '-order.gif" alt="tässä pitäisi näkyä merkin vetojärjestys"><br>\n'
	return img_alku + kanji + img_loppu

HTML_ALKU = '''
<!DOCTYPE html>\n
<meta charset="utf-8">\n
<html>\n
<head>\n
</head>\n
<body>\n
\t<!-- seuraavat kolme linkkiä liittyvät bootstrap-kirjastoon-->\n
\t<!-- Latest compiled and minified CSS -->\n
\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"\n
\tcrossorigin="anonymous">\n
\t<!-- Optional theme -->\n
\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"\n
\tcrossorigin="anonymous">\n
\t<!-- Latest compiled and minified JavaScript -->\n
\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"\n
\tcrossorigin="anonymous"></script>\n
\t<h1>Kanjilista</h1>\n
\t<div>Sinisellä merkitty jooyoo-kanjit, keltaisella vain komponentteina esiintyvät. Listaa ei ole tarkistettu tai muokattu käsin vielä lainkaan, vaan se sisältää vain suoraa tietokannoista generoitua raakasisältöä. Datan lähteet: <a href="https://github.com/ahaavisto/ahaavisto.github.io">github.com/ahaavisto/ahaavisto.github.io</a> </div>
'''
KANJI_DIV = '<div class="panel panel-info">\n'
COMPONENT_DIV = '<div class="panel panel-warning">\n'
HEADER_DIV = '<div class="panel-heading"><h1>\n'
BODY_DIV = '<div class="panel-body">\n'
FONT_DIV = '<div class="jpn">'
DIV_CLOSE = '</div>\n'
HTML_LOPPU = '</body>\n</html>'

def luo_html():
	html = ""
	i = 1
	for kanji in kanit:
			lista = ''
			for entry in juuri.findall('character'):		
				if kanji == entry.find('literal').text:
					if onko_jooyoo(entry):
						lista += KANJI_DIV 
					else:
						lista += COMPONENT_DIV #eri väri, jos vain komponentti eikä jooyookani
					lista += HEADER_DIV + FONT_DIV + kanji + '</h1>' + DIV_CLOSE + DIV_CLOSE
					lista += BODY_DIV + FONT_DIV + "Komponentit:" + etsi_komponentit(kanji) + DIV_CLOSE
					lista += str(i) + '. merkki\n'
					#lista += vetojarjestys(kanji)
					lista += add_enkku(entry).replace('"', '') + '\n'
					lista += ','.join(add_lukutavat(entry)) + '\n'
					if onko_jooyoo(entry):
					    lista += '\n'.join(valkkaa_sanastoa(kanji, True))
					lista += DIV_CLOSE + DIV_CLOSE
					lista = lista.replace(';', '')
					#lista = lista.replace('\n', '\n<br>')
			for rivi in lista.split('\n'):
				html += rivi + '<br>\n'
			i += 1
	print(HTML_ALKU, html, HTML_LOPPU)

taul = []	
	
def lue_tsv():
	with open (TSV_FILE, 'r') as f:
		for rivi in f:
			taul.append(rivi.split('\t'))

def lue_tsv_ja_lisaa_komponentit():
	with open ('../kanji/pelkka_jarjestys_komponentein.txt', 'r') as f:
		for rivi in f:
			taul.append(rivi.split('\t')[1][0]) #taulukkoon pelkkä kanji
	
	kirjan_data = []
	with open (TSV_FILE, 'r') as f:
		for rivi in f:
			kirjan_data.append(rivi.split('\t'))
	i = 0
	print(kirjan_data[0])
	
	for rivi in taul:
		for entry in kirjan_data:
			if entry[0] == rivi[0]:
				print(entry[0])
				taul[i] = entry
			else:
				taul[i] = rivi
		i += 1
	print(taul)
	
'''kirjan tsv-muotoa varten täytetään taulukko kanjidic-tietokannalla'''		
def luo_kentat():
	for entry in juuri.findall('character'):		
		for rivi in taul:
			kanji = rivi[0]
			if kanji == entry.find('literal').text:
				rivi[3] = etsi_komponentit(kanji)
				if rivi[6] == '': rivi[6] = add_enkku(entry) #lisätään enkku vain, jos ei ollut ennestään jotain
				if rivi[4] == '': rivi[4] = ','.join(add_lukutavat(entry))
				if rivi[7] == '': rivi[7] = ','.join(valkkaa_sanastoa(kanji, False))
				#sekalaiset:
				rivi[23] = 'Merkin vetojen lukumäärä: ' + get_vetomaara(entry) + ' <br> <a href="https://jisho.org/search/' + kanji + '%23kanji" target="_blank">'+ kanji + ' Jisho-sanakirjassa</a>'

def tee_tsv():
	luo_kentat()
	with open ('kirja/tuloste_komponentein.tsv', 'w') as f:
		for rivi in taul:
			for juttu in rivi:
				if juttu is not '\n':
					f.write(juttu + '\t')
			f.write('\n')

'''
pääohjelma alkaa
'''

#lue_tsv()
lue_tsv_ja_lisaa_komponentit()

tee_tsv()

#tulosta_fancysti()

#katakana_hiraganaksi()

#luo_anki()

#luo_html()

#tulosta_vain_jooyoo()

#__________________

#print(juuri.tag)
