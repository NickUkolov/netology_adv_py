from collections.abc import Iterable


class FlatIterator:

    def __init__(self, iter_list):
        self.iter_list = iter_list

    def __iter__(self):
        self.cursor = -1
        self.counter = 0
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.iter_list):
            raise StopIteration
        if isinstance(self.iter_list[self.cursor], list):
            if self.counter >= len(self.iter_list[self.cursor]):
                self.counter = 0
                self.cursor += 1
                if self.cursor == len(self.iter_list):
                    raise StopIteration
                element = self.iter_list[self.cursor][self.counter]
                self.cursor -= 1
                self.counter += 1
                return element

            else:
                element = self.iter_list[self.cursor][self.counter]
                self.counter += 1
                self.cursor -= 1
                return element


def flat_generator(iter_list):
    """этот ГЕНЕРАТОР Обрабатывает списки любой вложенности"""
    for el in iter_list:
        if isinstance(el, Iterable) and not isinstance(el, (str, bytes)):
            for sub_el in flat_generator(el):
                yield sub_el
        else:
            yield el
