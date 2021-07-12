

#        순수할인 채 , 액면가, 시장이자율
year1,need1,mrate1 = 5,100,0.05
pap= (mrate1 + 1)**year1
results = need1 / pap
print("순수할인채격 가치" ,results)

# cost of bond
#       액면가 , 만기
a2,y2 = 10000 , 2
#                액면 이자율  시장금리
f_rate ,m_rate = 0.05 , 0.06
re1 =(f_rate+1) * a2
a = ((1+m_rate)**y2)
re2 =( (f_rate * a2) / (1+m_rate))
re3 =re1/a+re2
print("사채 발행가",re3)


print(" ")
print(" ")

# 모현동 문제   사채 2 개      3번

expire , money  = 5 , 10000
bondgive  = 600
print("만기수익률",bondgive/money)
r = bondgive/money

srate , sexpire = 400 ,2
smoney =10000

a2,y2 = smoney , sexpire
m_rate =r
re1 =srate+smoney
a = ((1+r)**sexpire)
re2 =( (srate) / (1+r))
re3 =re2+ re1/a
print("사채 구입 가격",re3)
print(" ")

# ............................................................................

#                        옵션 가치 산출 모데
callopp, contract , point, = 155 , 10 , 3
#        거래승수
dealingcost = 250

# 정산  만기일의 코스피의 포인트
last = 160

# 만기일에  콜 옵션의 가치
callv = (last - callopp)*contract*dealingcost
if callv  >= 0:
    print("콜옵션의 만기일가치",callv)
else : print("콜옵션의 만기일가치",0)
costoption = point*contract*dealingcost
print("비용",costoption)
print("손익 :  가치 - 비용",callv - costoption)
print(" ")

#################################   선물 이론적가격?
# 단일 선물 가격            개월   코스피 포인트    무위험이자율
time , kp ,nodangerrate = 6 ,160.20, 0.1
meanexpect = 0.05
#거래승수
ppcost = 250000

rate1 = 1 + (nodangerrate-meanexpect)

future = kp * ppcost*rate1 * (time/12)

print("서물계약이론 가격",future)
print(" ")
print(" ")
############################################# 주당가격?

#           주강가격    수익률 요구
give , exrate1 = 1000,   0.1
print("주당가격 :", give * (1/exrate1))
print("    ")

#########  주식의 현재 가치 ?
#금년도 배당금
sgive = 20000
#배당금 증가
erateiny = 0.1
#요구 수익
exrate2 =  0.2


rate3 = exrate2 - erateiny

top = sgive *(1+erateiny)

print("주식의 현재가치 :", top/rate3)









