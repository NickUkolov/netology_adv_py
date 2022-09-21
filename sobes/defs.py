

class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element=None):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


def bracket_checker(data):
    opened = ['(', '[', '{']
    closed = [')', ']', '}']
    stack = Stack()
    for el in data:
        if el in opened:
            stack.push(el)
        elif el in closed and stack.size() > 0:
            stack.pop()
        else:
            return 'Не сбалансировано'

    if stack.isEmpty():
        return 'Сбалансировано'
    else:
        return 'Не сбалансировано'







