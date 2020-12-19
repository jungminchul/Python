#문자열 ""로 둘러싸여 있으면 모두 문자열
#a = "Hello world"
#print(a)

food = "python favorite food is per1"
print(food)


#food = 'python's favorite food is per1'
#print(food)

#문자열에 큰따옴표 포함시키기
say = '"Python is very easy." he says.'
print(say)

#백슬래시를 사용해서 '와 "를 문자열에포함시키기
food = 'Python\'s favorite food is per1'
say = "\"Python is very easy.\" he says."

#여러 줄인 문자열을 변수에 대입하고 싶을 떄
#1.줄을 바꾸기 위한 이스케이프 코드 \n 삽입하기.
multline = "Life is too short \n You need python"
print(multline)
#2.연속된 작은따욤표 3개 또는 큰따옴표 3개 사용하기
multline2='''
Life is too short
You need python
'''
print(multline2)

#문자열 연산하기
#1.문자열 더해서 연결하기
head = "Python"
tail = " is fun! "
print(head+tail)

#2.문자열 곱하기
a = "python"
a = a*4
print(a)


#문자열 곱하기 응용
a = "="
a = a*50
b =  "My Program"
print(a,b,a)

#문자열 길이구하기 len > print(len(a))
a = "Life is too shrot"
print(len(a))

#문자열 인덱싱
a = "Life is too shrot, You need Python"
print(a[3])

#문자 인덱싱 활용하기
c = "Life is too short, You need Python"
print(c[3])
print(c[5])
print(c[12])
print(c[-1])

#문자열 슬라이싱
d = "Life is too short, You need Python"
e = a[0] + a[1] + a[2] + a[3]
print(e)
#위에를 간단하게 처리하려면
f = "Life is too short, You need Python"
g = a[0:4]
print(g)

#이름바꾸기
n = "pithon"
print(n[:1])
print(n[2:])
print(n[:1] + 'y' + n[2:])
#숫자바로대입
qw = "I eat %d apples." %3
print(qw)
#문자열 바로 대입
er = "i eat %s apples." % "five"
print(er)
#숫자값을 나타내는 변수로 대입
number = 63
rt = "I eat %d apples." % number
print(rt)

number = 10
day = "three"
gdf = "I ate %d apples. so I was sick for %s days." % (number, day)
print(gdf)

#포맷format 1. 숫자대입하기 , 문자대입하기.format(five), 이름으로 넣기 {number} < .format(number=10, day=3)
ggfd = "I eat {0} apples." .format(3)
print(ggfd)
print("I eat " + str(3) + "apples") # 3번째



#문자 개수 세기(count)
fsd = "hobby"
print(fsd.count('b'))

#위치 알려주기(find)
qrw = "Python is the best choice"
print(qrw.find('b'))
print(qrw.find('k'))

#소문자를 대문자로 바꾸기 upper
hd = "hi"
print(hd.upper))
#대문자를 소문자로 바꾸기 lower