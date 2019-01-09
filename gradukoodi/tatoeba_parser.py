

def choose_language():
	lista = list()
	with open ('sentences.csv', 'r') as f:
		for rivi in f:
			if rivi.split('\t')[1] == 'fin':
				lista.append(rivi)

	with open ('sentences_fin.txt', 'w') as f:
		for rivi in lista:
			f.write(rivi)
