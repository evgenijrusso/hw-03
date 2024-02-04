##  просто тест

def add(*numbers):
    addi=0
    for nam in numbers:
        addi = addi + nam
        return addi


if __name__ == '__main__':

    print(add(20))
