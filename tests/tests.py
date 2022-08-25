from mypackage import myModule

def test_oddnum():
    
   assert myModule.oddnum([9,25,49,81,4,16])==[3,5,7,9], "incorrect"
   assert myModule.oddnum([1,25,49,81])==[1,5,7,9], "incorrect"
