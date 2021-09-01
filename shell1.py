Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7//3
2
>>> 7/3
2.3333333333333335
>>> 6 == 6
True
>>> a = 20; a+= 30; a%=3; print(a)
2
>>> True * False
0
>>> True & False
False
>>> True and False
False
>>> ((6>3) and (7<4) or (18==3)) and (9>3)
False
>>> True is False
False
>>> False in ‘False’
SyntaxError: invalid character '‘' (U+2018)
>>> ((True == False) or (False > True)) and (False <= True)
False
>>> ##############################################
>>> 
>>> s1="Nice to have it"
>>> s2="here"
>>> s1+' '+s2
'Nice to have it here'
>>> #############################################
>>> 
>>> a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2][0]
'hello'
>>> #################################################
>>> a.insert(0,s1)
>>> a.insert(len(a),s2)
>>> a
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, 'here']
>>> #########################################################
>>> numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
 742, 717, 958,743, 527]
>>> 
=== RESTART: C:/Users/simran/AppData/Local/Programs/Python/Python39/Assignment1.py ===
236
162
104
58
24
>>> #######################################################
>>> 
KeyboardInterrupt
>>> 
>>> color_list_1 = set(["White", "Black", "Red"])
>>> color_list_2 = set(["Red", "Green"])
>>> color_list_1.difference(color_list_2)
{'Black', 'White'}
>>> 
=== RESTART: C:/Users/simran/AppData/Local/Programs/Python/Python39/Assignment1.py ===
236
162
104
58
24
Input an integer : 5
615
>>> ###########################################33
>>> 