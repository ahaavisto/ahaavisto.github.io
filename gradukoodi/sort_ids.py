sanakirja = {}
order = list()
valmis = list()
with open ('ids_jooyoo+_chine_muokattu.txt', 'r') as f:
	for rivi in f:
		sanakirja[rivi.split()[0]] = rivi.split()[1]
		
with open ('pelkka_algon_tulos_BCCWJ.txt', 'r') as f:
	for rivi in f:
		order.append(rivi.split()[1])

for entry in order:
	stringi = entry + ' ' + sanakirja[entry]
	valmis.append(stringi)
	
with open ('ids_jooyoo+_chine_muokattu.txt', 'w') as f:
	for rivi in valmis:
		f.write(rivi + '\n')
