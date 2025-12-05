const form = document.querySelector('form');
const shep = document.querySelector('input[name=shepherd]');
const target = document.getElementById('target');
let nro = 42;

form.addEventListener('submit', function(evt) {
    evt.preventDefault();
    target.innerText = "";
    nro = document.querySelector('input[name=henk]').value;
	if (form.shepherd.checked) {
		shepherd();
	}
	if (form.intia.checked) {
		intia();
	}
	if (form.papu.checked) {
		papukeitto();
	}
	if (form.okonomiyaki.checked) {
		okonomiyaki();
	}
	if (form.seitan.checked) {
		seitan();
	}
	if (form.sose.checked) {
		sose();
	}
	if (form.bolo.checked) {
		bolo();
	}
	if (form.tofut.checked) {
		tofut();
	}
	if (form.hernari.checked) {
		hernari();
	}
	if (form.pizza.checked) {
		pizza();
	}
	if (form.skonssit.checked) {
		skonssit();
	}
	if (form.piirakka.checked) {
		piirakka();
	}
	if (form.rieska.checked) {
		rieska();
	}
	if (form.sampylat.checked) {
		sampylat();
	}
	if (form.letut.checked) {
		letut();
	}
	
});

function p(maara) {
	let tulo = maara * nro;
	if (tulo.toString().length > 3) {
		return tulo.toFixed(2);
	} else {
		return tulo;
	}
}

function shepherd(){
	target.innerHTML += "<h2>Shepherd's pie</h2>" + 
	p(0.33) + " sipulia (1 sipuli n. 100 g)<br> " + 
	p(0.2) + " porkkanaa (1 porkkana n. 150 g)<br> " + 
	p(0.33) + " kynttä valkosipulia<br>" +
	p(0.33) + " tl tinjamia<br>" +
	p(0.33) + " laakerinlehteä<br>" +	
	p(0.17) + " tl soijakastiketta<br>" +
	"herneitä, jos halutaan<br>" +
	"suolaa maun mukaan<br>" +

	p(30) + " g kaurajauhista (tai muuta käyttövalmista vegeproteiinia)<br>" +			
	p(35) + " g tomaattimurskaa<br><br>" +
		
	p(140) + " g perunaa<br>" +
	p(35) + "g kaurakermaa<br>" +
	"suolaa maun mukaan<br><br>" +
	"Keitä perunat. Muussaa, lisää nestettä vähitellen, jotta muussista ei tule liian laihaa. Tarkista suolan määrä.<br><br>" +
	"Pilko sipuli, valkosipuli ja porkkanat melko pieniksi. Paista rasvassa hetki. Lisää laakerinlehdet ja proteiini, paista vähän lisää. Lisää sitten tomaattimurska ja muut mausteet. Keitä hetki. Kastikkeen pitää olla aika paksua. Tarkista maku.<br><br>" +
	"Levitä vuuan pohjalle kastike. Levitä päälle kerros perunamuussia. Paista noin 30 min 200-asteisessa uunissa. Anna vetäytyä hetki ennen tarjoilua.<br> Tämän ruuan annoskoko saattaa olla aika iso.<br><br>" +
	"Oma resepti, yhdistelmä useista netin resepteistä.";
}

function intia() {
	document.getElementById("teksti").innerHTML += "<h2>Intiasoossi</h2>" + 
	p(30) + " g sipuli<br> " + 
	p(0.8) + " kynttä valkosipulia<br>" +
	p(0.25) + " tl inkivääriä<br>" +
	p(0.25) + " laakerinlehti<br>" +

	0.6*nro + " dl linssejä<br>" +
	0.5*nro + " tl curryjauhetta<br>" +
	0.25*nro + " tl kurkumaa<br>" +

	p(1.8) + " dl kasvislientä \(tai vajaa\)<br>" +
	60*nro + " g perunaa/bataattia<br>" +
	30*nro + " g kookosmaitoa<br>" +
	"vähän soijakermaa/maitoa<br><br>" +
	"Pilko sipulit, paista. Lisää mausteet paistamisen loppupuolella. Lisää kasvisliemi ja linssit. Keitä n. 30 minuuttia, lisää bataatti/peruna n. 20 min ennen valmistumista. Vähän ennen valmistumista lisää kookosmaito ja halutessasi kermaa.";
}

