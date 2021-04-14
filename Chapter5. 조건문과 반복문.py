''' 5-1. if 문 '''
# if문 : 조건 실행명령문
a = "AA"
b = "BB"
if a == "CC" : # if 조건에 해당하는 실행문
    print("a = AA")
elif b == "CC" : # elif 조건에 해당하는 실행문(여러개 설정 가능)
    print("b = BB")
else : # 모두 해당되지 않을 때의 실행문
    print("c = CC")

''' 5-2. for 문 '''
# for 문 : 다양한 객체 집합을 이용한 반복문
for i in [0, 1, 2, 3, 4] : # i : 리스트 내 객체 순서대로 입력
    print("for[{0}]\t".format(i), end = "") # print(A, end="") : 출력문 마무리 설정 가능
print("")
for i in range(0,5) :
    print("for[{0}]\t".format(i), end = "")
print("")
I = {0, 1, 2, 3, 4} # 튜플, 세트 모두 가능
for i in I : 
    print("for[{0}]\t".format(i), end = "")
print("")
I = [len(str(i**10)) for i in I] # A for a in B : B의 객체 a를 A로 변환, 한줄 for 문
print(I) # len(str) : str 타입 문자열 길이

''' 5-3. Continue & Break '''
a = [1, 3, 5, 7, 9]
b = [i+1 for i in a]
for i in range(1, 12) :
    if i in a :
        continue # continue 이전의 실행문은 실행, 이 후 실행문은 미실행, 이 후 다음 i 로 이동
    elif i in b :
        print("b = ", end = "")
    elif i not in a or b : 
        print("BREAK")
        break # 이 후 실행문 실행 않고 for문 탈출
    print("{0}\t".format(i), end = "")

''' 5-4. while 문 '''
# while 문 : 다른 반복문, True 일 시 계속 반복
a = 5
while a >= 1 : # while True : 무한 반복(무한루프, ctrl + c 로 탈출)
    print ("a = {0}\t".format(a), end = "")
    a -= 1
    if a == 0:
        print("") # continue & break 모두 사용 가능