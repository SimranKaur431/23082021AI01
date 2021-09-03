s='ssii'
c={i:s.count(i) for i in s}
d=list(set(c.values()))

for i in range(len(d)):
   if len(d)==1 or len(d)==2 :
      print("yes")
      break
   
   else:
       print('no')
       break
