def use_of_lists1():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.append('apple')
    print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
    fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
    fruits.append('lime')
    fruits.append('lime')
    print(fruits)

def use_of_lists2():
    fruits = list()
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.insert(2, 'apple')
    print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
    fruits.insert(0, 'lime')   # ['lime', 'banana', 'orange', 'apple', 'mango', 'lemon']
    print(fruits)

def use_of_lists3():
    fruits = []
    print(len(fruits)) # 0

    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.insert(2, 'apple')
    print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
    fruits.insert(0, 'lime')   # ['lime', 'banana', 'orange', 'apple', 'mango', 'lemon']
    print(fruits)
    print(len(fruits)) # 6

def access_list_with_positive_index():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    print(fruits[0]) # banana
    print(fruits[1]) # orange
    print(fruits[2]) # mango
    print(fruits[3]) # lemon

def access_list_with_negative_index():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    print(fruits[-1]) # lemon
    print(fruits[-2]) # mango
    print(fruits[-3]) # orange
    print(fruits[-4]) # banana

def unpacking_list():
    lst = ['item1','item2','item3', 'item4', 'item5']
    first_item, second_item, third_item, *rest = lst
    print(first_item)     # item1
    print(second_item)    # item2
    print(third_item)     # item3
    print(rest)           # ['item4', 'item5']

def unpacking_list2():
    lst = ['item1','item2','item3', 'item4', 'item5']
    first_item, second_item, *rest, last_item = lst
    print(first_item)     # item1
    print(second_item)    # item2
    print(rest)           # ['item3', 'item4']
    print(last_item)      # item5

def unpacking_list3():
    # First Example
    fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
    first_fruit, second_fruit, third_fruit, *rest = fruits
    print(first_fruit)     # banana
    print(second_fruit)    # orange
    print(third_fruit)     # mango
    print(rest)           # ['lemon','lime','apple']
    # Second Example about unpacking list
    first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
    print(first)          # 1
    print(second)         # 2
    print(third)          # 3
    print(rest)           # [4,5,6,7,8,9]
    print(tenth)          # 10
    # Third Example about unpacking list
    countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
    gr, fr, bg, sw, *scandic, es = countries
    print(gr)
    print(fr)
    print(bg)
    print(sw)
    print(scandic)
    print(es)

def slicing_items_in_list_positive_index():
    #Positive Indexing: We can specify a range of positive indexes by specifying the start,
    # end and step, the return value will be a new list.
    # (default values for start = 0, end = len(lst) - 1 (last item), step = 1)
    fruits = ['banana', 'orange', 'mango', 'lemon']
    all_fruits = fruits[0:4] # it returns all the fruits
    print(all_fruits)
    # this will also give the same result as the one above
    all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
    print(all_fruits)
    orange_and_mango = fruits[1:3] # it does not include the first index
    print(orange_and_mango)
    orange_mango_lemon = fruits[1:]
    print(orange_mango_lemon)
    orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
    print(orange_and_lemon)

def slicing_items_in_list_negative_index():
    #    Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.
    fruits = ['banana', 'orange', 'mango', 'lemon']
    all_fruits = fruits[-4:] # it returns all the fruits
    print(all_fruits)
    orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
    print(orange_and_mango)
    orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
    print(orange_mango_lemon)
    reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']
    print(reverse_fruits)

def modifying_list():
    #List is a mutable or modifiable ordered collection of items. Lets modify the fruit list.

    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits[0] = 'avocado'
    print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
    fruits[1] = 'apple'
    print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
    last_index = len(fruits) - 1
    fruits[last_index] = 'lime'
    print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
    fruits.append('orange')
    fruits.append('banana')
    fruits.sort()
    print(fruits)        #  ['avocado', 'apple', 'banana', 'lime', 'mango', 'orange']
    fruits.pop(0)
    print(fruits)        #  ['apple', 'banana', 'lime', 'mango', 'orange']
    fruits.pop(3)
    print(fruits)     #  ['apple', 'banana', 'lime', 'orange']
    


if __name__ == "__main__":
    print('Start of the program')
    modifying_list()



    print('End of the program')