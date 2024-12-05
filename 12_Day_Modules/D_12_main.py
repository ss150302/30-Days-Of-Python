
import math
import os
import sys
import datetime
import json
import requests
#from dotenv import load_dotenv

from D_12_mymodule import generate_full_name as fullname, sum_two_nums as total, \
    person as p, gravity as g

def main_D_12_main():
    print(fullname('Asabneh','Yetayeh'))
    print(total(1, 9))
    mass = 100;
    weight = mass * g
    print(weight)
    print(p)
    print(p['firstname'])

def use_math_modules ():
    print(math.pi)
    print(math.sqrt(2))
    print(math.pow(2, 3))
    print(math.exp(1))
    print(math.log(10))
    print(math.sin(45))
    print(math.cos(45))
    print(math.tan(45))
    print(math.degrees(10))
    print(math.radians(12))
    print(math.factorial(5))
    print(math.ceil(9.81))
    print(math.floor(9.81))

def use_os_modules():
    print(os.getcwd())
    print(os.listdir())
    #os.rmdir('test')
    os.listdir()
    os.mkdir('test')
    #os.rmdir('test')
    os.rename('test', 'new_one')
    os.system('touch file.txt')

    os.system('ls')
    os.system('pwd')
    #os.remove('file.txt')
    os.system('echo hello')

    os.system('ls')
    os.system('pwd')
    os.rename('new_one', 'test')
    os.system('pwd')
    os.rmdir('test')
    os.system('echo hello')
    # Creating a directory
    os.mkdir('directory_name')
    # Changing the current directory
    os.chdir('path')
    # Getting current working directory
    os.getcwd()
    # Removing directory
    #os.rmdir()
from statistics import * # importing all the statistics modules
def use_statistics_module():
    ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
    print(mean(ages))       # ~22.9
    print(median(ages))     # 23
    print(mode(ages))       # 20
    print(stdev(ages))      # ~2.3

import math
def use_math_modules():
    print(math.pi)           # 3.141592653589793, pi constant
    print(math.sqrt(2))      # 1.4142135623730951, square root
    print(math.pow(2, 3))    # 8.0, exponential function
    print(math.floor(9.81))  # 9, rounding to the lowest
    print(math.ceil(9.81))   # 10, rounding to the highest
    print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi
from math import sqrt, pow, floor, ceil, log10
def use_math_modules_imports():
    print(pi)                 # 3.141592653589793
    print(sqrt(2))            # 1.4142135623730951
    print(pow(2, 3))          # 8.0
    print(floor(9.81))        # 9
    print(ceil(9.81))         # 10
    print(math.log10(100))    # 2
    print(pi)

from math import *
#But if we want to import all the function in math module we can use * .
def use_math_modules_import_all():
    print(pi)                  # 3.141592653589793, pi constant
    print(sqrt(2))             # 1.4142135623730951, square root
    print(pow(2, 3))           # 8.0, exponential
    print(floor(9.81))         # 9, rounding to the lowest
    print(ceil(9.81))          # 10, rounding to the highest
    print(math.log10(100))     # 2
# When we import we can also rename the name of the function.
def use_math_modules_import_as():
    from math import pi as  PI
    print(PI) # 3.141592653589793

def use_of_string_module():
    import string
    print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    print(string.digits)        # 0123456789
    print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

def use_of_datetime_module():
    import datetime
    print(datetime.datetime.now())
    print(datetime.datetime.now().year)
    print(datetime.datetime.now().month)
    print(datetime.datetime.now().day)
    print(datetime.datetime.now().hour)
    print(datetime.datetime.now().minute)
    print(datetime.datetime.now().second)
    print(datetime.datetime.now().microsecond)

def use_of_random_module():
    import random
    print(random.random()) # random float
    print(random.randint(1, 100)) # random integer between 1 and 100
    print(random.choice([1, 2, 3, 4, 5])) # random element from a list
    print(random.choices([1, 2, 3, 4, 5], k=2)) # two random elements from a list
    print(random.shuffle([1, 2, 3, 4, 5])) # shuffle a list

def use_of_json_module():
    import json
    person = {
        'name': 'Asabeneh',
        'country': 'Finland',
        'city': 'Helsinki',
        'skills': ['JavaScript', 'React', 'Python']
    }
    # convert into JSON:
    person_json = json.dumps(person)
    print(person_json)
    # convert into Python:
    person_dict = json.loads(person_json)
    print(person_dict)


if __name__ == "__main__":
    print("Entering main...")
    #main_D_12_main()
    #use_math_modules()
    #use_os_modules()
    #use_statistics_module()
    #use_math_modules_import_as()
    #use_of_string_module()
    #use_of_datetime_module()
    #use_of_random_module()
    use_of_json_module()

    print("Exiting main...")

