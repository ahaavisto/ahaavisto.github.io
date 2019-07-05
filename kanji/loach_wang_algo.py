'''Kanjikirjaa varten algoritmin luoman järjestyksen käpistelyä ns. käsin
perustuu osin gradukoodi_0918.py koodiin'''

def uusi_centrality():
	#taulukoksi kanjikirjaa varten luotu excel
	data = []
	with open ('../gradukoodi/kirja/tuloste.tsv', 'r') as f:
		for rivi in f:
			data.append(rivi.split('\t'))
		
	centrality_order = []
	with open ('../gradukoodi/tuloksia/centrality_of_kanjis_BCCWJ.txt', 'r') as f:
		for rivi in f:
			centrality_order.append([rivi.split()[0], float(rivi.split()[1])])
		
	#käydään läpi järjestyksessä kirjan data ensin opeteltavasta alkaen eteenpäin opiskelujärkkää ja nostetaan ylös centralityssä niitä kanjeja, jotka kirjan järkässä halutaan tulevan ensin
	new_centrality = 10000
	for rivi in data:
		for entry in centrality_order:
			if entry[0] == rivi[0]: #sama kanji
				entry[1] = new_centrality
				new_centrality -= 1

	centrality_order.sort(key=lambda x: x[1]) #sortataan cent. perusteella

	with open ('muokattu_centrality.txt', 'w') as f:
		for rivi in centrality_order:
			f.write(rivi[0] + ' ' + str(rivi[1]) + '\n')
			
'''main'''

#uusi_centrality()
