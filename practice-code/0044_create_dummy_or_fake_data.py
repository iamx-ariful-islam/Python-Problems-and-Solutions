# pip install faker

from faker import Faker

fake = Faker()

# generate fake information or dummy data
print('Name      :', fake.name())
print('Address   :', ', '.join(fake.address().split('\n')))
print('Some Text :', fake.text())
print('Email     :', fake.email())
print('Country   :', fake.country())
print('Latitude  :', fake.latitude())
print('Longitude :', fake.longitude())
print('Url       :', fake.url())