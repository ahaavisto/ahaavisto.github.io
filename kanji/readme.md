Kirjan workflow

1. lataa taulukko .tsv -tiedostomuodossa Google drivestä.
2. aja kanji/loach_ wang _algo _alkua.py, argumenttina tuo taulukko. Koodi luo muokattu _cetrality.txt -listan, jossa nostettu priorisoitavaksi halutut merkit listan loppuun.
3. aja varsinainen algo eli gradukoodi/algoritmi.py -tiedoston funktiot alkaen funktiosta luo _jarjestattavat. Nyt oppikirjan listaan on lisätty komponentitkin
4. aja kanjidic2_parser.py -filun lue _ tsv _ja _lisaa _komponentit() sekä tee _tsv(taulukko), argumenttina tsv-muodossa kirjan data (tässä kestää hetki)
5. Nyt tiedostossa kanji/tuloste_komponentein.tsv on sisällöltään uudistettu tsv-tiedosto, jonka ALUN voit kopioida Google driveen ja jonka pohjalta voi luoda html-sivun. Älä kopioi koko tiedostoa, siinä on kaikki jooyoo-merkit.

HUOM: Tällä hetkellä tiedostoon generoituu liikaa rivinvaihtoja. Poista ne , eli poista \n\t. Lisäksi komponentteina aiemmin esiintyvät kanjit hyppäävät kokonaan sinne, missä ne ovat komponenttina, vaikka niiden pitäisi olla siellä komponenttina ja oikeassa sijainnissaan laajemmin tiedoin. Korjaa käsin. 八、日、木、口、土

6. aja sivustonLuonti.py > kirjaa_varten.html, argumenttina tuloste _komponentein.tsv. Poista kirjaa _varten.html tiedostosta ‣-merkki sijainneista ">‣ <" ja ">‣<" eli tyhjät esimerkkilauseet sekä täyteteksti "Tähän voi kirjoittaa käsin lisätietoja"

7. poista virallisen nettisivun kanji/kanji.html sisältö alun johdantoja lukuunottamatta, ja luomasi html sen tilalle
