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
second= float(input("What is the second number?"))

for key in operations:
    if key == operator:
        result = operations[key](first,second)
        print(f'{first} {key} {second} = {result}')
        break
else:
        print('inalid operator')

question= input("You want to continue with previous result?")

continue_calculation = True

while continue_calculation:
    if question == 'yes':
        first= result
        operator= input("Type the mathematical operator.")
        second= float(input("What is the second number?"))

        for key in operations:
            if key == operator:
                result = operations[key](first,second)
                print(f'{first} {key} {second} = {result}')
                continue_calculation = False
                break

        else:
                print('inalid operator')

# if question == 'no':
#     print('Thankyou')