#   Q1 Ans/

from cmath import pi
from itertools import count


String = "bluhbluhbluh"

NewString = String.replace('b', '')
print(NewString)  

#   Q2 Ans/

for num in range(0,30):
    if num >1:
        for j in range(2,num):
            if num % j == 0:
                break
        else:
            print(num)

#   Q3 Ans/

AnothaString = 'ahhhhhhhahhahhahhah pfffttt'
char = 'a'
i = 0
count = 0
while i < len(AnothaString):
    if AnothaString[i] == char:
        count += 1
    i += 1
print(f"total char no {count}")
 
