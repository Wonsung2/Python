import mpg as m
from statistics import mean
import pandas as pd
mpgLst = []
with open('../data/mpg.txt', 'r', encoding='utf-8') as file :
    file.readline()
    line = file.readline()
    while line != '' :
        row = line.strip('\n').split(',')
        mpgLst.append(row)
        line = file.readline()

# print(type(mpgLst))
df = pd.DataFrame(mpgLst, columns=['manufacturer','model','displ','year','cyl','trans','drv','cty','hwy','fl','class'])

# print(df.info())
# print(df.describe(include='all'))
# print(df)
# 1. displ(배기량)이 4 이하인 자동차와 5 이상인 자동차 중
# 어떤 자동차의 hwy(고속도로 연비)가 평균적으로 더 높은지 확인하세요.]
df_1 = df[['displ', 'hwy']].astype(float)
# print(df_1)
df_14 = df_1.loc[df_1['displ'] <= 4]
df_15 = df_1.loc[df_1['displ'] >= 5]
print(df_14)
print(df_15)
df_m1 = df_14['hwy'].mean()
df_m2 = df_15['hwy'].mean()
print(df_m1, df_m2)
# 2. 자동차 제조 회사에 따라 도시 연비가 다른지 알아보려고 한다.
# "audi"와 "toyota" 중 어느 manufacturer(제조회사)의 cty(도시 연비)가
# 평균적으로 더 높은지 확인하세요.
df_2 = df[['manufacturer', 'cty']]
df_a = df_2.loc[df_2['manufacturer'] == 'audi']
df_t = df_2.loc[df_2['manufacturer'] == 'toyota']
df_am = df_a['cty'].astype(float).mean()
df_tm = df_t['cty'].astype(float).mean()
print(df_am, df_tm)
# 3. "chevrolet", "ford", "honda" 자동차의 고속도로 연비 평균을 알아보려고 한다.
# 이 회사들의 데이터를 추출한 후 hwy(고속도로 연비) 평균을 구하세요.
df_3 = df[['manufacturer', 'hwy']]
df_c = df_3.loc[df_3['manufacturer'] == 'chevrolet']
df_cm = df_c['hwy'].astype(float).mean()
df_f = df_3.loc[df_3['manufacturer'] == 'ford']
df_fm = df_f['hwy'].astype(float).mean()
df_h = df_3.loc[df_3['manufacturer'] == 'honda']
df_hm = df_h['hwy'].astype(float).mean()
print(df_cm, df_fm, df_hm)
# 4. "audi"에서 생산한 자동차 중에 어떤 자동차 모델의 hwy(고속도로 연비)가
# 높은지 알아보려고 한다. "audi"에서 생산한 자동차 중 hwy가 1~5위에 해당하는
# 자동차의 데이터를 출력하세요.
df_4 = df[['manufacturer', 'model', 'hwy']]
df_4_target = df_4.loc[df['manufacturer'] == 'audi']
print(df_4_target.sort_values(by='hwy', ascending=False).values[0:5])
# 5. mpg 데이터는 연비를 나타내는 변수가 2개입니다.
# 두 변수를 각각 활용하는 대신 하나의 통합 연비 변수를 만들어 사용하려 합니다.
# 평균 연비 변수는 두 연비(고속도로와 도시)의 평균을 이용합니다.
# 회사별로 "suv" 자동차의 평균 연비를 구한후 내림차순으로 정렬한 후 1~5위까지 데이터를 출력하세요
print(df)
df_5 = df[['manufacturer', 'cty', 'hwy','class']]
df_5['mean'] = (df_5['cty'].astype(float) + df_5['hwy'].astype(float))/2
print(df_5)
df_5_target = df_5.loc[df_5['class'] == 'suv']
df_5_target1 = df_5_target[['manufacturer', 'mean']]
print(df_5_target1.sort_values(by='mean',ascending=False))

# 6. mpg 데이터의 class는 "suv", "compact" 등 자동차의 특징에 따라
# 일곱 종류로 분류한 변수입니다. 어떤 차종의 도시 연비가 높은지 비교하려 합니다.
# class별 cty 평균을 구하고 cty 평균이 높은 순으로 정렬해 출력하세요.
df_6 = df[['class', 'cty']]
df_6_target = df_6.groupby(by='class').mean().sort_values(by='cty',ascending=False)
print(df_6_target)
# 7. 어떤 회사 자동차의 hwy(고속도로 연비)가 가장 높은지 알아보려 합니다.
# hwy(고속도로 연비) 평균이 가장 높은 회사 세 곳을 출력하세요.
df_7 = df[['manufacturer', 'hwy']].sort_values(by='hwy', ascending=False)
print(df_7[:3])


# 8. 어떤 회사에서 "compact" 차종을 가장 많이 생산하는지 알아보려고 합니다.
# 각 회사별 "compact" 차종 수를 내림차순으로 정렬해 출력하세요.
df_8 = df[['manufacturer', 'class']]
df_8_target = df_8.loc[df_8['class'] == 'compact']
df_8_target_2 = df_8_target.groupby(by='manufacturer').count()
df_8_target_3 = df_8_target_2.sort_values(by='class', ascending=False)
print(df_8_target_3)