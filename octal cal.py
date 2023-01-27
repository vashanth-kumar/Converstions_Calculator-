print("\n\t WELCOME TO OCTAL CALCULATOR....!")
a=int(input("\nEnter the Value  to Convert Octal Number To Decimal, Binary & Hexa Decimal: "))
print("Entered Octal Value is:", a)


print("\n",a,"in Binary value is :",bin(a) )
print("\n",a,"in HexaDecimal value is :",hex(a) )
octnum = a
chk = 0
i = 0
decnum = 0
while octnum != 0:
    rem = octnum % 10
    if rem>7:
        chk = 1
        break
    decnum = decnum + (rem * (8 ** i))
    i = i+1
    octnum = int(octnum/10)
    if chk == 0:
        print("\n",a,"in Decimal value is :",decnum)
print("\n--------------------------------------------------------------------------------------------------------")
print("\n\t Note :")
print("\n\t The Last  Of the Decimal Number is  correct don't take the Before Values of Decimal Numbers.....","\n\t Sorry We Correct The Mistake Soon")
