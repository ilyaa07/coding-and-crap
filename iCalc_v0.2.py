print("iCalc v0.2")

function = input("What Function Would You Like To Do? {+,-,*,/ or Quit} ")

A1 = input("Select A Number ")
A2 = input("Select Another Number ")
if function == "+":
    Result = float(A1) + float(A2)
    
if function == "-":
    Result = float(A1) - float(A2)
    
if function == "*":
    Result = float(A1) * float(A2)
    
if function == "/":
    Result = float(A1) / float(A2)
    
print(Result)
