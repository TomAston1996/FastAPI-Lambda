import random

def random_component(): 
    components = ['TCU', 'Bogie', 'Pantograph', 'VCB', 'Window']
    return random.choice(components)

if __name__ == '__main__': 
    print(random_component())