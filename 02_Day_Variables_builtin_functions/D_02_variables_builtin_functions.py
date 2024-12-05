def main_02_variable_builtin_functions():
    print("Hello World!")
    print('Hello, World!')  # The text Hello, World! is an argument
    print('Hello', ',', 'World', '!')  # it can take multiple arguments, four arguments have been passed
    print(len('Hello, World!'))  # it takes only one argument

    # Variables in Python
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    country = 'Finland'
    city = 'Helsinki'
    age = 250
    is_married = True
    skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
    person_info = {
        'firstname': 'Asabeneh',
        'lastname': 'Yetayeh',
        'country': 'Finland',
        'city': 'Helsinki'
    }

    #Let us print and also find the length of the variables declared at the top:

    #Example:

    # Printing the values stored in the variables

    print('First name:', first_name)
    print('First name length:', len(first_name))
    print('Last name: ', last_name)
    print('Last name length: ', len(last_name))
    print('Country: ', country)
    print('City: ', city)
    print('Age: ', age)
    print('Married: ', is_married)
    print('Skills: ', skills)
    print('Person information: ', person_info)

    #Declaring Multiple Variable in a Line
    #Multiple variables can also be declared in one line:

    #Example:

    first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 25, True

    print(first_name, last_name, country, age, is_married)
    print('First name:', first_name)
    print('Last name: ', last_name)
    print('Country: ', country)
    print('Age: ', age)
    print('Married: ', is_married)
    #Getting user input using the input() built-in function. Let us assign the data we get from a user into first_name and age variables. Example:

    first_name = input('What is your name: ')
    age = input('How old are you? ')

    print(first_name)
    print(age)
    #Data Types
    #There are several data types in Python. To identify the data type we use the type built-in function.
    # I would like to ask you to focus on understanding different data types very well.
    # When it comes to programming, it is all about data types.
    # I introduced data types at the very beginning and it comes again,
    # because every topic is related to data types.
    # We will cover data types in more detail in their respective sections.
    #Checking Data types and Casting

    # Different python data types
    # Let's declare variables with various data types

    first_name = 'Asabeneh'     # str
    last_name = 'Yetayeh'       # str
    country = 'Finland'         # str
    city= 'Helsinki'            # str
    age = 250                   # int, it is not my real age, don't worry about it

    # Printing out types
    print(type('Asabeneh'))          # str
    print(type(first_name))          # str
    print(type(10))                  # int
    print(type(3.14))                # float
    print(type(1 + 1j))              # complex
    print(type(True))                # bool
    print(type([1, 2, 3, 4]))        # list
    print(type({'name':'Asabeneh'})) # dict
    print(type((1,2)))               # tuple
    print(type(zip([1,2],[3,4])))    # zip

    #Casting:
    # Converting one data type to another data type.
    # We use int(), float(), str(), list, set
    # When we do arithmetic operations string numbers should be first converted to int or float
    # otherwise it will return an error.
    # If we concatenate a number with a string, the number should be first converted to a string.
    # We will talk about concatenation in String section.
    #Examples:

    # int to float
    num_int = 10
    print('num_int',num_int)         # 10
    num_float = float(num_int)
    print('num_float:', num_float)   # 10.0

    # float to int
    gravity = 9.81
    print(int(gravity))             # 9

    # int to str
    num_int = 10
    print(num_int)                  # 10
    num_str = str(num_int)
    print(num_str)                  # '10'

    # str to int or float
    num_str = '10.6'
    num_float = float(num_str)
    print('num_float', float(num_str))  # 10.6
    num_int = int(num_float)
    print('num_int', int(num_int))      # 10

    # str to list
    first_name = 'Asabeneh'
    print(first_name)               # 'Asabeneh'
    first_name_to_list = list(first_name)
    print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']



if __name__ == "__main__":
    print("Entering main...")
    main_02_variable_builtin_functions()
    print("Exiting main...")
