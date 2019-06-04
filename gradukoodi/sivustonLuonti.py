HTML_ALKU = '''<!DOCTYPE html>\n
<meta charset="utf-8">\n
<html>\n
<head>\n
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js"></script>\n
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
\t<h1>Kanjilista</h1>\n
\t<div>Sinisellä merkitty jooyoo-kanjit, keltaisella vain komponentteina esiintyvät. WORK IN PROGRESS. Datan lähteet: <a href="https://github.com/ahaavisto/ahaavisto.github.io">github.com/ahaavisto/ahaavisto.github.io</a> </div>\n
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
with open ('kirja/tuloste.tsv', 'r') as f:
	i = 0
	for rivi in f:
		data.append(rivi.split('\t'))
		i += 1

def luo_html():
	html = ""
	i = 1
	kirjanLuku = 0
	for entry in data:
		lista = ''
		if kirjanLuku != entry[1]:
			kirjanLuku = entry[1]
			lista += "<h1> Kokonaisuus " + kirjanLuku + "</h1>\n"
			lista += "\n"
		if entry[2] == "target":
			lista += KANJI_DIV 
		else:
			lista += COMPONENT_DIV #eri väri, jos vain komponentti eikä jooyookani
		otsikko = FONT_DIV + str(i) + ". " + entry[0] + DIV_CLOSE + "\n" + DIV_CLOSE
		lista += HEADER_DIV + '\n <a data-toggle="collapse" href="#' + str(i) + '">' + otsikko + '</a>'
		lista += '<div id="' + str(i) + '" class="panel-collapse collapse">'
		lista += BODY_DIV + entry[6] + '<br><br>\n' #suomennos
		lista += "Tähän tulee vetojärjestys<br><br>"
		lista += FONT_DIV + "Komponentit:" + entry[3] + "<br>" + DIV_CLOSE
		lista += 'Merkin lukutapoja:' + entry[5] + '<br><br>\n' #lukutavat
		
		#esimerkit
		lista += '<div class="row"> <br>'
		lista += '<div class="col-sm-4">' + entry[8] + ' ' + entry[9] + '</div>'
		lista += '<div class="col-sm-8">' + entry[16] + ' ' + entry[17] + '</div>'
		lista += '<div class="col-sm-4">' + entry[10] + ' ' + entry[11] + '</div>'
		lista += '<div class="col-sm-8">' + entry[18] + ' ' + entry[19] + '</div>'
		lista += '<div class="col-sm-4">' + entry[12] + ' ' + entry[13] + '</div>'
		lista += '<div class="col-sm-8">' + entry[20] + ' ' + entry[21] + '</div>'
		lista += '<div class="col-sm-4">' + entry[14] + ' ' + entry[15] + '</div>'
		lista += '<div class="col-sm-8">' + entry[22] + '</div>'
		lista += '</div><br>'
		
		lista += entry[23] + '\n<br> ' + entry[24] + '\n<br><br>' #ekstrahommat
		
		lista += str(i) + '. merkki\n'
		lista += DIV_CLOSE + DIV_CLOSE + DIV_CLOSE
		print(lista)	
		for rivi in lista.split('\n'):
			html += rivi + '\n'
		html += "<br>\n"
		i += 1
	print(HTML_ALKU, html, HTML_LOPPU)
	
	
	
luo_html()
