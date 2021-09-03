Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,6):
	print("*" * i)

	
*
**
***
****
*****
>>> for i in range(1,6):
	print(' ' * (5-i) + '*' * i)

    *
   **
  ***
 ****
*****
>>> 
>>> for i in range(1,6):
    for j in range(1,i+1):
       print(j,end=" ")
    print('')

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
>>> for i in range(0,6):
   for j in range(0,i):
       print(i,end=" ")
   print('')

   

1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
>>> for i in range(1,6):
	print('*' * i + ' ' * (10-2*i) + '*' * i)

	
*        *
**      **
***    ***
****  ****
**********
>>> 