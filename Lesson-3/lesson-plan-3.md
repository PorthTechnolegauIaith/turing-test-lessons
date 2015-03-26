# Gwers 3 - Cymreigio'r robot

## Cyflwyniad

Bydd y wers yma yn cyflwyno'r plant i adnoddau elfennol ar gyfer prosesu
testunau Cymraeg, gan gynnwys adnabod iaith, gwirio gramadeg a sillafu, a mwy. 
Bydd y wers hefyd yn dysgu myfyrwyr i gymryd eu rhaglenni robotiaid sgwrsio,
sydd ar hyn o bryd yn argraffu'r sgwrs ar y sgrin, a’u troi yn
robotiaid sy’n llefaru Cymraeg, lle y bydd modd iddyn nhw glywed eu robot yn 
gofyn y cwestiwn.

Bydd yn rhaid i chi sicrhau bod llyfrgell adnoddau'r Porth Technolegau Iaith 
wedi ei llwytho i lawr a’i gosod ar y cardiau SD  - sef yr is-ffolder 'src' o fewn
y project hwn.

Bydd angen i fyfyrwyr gael mynediad at glustffonau er mwyn clywed y seiniau.
Efallai y bydd angen seinydd arnoch chi er mwyn arddangos i’r dosbarth.

Yn olaf, bydd yn rhaid i chi sicrhau bod sain yn cael ei orfodi i mewn i 
glustffonau yn hytrach na HDMI drwy deipio `amixer cset numid=3 1`, neu drwy 
glicio ddwywaith ar yr eicon Python Games a dewis **Force Headphones**. 

## Amcanion dysgu 

- Adnabod a defnyddio dyfeisiau mewnbwn ac allbwn ar y Rasberry Pi.
- Gallu ychwanegu cod at y rhaglenni robot sgwrsio ar y Rasberry Pi er
mwyn caniatáu iddo ddarllen testun ar lafar.
- Profi a gwerthuso'r rhaglenni robot sgwrsio a grëwyd hyd yn hyn.


## Deilliannau dysgu

### Pob myfyriwr yn gallu: 

- Adnabod dyfais mewnbwn ac allbwn ar gyfrifiadur Raspberry Pi.
- Ychwanegu cod at raglen robot sgwrsio er mwyn caniatáu iddo ddarllen testun 
ar lafar.
- Ychwaengu cod prosesu iaith Cymraeg er mwyn rhoi'r argraff bod y robot yn 
deall Cymraeg rywfaint. 


### Y rhan fwyaf o fyfyrwyr yn gallu:

- Profi a chynnig adborth i’w cyfoedion ar eu rhaglen robot sgwrsio

### Rhai myfyrwyr yn gallu:

- Dyfeisio ffyrdd i wella'r rhaglen robot sgwrsio drwy werthuso.  


## Crynodeb Gwers    

- Gweithgaredd labelu darnau 
- Ychwanegu testun-i-lais
- Rhaglenni Python wedi’u gwella  

## Man Dechrau

Gosodwch o leiaf bedwar set o’r canlynol, neu faint bynnag fedrwch chi eu 
ffeindio o bob eitem ar y rhestr, ar ddesgiau, heb eu cysylltu: 

- Raspberry Pi 
- Seinydd
- Clustffonau
- Camera Pi (os oes un gennych chi) 
- Gwe Gamera
- Bysellfwrdd
- Llygoden
- Monitor 

Dosbarthwch y myfyrwyr mewn i grwpiau a rhoddwch nodiadau gludiog neu bapur 
lliw gwahanol i bob grŵp. Rhowch amser i’r myfyrwyr labelu'r holl gydrannau 
gyda’r wybodaeth ganlynol:

- Beth ydyw
- A yw’n fewnbwn, proses neu ddyfais allbwn
- Yr hyn y mae'n ei wneud

