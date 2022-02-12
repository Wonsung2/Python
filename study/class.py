'''
oop(객체지향 프로그래밍)
- class( 변수 + 함수 ) - instance 생성할 수 있다.
- 클래스에 정의된 구성요소는 클래스의 소유가 아닌 인스턴스의 소유로 봐야한다.

- initializer( 초기화 함수, 생성자 )
- magic function
- object vs instance
- object - 명사적(변수), 동사적(함수)
- 함수 < 클래스 < 모듈(클래스(변수+함수)) < 패키지
- self <- 인스턴스를 대표하는 키워드
'''
'''
[실습]
- 1. Account class 작성
- 2. 인스턴스 변수 - account, balance, interestRate
- 3. accountInfo() - 계좌정보를 출력하는 함수
- 4. deposit(amount)  - 매개변수들어온 amount를 balance 입금
- 5. withDraw(amount) - 매개변수들어온 amount를 balance 출금
- 5-1. 단) 잔고가 부족할 경우 '잔액이 부족하여 출금이 안돼요'
- 6. printInterestRate() - 현재 잔액에 이자율을 계산하여 소수점 2자리 까지 출력  
'''

class Account :
    def __init__(self, account, balance, interestRate):
        self.account = account
        self.balance = balance
        self.interestRate = interestRate
    def accountinfo(self):
        print('계좌번호 : {} 잔액 : {}'.format(self.account, self.balance))
    def withDraw(self, amount):
        if self.balance >= amount :
            self.balance -= amount
        else :
            print('잔고가 부족하여 출금이 어렵습니다.')
    def deposit(self, amount):
        self.balance += amount
    def printInterestRate(self):
        self.balance = self.balance * ( 1 + self.interestRate )
        print('%.2f'% self.balance)

# caller
account = Account('444-1111-1111', 500000, 0.073)
print('계좌 정보 출력 - ')
account.accountinfo()
account.withDraw(600000)
account.deposit(200000)
account.accountinfo()
account.withDraw(600000)
account.accountinfo()
print('현재 잔액의 이자를 포함한 금액 - ')
account.printInterestRate()


class Car :
    def __init__(self, name, door, cc, price):
        self.utype = self.__class__.__name__
        self.name = name
        self.door = door
        self.cc = cc
        self.price = price
    def carInfo(self):
        if self.cc >= 5000 :
            self.grade = '대형차'
        elif self.cc >= 3000 :
            self.grade = '중형차'
        else :
            self.grade = '소형차'
        self.display()
    def display(self):
        print('%s 는 %d cc이고(%s) 문짝은 %d개 입니다.'%(self.name, self.cc, self.grade, self.door))

# caller
myDreamCar = Car('티코', 5, 800, 350)
print('utype - ', myDreamCar.utype)
myDreamCar.carInfo()

# oop(Object Oriented Programming)
# - 은닉화, 상속, 다형성
# 상속(Inheritance), object(최상위 클래스)
# 부모 - 자식 관계 ( is a ~ )
# A(A~Y)A + (Z)
# 구문형식 : class class_name(부모 클래스) :

# 은닉화(encapsulation) - information hidding
# 구문형식 : __변수명
# 직접적으로 변수에 접근할 수 없지만, 함수를 통한 간접 허용
# setXXXX(), getXXXX()

class UserDate(object) :
    def __init__(self):
        self.__year = 2022
        self.month = 2
        self.day = 4
    def setYear(self, year):
        if year <= 0 :
            self.__year = 2022
        else :
            self.__year = year
    def getYear(self):
        return self.__year

myDate = UserDate()
myDate.setYear(-2022)
print('year - ', myDate.getYear())
print('month - ', myDate.month)
print('day - ', myDate.day)

# 상속
# 함수 재지정(Overriding) - 다형성
class Super(object) :
    def __init__(self):
        pass
    def super_function(self):
        print('부모 소유함수 - super function')

    def sayEcho(self, name):
        return name + "님, 즐거운 코딩 하자구요!"

