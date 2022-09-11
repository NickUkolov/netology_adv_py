from func import FlatIterator, flat_generator

nested_list_iter = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', ['h', [5, [5, [87, [98, 86]]]] , 67], False],
    [1, 2, None],
]

if __name__ == '__main__':
    print('iterator')
    for item in FlatIterator(nested_list_iter):
        print(item)
    print('list comprehension')
    print([item for item in FlatIterator(nested_list_iter)])
    print('generator')
    for it in flat_generator(nested_list_iter):
        print(it)



