from collections.abc import Iterable
from func import logger

nested_list_iter = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', ['h', [5, [5, [87, [98, 86]]]] , 67], False],
    [1, 2, None],
]

@logger('data.txt')
def flat_generator(iter_list):
    """этот ГЕНЕРАТОР Обрабатывает списки любой вложенности"""
    for el in iter_list:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            for sub_el in flat_generator(el):
                yield sub_el
        else:
            yield el

if __name__ == '__main__':
    for item in flat_generator(nested_list_iter):
        print(item)
