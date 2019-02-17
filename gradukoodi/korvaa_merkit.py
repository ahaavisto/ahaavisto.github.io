import re

sanakirja = {}
with open ('korvattavat.txt', 'r') as f:
	for rivi in f:
		sanakirja[rivi.split('\t')[0]] = rivi.split('\t')[1].strip()

ids = []

with open ('ids_jooyoo+_chine_muokattu.txt', 'r') as f:
	for rivi in f:
		for juttu in sanakirja:
			rivi = rivi.replace(juttu, sanakirja[juttu])
		ids.append(rivi)

with open ('apu.txt', 'w') as f:
	for juttu in ids:
		f.write(juttu)
				