function papukeitto() {
	document.getElementById("teksti").innerHTML += "<h2>Papukeitto</h2>" + 
	p(0.25) + " kpl sipulia<br> " + 
	0.5*nro + " tl inkivääriä<br>" +
	0.5*nro + " tl curryjauhetta<br>" +

	0.5*nro + " tl paprikajauhetta<br>" +
	0.25*nro + " tl rakuunaa<br>" +
	0.5*nro + " tlk papuja<br>" +
	0.5*nro + " tlk tomaattimurskaa<br>" +
	0.5*nro + " dl kermaa<br>" +
	"chiliä, jos halutaan<br><br>" +
	"Pilko sipulit, paista. Lisää mausteet paistamisen loppupuolella. Lisää tomaatti ja pavut, keittele kunnes sipuli sopivan kypsää. Lopussa lisää kerma (toimii ilmankin). <br><br>" +
	"Lähde: Helsingin Sanomat 2011, ei juuri muokattu";
}

function okonomiyaki() {
	document.getElementById("teksti").innerHTML += "<h2>Okonomiyaki</h2>" + 
	50 * nro + " g vehnäjauho<br> " + 
	0.8 * nro + " dl vettä<br>" +
	1*nro + " kananmunaa<br>" +
	0.5*nro + " rkl perunajauhoa (suunnilleen)" +
	150*nro + " g kaalia pienenä silppuna<br>" +
	"sopivasti täytteitä, kuten vegepekonia, ituja, sieniä...<br>" +	
	"sopivasti purjoa/kevätsipulia silppuna<br><br>" +
	"Päälle okonomiyakikastiketta, japanimajoneesia, kalahiutaleita";
}		
		
function seitan() {		
	document.getElementById("teksti").innerHTML +=
	"<h2>Siskon bataattiseitan</h2>" + 
	p(133) + " g bataattisosetta<br>" + 
	p(0.66) + " dl gluteenijauhoa<br>" + 
	p(0.33) + " tl suolaa<br>" + 
	p(0.33) + " rkl soijakastiketta<br>" + 
	p(0.66) + " rkl hiivahiutaleita<br>" + 
	p(0.33) + " tl sitruunamehua<br>" + 
	"vähän makeutusta<br>" + 
	p(0.33) + " tl salviaa<br>" + 
	p(0.166) + " tl basilikaa<br>" + 
	p(0.166) + " tl timjamia<br>" + 
	p(0.166) + " tl inkivääriä<br>" + 
	p(0.08) + " tl muskottia<br>" + 
	p(0.166) + " tl juustokuminaa<br>" + 
	p(0.08) + " tl valkopippuria<br>" + 
	p(0.166) + " tl valkosipulijauhetta<br><br>" +
	"Pirkan bataattisose on 'se oikea' tähän, mutta soseen voi yrittää valmistaa itsekin bataatteja keittämällä. Itse en ole saanut kuitenkaan rakeenteesta hyvää silloin. Mausteista voi jättää pois muutaman aivan hyvin. <br> Sekoita kuivat aineet keskenään ja märät aineet keskenään. Yhdistä, muotoile pihveiksi, paista 35-40 min 190C (ei liikaa etteivät pihvit käy liian kumimaisiksi)";
}	

function sose() {	
	document.getElementById("teksti").innerHTML += "<h2>Kasvissosekeitto</h2>" + 
	p(0.33) + " dl punaisia linssejä<br> " + 
	p(1.5) + " dl vettä<br>" +
	p(0.25) + " liemikuutiota<br>" +
	p(55) + " g porkkanaa<br>" +
	p(45) + " g perunaa<br>" +
	p(60) + " g sipulia<br>" +
	"Valkosipulia sopivasti<br>" +
	"(Kaurakermaa)<br><br>" +
	"Pilko ainekset, laita kiehumaan. Lisää vettä tarvittaessa. Paista sipuli eka, jos jaksat. Liemikuutioita ja vettä voi lisätä, jos tarvetta on. Kaurakerman voi lisätä lopuksi ennen soseuttamista.<br><br>"+
	"Oma resepti. Testattu leireillä, ainoa miinus: jos laittaa vihreitä linssejä, keitto näyttää vähän pelottavalta.";
}	

