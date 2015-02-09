from cysill import gwirio_testun
from lleferydd import llefaru

testun=""

while not testun.strip():
    llefaru("Ysgrifennwch destun er mwyn i mi ei chywiro")
    testun=input("Ysgrifennwch destun er mwyn i mi ei chywiro : \n")
    
    
testun_wedi_gwirio = None

while True:
    testun_wedi_gwirio, nifer_cywiriadau = gwirio_testun(testun_wedi_gwirio or testun)
    if nifer_cywiriadau==0:
        break
    
print ("Y testun cywir yw : %s" % testun_wedi_gwirio)
