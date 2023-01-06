# Monkey in the Middle

def openfile():
    with open('input11.txt', 'r') as f:
        file = f.read()
        return file

class Monkey:
    def __init__(self, name, starting_items, operation, tester, if_true, if_false):
        self.name = name
        self.starting_items = starting_items
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
    #
    # def multiply(self, x):
    #     return x * self.n
    #
    # def square(self, x):
    #     return x ^^ 2
    #
    # def plus(self, x):
    #     return x + self.n
    #
    # def test(self, x):
    #     if x % test == 0:
    #         return if_true
    #     elif x % test != 0:
    #         return if_false

    # def __repr__(self):
    #     return name, starting_items, operator, n, test, if_true, if_false



def Part1():
    file = openfile()
    monkeys = file.split('\n\n') # monkey is a list
    for monkey in monkeys:
        #print(monkey)
        list = monkey.split('\n')
        name = list[0].strip(':').replace(' ', '_')
        starting_items = list[1].split(':')[1].split(',')
        operation = list[2].split(':')[1]
        # operator = operation.split(' ')[3]
        # n = operation.split(' ')[4]
        tester = list[3].split(':')[1].split(' ')[-1]
        if_true = list[4].split(':')[1].split(' ')[-1]
        if_false = list[5].split(':')[1].split(' ')[-1]

        print(name, starting_items, operation, tester, if_true, if_false)
        #Monkey(name, starting_items, operation, tester, if_true, if_false)



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