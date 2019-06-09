import shutil
import os

import xml.etree.ElementTree as ET

puu = ET.parse('../kanjidic2.xml')
juuri = puu.getroot()

kanit = []

with open ('tuloste.tsv') as f:
	for entry in f:
		kanit.append(entry[0])

vedot = os.listdir('../../../kanji_stroke_order')

sanakirja = {}

for kanji in juuri.findall('character'):
	merkki = kanji.find('literal').text
	heksa = hex(ord(merkki))
	heksa = heksa.replace('x', '')
	sanakirja[heksa + '.svg'] = merkki


for kuva in vedot:
	if kuva in sanakirja:
		path = '../uuet/'+sanakirja[kuva]
		shutil.copy('../../kanji_stroke_order/'+kuva, path)
		print('moi')
	else:
		print('ei')