function bolo() {	
	document.getElementById("teksti").innerHTML += "<h2>Bolognese</h2>" + 
	p(60) + " g makaronia<br><br> " + 

	p(85) + " g tomaattimurskaa<br>" +
	p(8) + " g tomaattisosetta<br>" +
	p(0.4) + " tl basilikaa (oreganoakin voi laittaa)<br>" +
	p(0.4) + " tl sokeria<br>" +
	p(25) + " g sipulia<br>" +
	"Valkosipulia sopivasti<br>" +
	"Soijarouhetta sopivasti, ehkä soijakastiketta siihen<br>" +
	"Suolaa, ehkä pippuria<br><br>" +
	"Pilko sipulit, paista ne ja lisää lopuksi soijarouhe hetkeksi pannuun. Lisää vettä niin paljon kuin rouhe imee sitä, lisää sitten muut aineet. Keittele, kunnes sipuli pehmeää. Lisää vettä tarvittaessa.<br><br>"+
	"Yhdistelty useista resepteistä. Testattu leireillä: annoskoko lastenleirillä hyvä, nuorisolle olen tehnyt isomman erän. Ei ole maailman herkullinen bolognese, mutta ihan jees.";
}	

function pizza() {	
	document.getElementById("teksti").innerHTML += "<h2>Pizza</h2>" + 
	p(0.5) + " dl jauhoja<br> " + 
	p(0.21) + " dl vettä<br>" +
	p(3.6) + " g hiivaa<br>" +
	"suolaa, öljyä<br><br>" +
	
	p(66.6) + " g tomaattimurskaa<br>" +
	p(5.33) + " g tomaattisosetta<br>" +
	p(0.2) + " kpl valkosipulinkynttä<br>" +
	p(8.66) + " g sipulia<br>" +
	p(0.133) + " rkl basilikaa<br>" +
	p(0.133) + " rkl oreganoa<br>" +
	p(0.1) + " rkl sokeria<br>" +
	"suolaa sopivasti<br><br>" +
	
	p(25) + " g paprikaa<br>" +
	p(23) + " g ananasta<br>" +
	p(0.5) + " dl soijarouhetta/tofua/tms<br>" +
	p(20) + " g juustoraastetta<br><br>" +
	"[to be added]<br><br>"+
	"Lähde: modailtu kotitalouden kirjasta. Testattu leireillä.";
}
	
function piirakka() {	
	document.getElementById("teksti").innerHTML += "<h2>Kasvispiirakka</h2>" + 
	p(25) + " g tofua (voi olla maustettua tai ei)<br> " + 
	p(0.6) + " dl kaurakermaa<br>" +
	p(0.6) + " rkl perunajauhoa<br>" +
	p(0.1) + " rkl basilikaa<br>" +
	p(0.2) + " tl suolaa ja vähän pippuria<br>" +
	p(16) + " g tomaattia/paprikaa tms<br>" +
	p(16) + " g sipulia<br>" +
	"Piirakkataikinaa sopivasti<br><br>" +
	"Tee taikina. Esipaista, jos ohje sanoo niin. Pilko kasvikset, esipaista pannulla hieman. Murskaa tofu ja sekoita kaikki täyteaineet ja sipuli. Sauvasekoitin on kiva, muttei pakollinen. Kaada täytemössö taikinapohjan päälle ja lisää tomaatti/muut kasvikset/sienet/tms. Paista noin 30 minuuttia 200 asteisessa uunissa. Hyvää myös kylmänä - pysyy silloin paremmin kasassa.<br><br>"+
	"Modailtu hieman Vegaanin kotiruokakirjasta. Testattu leireillä, miinuksena että taikinan ja täytteen määrä suhteessa toisiinsa vaikea arvioida. Täytemössöä voi tehdä vähemmänkin.";
}	
	
function tofut() {	
	document.getElementById("teksti").innerHTML += 
	"<h2>Tomaattiset tofupyörykät</h2>" +
	p(0.33) + " pkt tofua (siis n. 250 g paketti). Voi käyttää ainakin maustamatonta tai marinoitua<br>" + 
	p(0.33) + " dl gramjauhoa (laita oikeasti vain sen verran kun tarvitset, tyylin puolet riittänee)<br>" + 
	p(0.6) + " rkl soijakastiketta<br>" + 
	p(20) + " g sipulia<br>" + 
	p(0.33) + " kynttä valkosipulia<br>" + 
	p(0.33) + " rkl oregano<br>" + 
	p(0.25) + " dl tomaattisosetta<br>" + 
	p(0.5) + " rkl basilikaa<br>" + 
	"Voit lisätä myös esim. porkkanaraastetta, ciliä, papuja, mitä vaan <br>"+ 
	"Leirillä lisäkkeeksi: " + p(50) + " g riisiä<br><br>" +
	"Pilko sipuli ja valkosipuli mahdollisimman pieneksi ja paista niitä hetki. Mössää tofu, sipulit (kannattaa antaa eka jäähtyä...) ja muut ainekset paitsi jauhot keskenään. Sauvasekoittimesta on etua, pitää mössätä kunnolla. Sekoita lopuksi gramjauhoja taikinaan sen verran, että saat pullat pysymään kasassa (ei ihan pakollinen vaihe). Pyörittele suht tasakokoisia pullia, pienet pysyvät helpommin kasassa ja kypsyvät nopeammin kuin isot. Paista 200 asteessa n. 20 min kunnes pullat tummenevat vähän ja/tai tuntuvat kypsiltä jos niitä tökkii haarukalla.<br><br>"+
	"Lähde: modailtu Kiskola&Miettunen Tofu-keittokirjasta. Testattu leireillä.";
}	

