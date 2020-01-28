import re

funRegex = re.compile(r'(Alice|Bob|Carol )\s(pets|throws|eats)\s(cats|Apples|baseballs).', re.IGNORECASE)

print(funRegex.findall('Bob pets cats.'))
print(funRegex.findall('Bob pets cats'))
print(funRegex.findall('Bob throws footcats.'))
print(funRegex.findall('Bob pets 7 cats.'))
