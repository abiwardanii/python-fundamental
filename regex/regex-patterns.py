import re
phone_number  = '2004-959-559 # This is Phone Number'
phone = re.search(r'\d\d\d\d-\d\d\d-\d\d\d', phone_number)
print(phone)
print(phone.group())

#quantifiers
phone = re.search(r'\d{4}-\d{3}-\d{3}', phone_number)
print(phone)
print(phone.group())

phone = re.compile(r'\d{4}-\d{3}-\d{3}')
hasil = phone.search(phone)
print(hasil.group())
print(hasil.group(1))
print(hasil.group(2))
print(hasil.group(3))

