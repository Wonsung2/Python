# magic function
# __XXXX__()
# - 매직함수, 데코레이터, 제너레이터, 일급함수, 파일입출력

# class MagicClass(object) :
#     def __init__(self):
#         print('객체 생성시 호출')
#     def __del__(self):
#         print('객체 삭제시 호출')
#     def __str__(self):
#         return '이제는 주소값이 아니라 문자열이 출력'
# obj = MagicClass()
# print(obj)

# 일급함수, first class
# - 변수에 함수를 저장할 수 있다.
# - 함수를 다른 함수의 인자로 전달할 수 있다.

def userAdd(x, y) :
    return x + y

print('add - ', userAdd(10, 20))
print('function address - ' , userAdd)
f = userAdd # 함수를 변수에 저장
print('f - add - ', f(10, 20))

# 함수를 다른 함수의 인자로 전달
def userOperation(func, arg) :
    return func(arg[0], arg[1])

def userMinus(x, y) :
    return x - y
data = (10, 22)
result = userOperation(userAdd, data)
print('add - ', result)

# 함수의 리턴값으로 다른 함수를 사용할 수 있다.
# closure(함수 내부에 자료구조를 생성하여 값을 저장해 놓는 개념)
def outer(x) :
    def inner(y) :
        return x + y
    return inner

# caller
result = outer(5)
print('result - ', result(10))

# generator (반복문) - yield, next()
# - 장점 : 빠른 수행속도 , 적은 메모리 사용으로 인한 성능 향상

def loopFunc(lst) :
    result = []
    for tmp in lst :
        result.append(tmp ** 2)
    return result

# caller
data = [1, 2, 3, 4, 5]
result = loopFunc(data)
print('result - ', result)

def generatorFunc(lst) :
    for tmp in lst :
        yield tmp ** 2

result = generatorFunc(data)
print('generator type - ', type(result)) # > generator 타입
# print('next - ', next(result))
# print('next - ', next(result))
# print('next - ', next(result))
# print('next - ', next(result))
# print('next - ', next(result))
for e in result :
    print(e)

lst = [ tmp ** 2 for tmp in data]
print('list comprehension - ', lst)
generator = ( tmp ** 2 for tmp in data)
print('type - ', generator)
for g in generator :
    print(g)
print('end for~')
print('generator - ', list(generator))
for g in generator :
    print(g)

# 파일입출력
# 순수 파이썬기반 입출력 , pandas 기반 입출력
'''
텍스트 파일
- open(file=xxxxx, mode = 'r|w|a', encoding=xxxx) r: 읽기, w: 쓰기, a: 추가 + close
- with open() ~ as file :
'''
def readTxt(path, mode) :
    try :
        file = open(path, mode, encoding='utf-8')
        print('file type - ', type(file), file)

    except Exception as e :
        print(str(e))
    else :
        print('read - \n', file.read())
    finally :
        if file != None :
            file.close()
# caller

readTxt('./data/greeting.txt', 'r')

# 출력
def writeTxt(path, mode) :
    file = open(path, mode, encoding='utf-8')
    file.write('\nHello~, Seop^*^')

    file.close()

# caller
# writeTxt('./data/test.txt', 'a')

def with_open_file(path, mode, e) :
    with open(path, mode, encoding='utf-8') as file :
        # print(file.read()) # read 로 불러오면 문자열로 가져오지만, readlines로 가져오면 각 줄을 리스트의 형태로 가져오게 된다.
        # line = None
        # while line != '' :
        #     line = file.readline()
        #     print(line.strip('\n')
        # readlines()
        lst = file.readlines()
        for s in lst :
            print(s.strip('\n'))
#caller
with_open_file('./data/greetin.txt', 'r', 'utf-8')





















