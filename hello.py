print ('hello python world')
a=3
b=2
print (a*b)
c = "life is too short "
print(len(c))
print(c[1])
print(c[-2])
print(c[0:5])

#문자열대입
c = "life is %s short " %"five"
print(c)
number =10
day="four"
d="i ate %d apples. so i was sick for %s days."%(number,day)
print(d)

#format함수
e="i ate {0} apple".format(3)
print(e)
e="i ate {0} apple".format(number)
print(e)
e="i ate {0} apple".format("four")
print(e)
e="I ate {number} apples. for {day} days.".format(number=2, day=3)
print(e)

#문자열 관련 
a="i enjoy watching the movie (avengers endgame)"
print(a.count('b'))             #문자 개수
print(a.find('y'))              #위치 찾기,0부터 시작
print(a.index('e'))             #위치 찾기,0부터 시작
print(":".join('abcd'))         #문자열 삽입 -> a:b:c:d
print(":".join(['a','b','c','d'])) #문자열 삽입 -> a:b:c:d, 반드시 []
print(a.upper())                #소문자>대문자
print(a.lower())                #대문자>소문자
a="  wow  "
print(a.strip())                #양쪽 공백지우기
print(a.lstrip())               #왼쪽 공백지우기
print(a.rstrip())               #오른쪽 공백지우기
a="i enjoy the eating"
print(a.split())                #문자열 나누기 ()안에 들어가는것에 기준

#리스트(값 변경o,[]로 감싼다)
a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0])                     #1
print(a[-1])                    #['a','b','c']
print(a[3])                     #['a','b','c']
print(a[-1][0])                 #a

#리스트 슬라이싱
a=[1,2,3,4,5]
b=[12,34,56]
print(a[0:2])                   #[1,2]
print(b[0:3])                   #123, 3번째 칸인 4 출력x
print(a[:2])                    #[1,2]
print(a[2:])                    #[3,4,5]

print(a+b)                      #리스트 더하기
print(a*3)                      #리스트 곱하기
print(len(a))                   #리스트 길이

a[2]=4                          #수정
print(a)
del a[3]                        #위치삭제
print(a)
a.append(3)                     #추가
print(a)
a.sort()                        #정렬
print(a)
a.reverse()                     #역순(리스트 자체) 
print(a)
a.insert(0,0)                   #삽입(변경)
print(a)
a.remove(4)                     #지정삭제
print(a)
a.pop()                         #마지막요소반환 및 삭제
print(a)
a.pop(1)                        #위치반환(a[1]반환)
print(a)
a.extend([1,4])                 #리스트확장
print(a)
a.sort()
print(a)

#튜플 (값변경x인 리스트,()로 감싼다)
t1=(0,1,2,'a','b')
print(t1[2])                    #인덱싱
print(t1[2:])                   #슬라이싱

#딕셔너리
dic={'name':'harry','phone':'010','birth':'5/5'}
c={1:'hi'}
c={'c':[1,2,3]}                 #리스트도 삽입가능

c={1:'a'}                       #첫 딕셔너리
c[2]='b'                        #딕셔너리 쌍 추가
c['name']='oracle'
c[3]=[1,2,3]
print (c)

del c[1]                        #딕셔너리 삭제
print(c)
print(c['name'])                #key 사용해 value 얻기
print(dic['name'])
print(dic['phone'])

c={1:'a',1:'b'}                 #key 중복 시
print(c)                        #처음이 무시됨

print(dic.keys())               #key 리스트
f=list(dic.keys())              #dic.keys를 리스트로 변환하고자 할때
print(f)
print(dic.values())             #value 리스트
print(dic.items())              #key,value 쌍얻기
print(dic.get('name'))          #key로 value얻기
print('name' in dic)            #해당키가 딕셔너리안에 있는지 조사
#>>True
print('email' in dic)
#>>False
dic.clear()                     #쌍 지우기
print(dic)


