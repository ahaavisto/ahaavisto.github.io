const form = document.querySelector('form');
const shep = document.querySelector('input[name=shepherd]');
const target = document.getElementById('target');
const nro = 42;

form.addEventListener('submit', function(evt) {
    evt.preventDefault();
    //nro = document.querySelector('input[name=henk]').value;
    if (shep.checked) {
    	console.log("shepherd klikattu");
    }
    p.innerText = `Onko valittu shepherd's: ${shep.checked}`;
	if (form.shepherd.checked) {
		shepherd();
	}
});

function p(maara) {
	var tulo = maara * nro;
	if (tulo.toString().length > 3) {
		return tulo.toFixed(2);
	} else {
		return tulo;
	}
}

function shepherd(){
	target.innerHTML += "<br><br>Shepherd's pie<br><br>" + 
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
