s='ssiieeedsf'
c={i:s.count(i) for i in s}
d=list(set(c.values()))

for i in range(len(d)):
   if len(d)==1 :
      print("yes")
   elif len(d)==2:
      if d[0]<d[1]:
        print("yes")
        break
   else:
       print('no')
       break
