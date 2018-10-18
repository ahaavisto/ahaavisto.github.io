'''parseaa dbnaryn jpn-filusta entryt joissa käännös suomeksi
'''


kirjoitettava = ""
'''
with open ('ja_dbnary_ontolex.ttl', 'r') as f:
	rivi = f.readline()
	suomea = False
	while rivi:
		rivi = f.readline()
		if rivi[0] == 'j': #otsikkorivi
			entry = rivi
			rivi = f.readline()
			try:
				while rivi[0] != 'j':
					entry += rivi
					rivi = f.readline()
					if 'lexvo:fin' in rivi:
						suomea = True
			except IndexError:
				print("index error")
			if suomea:
				#print("suomea:", kirjoitettava)
				kirjoitettava += entry
				suomea = False


with open ('dbnary_jpn_fi.txt', 'w') as f:
	for rivi in kirjoitettava:
		f.write(str(rivi))
'''
kirjattava = ""	
		
with open ('dbnary_jpn_fi.txt', 'r') as f:
	for rivi in f:
		if rivi[0] == 'j':
			kirjattava += rivi.split('_')[5] + ' ' #vain japaninnos otetaan
		elif 'dbnary:writtenForm' in rivi:
			kirjattava += rivi.split('"')[1] + '\n' #vain suomennos otetaan

with open ('dbnary_jpn_fi_siivottu.txt', 'w') as f:
	for rivi in kirjattava:
		f.write(str(rivi))

