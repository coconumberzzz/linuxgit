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

#리스트
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
