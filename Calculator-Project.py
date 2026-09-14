def add(a,b):
    return a+b

def subtract (a,b):
    return a-b

def divide(a,b):
    return a/b

def multiply(a,b):
    return a*b

operations={
    '+':add,
    '-':subtract,
    '/':divide,
    '*':multiply
}

first= float(input("What is the first number?"))
operator= input("Type the mathematical operator.")
if operator not in operations:
        print('invalid operator')
        
second= float(input("What is the second number?"))

for key in operations:
    if key == operator:
        result = operations[key](first,second)
        print(f'{first} {key} {second} = {result}')
        break
else:
        print('invalid operator')


continue_calculation = True

while continue_calculation:
    question= input("You want to continue with previous result?").lower()

    if question == 'yes':
        first= result
        operator= input("Type the mathematical operator.")
        if operator not in operations:
            print('invalid operator')
            continue
        second= float(input("What is the second number?"))

        for key in operations:
            if key == operator:
                result = operations[key](first,second)
                print(f'{first} {key} {second} = {result}')
                break

            else:
                print('invalid operator')

    else:
         print('thankyou')
         continue_calculation=False