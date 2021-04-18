''' 7-1. 표준입출력 '''
# sys 모듈 : 파이썬의 쉘을 컨트롤하기 위한 시스템 함수 제공
import sys # 시스템 로그를 남길 때 사용
print("AAA", "BBB", file = sys.stdout) # 표준출력으로 문장 처리(일반적인 내용)
print("AAA", "BBB", file = sys.stderr) # 표준에러로 문장 처리 (오류 로그 출력)
# ljust & rjust : 출력 자리값 확보, 빈칸 출력(출력물 포함)
dictionary = {"AA" : 100, "BB" : 90, "CC" : 80}
for key, value in dictionary.items() : # sep : print문의 , 대신 쓸 구문 입력
    print(key.ljust(5), str(value).rjust(5), sep = ":", end = "    /    ")
print("")
# zfill : 출력 자리값 확보, 0 출력(출력물 포함)
for i in range(1, 5) : 
    print(str(i).zfill(3), end = "    /    ") # zfill 앞은 str만 입력 가능
print("")
for i in ["AA", "BB", "CC"] : 
    print(i.zfill(3), end = "    /    ") # zfill(a) : a는 정수만 가능
print("")