print("\n\t WELCOME TO BINARY CALCULATOR....!")
b=list(input("\nEnter the Value of Binary number to Convert in Decimal: "))
a=int(input("\nEnter the Value of Binary number to Convert in octal & Hexa Decimal: "))
print("Entered Binary Value is:", a)
value=0
for i in range(len(b)):
    digit=b.pop()
    if digit=='1':
        value=value + pow(2,i)
print("\n",b,"in Decimal value is:",value)

print("\n",a,"in Octal value is :",oct(a) )
print("\n",a,"in HexaDecimal value is :",hex(a) )
"""
a=list(input("\n\t Enter the Binary Number:"))
value=0
for i in range(len(a)):
    digit=a.pop()
    if digit=='1':
        value=value + pow(2,i)
print("\n",a,"in Decimal value is:",value)
"""

