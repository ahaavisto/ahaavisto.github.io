import re, random

def poista_ids_turhat(lue, kirjoita):
	'''netin ids-filusta pois turhat jutut'''
	ideographic_description_characters = [u'\u2FF0', u'\u2ff1', u'\u2ff2', u'\u2ff3', u'\u2ff4', u'\u2ff5', u'\u2ff5', u'\u2ff6', u'\u2ff7', u'\u2ff8', u'\u2ff9', u'\u2ffa', u'\u2ffb'] #niiden unicodekoodit, poistetaan ids-listasta
	with open (kirjoita, 'w') as kirjoitettava :
		with open (lue, 'r') as f:
			for rivi in f:
				for merkki in ideographic_description_characters:
					rivi = rivi.replace(merkki,'')
				rivi = rivi.split('[')[0] #poistetaan rivin lopun vaihtoehtojutut, turhia(?)
				kirjoitettava.write(rivi.split()[1] + ' ' + rivi.split()[2] + '\n')
	
	
def poista_duplikaatit(trimmattava):
	trimmattu = set(trimmattava)
	return ''.join(trimmattu)

komponenttisanakirja = {}
sanakirja_lopullinen = {}

def luo_komponenttisanakirja(lue):
	with open (lue, 'r') as f:
		for rivi in f:
			avain = rivi.split()[0]
			arvo = rivi.split()[1]
			komponenttisanakirja[avain] = arvo

def rekursoi_komponentit(merkki):
	komponentit = komponenttisanakirja[merkki]	
	if len(komponentit) == 1: #oli primitiivi
		return set(merkki)	
	lista = set()
	for osa in komponentit:
		lista.add(osa)
		lista = lista.union(rekursoi_komponentit(osa))
	return(lista)

def generoi_komponentit(lue, kirjoita):
	'''generoidaan ids-listaan kaikki komponentit eli käydään rekursiivisesti läpi'''
	luo_komponenttisanakirja(lue) #luetaan filu dictionaryksi
	for merkki in komponenttisanakirja:
		sanakirja_lopullinen[merkki] = rekursoi_komponentit(merkki)

	with open (kirjoita, 'w') as f:
		for avain,arvo in sanakirja_lopullinen.items():
			f.write(avain + ' ' + ''.join(arvo) + '\n')

def lue_stroke_count():
	sanakirja = {}
	with open ('vedot.txt', 'r') as f:
		for rivi in f:
			sanakirja[rivi.split(' ')[0]] = rivi.split(' ')[1]
			#sanakirjaan avaimeksi merkki ja arvoksi vetojen määrä
	return sanakirja
	
def poista_ei_jooyoo(lue, kirjoita):
	'''poista ids -listasta ne jotka ei ole jooyoo
	onnistuu näin koska kanji_strokes.csv filussa on tasan jooyoo-kanjit''' 
	#TODO muokkaa  koska stroke countia ei voi lukea kys filusta
	#vedot = lue_stroke_count()	
	kirjoitettava = ""	
	with open (lue, 'r') as f:
		for rivi in f:
			if rivi.split()[0] in vedot: #koska kanji_strokes.csv:ssa tasan jooyoo
				kirjoitettava += rivi
				
	with open (kirjoita, 'w') as f:
		f.write(kirjoitettava)
	
def lisaa_ei_jooyoo_komponentit(lue, kirjoita):
	jooyoo_kanit = ""
	kirjoitettava = set()	
	with open (lue, 'r') as f:
		for rivi in f:
			jooyoo_kanit += rivi.split()[0]
	
	with open (lue, 'r') as f:
		for rivi in f:
			for komponentti in re.findall(r'&[^;]+;|[^&]', rivi.split()[1]):
				if komponentti not in jooyoo_kanit:
					kirjoitettava.add(komponentti + ' ' + komponentti + '\n')
				kirjoitettava.add(rivi)
	
	with open (kirjoita, 'w') as f:
		f.write(''.join(kirjoitettava))	

		
