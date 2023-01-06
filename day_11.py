# Monkey in the Middle

def openfile():
    with open('input11.txt', 'r') as f:
        file = f.read()
        return file

class Monkey:
    def __init__(self, name, starting_items, operation, test, if_true, if_false):
        self.name = name
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false

    operator = operation.splix(' ')[3]
    n = operation.split(' ')[4]

    if operator == '*' and n == 'old':
        def operation(x):
            return x ** 2

    elif operator == '+':
        def operate(self):
            return x + int(n)

    def devide(x):
        if x % test == 0:
            return if_true
        elif x % test != 0:
            return if_false

    def __repr__(self):
        return name, starting_items, operation, test, if_true, if_false



def Part1():
    file = openfile()
    monkeys = file.split('\n\n') # monkey is a list
    for monkey in monkeys:
        print(monkey)
        list = monkey.split('\n')
        name = list[0].strip(':')
        starting_items = list[1].split(':')[1].split(',')
        operation = list[2].split(':')[1]
        test = list[3].split(':')[1].split(' ')[-1]
        if_true = list[4].split(':')[1].split(' ')[-1]
        if_false = list[5].split(':')[1].split(' ')[-1]
        print(name, starting_items, operation, test, if_true, if_false)
        Monkey(name, starting_items, operation, test, if_true, if_false)


    # for i in str:
    #     print('find a monkey:', i)
        # if line[:6] == 'Monkey':
        #     name =
        #     print('Monkey: {}, starting_items: {}, operation: {}, test: (), True: {}, False: {}.'.format(name, starting_items, operation, test, testT, testF))

        #print(line.strip())


def main():
    print(Part1())

if __name__ == '__main__':
    main()