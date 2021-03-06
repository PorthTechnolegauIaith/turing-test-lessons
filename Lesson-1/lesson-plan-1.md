# Gwers 1 – Sut mae cyfrifiaduron yn meddwl?

## Cyflwyniad

Sut mae cyfrifiaduron yn meddwl? Yn y wers yma, bydd myfyrwyr yn ystyried y ffordd y mae angen i gyfrifiaduron a robotiaid ddilyn cyfres o orchmynion er mwyn cyflawni tasg. Mae rhan sylweddol o’r wers yma wedi’i chysegru i gael myfyrwyr i ddefnyddio Raspberry Pi am y tro cyntaf, mewngofnodi, cael mynediad at IDLE3, a theipio cyfres fer o gyfarwyddiadau er mwyn creu siâp.

## Amcanion Dysgu

- Gwybod fod cyfrifiaduron yn dilyn cyfres o gyfarwyddiadau i achosi i rywbeth ddigwydd.
- Gallu gosod y Raspberry Pi, a rhoi cyfres o gyfarwyddiadau mewn Python i greu siâp. 


## Deilliannau Dysgu

### Pob myfyriwr yn gallu: 

- Gwybod fod cyfrifiaduron yn rhedeg rhaglenni sydd yn gyfres o gyfarwyddiadau i wneud i rywbeth ddigwydd.
- Ysgrifennu rhaglen syml. 

### Y rhan fwyaf o fyfyrwyr yn gallu:

- Gwybod fod Python yn iaith rhaglennu gyfrifiadurol.  
- Ysgrifennu rhaglen Python syml ac egluro ei dilyniant.

### Rhai myfyrwyr yn gallu: 

- Ysgrifennu rhaglen i greu siâp mwy cymhleth.


## Crynodeb Gwers

- Cyflwyniad at rannau corfforol sylfaenol Raspberry Pi 
- Arddangosiad y gall y Raspberry Pi ymddwyn fel cyfrifiadur traddodiadol
- Y rhaglen Python gyntaf 

## Man Cychwyn

Yn gyntaf, dewiswch dri neu bedwar myfyriwr i fod yn robotiaid, ac yna rhannwch y myfyrwyr sy’n weddill yn dri neu bedwar tîm. Mae pob tîm yn cystadlu mewn ras i weld pwy all dywys ‘robot’ o gwmpas y dosbarth, neu ‘ddrysfa’ (maze). Gallai hyn fod yn dasg awyr agored. Eglurwch i’r ‘robotiaid’ fod yn rhaid iddyn nhw esgus bod yn dwp, a dim ond dilyn y cyfarwyddiadau maen nhw’n derbyn gan y myfyrwyr eraill. 

Yn ystod y ras, gwnewch yn sicr fod y myfyrwyr yn defnyddio cyfarwyddiadau fel “camu ymlaen 10 cam” neu “troi 90 gradd i’r dde”.

Unwaith fod y ras wedi’i hennill, trafodwch unrhyw broblemau ddaeth y timau ar eu traws wrth geisio cael y robot i ddilyn eu cyfarwyddiadau.  Ceisiwch dynnu sylw'r myfyrwyr at y ffaith na allasai’r robot wneud ei benderfyniadau ei hun, a'u bod wedi gorfod bod yn benodol iawn ynglŷn â throeon a chamau oherwydd hynny. 

Eglurwch fod cyfrifiadur yn gweithio drwy gyflawni datganiadau un ar ôl y llall mewn dilyniant penodol. Gelwir dilyniant arbennig o ddatganiadau yn rhaglen. Mae pob rhaglen yn gweithredu gyda llif reolaeth arbennig ; mae hyn yn disgrifio pa ddatganiad y byddem yn ei gyflawni, a beth fydd y datganiad nesaf. 

## Prif Ddatblygiad

1. Arddangoswch Raspberry Pi wedi’i gysylltu yn barod, a’r rhaglen robot sgwrsio olaf yn rhedeg.  Dangoswch famfwrdd Raspberry Pi a gofynnwch i’r myfyrwyr beth maen nhw’n meddwl ydyw. Eglurwch mai cyfrifiadur ydyw mewn gwirionedd ac ein bod ni am wneud rhywbeth arbennig iawn gydag ef yn y gwersi sydd i ddod. Yn lle rhedeg apiau a gemau mae pobl eraill wedi eu creu ar ein cyfer, byddem yn dysgu sut i ysgrifennu meddalwedd er mwyn creu robot sy’n sgwrsio â ni.  

