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

algo = []
with open ('tuloksia/pelkka_algon_tulos_BCCWJ.txt', 'r') as f:
	i = 0
	for rivi in f:
		algo.append(rivi.split('\t')[1][:-1])
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
			
print((bkb))
	
frek = []
with open ('freq_BCCWJ.txt', 'r') as f:
	i = 0
	for rivi in f:
		frek.append(rivi.split('\t')[0])
		i += 1
		if i >= minne_asti:
			break
	
algon_tulos = []	
i = 0
for juttu in algo:
	for kanji in frek:
		if kanji == juttu:
			i += 1
	algon_tulos.append(i)
	
heisig_tulos = []	
i = 0
for juttu in heisig:
	for kanji in frek:
		if kanji == juttu:
			i += 1
	heisig_tulos.append(i)	
	
bkb_tulos = []	
i = 0
for juttu in bkb:
	for kanji in frek:
		if kanji == juttu:
			i += 1
	bkb_tulos.append(i)	


plt.plot(algon_tulos, label='Algoritmin tulos')
plt.plot(heisig_tulos, color='green', label='Heisig')
plt.plot(bkb_tulos, color='red', label='BKB 1')
plt.plot(range(1, minne_asti+1), color='violet')
plt.ylabel('Osuus korpuksen yleisimmista merkeista')
plt.xlabel('Opiskellut merkit')
pylab.legend(loc='upper left')
plt.axis([1, minne_asti, 1, minne_asti])
plt.show()

