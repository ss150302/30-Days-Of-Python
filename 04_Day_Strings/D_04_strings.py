

def main_D_04_strings():
    #Text is a string data type. Any data type written as text is a string. Any data under single,
    # double or triple quote are strings. There are different string methods and built-in
    #functions to deal with string data types. To check the length of a string use the len() method.
    letter = 'P'                # A string could be a single character or a bunch of texts
    print(letter)               # P
    print(len(letter))          # 1
    greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
    print(greeting)             # Hello, World!
    print(len(greeting))        # 13
    sentence = "I hope you are enjoying 30 days of Python Challenge"
    print(sentence)

def multiline_string_methods():
    #Multiline string is created by using triple single (''')
    # or triple double quotes ("""). See the example below.
    multiline_string = '''I am a teacher and enjoy teaching.
    I didn't find anything as rewarding as empowering people.
    That is why I created 30 days of python.'''
    print(multiline_string)

    # Another way of doing the same thing
    multiline_string = """I am a teacher and enjoy teaching.
    I didn't find anything as rewarding as empowering people.
    That is why I created 30 days of python."""
    print(multiline_string)

def escape_sequences_in_strings():
    #In Python and other programming languages \ followed by a character is an escape sequence
    print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
    print('Days\tTopics\tExercises') # adding tab space or 4 spaces
    print('Day 1\t5\t5')
    print('Day 2\t6\t20')
    print('Day 3\t5\t23')
    print('Day 4\t1\t35')
    print('This is a backslash  symbol (\\)') # To write a backslash
    print('In every programming language it starts with \"Hello, World!\"')
    # to write a double quote inside a single quote

def string_formatting_old_style():
    # Strings only
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    language = 'Python'
    formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
    print(formated_string)

def new_Style_String_Formatting():
    #print("This formatting is introduced in Python version 3")
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    language = 'Python'
    formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
    print(formated_string)

    a = 4
    b = 3

    print('{} + {} = {}'.format(a, b, a + b))
    print('{} - {} = {}'.format(a, b, a - b))
    print('{} * {} = {}'.format(a, b, a * b))
    print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
    print('{} % {} = {}'.format(a, b, a % b))
    print('{} // {} = {}'.format(a, b, a // b))
    print('{} ** {} = {}'.format(a, b, a ** b))

def strings_and_numbers_formatting():
    radius = 10
    pi = 3.14
    area = pi * radius ** 2
    formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
    print(formated_string)

def string_Interpolation_f_Strings(): #Python 3.6+
    #Another new string formatting is string interpolation, f-strings.
    # Strings start with f and we can inject the data in their corresponding positions.

    a = 4
    b = 3
    print(f'{a} + {b} = {a +b}')
    print(f'{a} - {b} = {a - b}')
    print(f'{a} * {b} = {a * b}')
    print(f'{a} / {b} = {a / b:.2f}')
    print(f'{a} % {b} = {a % b}')
    print(f'{a} // {b} = {a // b}')
    print(f'{a} ** {b} = {a ** b}')

def python_Strings_as_Sequences_of_Characters():
    #Unpacking Characters
    language = 'Python'
    a,b,c,d,e,f = language # unpacking sequence characters into variables
    print(a) # P
    print(b) # y
    print(c) # t
    print(d) # h
    print(e) # o
    print(f) # n

def accessing_Characters_in_Strings_by_Index():
    #In programming counting starts from zero.
    # Therefore the first letter of a string is at zero index and
    # the last letter of a string is the length of a string minus one.
    language = 'Python'
    first_letter = language[0]
    print(first_letter) # P
    second_letter = language[1]
    print(second_letter) # y
    last_index = len(language) - 1
    last_letter = language[last_index]
    print(last_letter) # n

def slicing_Python_Strings():
    #In python we can slice strings into substrings.
    language = 'Python'
    first_three = language[0:3] # starts at zero index and up to 3 but not include 3
    print(first_three) #Pyt
    last_three = language[3:6]
    print(last_three) # hon
    # Another way
    last_three = language[-3:]
    print(last_three)   # hon
    last_three = language[3:]
    print(last_three)   # hon

def reversing_a_String():
    #We can easily reverse strings in python.
    greeting = 'Hello, World!'
    print(greeting[::-1]) # !dlroW ,olleH
def skipping_Characters_While_Slicing():
    #It is possible to skip characters while slicing by passing step argument to slice method.
    language = 'Python'
    pto = language[0:6:2] #
    print(pto) # Pto
    pto = language[0:6:3] #
    print(pto) # Pto
def string_methods_to_format_strings():
    challenge = 'thirty days of python'
    print(challenge.capitalize()) # 'Thirty days of python' capitalize():
    ## Converts the first character of the string to capital letter

def occurrences_of_substring_in_string():
    challenge = 'thirty days of python' # count(substring, start=.., end=..)
    print(challenge.count('y')) # 3
    print(challenge.count('y', 7, 14)) # 1,
    print(challenge.count('th')) # 2

def use_of_random_module():
    import random
    print(random.random()) # random float
    print(random.randint(1, 100)) # random integer between 1 and 100
    print(random.choice([1, 2, 3, 4, 5])) # random element from a list
    print(random.choices([1, 2, 3, 4, 5], k=2)) # two random elements from a list
    print(random.shuffle([1, 2, 3, 4, 5])) # shuffle a list

    print(random.randbytes(1,5)) # random bytes



def generate_random_user_id():
    import random
    import string
    characters = string.ascii_letters + string.digits
    user_id = ''.join(random.choices(characters, k=6))
    return user_id
    # Example usage
    #print(generate_random_user_id())






def split_pdf(input_pdf, output_folder):
    import PyPDF2
    # Open the input PDF file
    with open(input_pdf, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for i in range(num_pages):
            pdf_writer = PyPDF2.PdfWriter()
            page = pdf_reader.pages[i]
            pdf_writer.add_page(page)

            # Create the output PDF file for each page
            output_pdf = f"{output_folder}/page_{i + 1}.pdf"
            with open(output_pdf, "wb") as output_file:
                pdf_writer.write(output_file)

            print(f"Page {i + 1} saved as {output_pdf}")

            # Specify the input PDF file and output folder
            #input_pdf = "path/to/your/input.pdf"
            #output_folder = "path/to/output/folder"

            #split_pdf(input_pdf, output_folder)



if __name__ == "__main__":
    print("Entering main...")
    #main_D_04_strings()
    #accessing_Characters_in_Strings_by_Index()
    #slicing_Python_Strings()
    #string_Interpolation_f_Strings()
    #reversing_a_String()
    #skipping_Characters_While_Slicing()
    #string_methods_to_format_strings()
    # occurrences_of_substring_in_string()
    #use_of_random_module()
    #print(generate_random_user_id())
    split_pdf("input/0004-Education.pdf", "report/")
    print("Exiting main...")


