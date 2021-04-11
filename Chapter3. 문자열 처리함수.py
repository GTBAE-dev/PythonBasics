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