function rieska() {	
	document.getElementById("teksti").innerHTML += "<h2>Hillopuurorieska</h2>" +
	"Ainekset yhteen pellilliseen:<br>" + 
	"3 dl jauhoja<br> " + 
	"5 dl puuroa (ei kuumana)<br>" +
	"1 tl suolaa<br>" +
	"2 rkl öljyä<br>" +
	"1 dl paistonkestävää omena/appelsiinimarmeladia (voi jättää poiskin)<br><br>" +
	
	"Sekoita ainekset. Levitä pellille (rieska tasoittuu hieman uunissa, ei haittaa jos se ei ole kovin tasainen uuniin mennessään. Paista 225 asteessa 20-25 minuuttia - jos teet rieskalevyn sijaan pikkurieskoja, paistoaika lyhenee. Maistuu parhaalta tuoreeltaan.<br><br>"+
	"Lähde: muokattu Myllyn Parhaan nettisivujen reseptistä yksinkertaimmaksi. Testattu monella leirillä, helppo tapa käyttää puuron jämät.";
}	

function sampylat() {
	document.getElementById("teksti").innerHTML += "<h2>Perussämpylät</h2>" + 
	p(0.25) + " dl nestettä<br>" + 
	p(2.5) + " g hiivaa<br>" + 
	p(0.1) + " tl sokeria<br>" + 
	p(0.05) + " tl suolaa<br>" + 
	p(0.6) + " dl jauhoja<br>" + 
	p(0.2) + " rkl öljyä<br>" + 
	
	"Tee sämpylät. Paista 225 asteessa n. 10 minuuttia. Yksi annos on noin yksi sämpylä.<br><br>"+
	"Lähde: Köksänkirja :D. Testattu leireillä.";
}	
	
function letut() {	
	document.getElementById("teksti").innerHTML += "<h2>Lettutaikina</h2>" + 
	p(1) + " dl maitoa<br>" + 
	p(0.66) + " dl jauhoja<br>" + 
	p(0.33) + " rkl perunajauhoja<br>" + 
	p(0.17) + " tl suolaa<br>" + 
	
	"Osannet tehdä lettuja ^^";
}

function hernari() {	
	document.getElementById("teksti").innerHTML += "<h2>Hernekeitto</h2>" + 
	p(71) + " g kuivattuja herneitä<br>" + 
	p(0.14) + " tl suolaa<br>" + 
	p(17) + " g sipulia<br>" + 
	p(50) + " g porkkanaa<br>" + 
	p(0.2) + " kynttä valkosipulia<br>" +
	p(0.29) + " tl meiramia<br>" + 
	"mustapippuria<br><br>" + 
	
	"Liota herneitä yön yli kattilassa. Aamulla hella päälle & parin tunnin päästä lisää sipuli ja porkkana, nauti kun nekin ovat kypsiä.<br><br>"+
	"Lähde: modailtu Pirkan nettisivuilta. Testattu leireillä.";
}	
	
function skonssit() {	
	document.getElementById("teksti").innerHTML += "<h2>Professori Shadwellin skonssit</h2>" + 
	p(0.8) + " dl vehnäjauhoa<br> " + 
	p(0.4) + " tl leivinjauhetta<br>" +
	p(0.1) + " tl suolaa<br>" +
	p(10) + " g margariinia<br>" +
	p(0.3) + " dl (kaura)maitoa <br><br>" +

	"Sekoita kuivat aineet. Nypi sekaan rasva. Lisää maito, sekoita mahdollisimman vähän mutta kuitenkin hyvin. Yksi annos vastaa suunnilleen yhtä skonssia.<br><br>" +
	"Paista 230 asteessa 12-14 min.<br><br>Resepti saatu kirjelarpissa professori Shadwellilta, on oikeasti kyseisen pelaajan brittikeittokirjasta."+
	"";
}
