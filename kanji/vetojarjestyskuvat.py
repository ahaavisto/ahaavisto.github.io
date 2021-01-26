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


'''yhdistetään kanji ja sen heksakoodi'''
for kanji in juuri.findall('character'):
	merkki = kanji.find('literal').text
	heksa = hex(ord(merkki))
	heksa = heksa.replace('x', '')
	sanakirja[heksa + '.svg'] = merkki

'''kopioidaan ja uudelleen nimetään kuvakansiosta halutut merkit'''
for kuva in vedot:
	if kuva in sanakirja and sanakirja[kuva] in kanit:
		path = '../../vedot/' + sanakirja[kuva] + '.svg'
		shutil.copy('../../../kanji_stroke_order/'+kuva, path)
