## first install Faker from your terminal by using this command -> pip install Faker

from faker import Faker
fake = Faker()
print(fake.name())
print(fake.email())
print(fake.country())
print(fake.profile())