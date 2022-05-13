def romtoint(s):
 integer=0
 # dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

 for i in range(len(s)):
   if(s[i]=="I"):
    integer+=1
   elif(s[i]=="V"):
    if(i!=0 and s[i-1]=="I"):
     integer+=3
    else:
     integer+=5
   elif(s[i]=="X"):
    if(i!=0 and s[i-1]=="I"):
     integer+=8
    else:
     integer+=10
   elif(s[i]=="L"):
    if(i!=0 and s[i-1]=="X"):
     integer+=30
    else:
     integer+=50
   elif(s[i]=="C"):
    if(i!=0 and s[i-1]=="X"):
     integer+=80
    else:
     integer+=100
   elif(s[i]=="D"):
    if(i!=0 and s[i-1]=="C"):
     integer+=300
    else:
     integer+=500
   elif(s[i]=="M"):
    if(i!=0 and s[i-1]=="C"):
     integer+=800
    else:
     integer+=1000
 return integer

print(romtoint("MCMXCIV"))
   
    
   
    
   
   
  
  