Ar ôl i’r myfyrwyr labelu'r cydrannau, gofynnwch i’r grwpiau egluro eu hatebion.
Nodwch unrhyw rai sy’n anghywir neu'n arbennig o ddiddorol, a thrafodwch y 
rhesymu gyda’r dosbarth. Eglurwch fod gan bob cyfrifiadur fewnbynnau ac 
allbynnau. Mae’n bwysig nodi hyn ar gyfer eu rhaglen robot sgwrsio, gan fod yn 
rhaid iddyn nhw glywed lleferydd y robot yn allbynnu i’r clustffonau neu seinydd.

![](audio_output.png)

## Prif Ddatblygiad

(1) Gofynnwch i’r myfyrwyr osod eu hoffer Raspberry Pi, ei droi ymlaen a 
mewngofnodi ar eu Pi gan ddefnyddio'r enw defnyddiwr `pi` a’r cyfrinair 
`raspberry`. Wedyn dylent lwytho eu rhaglenni robot sgwrsio gan ddefnyddio 
**IDLE3**. 
	
(2)  Gan ddefnyddio eu gwaith cartref o’r wers flaenorol, cyfarwyddwch y 
myfyrwyr i ychwanegu mwy o gwestiynau at eu cod gan ddefnyddio `input` a `print`.

(3)  Eglurwch y bydd angen i’r myfyrwyr ychwanegu rhywfaint o god fel y gall 
y Raspberry Pi lefaru'r geiriau a phrosesu iaith yn y rhaglen. Bydd angen i’r
myfyrwyr ychwanegu'r cod canlynol at frig eu rhaglenni:

```python   
# Fy rhaglen Python gan ...
from cysill import gwirio_testun
from lleferydd import llefaru, cwestiwn
from canfodiaith import iaith_testun
from rhannauymadrodd import enw_lle, enw_person
```
	
*Nodwch fod y bylchau yn bwysig; dylai’r golygydd testun yn IDLE3 greu’r 
bylchau yn awtomatig ar eich rhan. Hefyd, mae’r bylchau rhwng y geiriau a’r 
defnydd o ddyfynodau yn bwysig. Ni fydd y rhaglen yn gweithio os nad ydyn 
nhw yno.*    

(4) Gofynnwch i’r myfyrwyr gadw hwn fel ffeil newydd drwy glicio ar **File** 
a **Save As**, ac yna ei enwi yn **robot1**. Gallent redeg eu rhaglenni, a 
dylent glywed llais yn dweud “helo”! 

(5) Nesaf, eglurwch ei bod hi nawr yn bosib, yn lle argraffu cwestiynau at y 
sgrin, i gael eu llais robot i’w llefaru nhw ac wedyn ateb. I wneud hyn, yn 
gyntaf mae angen iddyn nhw dynnu'r gair 'print' ac ailosod yr enw ffwythiant 
`robot` yn ei le, yna tynnu'r coma `,` a’i gyfnewid gyda’r symbol `+`. Gofynnwch
i’r myfyrwyr gadw a phrofi ar y pwynt yma. Allen nhw egluro beth sydd yn 
digwydd? Mae pwyntiau bonws ar gyfer unrhyw un all feddwl am ffordd i gael y 
robot i ofyn y cwestiynau hefyd! Yr ateb yw ychwanegu llinell arall uwchben y 
llinell mewnbwn gan ddefnyddio'r ffwythiant `robot`, er enghraifft: 
	
```python
enw = cwestiwn('beth yw dy enw?')
llefaru("Braf cwrdd â ti " + enw)
```

(6) Adnabod iaith 

