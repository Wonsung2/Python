# Que 1
# special_word.txt 파일로부터 문자 'c'가 포함된 단어를 출력
# 단, 단어를 출력할 때 등장한 순서대로 출력

def que01() :
    with open('../data/special_words.txt', 'r', encoding='utf-8') as file :
        lines = file.readline().split()
        lines = [i.strip(',.') for i in lines]
        print(lines)
        for word in lines :
            if 'c' in word :
                print(word)


# caller
# que01()


# Que2
# special_words.txt 파일로부터 줄 단위로 읽어서 단어의 길이가
# 10 이하인 단어를 출력하고 카운팅 하세요

def que02() :
    cnt = 0
    with open('../data/special_words.txt', 'r', encoding='utf-8') as file :
        lines = file.readline().split()
        lines = [i.strip(',.') for i in lines]
        print(lines)
        for word in lines:
            if len(word) <= 10 :
                cnt += 1
        print('단어의 길이가 10이하인 단어의 갯수 : {}'.format(cnt))
#caller
# que02()

# zipcode.txt
# input 함수를 이용해서 동 이름을 입력받아
# 예) 개포
# 해당하는 동의 주소를 출력하는 함수를 정의한다
# hint - \t
# startwith() 함수를 이용
# 예외처리
def que03() :
    dong = input("동을 입력하세요 예) 개포 : ")
    try :
        with open('../data/zipcode.txt' , 'r', encoding='utf-8') as file :
            line = file.readline()
            while line :
                addr_lst = line.split('\t')
                if addr_lst[3].startswith(dong) :
                    print(addr_lst)
                line = file.readline()
    except Exception as e :
        print(str(e))


#caller
que03()