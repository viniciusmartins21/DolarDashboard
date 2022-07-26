from random import randint
from sre_parse import DIGITS
from faker import Faker


def rand_ratio():
     return randint(840, 900), randint(473, 573)

fake = Faker('pt_BR')

def make_cotation():
    return {
        'titulo_cotacao': fake.name(),
        'data': fake.date(),
        'hora': fake.time(),
        'preco': fake.pricetag(),
        'id': fake.pyint(),
    }
    
if __name__ == '__main__':
    from pprint import pprint
    pprint(make_cotation())
    
    
    
