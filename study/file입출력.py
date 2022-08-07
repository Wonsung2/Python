# # 파일 입출력
# # xxxx.csv , xxxx.xls
# # 분석 - nd array, DataFrame, Series
# # AJAX - 비동기 통신 (restful service)
# # json - { key : value }, value 로 { key : value } 가 들어갈 수도 있고
# # key 에 [ { key : value }, { key : value }, , , ,} 가 들어갈 수도 있음.
#
# # 회문(palindrome)
# # madam, sos, level, rotator, nurses run
# # 회문을 검사하는 로직을 생각해 본다면?

# # word = 'madam'
# # if word == word[::-1] :
# #     pass
# # if list(word) == list(reversed(word)) :
# #     pass
# #
# # print(' len - ', len(word))
# # for i in range(len(word) // 2) :
# #     word[i] != word[-1-i]
#
# # palindrome_words.txt 파일로부터 회문인 단어만 출력하고
# # 카운팅 해 본다면
# # 주의 ) 단어사이의 줄바꿈이 두 번 일어나면 안된다.
#
# def palindrome_words_func() :
#     with open('../data/palindrome_words.txt', 'r', encoding='utf-8') as file :
#         for line in file :
#             # print(type(line), line)
#             isFlag = True
#             line = line.strip('\n')
#             for i in range(len(line)//2) :
#                 if line[i] != line[-1-i] :
#                     isFlag = False
#                     break
#             if isFlag :
#                 cnt += 1
#                 print(line)
#     print('회문 단어의 갯수는 : {} 입니다.'.format(cnt))
# # caller
# # palindrome_words_func()
#
# import pandas as pd
# # .csv , .xls , xlsx , .txt
# # pd.read_csv() - DataFrame
# # pd.ExcelFile() - DataFrame
import pandas as pd


def load_file(filePath) :
    data = None
    if filePath.split('.')[-1] == 'csv' :
        data =  pd.read_csv(filePath, encoding='ms949', header=None)
    elif filePath.split('.')[-1] == 'xls' or filePath.split('.')[-1] == 'xlsx' :
        data = pd.ExcelFile(filePath)
    else :
        with open(filePath, 'r', encoding='utf-8') as file :
            lines = file.readlines()
            # print(type(lines[0]), lines[0])
            # print(type(j.loads(lines[0])))
            lines = [ j.loads(line) for line in lines]
            # print(type(lines[0]))
            # print(type(lines[0]['c']))
            data = pd.DataFrame(lines)
    return data
#
# def csv_file(filePath) :
#     data = load_file(filePath)
#     print(data.head())
# csv_file('../data/service_bmi.csv')
#
# def excel_file(filePath) :
#     data = load_file(filePath)
#     print('type - ', type(data))
#     data = data.parse('sam_kospi')
#     print('type - ', type(data))
#     print(data.info())
#     print(data.head())
#     print(data.describe())
# # excel_file('../data/sam_kospi.xlsx')
#
# # json
# # 네트워크 상에서 표준프로토콜로 사용되는 파일 형식
# # json -> python(dict, list) : decoding
# # json <- python(dict, list) : encoding
#
import json as j
# tmpDict = { 'id' : 'jslim', 'pwd' : 'jslim'}
# print('type - ', type(tmpDict), tmpDict)
#
# # dict > json
# jsonDict = j.dumps(tmpDict)
# print('type - ', type(jsonDict), jsonDict)
#
# # json > dict
# pyDict = j.loads(jsonDict)
# print('type - ', type(pyDict), pyDict)

def json_file(filePath) :
    data = load_file(filePath)
    print('type - ', type(data))
    print(data.info())
    print()
    print(data.head())
    print(data.describe())

# caller
# json_file('../data/usagov_bitly.txt')
import re
# sub() - 정규표현식에 해당하는 것들을 다른 문자로 대체
def clean_txt(msg) :
    msg = re.sub('[,.?!:;]', ' ', str(msg))
    msg = re.sub('[a-zA-Z0-9]', ' ', str(msg))
    return msg
def spam_func(filePath) :
    data = load_file(filePath)
    print('spam data type - ', type(data))
    # print(data[0])
    target = data[0]
    msg = data[1]
    print('target -\n ', target)
    target = [1 if t == 'spam' else 0 for t in target ]
    print(' target encoding - \n' , target)
    print(msg)
    print(clean_txt(msg))
# caller

spam_func('../data/spam_data.csv')

