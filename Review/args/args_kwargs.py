def add(*args):
    r=0
    for n in args:
        r+=n
    
    print(r)

# add(1,2,3,4,5)

def print_kwargs(**kwargs):
    print(f"{kwargs.get('name')} {kwargs.get('lname')}")

# print_kwargs(name='Kevin',lname='Carrillo')


m_dict = {'key':12,'key2':15}

print(m_dict.get('key'))