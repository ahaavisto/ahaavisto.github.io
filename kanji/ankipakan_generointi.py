from sys import argv

data = []
inputfilu = argv[1]
with open (inputfilu, 'r') as f:
	for rivi in f:
		data.append(rivi.split('\t'))


lopul_data = []

def kokopakka():
	for entry in data:
			lista = []
			lista.append(entry[0]) #kanji
			lista.append(entry[6]) #suomennos
			lista.append("Komponentit: " + entry[3])
			lista.append('Merkin lukutapoja: ' + entry[5])
			#esimerkit:
			lista.append('"' + entry[8] + ' ' + entry[9] + '\n' + entry[16] + ' ' + entry[17] + '"')
			lista.append('"' + entry[10] + ' ' + entry[11]+ '\n' + entry[18] + ' ' + entry[19] + '"')
			lista.append('"' + entry[12] + ' ' + entry[13]+ '\n' + entry[20] + ' ' + entry[21] + '"')
			lista.append('"' + entry[14] + ' ' + entry[15]+ '\n' + entry[22] + '"')
		
			lista.append(entry[23].split('<')[0]) #vetomäärä TODO fiksummin
		
			lista.append('kokonaisuus' + entry[1]) #kokonaisuuden numero tunnisteeksi
		
			lopul_data.append('\t'.join(lista) + '\n')


def luo_rivi(entry, i, tuleeko_lauseita):
	jap = entry[i]
	kanji = jap.split('・')[0]
	yomi = jap.split('・')[1]
	suomi = entry[i+1]
	loppu = 'osa' + entry[1]
	if tuleeko_lauseita:
		loppu = lisaa_lause(entry, i) + '\t' + loppu
	return kanji + '\t' + yomi + '\t' + suomi + '\t' + loppu
	
def lisaa_lause(entry, i):
	jap = entry[i+8]
	if i == 14: return jap + '\t' #jos ollaan lisäesimerkin kohdalla, suomi on samassa sarakkeessa
	suomi = entry[i+9]
	return jap + '\t' + suomi

def sanastopakka(tuleeko_lauseita):
	for entry in data:
		if entry[2] == 'comp': continue #jos komponentti, skipataan
		
		tunniste = 'osa' + entry[1]
			
		if entry[8] != '':	
			lopul_data.append(luo_rivi(entry, 8, tuleeko_lauseita))
		if entry[10] != '':
			lopul_data.append(luo_rivi(entry, 10, tuleeko_lauseita))
		if entry[12] != '':
			lopul_data.append(luo_rivi(entry, 12, tuleeko_lauseita))
		if entry[14] != '':
			lopul_data.append(luo_rivi(entry, 14, tuleeko_lauseita))
			

		
'''main'''
sanastopakka(True)
#kokopakka()

with open ('sanastoanki.txt', 'w') as f:
	for juttu in lopul_data:
		f.write(juttu + '\n')
