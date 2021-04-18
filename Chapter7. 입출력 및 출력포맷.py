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

''' 7-2. 다양한 출력 포맷 '''
print("{0:>10}".format(-100)) # {0:>10} : 오른쪽 정렬, 출력물 포함 10 빈칸 확보
print("{0:>+10}".format(100)) # {0:>+10} : 양수, 음수 여부 출력
print("{0:_<+10}".format(100000)) # {0:a<+10} : 빈칸에 a 채움
print("{0:-<+30,}".format(10000000000)) #{0:10,} : 3자리 마다 , 출력
print("{0:f}".format(4/3)) # {0:f} : 실수 값 출력
print("{0:.2f}".format(4/3)) # {0:.2f} : 소수점 2번째 자리까지 출력
print("{0:->+30.2f}".format(4/3)) # 채우기, 정렬 뒤에 소수점 자리 설정 가능
