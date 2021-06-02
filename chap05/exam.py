def dan(num):
    for i in range(1, 10):
        print('{} * {} = {:2}'.format(num, i, num*i))


def gugudan():
    for i in range(2, 10):
        dan(i)

def gugudan2():
    for j in range(1, 10):
        print()
        for i in range(2, 10):
            print('{} * {} = {:2} '.format(i, j, i*j), end='')


if __name__ == "__main__":
    gugudan2()
