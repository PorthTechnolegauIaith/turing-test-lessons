# Cyfarwyddiadau i Fyfyrwyr 1

## Cysylltu eich Raspberry Pi

Mae’r Raspberry Pi yn gyfrifiadur syml. Nid yw’n ddefnyddiol iawn ar ben ei hun. Er mwyn rhaglennu sain gydag ef, bydd yn rhaid i ni gysylltu amryw o bethau ato.

- **   Cerdyn SD**. Mae’r cerdyn hwn yn cynnwys y rhaglenni all gael eu llwytho ar i’r Raspberry Pi er mwyn iddo allu gwneud pethau. Mae angen i chi ei lithro i mewn i’r slot gyda’r piniau yn wynebu i mewn tuag at y Raspberry Pi. Dylai fod y label yn weladwy pan mae wedi’i osod yn iawn. 
- **Bysellfwrdd**. Plygiwch y bysellfwrdd i mewn i un o’r ddau borth USB.  Ystyr USB yw USB Universal Serial Bus. Mae’n fath o declyn cysylltu ar gyfer pob math o ddyfeisiau. Y bysellfwrdd fydd y prif fath o arf y byddwn ni yn ei ddefnyddio er mwyn cysylltu ein rhaglenni at y Raspberry Pi.
- **Llygoden**. Plygiwch y llygoden i mewn i’r porth USB arall. 
- **Holltwr sain**. . Mae hwn yn gebl bydd yn hollti’r signal sain mewn dau gyfeiriad. Plygiwch hwn i mewn i’r jac sain ar y Raspberry Pi.
- **Clustffonau**. Bydd y rhain yn caniatáu i chi glywed y sain y byddwch yn ei gynhyrchu. Plygiwch y rhain i mewn i’r holltwr sain.  
- **Monitor**. Bydd hwn yn caniatáu i chi weld y rhaglen rydych chi yn ei chreu. Plygiwch y cysylltwr HDMI i mewn i borth HDMI y Raspberry Pi. Plygiwch ochr arall y cebl HDMI i mewn i’ch monitor. Bydd angen i chi wneud yn sicr fod y monitor wedi’i bweru, a'i fod wedi’i droi ymlaen ac ei fod wedi’i osod i ddangos yr hyn sydd yn dod drwy’r cebl (yr opsiwn digidol fel arfer).
- **Addaswr pŵer**. Plygiwch yr addaswr pŵer i mewn i soced ac yna plygiwch gysylltwr USB bach i mewn i’r Raspberry Pi. Pan rydych yn troi swîts y soced ymlaen, dylech weld y Raspberry Pi yn fflachio a dylai fod testun yn ymddangos ar y monitor. 

## Mewngofnodi

1. Unwaith mae’r Raspberry Pi wedi gorffen cychwyn ac mae’r testun wedi gorffen hedfan heibio ar y sgrin, byddwch yn gweld promt syml yn gofyn am eich enw defnyddiwr.  
2. Teipiwch 'pi' ac yna **Enter**. 
3. Nesaf, bydd y rhaglen yn gofyn am eich cyfrinair. Teipiwch raspberry ac yna gwasgwch Enter eto. Peidiwch â phoeni os nad ydych chi’n gweld y cyfrinair ar y sgrin wrth i chi ei deipio. Mae hon yn nodwedd diogelwch er mwyn gwneud yn sicr na all pobl edrych dros eich ysgwydd a dwyn eich cyfrinair. Dylech nawr weld promt testun rhyfedd. 

## Dechrau yr Amgylchedd Graffigol

Mae’r promt testun rhyfedd rydych chi’n edrych arno yn un o’r ffyrdd mwyaf pwerus i gyfathrebu gyda chyfrifiadur. Fodd bynnag, nid yw’n hawdd iawn ac mae’n llawn gorchmynion rhyfedd a dirgel, yn debyg i gynnwys swyn hud. Gallwn felly symud i amgylchedd graffigol mwy cyfarwydd, gyda ffenestri a bariau dewislen, fydd gobeithio yn teimlo yn fwy cyfforddus. I wneud hyn teipiwch y swyn hud `startx` i mewn i’r derfynell testun a gwasgwch **Enter**.

## Dechrau Amgylchedd Raglennu Python 3  

Unwaith mae’r amgylchedd graffigol wedi cychwyn, gallwch glicio ar y **start menu** ar waelod ochr chwith y sgrîn (mae’n edrych fel aderyn bach) a dewis **IDLE3** o’r **Programming menu**. 

![](idle3.png)

## Ysgrifennu Rhaglen Syml

Rydych yn mynd i ysgrifennu rhaglen er mwyn creu llun o siâp. 

1. Wrth y tri saeth `>>>` neu bromt teipiwch: 

	```python
	import turtle
	```
	Yna gwasgwch **Enter**.
	
2. wrth y `>>>` nesaf neu bromt teipiwch:

	```python
	robot = turtle.Turtle()
	```
			
	Mae'r gorchymyn hwn yn agor ffenest Turtle Graphics gyda saeth yn y canol. Dyma eich crwban chi, o'r enw robot, a gallwch roi cyfarwyddiadau iddo er mwyn gwneud iddo symud. 
	
3. Beth am wneud iddo edrych mwy fel crwban robotaidd drwy deipio:

	```python
	robot.shape("turtle")
	```

4. I gyfarwyddo i'ch crwban robotaidd symud, teipiwch:

	```python
	robot.forward(100)
	robot.right(90)
	```
	
	Beth sy'n digwydd? Beth arall fyddai angen i chi ei wneud er mwyn creu siap sgwâr? 
	![](robot-turtle.png)