def get_vetomaara(merkki):
	y = 0.1 #y vakio kuten artikkelissa
	if merkki in vedot:
		paino = 1 + float(vedot[merkki])*y
	else:
		print("vetomäärää ei löytynyt:", merkki)
		paino = 5.5
	return paino
	
#tässä tallennetaan dictionaryksi ids-komponenttilista
#TODO tääkin tiedosto parametriksi!
ids = {}
with open ('ids_jooyoo+_chine_muokattu.txt', 'r') as f:
	for rivi in f:
		ids[rivi.split(' ')[0]] = rivi.split()[1]		

def laske_painot(lue, kirjoita):
	'''kuten cost artikkelissa, eli primitiiveille 1+y*vetojen_määrä, ja yhdistelmille eri vaihtoehdot -1'''
	painot = {}
	
	for merkki in ids: #ids globaali
		if merkki == ids[merkki]: #on primitiivi, jos on oma komponenttinsa
			paino = get_vetomaara(merkki)
		else:
			paino = len(re.findall(r'&[^;]+;|[^&]', ids[merkki])) -1 #shaapun taikaregex
		painot[merkki] = paino
	
	with open (kirjoita, 'w') as f:
		for avain,arvo in painot.items():
			f.write(avain + ' ' + str(arvo) + '\n')

freq_sanakirja = {}
def lue_frekvenssit_sanakirjaksi(freq):
	with open(freq, 'r') as f:
		for rivi in f:
			freq_sanakirja[rivi.split('\t')[0]] = rivi.split('\t')[1][:-1]

def lue_frek(merkki):
	if merkki in freq_sanakirja:
		return freq_sanakirja[merkki]

def laske_centrality(lue, kirjoita):
	centrality = {}
	kirjoitettava = {}
	
	with open(lue, 'r') as f:
		for rivi in f:
			merkki = rivi.split()[0]
			paino = float(rivi.split()[1])
			freq = lue_frek(merkki)
			paino = paino or 1 #jos paino on 0 koska moka aiemmissa laskuissa ts. algon kopsauksessa, purkkafix paras fix
			if freq is not None:
				centrality[merkki] = float(freq) / float(paino)
			else:
				centrality[merkki] = 0.1 #joku random pieni jos niin harvinainen, ettei mukana frekvenssilistassa

	with open (kirjoita, 'w') as f:
		sortattu = [(k, centrality[k]) for k in sorted(centrality, key=centrality.get, reverse=False)]
		for k, v in sortattu:
			f.write(str(k) + ' ' + str(v) + '\n')

def etsi_merkin_indeksi(data, merkki):
	for rivi in data:
		if merkki in rivi:
			if merkki in rivi.split(" ")[0]:
				return data.index(rivi)

jarjestettavat = []

def luo_jarjestettavat(lue):
	with open (lue, 'r') as f:
		for rivi in f:
			jarjestettavat.append(rivi)
			
def algon_rekursio(merkki, merkin_indeksi):
	global jarjestettavat
	#print(merkki, merkin_indeksi)
	if len(re.findall(r'&[^;]+;|[^&]', ids[merkki])) < 2:
		return
	for komponentti in re.findall(r'&[^;]+;|[^&]', ids[merkki]):
		komponentin_indeksi = etsi_merkin_indeksi(jarjestettavat, komponentti)
		#print(merkki, merkin_indeksi, komponentti, komponentin_indeksi)
		if komponentin_indeksi < merkin_indeksi: #vaihdetaan
			komponentin_centrality = jarjestettavat[komponentin_indeksi].split()[1]
			jarjestettavat.pop(komponentin_indeksi)
			jarjestettavat.insert(merkin_indeksi, komponentti + ' ' + komponentin_centrality + '\n')
			komponentin_indeksi = etsi_merkin_indeksi(jarjestettavat, komponentti)
		algon_rekursio(komponentti, komponentin_indeksi)

				
