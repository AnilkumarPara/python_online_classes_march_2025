a = 10  # Global variable
def local_global():
    a = 5 # Local Variable
    global_variable= globals()
    print("within the function global variable before modification a= ", global_variable['a'])
    print("within the function local variable before modification a= ", a)
    a = 30
    global_variable['a']=20
    print("within the function global variable after modification a= ", global_variable['a'])
    print("within the function local variable after modification a= ", a)

local_global()
# a = a + 1
# print(f"outside the function a=  {a}")