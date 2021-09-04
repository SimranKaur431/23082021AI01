s='ssiieeefefd'
c={i:s.count(i) for i in s}
d=list(set(c.values()))
if len(d)==1 or len(d)==2 :
   print("My String")
else:
   print('Not my string')
      
