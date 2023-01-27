print("\n\t WELCOME TO THE MATHAMATICAL CONVERSTIONS CALCULATORS")
print("\n Enter 1 for Decimal Calculatour""\n Enter 2 for Binary calculatour""\n Enter 3 for Octal calculatour""\n Enter 4 for Hexa Decimal calculatour")
r=int(input("\n\t Enter your Choice :"))
def decimal():
 print("\n\t WELCOME TO DECIMAL CALCULATOR....!")
 a=int(input("\nEnter the Value of Decimal number to Convert in All Forms: "))
 print("Entered Binary Value is:", a)
 print("\n",a,"in binary value is :",bin(a) )
 print("\n",a,"in Octal value is :",oct(a) )
 print("\n",a,"in HexaDecimal value is :",hex(a) )

def binary():
    print("\n\t WELCOME TO BINARY CALCULATOR....!")
    b = list(input("\nEnter the Value of Binary number to Convert in Decimal: "))
    a = int(input("\nEnter the Value of Binary number to Convert in octal & Hexa Decimal: "))
    print("Entered Binary Value is:", a)
    value = 0
    for i in range(len(b)):
        digit = b.pop()
        if digit == '1':
            value = value + pow(2, i)
    print("\n", b, "in Decimal value is:", value)

    print("\n", a, "in Octal value is :", oct(a))
    print("\n", a, "in HexaDecimal value is :", hex(a))

def octal():
    print("\n\t WELCOME TO OCTAL CALCULATOR....!")
    a = int(input("\nEnter the Value  to Convert Octal Number To Decimal, Binary & Hexa Decimal: "))
    print("Entered Octal Value is:", a)

    print("\n", a, "in Binary value is :", bin(a))
    print("\n", a, "in HexaDecimal value is :", hex(a))
    octnum = a
    chk = 0
    i = 0
    decnum = 0
    while octnum != 0:
        rem = octnum % 10
        if rem > 7:
            chk = 1
            break
        decnum = decnum + (rem * (8 ** i))
        i = i + 1
        octnum = int(octnum / 10)
        if chk == 0:
            print("\n", a, "in Decimal value is :", decnum)
    print("\n--------------------------------------------------------------------------------------------------------")
    print("\n\t Note :")
    print("\n\t The Last  Of the Decimal Number is  correct don't take the Before Values of Decimal Numbers.....",
          "\n\t Sorry We Correct The Mistake Soon")

def hexa():
    import math
    print("\n\t WELCOME TO HEXADECIMAL CALCULATOR....!")
    a = (input("\nEnter the Value of HexaDecimal number to Convert in  Octal & Binary: "))
    """
    print("Entered Binary Value is:", a)
    print("Entered HexaDecimal Value is:", a)
    print("\n",a,"in binary value is :",bin(a) )
    print("\n",a,"in Octal value is :",oct(a) )

    print("\n",a,"in Decimal value is :",hex(a) )"""

    j = a
    i = int(j, base=16)
    bin_value = bin(i)
    print("\n", a, "in binary value is :""\n", bin_value)

    hexdecnum = a

    chk = 0
    decnum = 0
    hexdecnumlen = len(hexdecnum)
    hexdecnumlen = hexdecnumlen - 1
    i = 0
    while hexdecnumlen >= 0:
        rem = hexdecnum[hexdecnumlen]
        if rem >= '0' and rem <= '9':
            rem = int(rem)
        elif rem >= 'A' and rem <= 'F':
            rem = ord(rem)
            rem = rem - 55
        elif rem >= 'a' and rem <= 'f':
            rem = ord(rem)
            rem = rem - 87
        else:
            chk = 1
            break
        decnum = decnum + (rem * (16 ** i))
        hexdecnumlen = hexdecnumlen - 1
        i = i + 1

    if chk == 0:
        i = 0
        octnum = []
        while decnum != 0:
            rem = decnum % 8
            octnum.insert(i, rem)
            i = i + 1
            decnum = int(decnum / 8)

        print("\nEquivalent Octal Value is: ")
        i = i - 1
        while i >= 0:
            print(octnum[i], end="")
            i = i - 1
        print()
    else:
        print("\nInvalid Input!")
    print("\n----------------------------------------------------------------------------------------------")
    print("\n\t Note :")
    print("\n\t We Cannot Give A HexaDecimal to Decimal Numbers it is in process....!",
          "\n\t Sorry We Correct The Mistake Soon")

if(r==1):
 decimal()
elif(r==2):
 binary()
elif(r==3):
 octal()
elif(r==4):
 hexa()
else:
 print("\n Invalid Number Input....")
 print("\n Sorry Try Again...!")



