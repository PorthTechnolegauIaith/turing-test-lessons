from cysill import gwirio_testun
from lleferydd import llefaru, cwestiwn

testun=""

while not testun.strip():    
    testun=cwestiwn("Ysgrifennwch destun er mwyn i mi ei chywiro :")
    
testun_wedi_gwirio = None

while True:
    testun_wedi_gwirio, nifer_cywiriadau = gwirio_testun(testun_wedi_gwirio or testun)
    if nifer_cywiriadau==0:
        break
    
llefaru("Y testun cywir yw : %s" % testun_wedi_gwirio)