class Sub(Super):
    def __init__(self):
        pass
    def subfucntion(self):
        print('본인 소유 함수 - sub function')
    def sayEcho(self, name):
        return name + "님, 즐거운 코딩@_@"

# 인스턴스 생성 구문
child = Sub()
child.super_function()
child.subfucntion()
print('print - ', child.sayEcho('dsadas'))
print()
parent = Super()
parent.super_function()
# parent.subfunction() - 부모타입으로 자식 소유의 구성요소에 접근 불가

print()
print('스타크래프트를 활용한 상속 구현 - ')
print()

# self. super()
class Unit(object) :
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        self.__damage = damage
        self.__life = life
    def status(self):
        return '타입 : {}\t공격력 : {}\t생명력 : {}\t'.format(self.utype, self.__damage, self.__life)
    def setDamage(self, damage):
        self.__damage = damage
    def setLife(self, life):
        self.__life = life
    def getDamage(self):
        return self.__damage
    def getLife(self):
        return self.__life

class Marine(Unit) :
    def __init__(self, damage, life, offenseUp, defenseUp):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.offenseUp = offenseUp
        self.defenseUp = defenseUp
    def status(self):
        return super().status() + '공격력 업글 : {}\t방어력 업글 : {}'.format(self.offenseUp, self.defenseUp)

    def attack(self):
        print('마린이 공격을 시작합니다 땅땅ㅇㄸ따땅')
    def stimPack(self):
        if self.getLife() > 40 :
            print('stimPack 사용합니다.')
            super().setDamage(super().getDamage() * 1.5)
            super().setLife(super().getLife() - 10 )

        else :
            print('체력이 낮아 stimPack을 사용할 수 없습니다.')

class Medic(Unit) :
    def __init__(self, damage, life, defenseUp):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.defenseUp = defenseUp
    def status(self):
        return super().status()+'방어력 업글 : {}'.format(self.defenseUp)

    def attack(self):
        print('메딕이 치료를 시작합니다.')

unit = Unit(100, 100)
print('info - ', unit.status())

marine = Marine(100, 100, 50, 50)
print('marine info - ', marine.status())
marine.attack()
marine.stimPack()
print('marine info - ', marine.status())

print()
medic = Medic(0, 100, 0)
print('medic info - ', medic.status())
print()
print('type - ')
unit_lst = [marine, medic]
for u in unit_lst :
    print(u.utype)
    print('info - ', u.status())

print()

print('marine 과 medic을 이동시키는 수송기 unit 설계 -')
class DropShip(Unit) :
    def __init__(self, damage, life):
        self.utype = self.__class__.__name__
        super().__init__(damage, life)
        self.unitlst = []
    def board(self, crew):
        self.unitlst.append(crew)

    # isinstance() : 타입 체크가 가능하다
    def drop(self):
        for u in self.unitlst :
            if isinstance(u, Marine) :
                u.stimPack()
            else :
                u.attack()

    def move(self):
        print('병력을 타겟지점으로 이동시키는 ing....')

print('DropShip 생성 - ')
ship = DropShip(0, 100)
print('info - ', ship.status())
print('부대원 이동을 위해서 DropShip에 승선시킨다.')
ship.board(marine)
ship.board(medic)
ship.move()
print('부대원 타켓지점에 낙하시킨다 - ')
ship.drop()
print('전투종료 후 상태확인 - ')
print('info - ', marine.status())
print('info - ', medic.status())


#  다중 상속 및 추상 클래스
# 추상화 - 클래스가 추상함수를 가질 수 있도록 하여 자식에서 반드시 오버라이딩 하도록 하는 방법

from abc import *
class Animal(object, metaclass=ABCMeta) :

    @abstractmethod
    def cry(self):
        pass
    def nonAbstractMethod(self):
        print('추상클래스에 정의된 일반 메서드 입니다.')
class Tiger(Animal) :
    def cry(self):
        print('어흥')
class Lion(Animal):
    def cry(self):
        print('어허흥')

class Liger(Lion, Tiger) :
    pass

liger = Liger()
liger.cry() # > 어허흥 Lion 을 먼저 상속받기 때문


tiger = Tiger()