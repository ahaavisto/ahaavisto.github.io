#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pylab

plt.rc('axes', labelsize=20)
plt.rc('legend', fontsize=20)

minne_asti = 500

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
'''
algo = []
with open ('tuloksia/algon_jooyoo_kanjit.txt', 'r') as f:
	i = 0
	for rivi in f:
		algo.append(rivi[:-1])
		i += 1
		if i >= minne_asti:
			break
'''

bkb = []
with open ('bkb1.txt', 'r') as f:
	i = 0
	for merkki in f:
		bkb.append(merkki[:-1])
		i += 1
		if i >= minne_asti:
			break
			
muok = []
with open ('tuloksia/muokattu_opiskelujarjestys.txt', 'r') as f: #komponentit
#with open ('muok_listan_jooyoo_kanjit.txt', 'r') as f: #vain jooyoo
	i = 0
	for merkki in f:
		muok.append(merkki[:-1])
		i += 1
		if i >= minne_asti:
			break
			
kyoiku = []
with open ('kyoiku.txt', 'r') as f:
	i = 0
	for merkki in f:
		kyoiku.append(merkki[:-1])
		i += 1
		if i >= minne_asti:
			break

kirja = []
with open ('kirja/kanjilista.txt', 'r') as f:
	i = 0
	for merkki in f:
		kirja.append(merkki[:-1])
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
kyoiku_tulos = luo_plot(kyoiku, [])
kirja_tulos = luo_plot(kirja, [])

plt.plot(range(1, minne_asti+1), color='grey', linestyle = 'dashed', label='Yleisyysjarjestys')
plt.plot(muok_tulos, linewidth=2, color='violet' , label='Muokattu algoritmin tulos')
#plt.plot(algon_tulos, linewidth=2, label='Algoritmin tulos')
plt.plot(kyoiku_tulos, color='orange', label='Kyooiku')
plt.plot(bkb_tulos, color='red', label='BKB 1')
#plt.plot(heisig_tulos, color='green', label='Heisig')
plt.plot(kirja_tulos, color='yellow', label='kirja')

plt.ylabel('Opiskeltujen merkkien osuus yleisimmista merkeista')
plt.xlabel('Opiskeltujen merkkien maara')
pylab.legend(loc='upper left')
plt.axis([1, minne_asti, 1, minne_asti])
plt.show()
