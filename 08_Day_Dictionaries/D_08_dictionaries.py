
def data_dictionary_usage():
    # A dictionary is a collection of unordered, modifiable(mutable) paired (key: value)
    # data type.
    person = {
        'first_name':'Asabeneh',
        'last_name':'Yetayeh',
        'age':250,
        'country':'Finland',
        'is_marred':True,
        'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'street':'Space street',
            'zipcode':'02210'
        }
    }
    print(person.get('first_name')) # Asabeneh
    print(person.get('country'))    # Finland
    print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
    print(person.get('city'))   # None

def checking_keys_in_dictionary():
    person = {
        'first_name':'Asabeneh',
        'last_name':'Yetayeh',
        'age':250,
        'country':'Finland',
        'is_marred':True,
        'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address':{
            'street':'Space street',
            'zipcode':'02210'
        }
    }
    print('first_name' in person) # True
    print('middle_name' in person) # False
    print('skills' in person) # True
    print('city' in person) # False



    #A dictionary is a collection of unordered, modifiable(mutable) paired (key: value)
    # data type.

if __name__ == "__main__":
    print("Entering main...")
    #data_dictionary_usage()
    checking_keys_in_dictionary()
    print("Exiting main...")
