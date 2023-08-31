S=input()
f=True
for i in S:
    a=((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122 ) or (ord(i)>=48 and ord(i)<=57))
    if not a:
        f=False
        break
print(f)
"""
input:eachNumber
output:True
"""
