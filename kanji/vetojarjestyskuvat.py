import shutil
import os

import xml.etree.ElementTree as ET

puu = ET.parse('../gradukoodi/kanjidic2.xml')
juuri = puu.getroot()

kanit = []

#joku lista jossa jooyoo + lisää merkkejä
with open ('4osa.txt') as f:
	for entry in f:
		kanji = entry.split('\t')[1][-2]
		kanit.append(kanji)
		print(kanji)

vedot = os.listdir('../../kanji_stroke_order')

sanakirja = {}

'''yhdistetään kanji ja sen heksakoodi'''
for kanji in juuri.findall('character'):
	merkki = kanji.find('literal').text
	heksa = hex(ord(merkki))
	heksa = heksa.replace('x', '')
	sanakirja[heksa + '.svg'] = merkki

#kopioidaan ja uudelleen nimetään kuvakansiosta halutut merkit
for kuva in vedot:
	if kuva in sanakirja and sanakirja[kuva] in kanit:
		print(kuva)
		path = '../../ippoippovedot/' + sanakirja[kuva] + '.svg'
		try:
			shutil.copy('../../kanji_stroke_order/'+kuva, path)
		except FileNotFoundError as e: 
			print(e)
			print('tiedostoa ei löydy')
