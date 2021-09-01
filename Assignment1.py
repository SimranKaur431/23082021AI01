numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
 742, 717, 958,743, 527]
for num in numbers:
    if(num<237 and num%2==0):
       print(num)
########################################
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
####################################
def ispangram(str):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for char in alphabet:
    if char not in str.lower():
      return False
  return True


string = input("Enter the string :")
if (ispangram(string) == True):
    print("Yes")
else:
    print("No")

##############################################
    

a_string = str(input())
count = 0;
string1 = ""
string2 = ""
numbers1 = []
numbers2 = []

for i in a_string:
    if (i == "#"):
        count = 1
        continue

    if (count == 0):
        string1 = string1 + i
    else:
        string2 = string2 + i

for word in string1.split():
    if word.isdigit():
        numbers1.append(int(word))

for word in string2.split():
    if word.isdigit():
        numbers2.append(int(word))

print("x = ", numbers1)
print("y = ", numbers2)

#####################################################################




items=[x for x in input().split(',')]
items.sort()

print( ','.join(items))

#########################################################

s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

########################################################

pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
dis=int((pos[1]**2+pos[0]**2)**1/2)

if(dis - int(dis) > 0.5000):
      ans=int(dis)+1
else:
      ans=int(dis)

print(ans)
##############################################################
