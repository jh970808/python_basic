a = 0

def add(a,b):
    return a + b

def sub(a,b):
    print(a - b)
    # return = a - b


def mul(a,b):
    return a * b

result = add(1,3)
print(result)

def indata():
    a = int(input("숫자를 입력하세요 >> "))
    return a 

data1 = indata()
data2 = indata()
sub(data1,data2)


def add_many(*args, mode = "dfv"):
    print(type(args))
    for k in args:
        print(k)
        result += k
    return result


#print(add_many(1,2,3,4,5,6,7,8,9,mode = "dfv"))


def item_print(**items):
    print(type(items))
    print(items)

item_print(a = "kang", b = 22)