2. Dechreuwch gyda holl gydrannau'r Raspberry Pi ar y bwrdd: bysellfwrdd, llygoden, seinydd, cerdyn cof, cyflenwad bŵer, monitor, cebl monitor, a’r Raspberry Pi ei hun. Gofynnwch i’r dosbarth enwi a disgrifio pob cydran wrth i chi ei gysylltu at y Raspberry Pi o flaen y dosbarth. I orffen, plygiwch y pŵer i mewn a gwyliwch y cyfrifiadur yn cychwyn. Arddangosiad amgen byddai i adael allan y cerdyn cof a cheisio cychwyn y Pi, fyddai yn methu. Gallech chi wedyn ddisgrifio'r cerdyn cof fel rhywbeth sy’n cynnwys cyfarwyddiadau sy’n dweud wrth y Pi sut i ddechrau.  Dylai fod y Raspberry Pis i gyd wedi cychwyn ac ar y sgrin mewngofnodi yn disgwyl am ddilysiad. 

3. Gofynnwch i’r myfyrwyr osod eu hoffer Raspberry Pi, ei droi ymlaen a mewngofnodi yn defnyddio eu henw defnyddiwr `pi` a’r cyfrinair `raspberry`. 

	*Nodwch na fydd y myfyrwyr yn gallu gweld unrhyw destun wrth deipio’r cyfrinair, ond sicrhewch iddyn nhw ei fod yn gweithio. Pam bod hyn yn digwydd? Cliw: beth fyddai yn digwydd petai rywun yn edrych dros eu hysgwyddau? *
	
4.   Nesaf, dylai’r myfyrwyr lwytho’r amgylchedd graffigol drwy deipio 'startx'. Unwaith mae’r bwrdd gwaith wedi llwytho, dangoswch i’r myfyrwyr sut mae agor **IDLE3** unai drwy glicio dwywaith ar yr eicon bwrdd gwaith, neud drwy glicio ar y **prif ddewislen** ac yna **rhaglennu** a dewis **IDLE3**.
	
	*Nodwch fod y gyfres yma o wersi yn defnyddio Python 3. Os yw’r myfyrwyr yn rhedeg IDLE falle na fydd eu cod yn rhedeg.*

5. Eglurwch i’r myfyrwyr fod **IDLE3** yn rhaglen neu yn amgylchedd sydd yn eich caniatáu i ysgrifennu rhaglen syml gan ddefnyddio'r iaith raglennu **Python**. Mae’n caniatáu i chi ysgrifennu, golygu a rhedeg cod. 

6. Dangoswch i’r myfyrwyr sut i greu siâp drwy deipio dilyniant o gyfeiriadau, linell wrth linell. Gwelwch y [Cyfarwyddiadau i Fyfyrwyr](student-instructions-1.md) ar gyfer y camau sydd eu hangen er mwyn cyflawni'r dasg hon. 

7. Gofynnwch i’ r myfyrwyr ddiffodd eu Raspberry Pis drwy glicio ar yr eicon **Cau i Lawr** ar y bwrdd gwaith. 

## Dod i derfyn

Ysgrifennwch y rhestr o eiriau canlynol ar y bwrdd gwyn: 

- Cyfarwyddiadau
- Dilyniant
- Raspberry Pi
- Python
- IDLE3

Dewiswch fyfyriwr ar hap o’r dosbarth. Mae’n rhaid iddyn nhw ddewis un o’r geiriau ar y bwrdd gwyn, sefyll ar eu traed a phwyntio at rywun arall yn y dosbarth sy’n gorfod egluro ystyr y gair. Bydd y person yna wedyn yn dewis person arall ac yn rhoi gair iddyn nhw egluro. 

## Gwaith cartref

Dylai'r myfyrwyr ysgrifennu dilyniant o gyfarwyddiadau ar gyfer tasg, fel gwisgo ar gyfer yr ysgol neu eu symudiadau dawns gorau.