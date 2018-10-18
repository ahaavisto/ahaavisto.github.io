#from sys import argv
#argumentti_muuttujaksi = argv[1];

import re


def poista_turhat_sarakkeet():
	lista = list()	
	with open ("BCCWJ_frequencylist_suw_ver1_0.tsv", 'r') as f:
		for rivi in f:
			lemma = rivi.split('\t')[2]
			if re.search(u'[\u4e00-\u9fff]+', lemma) == None: #jos sanassa ei ole kaneja, poistetaan
				continue
			
			putsattu_lemma = ""
			for char in lemma:
				if re.search(u'[\u4e00-\u9fff]+', char) == None: #jos merkki ei ole kani
					continue
				putsattu_lemma = putsattu_lemma + char
				
			lista.append(putsattu_lemma + '\t' + rivi.split('\t')[6] + '\n') #jätetään vain sana ja sen frekvenssi)
	lista.sort()	
				
	with open ("frekvenssilista_BCCWJ.txt", 'w') as kirjoitettava :
		for rivi in lista:
			kirjoitettava.write(rivi)
	
	
def poista_turhat_sarakkeet2():
	lista = list()	
	with open ("bccwj_raaka_lista.csv", 'r') as f:
		for rivi in f:
			lemma = rivi.split('\t')[1]

			lista.append(lemma + '\t' + rivi.split('\t')[5] + '\n') #jätetään vain sana ja sen frekvenssi)
	lista = sorttaa(lista)	
				
	with open ("freq_BCCWJ.txt", 'w') as kirjoitettava :
		for rivi in lista:
			kirjoitettava.write(rivi)
	
	
def hajota_yhdyssanat():
	lista = list()
	with open ("frekvenssilista_BCCWJ.txt", 'r') as f :
		for rivi in f:
			lemma = rivi.split()[0]
			for merkki in lemma:
				lista.append(merkki + '\t' + rivi.split()[1] + '\n')
				
	lista.sort()
	
	with open ("frekvenssilista_BCCWJ_kanjeittain.txt", 'w') as kirjoitettava :
		for rivi in lista:
			kirjoitettava.write(rivi)

def koosta_merkin_frekvenssit():
	lista = list()	
	with open ("frekvenssilista_BCCWJ_kanjeittain.txt", 'r') as f:
	#with open ("testi_n.txt", 'r') as f:
		edel_rivi = "xx xx"
		for rivi in f:
			if edel_rivi.split()[0] == rivi.split()[0]: #jos peräkkäiset kanit samoja, yhdistetään
				edellinen_summa = int(lista.pop().split()[1]) #poistetaan edellinen rivi, otetaan määrä talteen
				summa = edellinen_summa + int(rivi.split()[1])
				lista.append(rivi.split()[0] + '\t' + str(summa) + '\n')
				
			else:
				lista.append(rivi)
			edel_rivi = rivi
			
	lista = sorttaa(lista)
	
	with open ("frekvenssilista_BCCWJ_lopullinen.txt", 'w') as kirjoitettava :
		for rivi in lista:
			kirjoitettava.write(rivi)

def sorttaa(lista):
	def kakkossarake(e):
		return int(e.split()[1])

	lista.sort(reverse=True, key=kakkossarake)
	return(lista)



poista_turhat_sarakkeet2()
#hajota_yhdyssanat()
#koosta_merkin_frekvenssit()
