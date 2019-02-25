import matplotlib.pyplot as plt
import pylab

minne_asti = 250

heisig = []
with open ('heisig_order.txt', 'r') as f:
	kaikki = f.read()
	kaikki = kaikki.split(' ')
	i = 0
	for merkki in kaikki:
		heisig.append(merkki)
		i += 1
		if i >= minne_asti:
			break
			
#jos mukana komponentit
algo = []
with open ('tuloksia/pelkka_algon_tulos_BCCWJ.txt', 'r') as f:
	i = 0
	for rivi in f:
		algo.append(rivi.split('\t')[1][:-1])
		i += 1
		if i >= minne_asti:
			break

#jos mukana vain jooyoo-kanjit

algo = []
with open ('tuloksia/algon_jooyoo_kanjit.txt', 'r') as f:
	i = 0
	for rivi in f:
		algo.append(rivi[:-1])
		i += 1
		if i >= minne_asti:
			break

bkb = []
with open ('bkb1.txt', 'r') as f:
	i = 0
	for merkki in f:
		bkb.append(merkki[:-1])
		i += 1
		if i >= minne_asti:
			break
			
muok = []
#with open ('tuloksia/muokattu_opiskelujarjestys.txt', 'r') as f: #komponentit
with open ('muok_listan_jooyoo_kanjit.txt', 'r') as f: #vain jooyoo
	i = 0
	for merkki in f:
		muok.append(merkki[:-1])
		i += 1
		if i >= minne_asti:
			break
	
frek = []
with open ('freq_BCCWJ.txt', 'r') as f:
	i = 0
	for rivi in f:
		frek.append(rivi.split('\t')[0])
		i += 1
		if i >= minne_asti:
			break

def luo_plot(inputti, output):
	i = 0
	ei_leikkaus = ""
	leikkaus = ""
	onko_leikkauksessa = False
	for merkki in inputti:
		for kanji in frek:
			if kanji == merkki:
				i += 1
				leikkaus += kanji + ' '
				onko_leikkauksessa = True
				break				
		if not onko_leikkauksessa:
			ei_leikkaus += merkki + ' '
		onko_leikkauksessa = False			
		output.append(i)
	print("Opiskelujarjestyksen ja yleisimpien leikkaus:")
	print(leikkaus)
	print("Opiskelujarjestyksessa olleet, ei-yleiset merkit:")
	print(ei_leikkaus)
	return output

bkb_tulos = luo_plot(bkb, [])
algon_tulos = luo_plot(algo, [])
heisig_tulos = luo_plot(heisig, [])
muok_tulos = luo_plot(muok, [])

plt.plot(range(1, minne_asti+1), color='violet', label='Yleisyysjarjestys')
plt.plot(algon_tulos, label='Algoritmin tulos')
plt.plot(muok_tulos, color='orange' , label='Muokattu algoritmin tulos')
plt.plot(bkb_tulos, color='red', label='BKB 1')
plt.plot(heisig_tulos, color='green', label='Heisig')

plt.ylabel('Osuus korpuksen yleisimmista merkeista')
plt.xlabel('Opiskellut merkit')
pylab.legend(loc='upper left')
plt.axis([1, minne_asti, 1, minne_asti])
plt.show()
