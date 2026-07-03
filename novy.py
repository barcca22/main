from faker import Faker
fake = Faker(['cs_CZ'])
for _ in range(3):
    print(fake.name_female())
    print(fake.address())

import humanize
humanize.activate("de_DE")
print(humanize.intword(12345591313))
print(humanize.apnumber(10))