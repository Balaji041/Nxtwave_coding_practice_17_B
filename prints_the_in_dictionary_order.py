String=input()
first_word="z"
last_word="a"
word=""
for i in range(len(String)):
    char=String[i]
    if char!=" ":
        word+=char
    if char==" " or i==len(String)-1:
        if word.lower()<first_word.lower():
            first_word=word
        if word.lower()>last_word.lower():
            last_word=word
        word=""
        
print(first_word+" "+last_word)
"""
input:to get the Ball rolling
output:Ball to
"""
