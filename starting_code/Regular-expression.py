import re 
pattern = r"[A-Z]obody"

text = '''This is all about the journey which is performed by the karma in the previous time segment.
Nobody knows what is the purpose behind the moment which deliver the prosperity your life.
Don't through though time to the goal of the any person which signifies the death ofthe former performer this is you 
Nobody  It's you your set your path your justification at the end you'll face that.'''

# match = re.search(pattern, text)
# print(match)

matches = re.finditer(pattern, text)

for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])



