from random import shuffle

def choose_language():
	lista = list()
	with open ('sentences.csv', 'r') as f:
		for rivi in f:
			if rivi.split('\t')[1] == 'fin':
				lista.append(rivi)

	with open ('sentences_fin.txt', 'w') as f:
		for rivi in lista:
			f.write(rivi)
			
def map_translations():
	kaannokset = list()
	jpn = {}
	fin = {}
	with open ('sentences_jpn.txt', 'r') as f:
		for rivi in f:
			jpn[rivi.split('\t')[0]] = rivi.split('\t')[2]
	
	with open ('sentences_fin.txt', 'r') as f:
		for rivi in f:
			fin[rivi.split('\t')[0]] = rivi.split('\t')[2]
	
	with open ('links.csv', 'r') as f:
		for rivi in f:
			if rivi.split('\t')[0] in fin and rivi.split('\t')[1][:-1] in jpn:
				lauseet = fin[rivi.split('\t')[0]][:-1] + '\t' + jpn[rivi.split('\t')[1][:-1]]
				kaannokset.append(lauseet)
	
	with open ('kaannokset.tsv', 'w') as f:
		for rivi in kaannokset:
			f.write(rivi)

def shuffle_list():
	data = []
	with open ('kaannokset.tsv', 'r') as f:
		for rivi in f:
			data.append(rivi)
	shuffle(data)
	with open ('kaannokset.tsv', 'w') as f:
		for rivi in data:
			f.write(rivi)
	

'''pääohjelma alkaa'''


#map_translations()

#shuffle_list()
				
				
				
	
