import math
print("\n\t WELCOME TO HEXADECIMAL CALCULATOR....!")
a=(input("\nEnter the Value of HexaDecimal number to Convert in  Octal & Binary: "))
"""
print("Entered Binary Value is:", a)
print("Entered HexaDecimal Value is:", a)
print("\n",a,"in binary value is :",bin(a) )
print("\n",a,"in Octal value is :",oct(a) )

print("\n",a,"in Decimal value is :",hex(a) )"""


j=a
i=int(j,base=16)
bin_value=bin(i)
print("\n",a,"in binary value is :""\n",bin_value )

hexdecnum = a

chk = 0
decnum = 0
hexdecnumlen = len(hexdecnum)
hexdecnumlen = hexdecnumlen-1
i = 0
while hexdecnumlen>=0:
    rem = hexdecnum[hexdecnumlen]
    if rem>='0' and rem<='9':
        rem = int(rem)
    elif rem>='A' and rem<='F':
        rem = ord(rem)
        rem = rem-55
    elif rem>='a' and rem<='f':
        rem = ord(rem)
        rem = rem-87
    else:
        chk = 1
        break
    decnum = decnum + (rem * (16 ** i))
    hexdecnumlen = hexdecnumlen-1
    i = i+1

if chk==0:
    i = 0
    octnum = []
    while decnum!=0:
        rem = decnum%8
        octnum.insert(i, rem)
        i = i+1
        decnum = int(decnum/8)

    print("\nEquivalent Octal Value is: ")
    i = i-1
    while i>=0:
        print(octnum[i], end="")
        i = i-1
    print()
else:
    print("\nInvalid Input!")
print("\n----------------------------------------------------------------------------------------------")
print("\n\t Note :")
print("\n\t We Cannot Give A HexaDecimal to Decimal Numbers it is in process....!",
          "\n\t Sorry We Correct The Mistake Soon")
