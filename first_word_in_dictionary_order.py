String=input()
first_word=String
word=""
for i in range(len(String)):
    char=String[i]
    word+=char
    if char==" " or i==(len(String)-1):
        if word.lower()<first_word.lower():
            first_word=word
        word=""

print(first_word)
"""
input:He is bit slow
output:bit
"""
