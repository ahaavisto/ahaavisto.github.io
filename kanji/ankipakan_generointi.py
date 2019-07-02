
data = []
with open ('../gradukoodi/kirja/tuloste.tsv', 'r') as f:
	for rivi in f:
		data.append(rivi.split('\t'))


lopul_data = []

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

with open ('anki.txt', 'w') as f:
	for juttu in lopul_data:
		f.write(juttu)
