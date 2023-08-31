S=input()
vaild_value=False
for i in S:
    if ((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (i=="_")):
        vaild_value=True
        break
    else:
        vaild_value=False
        break
print(vaild_value)
"""
input:1stnumber
output:False
"""
