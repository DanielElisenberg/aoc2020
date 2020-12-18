class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data

    def get_value(self):
        if self.value.isdigit():
            return (int(self.value))
        elif self.value == '+':
            return self.left.get_value() + self.right.get_value()
        elif self.value == '*':
            return self.left.get_value() * self.right.get_value()


def value_or_nested_expression(line, i):
    if line[i] == '(':
        open_parenthesis = 1
        for j in range(i+1, len(line)):
            if line[j] == '(':
                open_parenthesis += 1
            if line[j] == ')':
                open_parenthesis -= 1
            if open_parenthesis == 0:
                return (parse_expression(line[i+1:j]), j+1)
    else:
        return (Node(line[i]), i+1)


def parse_expression(line):
    (root, i) = value_or_nested_expression(line, 0)
    while i < len(line)-1:
        new_root = Node(line[i])
        new_root.left = root
        (new_root.right, i) = value_or_nested_expression(line, i+1)
        root = new_root
    return root


with open('day18/input.data') as input:
    lines = [line.replace(' ', '') for line in input.read().split('\n')]

print(sum([parse_expression(line).get_value() for line in lines]))