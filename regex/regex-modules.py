import re 
text  = 'nomor agen konsultasi kami adalah 081-898-9090, silahkan hubungi agen konsultasi kami'
print('nomor' in text)

print('\n')

pattern  = 'agen'
match = re.search(pattern, text)
matches = re.findall(pattern, text)
print(match)
print(match.start())
print(match.end())
print(match.span())
print(matches)
