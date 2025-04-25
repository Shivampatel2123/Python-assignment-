def fun():
    print("Function fun() called.")

def disp():
    print("Function disp() called.")

def msg():
    print("Function msg() called.")

functions = [fun, disp, msg]

for function in functions:
    function()
