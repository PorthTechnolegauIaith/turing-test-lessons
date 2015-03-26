from cysill import gwirio_testun
from canfodiaith import iaith_testun

testun=""

while not testun.strip():    
    testun=input("Ysgrifennwch destun er mwyn i mi ei chywiro :\n")
    
testun_wedi_gwirio = None
iaith = iaith_testun (testun)

if (iaith=="cy"): 
    while True:
        testun_wedi_gwirio, nifer_cywiriadau = gwirio_testun(testun_wedi_gwirio or testun)
        if nifer_cywiriadau==0:
            break
        
    print("Y testun cywir yw : %s" % testun_wedi_gwirio)

else:
    
    print("Dwi ddim yn gallu gwirio testun iaith %s" % iaith)
    
