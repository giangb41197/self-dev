print("Hello World")
# f & e are global variable
f=1
e=2
# This function is to sum two number a and b. a and b are local variable

def sum(a,b):
    c=a+b
    print("a = " + str(a) + ", " + "b = " + str(b))
    return c
def mul(a,b):
    c=a*b
    print("a = " + str(a) + ", " + "b = " + str(b))
    return c    
   
''' Python only run this function
no input and output
'''
def main():
    result = sum(1,1)
    print(result)
if __name__=="__main__":
    main()    
result_1 = sum(1,1)
print("result 1 =" + str(result_1))
print(f)
print(e)
# Must put the string stuff before the return

result_2 = mul(2,3)
print("result 2 =" + str(result_2))    
'''put definition on top for cleaner code lines'''