# Codio Robot Sgwrsio Cymraeg

![](robot.png)

Mae'r wers hon wedi ei dylunio fel cyflwyniad i raglennu seiliedig ar destun gan ddefnyddio Python ar y Raspberry Pi. Erbyn diwedd y wers, byddwch wedi creu rhaglen sgwrsio ryngweithiol Cymraeg ar gyfer robot.

Bydd y wers yn eich cyflwyno at y cysyniad cyfrifiadurol o ddeallusrwydd artiffisial ('artificial intelligence') a rôl casgliad arbennig o adnoddau technolegau iaith datblygwyd ym Mhrifysgol Bangor.

# Rhan 1- Sut mae cyfrifiaduron yn meddwl 

Yn y wers yma, byddwch yn ystyried y ffordd mae angen i gyfrifiaduron a robotiaid ddilyn cyfres o orchmynion er mwyn cyflawni tasg.

Dewiswch dri neu bedwar myfyriwr i fod yn robotiaid, ac yna rhannwch y myfyrwyr sy'n weddill yn dri neu bedwar tîm. Mae pob tîm yn cystadlu mewn ras i weld pwy all dywys 'robot' o gwmpas y dosbarth, neu 'ddrysfa' (maze). Gallai hyn fod yn dasg awyr agored. Eglurwch i'r 'robotiaid' bod rhaid iddyn nhw esgus bod yn dwp, a dim ond dilyn y cyfarwyddiadau maen nhw'n derbyn gan y myfyrwyr eraill.

Trwy gydol y ras, gwnewch yn sicr fod y myfyrwyr yn defnyddio cyfarwyddiadau fel "cama ymlaen 10 cam" neu "troi 90 gradd i'r dde".

Unwaith mae'r ras wedi'i hennill, trafodwch unrhyw broblemau daethoch ar eu traws wrth drio cael y robot i ddilyn eich cyfarwyddiadau. Sylweddoloch chi na allasai'r robot wneud ei benderfyniadau ei hunain? Roedd yn rhaid i chi fod yn benodol iawn ynglŷn â throeon a chamau oherwydd hynny.

Mae cyfrifiadur yn gweithio drwy gyflawni datganiadau un ar ôl y llall mewn dilyniant penodol. Gelwir dilyniant arbennig o ddatganiadau yn rhaglen. Mae pob rhaglen yn gweithredu gyda llif reolaeth arbennig ; mae hyn yn disgrifio pa ddatganiad y byddwn yn ei gyflawni, a beth fydd y datganiad nesaf. Dyma sut mae pob cyfrifiadur yn gweithio!

# Ydy cyfrifiaduron yn gallu meddwl dros eu hunain?

