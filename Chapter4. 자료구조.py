''' 4-1. 리스트 '''
# 리스트 : 순서를 가지는 객체(자료형에 구애받지 않음)의 집합
list_number = [10, 10, 20, 20, 30, 30]
list_text = ["AA", "BB", "CC", "AA", "BB"]
list_mix = ["AA", "BB", 10, 20, "AA", 10]
print(list_mix) # 자료구조 리스트는 [대괄호]로 출력
list_text.append("CC")
print(list_text) # 리스트.append(A) : A를 리스트 맨 뒤에 삽입
list_number.insert(3, 25)
print(list_number) # 리스트.insert(a,A) : 위치 a에 A를 삽입
list_mix.pop()
print(list_mix) # 리스트.pop() : 리스트 맨 뒤 객체 제거
list_mix.extend(list_text)
print(list_mix) # 리스트.extend(A) : 리스트 뒤에 리스트 A 삽입
print(list_text) # extend 로 삽입해도 기존 리스트 삭제 X
print(list_mix.index("BB")) # 리스트.index(A) : 리스트 내 A 위치
print(list_mix.count("AA")) # 리스트.count(A) : 리스트 내 A 갯수
                            # 리스트 자료구조 find 와 replace 지원 X
list_mix.clear()
print(list_mix) # 리스트.clear() : 리스트 내 객체 비우기
list_number.sort()
print(list_number) # 리스트.sort() : 리스트 내 객체 작은거부터 정렬
list_text.sort()
print(list_text) # mix list는 sort, reverse 사용 X
list_number.reverse()
print(list_number) # 리스트.reverse() : 리스트 내 객체 순서 뒤집기
