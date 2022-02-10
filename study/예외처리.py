'''
학습목표
- 예외처리

'''

print("programming start - ")
print("*" * 50 )

age = input("나이를 숫자로 입력해 주세요 : ")
print(' your age is ', age, 'years old')

print("*" * 50 )
print("programming end - ")
'''
예외처리 구문
try : 
    예외가 발생 할 가능성이 있는 코드를 정의하는 곳
    A , B 예외 발생
except A :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
    A 처리
except B :
    발생한 예외를 잡기위한 객체를 정의하고 처리하는 곳
    B 처리
else : 
    예외가 발생되지 않을 때 실행되는 곳
finally : 
    예외발생 여부와 상관없이 실행되는 곳
'''
# function define - worker
def smpInput() :
    try :
        age = int(input("나이를 숫자로 입력해 주세요 : "))

    except ValueError as e : # ValueError 대신 Exception 을 사용해도 . 왜냐하면 Exception은 모든 Error의 부모 클래스
        print(str(e))
        smpInput()
    else :
        print(' your age is ', age, 'years old')
    finally :
        print('*** 예외발생 여부와 상관 없이 무조건 수행 ***')
# caller
smpInput()
print('programming end - ')

'''
매개변수로 넘겨 받은 각 첨자번지의 값에 제곱한 결과를
출력하려고 한다.
예외 발생을 확인하고 예외처리 구문을 추가하여
정상적인 흐름의 함수 호출이 되도록 만들어 본다면?
'''
def exceptionFunc(lst) :
    for e in lst:
        try :
            print('raw - ', e)
            sqrt = e ** 2
            print('squred - ', sqrt)
        except Exception as e :
            pass

# caller
# usrLst = [10, 20, 25, 'num', 40, 50]
# exceptionFunc(usrLst)

# 사용자 정의 예외 클래스를 만들 수 있다
class UserNagativeDivisionError(Exception) :
    def __init__(self, msg):
        self.msg = msg

def positiveDivide(x, y) :
    if (y < 0) :
        raise UserNagativeDivisionError('음수로 나눌 수 없습니다')
    else :
        return x/y
try :
    result = positiveDivide(10, 0)
    print('call positive func - ', result)
except UserNagativeDivisionError as e :
    print(e.msg)
except ZeroDivisionError as e :
    print(str(e))
    print(e.args[0])
print('programming end - ')