def algo(kirjoita):	
	global jarjestettavat
	for rivi in jarjestettavat:
		merkki = rivi.split()[0]
		#print(merkki,etsi_merkin_indeksi(jarjestettavat, merkki))
		algon_rekursio(merkki, etsi_merkin_indeksi(jarjestettavat, merkki))
		
		merkin_indeksi = etsi_merkin_indeksi(jarjestettavat, merkki)
	with open (kirjoita, 'w') as f:
		jarjestettavat = reversed(jarjestettavat)
		for rivi in jarjestettavat:
			f.write(rivi)

def printtaa_listana(lue, keskeisyys, frekvenssi, kirjoita):
	jarkka = ['index \talgo \tfreq \tcentrality']
	with open (lue, 'r') as f:
		for i, rivi in enumerate(f):
			jarkka.append(str(i+1) + '\t\t' + rivi.split()[0])
		
	with open (frekvenssi, 'r') as freq:
		for i, rivi in enumerate(freq):
			if i > 1200: #TODO vähemmän taikanumeroksi
				break		
			jarkka[i+1] += '\t\t' + rivi.split('\t')[0] #freq_bcc versio TODO fiksaa
			#jarkka[i+1] += '\t\t' + rivi.split(',')[0][2] #freq.txt versio
	
	centrality = []
	with open (keskeisyys, 'r') as centr:
		for rivi in centr:
			centrality.append(rivi.split()[0])
	centrality = reversed(centrality)
	for i, rivi in enumerate(centrality):
		if i > 1200: #TODO vähemmän taikanumeroksi
			break
		jarkka[i+1] += '\t\t' + rivi.split()[0]
	
	with open (kirjoita, 'w') as f:
		for juttu in jarkka:
			f.write(juttu + '\n')	


def printtaa_pelkka_algon_tulos(lue, kirjoita):
	with open (lue, 'r') as f:
		with open (kirjoita, 'w') as kirjoita:
			for i, rivi in enumerate(f):
				kirjoita.write(str(i+1) + '\t' + rivi.split()[0] + '\n')
				

			
'''pääohjelma alkaa'''

vedot = lue_stroke_count()
lue_frekvenssit_sanakirjaksi('freq_BCCWJ.txt')
'''
#trimmaa netistä otettu ids-lista
poista_ids_turhat('ids_chine.txt', 'ids_trimmatut_chine.txt')

#rekursiivisesti päivitetään lista
#ei käytetä chine-datan kanssa
#generoi_komponentit('ids_trimmatut.txt', 'ids_kaikki_komponentit.txt')
'''

#poistetaan ei-jooyoo-kanjit datasta
#poista_ei_jooyoo('ids_trimmatut_chine.txt', 'ids_jooyoo_chine.txt')

#lisätään ne komponentit, jotka ovat jooyoo:n osia mutta eivät itse jooyoo
#lisaa_ei_jooyoo_komponentit('ids_jooyoo_chine.txt', 'ids_jooyoo+_chine.txt')

#laske_painot('ids_jooyoo+_chine_muokattu.txt', 'painot_BCCWJ.txt') #atm ei käytä filua koska refaktorointi

#laske_centrality('painot_BCCWJ.txt', 'tuloksia/centrality_of_kanjis_BCCWJ.txt')

luo_jarjestettavat('tuloksia/centrality_of_kanjis_BCCWJ.txt') #taulukoksi myöhempään käyttöön

algo('tuloksia/jarjestys_BCCWJ.txt') #printtaa järkän + centralityn

printtaa_listana('tuloksia/jarjestys_BCCWJ.txt', 'tuloksia/centrality_of_kanjis_BCCWJ.txt', 'freq_BCCWJ.txt', 'tuloksia/vertailu_BCCWJ.txt') #printtaa vertailun

printtaa_pelkka_algon_tulos('tuloksia/jarjestys_BCCWJ.txt', 'tuloksia/pelkka_algon_tulos_BCCWJ.txt') #printtaa vain indeksin ja järjestyksen