Mae modd i'r robot adnabod os yw testun yn Gymraeg neu beidio. Mae'n gallu 
gwneud hyn am ei fod yn gwybod pob math o reolau sy'n gwahaniaethu rhwng 
gwahanol ieithoedd. Er mwyn defnyddio'r rhaglen hon, mae angen defnyddio'r 
gorchymyn print ac yna (iaith_testun. Wedyn ychwanegwch y testun yr hoffech ei adnabod 
rhwng cromfachau a dyfynodau. Edrychwch ar yr enghraifft o god isod sy'n cynnwys 
dadansoddiad o dri thestun mewn tair iaith wahanol. Pa ieithoedd ydych chi yn
meddwl yw'r rhain? Mewnbynnwch y cod er mwyn gweld!

```python
print(iaith_testun("Dw i'n byw yng Ngarndolbenmaen"))
print(iaith_testun("And they all lived happily ever after"))
print(iaith_testun("Je suis Charlie"))
```
(7) Enwau priod

Mae gan y robot hefyd y gallu i adnabod y gwahaniaeth rhwng enwau priod ac enwau
cyffredin. Enw priod yw enw am rywbeth penodol; fel enw person (e.e. Harry 
Styles), lle (e.e. Bangor) neu frand (e.e. Tesco). Mae enw priodol yn wahanol i
enw cyffredin, sy'n dynodi mathau o bethau, e.e. dyn, tre, siop. Un ffordd hawdd
iawn o adnabod y gwahaniaeth yw bod gan enwau priod lythyren fawr fel arfer!

Gall adnabod y gwahaniaeth hwn fod yn ddefnyddiol am sawl rheswm, ac mae gan
ein robot y gallu i wneud y dasg yn haws o lawer. Teipiwch y cod isod i mewn i'r 
derfynell. Mae'r testun yr hoffech chi ei archwilio yn mynd rhwng y dyfynodau yn y 
cromfachau. Bydd y robot yn edrych drwy'r testun ac yn darganfod pa eiriau sy'n 
enwau priod. Nodwch fod y gorchymyn ar gyfer chwilio am enw lle ac enw person 
yn wahanol!

```python
print(enw_lle("Mae Garndolbenmaen yn le braf ac yn heulog bob dydd"))
print(enw_person("Tudur Owen yw fy hoff berson ar S4C"))
```

 (8) Gwirio sillafu a gramadeg 

Un o adnoddau mwyaf poblogaidd a defnyddiol yr Uned yw'r gwirydd sillafu a 
gramadeg. Mae hyn yn caniatáu i'r robot wybod holl reolau sillafu a gramadeg yr 
iaith Gymraeg, fel ei fod wedyn yn gallu adnabod gwallau yn eich testun yn 
awtomatig. Mae hwn yn gymorth mawr i unrhyw un sydd eisiau cywiro eu Cymraeg, ac
mae llawer o bobl yn y byd gwaith yn ei ddefnyddio! 

Er mwyn ei ddefnyddio, bydd yn rhaid i chi osod y cod cywir fel y gwelir isod. 
Mewnbynnwch y testun yr hoffech chi ei wirio rhwng y dyfynodau sydd yn y cromfachau.
Isod rydym wedi mewnbynnu'r testun "mae hen gwlad fy tadau" sy'n cynnwys 
gwallau bwriadol! Allwch chi weld lle maen nhw? Rhedwch y cod isod i gael gweld 
ateb y gwirydd:

```python
gwirio_testun("Mae hen gwlad fy tadau")
```
Fel y gallwch weld, mae'r gwirydd wedi adnabod dau wall treiglo yn y testun. 
Dylai 'gwlad' fod yn 'wlad' (am fod enw benywaidd fel 'gwlad' yn treiglo'n 
feddal ar ôl ansoddair fel 'hen') a dylai 'tadau' fod yn 'nhadau' (am fod 
geiriau ar ôl 'fy' yn treiglo'n drwynol). Yn awr eich bod chi wedi gweld pa mor
ddefnyddiol yw hwn, beth am ei ddefnyddio er mwyn cywiro eich gwaith cartref?
Mae'n hawdd!

## Dod i Derfyn

Gofynnwch i'ch myfyrwyr gyfnewid seddi â phartner. Mae ganddyn nhw funud neu
ddwy i brofi rhaglen eu partner, ac i awgrymu o leiaf 
un gwelliant drwy ysgrifennu sylw drwy ddefnyddio'r symbol `#`. Dylai’r myfyrwyr 
wedyn ddychwelyd at eu rhaglenni a gwneud y gwelliant 
gafodd ei argymell. 

Fel tasg estynedig, gallai myfyrwyr dynnu un llinell o god o raglen eu partner,
newid yn ôl, a gweld os gallant drwsio'r cod gwallus!