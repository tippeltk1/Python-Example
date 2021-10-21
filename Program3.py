"""--------------------------------------------------------------------------
this is where the roman digit later in the program comes to be turned into
numbers. returns -1 if there is not a matching letter.
----------------------------------------------------------------------------"""
def value(roman_digit):
    if roman_digit == 'I':
        return 1
    if roman_digit == 'V':
        return 5
    if roman_digit == 'X':
        return 10
    if roman_digit == 'L':
        return 50
    if roman_digit == 'C':
        return 100
    if roman_digit == 'D':
        return 500
    if roman_digit == 'M':
        return 1000
    return -1
'''----------------------------------------------------------------------------
This is where the operand gets assigned to a roman digit to go back to value
above. Then is stored as a num to be used in a mthmatical formula using the
op that was pulled from the Doc. It returns the fianl value and the nums.
----------------------------------------------------------------------------'''
def PerformOperation(operand1, operand2, op):
    roman_digit = operand1
    value(roman_digit)
    num1 = RomanDigitValue(roman_digit)
    print("The first number is", num1)
    roman_digit = operand2                    #splits up the ops
    value(roman_digit)
    num2 = RomanDigitValue(roman_digit)
    print("The second number is", num2)
    #Here is where I start the math
    if op == '-':
        val = (num1 - num2)
        if val < 0:
            val = (val/-1)
    if op == '**':
        val = (num1 ** num2)
    if op == '*':
        val = (num1 * num2)
    if op == '/':
        val = (num1 / num2)
    if op == '//':
        val = (num1 // num2)
    if op == '%':
        val = (num1 % num2)
    if op == '+':
        val = (num1 + num2)
    return val, num1, num2
'''----------------------------------------------------------------------------
This is where the final value comes back to processed as a roman numeral.
It returns a ? when the numbers are below zero. It returns the final roman
numeral.
----------------------------------------------------------------------------'''
def RomanDigitChar(val):
    final = ''
    if val < 0:
        print('?')
    while val >= 1000:
        final += 'M'
        val -= 1000
    while val >= 500 and val < 1000:
        final += 'D'
        val -= 500
    while val >= 100 and val < 500:
        final += 'C'
        val -= 100
    while val >= 50 and val < 100:
        final += 'L'
        val -= 50
    while val >= 10 and val < 50:
        final += 'X'
        val -= 10
    while val >= 5 and val < 10:
        final += 'V'
        val -= 5
    while val >= 1 and val < 5:
        final += 'I'
        val -= 1
    return final
'''----------------------------------------------------------------------------
This is where the roman digit comes from above from the operand and is sent  to
value to be returned as number. Where num keeps the count of the the numbers.
----------------------------------------------------------------------------'''
def RomanDigitValue(roman_digit):
    print(roman_digit)
    num = 0
    for letter in roman_digit:
        num = num + value(letter)
    return num
'''----------------------------------------------------------------------------
This is where most things print.
----------------------------------------------------------------------------'''
def finalprnt(op, val, num1, num2, final):
    if op == '-':
        print("Arithmetic operation is", (op))
        if (val * -1) < 0:
            print("The difference of", (num1), "and", (num2), "is", "(-" + final + ")")
        else:
            if val == 0:
                print("The difference of", (num1), "and", (num2), "is Zero (0)")
            else:
                print("The difference of", (num1), "and", (num2), "is", "(" + final + ")")
    if op == '**':
        print("Arithmetic operation is", (op))
        print("The exponentiation of", (num1), "and", (num2), "is", "(" + final + ")")
    if op == '*':
        print("Arithmetic operation is", (op))
        print("The multiplication of", (num1), "and", (num2), "is", "(" + final + ")")
    if op == '/':
        print("Arithmetic operation is", (op))
        print("The division of", (num1), "and", (num2), "is", "(" + final + ")")
    if op == '//':
        print("Arithmetic operation is", (op))
        if val == 0:
            print("The quotient of", (num1), "and", (num2), "is Zero (0)")
        else:
            print("The quotient of", (num1), "and", (num2), "is", "(" + final + ")")
    if op == '%':
        print("Arithmetic operation is", (op))
        print("The remainder of", (num1), "and", (num2), "is", "(" + final + ")")
    if op == '+':
        print("Arithmetic operation is", (op))
        print("The sum of", (num1), "and", (num2), "is", "(" + final + ")")
    print("\n")
'''----------------------------------------------------------------------------
This is the main. Which i included as the get roman numeral. opens and reads
the file while it stores the line as a variable. And then it sends to the rest
of the operations to do the rest.
----------------------------------------------------------------------------'''
def GetRomanNumeral():
   empty_str =''
   input_file = open('Sample.txt', 'r')
   operand1 = input_file.readline()
   operand1 = operand1.strip('\n')
   while operand1:
       operand2 = input_file.readline()
       operand2 = operand2.strip('\n')
       op = input_file.readline()
       op = op.strip('\n')
       val, num1, num2 = PerformOperation(operand1, operand2, op)
       final = RomanDigitChar(val)
       finalprnt(op, val, num1, num2, final)
       operand1 = input_file.readline()
       operand1 = operand1.rstrip('\n')
GetRomanNumeral()
