Kirjan workflow 



12.58




1. lataa taulukko .tsv -tiedostomuodossa Google drivestä. Nimeä se tuloste.tsv
2. aja kanji/loach_ wang _algo.py joka tekee muokattu _cetrality.txt -listan, jossa nostettu ylös priorisoitavaksi halutu merkit
3. aja varsinainen algo eli gradukoodi _0918.py -tiedoston funktiot alkaen funktiosta luo _jarjestattavat. Nyt oppikirjan listaan on lisätty komponentitkin
4. aja kanjidic2_parser.py -filun lue _ tsv _ja _lisaa _komponentit() sekä tee _tsv(taulukko) (tässä kestää hetki)
5. Nyt tiedostossa kirja/tuloste_komponentein.tsv on uusi tsv-tiedosto, jonka ALUN voit kopioida Google driveen ja jonka pohjalta voi luoda html-sivun. Älä kopioi koko tiedostoa, siinä on kaikki jooyoo-merkit.

HUOM: atm tiedostoon generoituu liikaa rivinvaihtoja. Poista ne. Lisäksi komponentteina aiemmin esiintyvät kanjit hyppäävät kokonaan sinne, missä ne ovat komponenttina, vaikka niiden pitäisi olla siellä komponenttina ja oikeassa sijainnissaan laajemmin tiedoin. Korjaa käsin. 八、木、口、土

6. aja sivustonLuonti.py > kirjaa_varten.html, poista virallisen nettisivun kanji/kanji.html sisältö alun johdantoja lukuunottamatta, ja luomasi html sen tilalle
