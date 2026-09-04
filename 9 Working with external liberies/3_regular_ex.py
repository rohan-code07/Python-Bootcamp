import re

# https://regexr.com/

text = "The quick brown fox jumps over the lazy dog."

match = re.search("quick", text)
if match:
    print("match found")
    print(match.start())
    print(match.end())


matches = re.findall("the", text, re.IGNORECASE)   # Case-insensitive search
print("matches:", matches)

replace = re.sub("fox", "cat", text)
print(replace)