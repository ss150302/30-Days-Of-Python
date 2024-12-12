import csv
from io import StringIO

def split_comma_separated_string(input_string):
    f = StringIO(input_string)
    reader = csv.reader(f, delimiter=',')
    return next(reader)
def use_split_comma_separated_string():
    # Example usage
    input_string = 'usr1@aaa.com,usr2@bbb.com'
    result = split_comma_separated_string(input_string)
    for item in result:
        print(item)

def use_split_comma_separated_string_in_quote():
    input_string = 'usr1@aaa.com,usr2@bbb.com'
    result = split_comma_separated_string(input_string)
    for item in result:
        print(f'"{item}"')
def use_split_and_quote_comma_separated_string():
    # Example usage
    input_string = 'usr1@aaa.com,usr2@bbb.com'
    result = split_and_quote_comma_separated_string(input_string)
    print(result)  # Output: "usr1@aaa.com","usr2@bbb.com",

def split_and_quote_comma_separated_string(input_string):
    f = StringIO(input_string)
    reader = csv.reader(f, delimiter=',')
    items = next(reader)
    quoted_items = [f'"{item}"' for item in items]
    return ','.join(quoted_items)

if __name__ == "__main__":
    # Example usage
    use_split_comma_separated_string()
    use_split_comma_separated_string_in_quote()
    use_split_and_quote_comma_separated_string()