Ydych chi wedi clywed sôn am feddalwedd sgwrsio fel Elbot [http://www.elbot.com/](http://www.elbot.com/)? Wyddoch chi fod modd siarad gyda ffonau symudol er mwyn holi am wybodaeth, fel yn achos Siri a Cortana ar ddyfeisiau Apple a Google?

Gofynnwch gwestiynau i'r robot sgwrsio, naill ai yn Saesneg neu yn Gymraeg. Nodwch y gwahaniaeth yn yr atebion, a meddyliwch pam nad ydyn nhw'n cyfateb yn union gyda'r cwestiwn. Er enghraifft, cymharwch 'who is the best footballer in the world?' â 'pwy yw'r chwaraewr pêl droed gorau yn y byd?'.

Oes unrhyw resymau pam na fyddai'r robot yn gallu ateb eich cwestiynau fel y byddech chi'n disgwyl? Pam ei bod hi'n mor anodd i raglenni fel y rhain ddeall a rhyngweithio gyda bodau dynol? Pam eu bod nhw'n mor hawdd i'w drysu?

Mae cyfrifiaduron yn gweithredu neu'n rhedeg rhaglenni sy'n dilyn dilyniant o gyfarwyddiadau, ac dim ond y dilyniant yma allen nhw ei ddilyn.

Ydych chi wedi clywed am y Prawf Turing [http://en.wikipedia.org/wiki/Turing\_test](http://en.wikipedia.org/wiki/Turing_test)? Nod y prawf yw datblygu cyfrifiadur all rhywun ei gamgymryd am berson.

# Dechrau ar y codio

Edrychwch ar famfwrdd y Raspberry Pi. Beth ydych chi'n meddwl yw hwn?

Cyfrifiadur yw'r Raspberry Pi mewn gwirionedd, a byddwn yn ei ddefnyddio i wneud rhywbeth arbennig iawn. Yn lle rhedeg apiau a gemau mae pobl eraill wedi eu creu ar ein cyfer, byddwn yn dysgu sut i ysgrifennu meddalwedd er mwyn creu robot sy'n gallu sgwrsio â ni.

Byddwch yn rhaglennu Python drwy ysgrifennu rhaglen syml i gymryd mewnbwn defnyddiwr ac yna printio datganiadau at y sgrin.

- Gosodwch eich cyfarpar Raspberry Pi, ac yna trowch y peiriant ymlaen, a mewngofnodwch i'r Pi gan ddefnyddio'r enw defnyddiwr 'pi' a'r cyfrinair 'raspberry'.

_Nodwch na fydd y myfyrwyr yn gallu gweld unrhyw destun wrth deipio'r cyfrinair, ond sicrhewch iddyn nhw ei fod yn gweithio. Pam bod hyn yn digwydd? Cliw: beth fyddai yn digwydd petai rhywun yn edrych dros eu hysgwydd?_

- Nesaf, dylai'r myfyrwyr lwytho'r amgylchedd graffigol drwy deipio `startx`.

I ddechrau Python, cliciwch dwywaith ar yr eicon IDLE3 ar y bwrdd gwaith neu gliciwch ar y **prif ddewislen** a dewis **rhaglennu** , ac yna **IDLE3**.

 ![](idle3.png)

- Gellir teipio yn uniongyrchol i mewn i'r ffenest ar ôl y promt, fydd yn edrych fel hyn: '>>>'. Gelwir y ffenest hwn yn ddehonglydd neu gragen (shell). Gallwch deipio llinell o god ar ôl y promt a gwasgu Enter. Bydd hyn yn rhedeg y llinell hwnnw o god. Ceisiwch deipio y gorchymyn canlynol :

print("Helo Pawb!").

_Gofynnwch i'r myfyrwyr beth fydden nhw yn rhoi yn lle " Helo Pawb". Gadewch iddyn nhw arbrofi gyda defnyddio y ffenest ddehongli am funud neu ddwy. Cofiwch na all y cyfrifiadur ddilyn mwy nac un cyfarwyddiad ar y tro mewn **dilyniant**._

- all codio fynd yn fwy ac yn fwy blinedig wrth ddefnyddio'r dehonglydd wrth ysgrifennu lot o linellau o god. Felly, os ydych chi eisiau cadw eich cod, mae'n well defnyddio golygydd testun.

_Dangoswch i'r myfyrwyr sut i greu ffeil golygydd testun newydd drwy glicio ar **Ffeil>Ffenest Newydd** (**File>New Window**) o'r ddewislen ar frig y ffenest **IDLE3**. Dangoswch i'r myfyrwyr sut i gadw y ffeil hon, drwy glicio ar **Ffeil>Dewisiadau Cadw** (**File>Save Options**) a'i henwi yn enw1.py._

- Teipiwch y cod canlynol i mewn i ffenest y golygydd testun. Nodwch y gwahaniaeth rhwng sylw a llinell o god. Mae sylwadau yn rhan o'r rhaglen sy'n cael ei anwybyddu gan y cyfrifiadur, fel ein bod ni yn gallu gwneud nodiadau ynglŷn a beth sy'n digwydd yn y rhaglen.

	```python
	# Fy Rhaglen Python gan ....
	
	enw = input(‘beth yw dy enw: '), 
	print("Braf cwrdd â chi ", enw)
	```
_Nodwch fod y bylchau cyn_ " _yn y llinyn yn bwysig._

- Cadwch y ffeil fel ffeil Python drwy glicio ar **Ffeil** ac yna **Dewisiadau Cadw**, a'i henwi yn **robot**. 
Yna rhedwch y ffeil drwy glicio ar **Rhedeg** ac yna **Rhedeg Modiwl**.

Gall y myfyrwyr wedyn ychwanegu eu mewnbwn eu hunain a datganiadau 'print', efallai yn gofyn am oedrannau defnyddwyr a'u hoff lliwiau. 
Er enghraifft, gallent ychwanegu

```python
oedran = input(' pa mor hen wyt ti: ')
print("dwyt ti ddim yn edrych yn ", oedran)
```
Unwaith bydd gennych raglenni sy'n weithredol, ac yn cynnwys nifer o gwestiynau, bydd modd gosod bylchau rhwng y cwestiynau a ofynnwyd gydag amser. Fel arfer mewn sgwrs, mae saib rhwng ateb cwestiwn a gofyn yr un nesaf. Yr amcan yw creu robot sgwrsio all rywun ei gamgymryd am berson; felly, rydym angen gosod seibiau rhwng y cwestiynau. Gellir cyflawni hyn gan ddefnyddio'r modiwl `time`. I ychwanegu'r modiwl, bydd angen i chi ychwanegu `import time` o dan y sylw a chyn y cwestiynau. Wedyn rhwng y cwestiynau bydd angen i chi ddefnyddio `time.sleep(1)`, lle mae gwerth 1 yn cynrychioli 1 eiliad.


# Ychwanegu nodweddion ieithyddol Cymraeg 

Mae modd i chi greu robot sy'n siarad Cymraeg drwy ddefnyddio adnoddau technolegau iaith Cymraeg dros y we o'r Porth Technolegau Iaith.

Mae'r adnoddau hyn yn gallu :

- Nodi iaith y testun – Cymraeg neu unrhyw iaith arall
- Canfod a chynnig enw'r person neu le o fewn testun
- Cywiro gwallau sillafu ac/neu ramadeg testun Cymraeg
- Llefaru yn Gymraeg

Yn y rhan yma o'r wers bydd modd i chi ddod a'r holl adnoddau yma at ei gilydd er mwyn ffurfio rhaglen sgwrsio 'naturiol' Cymraeg soffistigedig eich hunain.

I ddechrau, ychwanegwch un neu fwy o'r canlynol at frig eich ffeil cod :

`from cysill import gwirio_testun`

`from lleferydd import llefaru, cwestiwn`

`from canfodiaith import iaith_testun`

`from rhannauymadrodd import enw_lle, enw_person`

Mae enghreifftiau o fewn yr is-ffolder 'ee' ar eich cyfrifiadur.

Bydd modd i chi, gyda help Mr Robertson a Mr Jones, lwytho eich rhaglen i ben y robot Rapiro.

 ![](rapiro.png)

# Casgliad

Beth fyddai eich gyrfa delfrydol chi? A oes unrhyw swydd heddiw nad ydyw wedi ei drawsnewid yn llwyr gan dechnoleg a chyfrifiaduron?

Ydy codio yn sgil defnyddiol / hanfodol ?

Wyddoch chi y bydd y byd gwaith wedi newid yn gyfan gwbl mewn 5 neu 10 mlynedd arall, unwaith yn rhagor oherwydd gwelliannau technolegol? Bydd cyfrifiaduron gydag elfennau o ddeallusrwydd artiffisial yn trawsnewid nifer o swyddi.

Ym mha ieithoedd bydd y technolegau newydd hyn?