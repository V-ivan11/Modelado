import re

strs = ["Este es mi sitio web: iverduzco:.com", 
        "wwwwwwwwwwwwwwowwwwwwww impresive"
        "Hola entra a riubi.me", 
        "Juan Gallardo",
        "zzzzzzzzz",
        "Este sitio kids.xyz es genial"]

for s in strs:
    # Replace all intenernet domains with the text "Link".
    s = re.sub(r"\w+\.(com|me|xyz)", "Link", s)
    # Replace all repeat letters with a single letter only at the end and the begining of the word.
    # Example: "wwwwwwwwwwwwwwowwwwwwww" -> "wow"
    # Example: "liverpool" -> "liverpol"
    
    
    print(s)

# Create a string that contains all the numbers from 1 to n without a space between each number.
# Example: n = 5 -> "12345"

n = 500
s = ""
for i in range(1, n+1):
        s += str(i)
print(s)
print(len(s))