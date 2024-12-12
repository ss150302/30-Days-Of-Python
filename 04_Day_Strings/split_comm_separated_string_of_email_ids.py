import csv
from io import StringIO

def split_comma_separated_string(input_string):
    f = StringIO(input_string)
    reader = csv.reader(f, delimiter=',')
    return next(reader)


if __name__ == "__main__":
    # Example usage
    input_string = 'usr1@aaa.com,usr2@bbb.com,'
    result = split_comma_separated_string(input_string)
    for item in result:
        print(item)