'''
input_date = input('十月五號')
print('十月五號',)
'''

'''
class_boy = 10
class_girl = 12

print('全班人數',class_boy + class_girl)
'''

'''
string1='啦課上次二第'
print(string1[-1:-7:-1])
'''

'''
input_1 = int(input("請輸入整數:"))
input_2 = int(input("請輸入整數:"))
print(input_1+input_2)
print('整數型態:',type(input_1+input_2))
print(input_1-input_2)
print(input_1*input_2)
print(input_1/input_2)
print(input_1%input_2)
print(input_1//input_2)
print(input_1**input_2)
'''

'''
a = int(input('請輸入數字:'))
b = int(input('請輸入數字:'))

if a%b == 0 :
    print(str(a)+'可以被'+str(b)+'整除')
else:
    print(str(a)+'不可以被'+str(b)+'整除')
''' 

'''
Day = input('請輸入星期幾:')
if Day == '一':
    print('吃麥當勞')
else :
    print('隨便')    
'''

'''
Day = input('請輸入星期幾:')
if Day == '一':
    print('麥當勞')
elif Day == '二':
    print('東門麥當勞')
elif Day == '三':
    print('擄胃專家')
else:
    print('都好')            
'''

'''
number1 = int(input('請輸入數字1:'))
number2 = int(input('請輸入數字2:'))
op = input("請輸入運算:+,-,*,/:")

if op == '+':
    print(number1 + number2)
elif op == '-':
    print(number1 - number2)
elif op == '*':
    print(number1 * number2)
elif op == '/':
    print(number1 / number2)
'''

'''
n = 1
while n < 5:
    print(n)
    n = n + 1 
print('結束了')    
'''

'''
for i in range(3):
    print('重要的事情要講三遍')
'''    

'''
for i in range(0,5):
    print(i)
'''

'''
for i in range(5):
    print(i)
'''

'''
for i in range(1,10,2):
    print(i)
'''

'''
n = int(input('請輸入迴圈次數:'))

for i in range(n):
    print('Hello,World')
'''

'''
String1 = 'Python'

for i in String1:
    print(i)

for i in range(len(String1)):
    print(i)
    print(String1[i])
'''

'''
for i in range(0,11,2):
    if i == 6:
        print('好')
        break
    print(i)
'''

'''
for i in range(0,11,2):
    if i == 6:
        print('好了')
        continue
    print(i)
'''

'''
list1 = [1,2,3,4,5]
for list1 in range(1,6):
    print(list1)
'''

'''
n = 0
for i in range(0,101):
    print(n)
    n = n + 1
'''

'''
n1 = int(input('請輸入數字:'))
n2 = 1

#方法1
print(n2)
for i in range(2,n1+1):
    if n1 % i == 0:
        print(i) 
#方法2
while n1 >= n2:
    if n1 % n2 == 0
    print(n2)
    n2 = n2 +1
'''

'''
Class_1 = ['B177793449','A134689794','G130949062','K147378503','B200674844',
'B163671690','B205054646','E231081836','D219055993','D183361919','X161067471'
,'B281840622','B153971781','N151829346','B283079309']

Taichung_people = []
Taichung_man = []
Taichung_woman = []

for i in Class_1:
    if i[0] == 'B':
        Taichung_people.append('Yes')
        if i[1] == '1':
            Taichung_man.append('Yes')
        elif i[1] == '2':
            Taichung_woman.append('Yes')
print('有',len(Taichung_people),'個台中人')  
print('台中男生有',len(Taichung_man),'個人')
print('台中女生有',len(Taichung_woman),'個人')
'''