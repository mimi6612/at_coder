a,b = map(int, input().split())
def isEven(num):
    return num % 2 == 0
    
if isEven(a) or isEven(b):
   print("Even") 
else:
    print("Odd")

