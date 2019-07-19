#집합
s1=set([1,2,3])
l1=list(s1)				#리스트로 변환
print(l1)
print(l1[0])
t1=tuple(s1)			#튜플로 변환
print(t1)
print(t1[0])

s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
s1&s2				#교집합
s1|s2				#합집합
s1-s2				#차집합

s1=set([1,2,3])
s1.add(4)				#1개 추가
s1.update(5,6,7)			#여러개 추가
s1.remove(7)			#삭제



# 튜플 >> (소괄호),
t1=(1,)				#하나일때 무조건 콤마
t2=(1,2,3)
t3=1,2,3
(t4)='python','life'
t4=('python','life')

# 딕셔너리 >> {중괄호},key(불변):value(변경),키중복x,값중복o
//함수 : keys,in,values,items 
dic = {1:"my",2:"name",3:"is",4:"python"}

#리스트 >> [대괄호],중복o
//함수 : sort(정렬),reverse,append(추가)
myscore = [100,90,85,78]
[a,b]=['python','life']

#집합 >> {중괄호},중복x,순서가없어 인덱스로 특정 값 접근x
//함수 : add(1개추가),update(여러개추가),remove(삭제)


#불
bool([1,2,3])			#T
bool('python')			#T
bool([])				#F
bool('')				#F


#변수
a=[1,2,3]
b=a
id(a)				#주소값 반환
id(b)				#a와 동일한 주소를 반환
a is b				#동일객체를 가르키는지 판단하는 명령어 >T
a[1]=4				#a와b모두 [1,4,3]으로 변경

a[1,2,3]
b=a[:]				#a의 전체를 복사
a[1]=4
print(a)				#[1,4,3]
print(b)				#[1,2,3]
b is a 				#False

from cop import copy
b=copy(a)			#b=a[:]와 동일
b is a				#False

a=3
b=5
a,b=b,a				#a에 b값(5)를 넣고 b에 a값(3)을 넣는다
print(a)				#5
print(b)				#3


#반복문
pocket = ['paper','money','phone','card']
money=2000
if 'money' in pocket:
	print("taxi")
elif card:
	print("card taxi")
else:
	print("walk")

treehit=0
while treehit<10:
	treehit+=1
	print("나무를 %d번 찍었습니다."%treehit)
	if treehit==10
		print("나무가 넘어갑니다.")

prompt="""
1.add
2.del
3.list
4.quit
enter number : """
number=0
while number!=4:
	print(prompt)		#위에 지정해둔 글 출력
	number(input())		#입력

a=0
while a<10:
	a=a+1
	if a%2==0 : continue	#continue는 while문 처음으로 돌아가게 함
	print(a)


