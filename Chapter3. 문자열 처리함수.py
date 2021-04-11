''' 3-1. 문자열 슬라이싱 '''
text_slicing = "123456789a"
print(text_slicing[5]) # 변수[a] : 문자열 중 a번째 문자 출력(시작위치 : 0)
print(text_slicing[0:5]) # 변수[a:b] : 문자열 중 a 이상 b 미만 번째 문자 출력
print(text_slicing[:5]) # 변수[:a] : 문자열 처음부터 a 미만 번째 문자 출력
print(text_slicing[5:]) # 변수[a:] : 문자열 a부터 마지막 문자까지 출력
print(text_slicing[-1:]) # 맨 뒤 문자위치는 -1

''' 3-2. 문자열 처리함수 '''
text_function = "ABCDEFGBCBCBC"
print(text_function.lower()) # 변수.lower() : 문자열 내 모든 문자 소문자로 변경
print(text_function.upper()) # 변수.upper() : 문자열 내 모든 문자 대문자로 변경
print(text_function[4].isupper()) # 변수[a].isupper() : 문자열 내 a 위치 문자가 대문자면 True
print(text_function[4].islower()) # 변수[a].islower() : 문자열 내 a 위치 문자가 소문자면 True
print(text_function.replace("ABC", "abc")) # 변수.replace(A,B) : 문자열 내 A를 B로 변경
print(text_function.index("C")) # 변수.index(A) : 문자열 내 A의 위치(A=문자열; 제일 첫 문자의 위치)
print(text_function.find("ABC")) # 변수.find(A) : 문자열 내 A의 위치(A=문자열; 제일 첫 문자의 위치)
print(text_function.find("H")) # 변수.find(A) : A가 문자열에 없으면 -1출력(함수 index는 오류 발생)
print(text_function.count("BC")) #변수.count(A) : 문자열 내 A의 갯수

''' 3-3. 문자열 포맷 '''
# %d & %c & %s
print("data %d" %4) # %d 에 숫자/정수만 입력
print("character %c" %"4") # %c 에 문자 입력
print("string %s" %"ABC") # %s 에 문자열, 숫자 모두 입력
print("string %s and %s" %("ABC",4)) # 여러개 입력 방법
# {} & format
print("format {}".format(4)) # {}에 문자열, 숫자 모두 입력
print("format {} and {}".format("ABC","CDE")) # 순서대로 {} 내에 출력
print("format {1} and {0}".format("ABC","CDE")) # {} 내 번호로 숫자순서로 출력
# f 이용 변수 출력
format1 = "ABC"
format2 = "CDE"
print(f"format1 {format1} and format2 {format2}") # f와 {} 내 변수명을 통한 출력

''' 3-4. 탈출문자 '''
# 따옴표 & \ 출력
print("\"ABC\", \'CDE\'") # \를 이용한 따옴표 출력(\" & \')
print("C:\\Users\\qorbx\\Desktop\\PythonWorkspace") # \를 이용한 \ 출력(\\)
# 커서 이동
print("ABC \n CDE") # \n 을 통한 줄바꿈, 그냥 줄바꾸면 에러 발생
print("ABC \t CDE") # \t 를 통한 tab(4칸) 띄어쓰기
print("ABC \b CDE") # \b 를 통한 backspace(한칸) 삭제
print("ABC \r CDE") # \r 을 통한 커서 맨앞 이동, 자리만큼 덮어쓰기(insert)
