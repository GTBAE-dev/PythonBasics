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

''' 7-3. 파일 입출력 '''
# 텍스트 파일 생성 및 덮어쓰기
file_chap7 = open("file_chap7.txt", "w", encoding = "utf8") # 파일명, w(writing), utf8(한글 정보 받기)
print("AAAAA", file = file_chap7) # 터미널에 출력물 안생김, 텍스트 파일 생성 후 내용 출력
file_chap7.write("BBBBB\n") # 텍스트 파일에 입력하는 방법 두가지, print만 줄바뀜
file_chap7.close() # w 기능 파일 닫기, w : 기존 내용 삭제 후 덮어쓰기(close 후 다시 w를 했을 때)
# 텍스트 파일 이어쓰기
file_chap7 = open("file_chap7.txt", "a", encoding = "utf8") # a(append) : 파일 뒤에 이어쓰기
file_chap7.write("CCCCC\n")
file_chap7.write("\n")
file_chap7.close()
file_chap7 = open("file_chap7.txt", "a", encoding = "utf8")
print("DDDDD", file = file_chap7)
file_chap7.close() # 추가하여도 이전 내용에 영향 X
# 텍스트 파일 읽기
file_chap7 = open("file_chap7.txt", "r", encoding = "utf8") # r(reading)
print(file_chap7.read()) # 한번에 모두 읽어오기
file_chap7.close()
file_chap7 = open("file_chap7.txt", "r", encoding = "utf8")
print(file_chap7.readline(), end = "") # 순서대로 한줄씩 읽어오기 
print(file_chap7.readline(), end = "") # print로 인해 한줄씩 더 띄워짐
file_chap7.close()
file_chap7 = open("file_chap7.txt", "r", encoding = "utf8")
while True : # 끝을 모르는 파일 끝까지 읽기
    line = file_chap7.readline()
    if len(line) == 0 : # if not line 과 동문 
        break # line 이 없으면 while 문 탈출
    print(line, end = "")
    print(len(line)) # 중간에 아무 것도 없는 줄 :  len = 1
file_chap7.close()
file_chap7 = open("file_chap7.txt", "r", encoding = "utf8")
lines = file_chap7.readlines() # readlines : list형태로 파일 내 모든 줄 저장
for i in lines :  # 끝을 모르는 파일 끝까지 읽기
    print(i, end = "")
file_chap7.close()
