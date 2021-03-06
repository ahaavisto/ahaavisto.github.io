from sys import argv

HTML_ALKU = '''<!DOCTYPE html>\n
<meta charset="utf-8">\n
<html>\n
<head>\n
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>\n
<meta name="viewport" content="width=device-width, initial-scale=1.0">\n
</head>\n
<body>\n
\t<!-- seuraavat kolme linkkiä liittyvät bootstrap-kirjastoon-->\n
\t<!-- Latest compiled and minified CSS -->\n
\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"\n
\tcrossorigin="anonymous">\n
\t<!-- Optional theme -->\n
\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp"\n
\tcrossorigin="anonymous">\n
\t<!-- Latest compiled and minified JavaScript -->\n
\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"\n
\tcrossorigin="anonymous"></script>\n
\t<div class="container">

<h1>Kanjien komponentit</h1>\n
<div><a href="kanji.html" class="btn" role="button">Takaisin kanjilistaan</a></div>\n\n
<div>Ippo ippo -materiaalin kanjit ja niiden komponentit. Sinisellä merkitty jooyoo-kanjit, valkoisella pohjalla tässä yhteydessä vain komponentteina esiintyvät. Datan lähteet: <a href="https://github.com/ahaavisto/ahaavisto.github.io">github.com/ahaavisto/ahaavisto.github.io</a> </div>\n

\t<div class="panel-group">
'''
KANJI_DIV = '<div class="panel panel-info">\n'
COMPONENT_DIV = '<div class="panel panel-warning">\n'
HEADER_DIV = '<div class="panel-heading">\n'
BODY_DIV = '<div class="panel-body">\n'
FONT_DIV = '<div class="jpn">'
DIV_CLOSE = '</div>\n'
HTML_LOPPU = '</div>\n</div>\n</body>\n</html>'

data = []
inputfilu = argv[1]
with open (inputfilu, 'r') as f:
#with open ('kirja/tuloste_komponentein.tsv', 'r') as f:
	i = 0
	for rivi in f:
		data.append(rivi.split('\t'))
		i += 1
		
def luo_komponenttilista(komponentit, onko_samalla_sivulla):
	res = ''
	if len(komponentit) < 2:
		return '-'	
	if onko_samalla_sivulla:
		for char in komponentit:
			res += '<a href="#' + char + '">' + char + '</a>, '
		return "alakomponentit: " + res[:-2] + ', '
	else:
		for char in komponentit:
			res += '<a href="komponentit.html#' + char + '">' + char + '</a> ' + str(suomennos(char)) + ', '
		return res[:-2]
	
def suomennos(merkki):
	for entry in data:
		if merkki == entry[0]:
			return entry[6]

def luo_html_perus():
	html = ""
	i = 1
	kirjanLuku = 0
	for entry in data:
		lista = ''
		if kirjanLuku != entry[1]:
			kirjanLuku = entry[1]
			lista += "<h1> Osa " + kirjanLuku + "</h1>\n"
			lista += "\n"
		if entry[2] == "target":
			lista += KANJI_DIV 
		else:
			continue #atm komponentteja ei mukaan tähän listaan
			lista += COMPONENT_DIV #eri väri, jos vain komponentti eikä jooyookani
		
		otsikko = FONT_DIV + str(i) + ". " + entry[0] + DIV_CLOSE + "\n" + DIV_CLOSE
		lista += HEADER_DIV + '\n <a data-toggle="collapse" href="#' + str(i) + '">' + otsikko + '</a>'
		lista += '<div id="' + str(i) + '" class="panel-collapse collapse">\n'
		lista += BODY_DIV + entry[6] + '<br><br>\n' #suomennos
		lista += '<img src="/vedot/' + entry[0] + '.svg" class="img-responsive" alt="vetojärjestys"><br><br>' #vetokuva
		lista += FONT_DIV + "Komponentit: " + luo_komponenttilista(entry[3], False) + "<br>" + DIV_CLOSE
		lista += 'Merkin lukutapoja: ' + entry[5] + '<br><br>\n' #lukutavat
		
		#esimerkit
		lista += '<div class="row">'
		lista += '\t<div class="col-sm-4">' + entry[8] + ' ' + entry[9] + '</div>\n'
		lista += '\t<div class="col-sm-8">‣' + entry[16] + ' ' + entry[17] + '</div>\n'
		lista += '</div> <div class="row">\n'
		lista += '\t<div class="col-sm-4">' + entry[10] + ' ' + entry[11] + '</div>\n'
		lista += '\t<div class="col-sm-8">‣' + entry[18] + ' ' + entry[19] + '</div>\n'
		lista += '</div> <div class="row">\n'
		lista += '\t<div class="col-sm-4">' + entry[12] + ' ' + entry[13] + '</div>\n'
		lista += '\t<div class="col-sm-8">‣' + entry[20] + ' ' + entry[21] + '</div>\n'
		lista += '</div> <div class="row">\n'
		lista += '\t<div class="col-sm-4">' + entry[14] + ' ' + entry[15] + '</div>\n'
		lista += '\t<div class="col-sm-8">‣' + entry[22] + '</div>\n'
		lista += '</div><br>\n'
		
		lista += entry[23] + '\n<br> ' + entry[24] + '\n<br><br>' #ekstrahommat
		
		#lista += str(i) + '. merkki\n'
		lista += DIV_CLOSE + DIV_CLOSE + DIV_CLOSE #+ DIV_CLOSE
		print(lista)	
		for rivi in lista.split('\n'):
			html += rivi + '\n'
		html += "<br>\n"
		i += 1
	#print(HTML_ALKU, html, HTML_LOPPU)


def luo_html_komponenttilista():
	html = ""
	i = 1
	kirjanLuku = 0
	for entry in data:
		lista = ''
		if kirjanLuku != entry[1]:
			kirjanLuku = entry[1]
			lista += "<h1> Osa " + kirjanLuku + "</h1>\n"
			lista += "\n"
		if entry[2] == "target":
			lista += '<div id="' + entry[0]+ '" class="p-3 mb-2 bg-info">'
		else:
			lista += '<div id="' + entry[0]+ '" class="p-3 mb-2 bg-light">' #eri väri, jos vain komponentti eikä jooyookani
		lista += entry[0] + '<br>'
		if entry[6] is not '': lista+= entry[6] + ', \n' #suomennos
		lista += luo_komponenttilista(entry[3], True)
		if entry[5] is not '': lista += '<br>lukutapoja: ' + entry[5] + ' \n' #lukutavat
		lista += DIV_CLOSE
	
		for rivi in lista.split('\n'):
			html += rivi + '\n'
		html += "<br>\n"
		i += 1
	print(HTML_ALKU, html, HTML_LOPPU)

	
'''main'''
#luo_html_komponenttilista()
luo_html_perus()
