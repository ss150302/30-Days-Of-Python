
# syntax
# Declaring a function
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name


def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum


def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age;



def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight


# Calling function
def main_D_11_main():
    print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))
    print('Sum of two numbers: ', sum_two_numbers(1, 9))
    print('Age: ', calculate_age(2021, 1819))
    print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))


if __name__ == "__main__":
    main_D_11_main()