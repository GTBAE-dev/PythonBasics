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

''' 4-2. 튜플 '''
# 튜플: 리스트와 달리 내용 수정이 불가함. 
tuple_mix = ("AA", 10, "BB", 20, 10)
print(tuple_mix[0]) # 튜플[a] : 튜플 내 a번째 객체 출력(리스트도 동일하게 가능)
# tuple_mix.add("CC") : 오류 발생, append, insert, pop, extend 모두 불가(수정 X)
tuple_number = (20, 30, 40, 10)
# tuple_number.reverse() : 오류 발생, sort, reverse, clear 모두 불가
print(tuple_number.index(10)) 
print(tuple_mix.count(10)) # 튜플 수정과 관련없는 기능은 사용 가능
tuple_alpha = (A, B, C) = ("AA", "BB", "CC") # 튜플 활용시 여러 변수 한번에 정의 가능
print(A, B, C)
A = "DD"
print(A, B, C) # 튜플로 정의한 변수 수정 가능
print(tuple_alpha) # 해당 튜플은 수정 적용 X

''' 4-3. 세트 '''
# 세트 : 중복이 안되고 순서가 없는 집합, 중괄호로 표시
set_number = {10, 10, 20, 20, 30}
print(set_number) # 중복된 값 없이 저장 및 출력
set_mix = set(["AA", "BB", "CC", 10, 20])
print(set_mix) # set(A) : 세트를 정의할 수 있는 다른 방법
# 교집합 : A 와 B의 교집합
print(set_number & set_mix)
print(set_number.intersection(set_mix))
# 합집합 : A 와 B의 합집합
print(set_number | set_mix)
print(set_number.union(set_mix)) # 순서 보장 X
# 차집합 : A 에서 B의 차집합
print(set_number - set_mix)
print(set_number.difference(set_mix))
# 집합 내용 수정
set_number.add(50) # 세트.add(A) : 세트에 A 추가
set_number.remove(20) # 세트.remove(A) : 세트 내 A 제거
print(set_number) # 순서 보장X, 위치(index, []) 출력 불가()

''' 4-4. 사전 '''
# 사전(dictionary) : key & value 로 구성된 객체의 조합, 중괄호로 표시
dictionary_1 = {1:"AA", 2:"BB", "str":"str"} # key와 value에 int / str 모두 가능
print(dictionary_1.get(1)) # 사전.get(a) : key a 의 value 가져오기
print(dictionary_1.get(4, "DD")) # value가 없는 key를 가져올때 A 없으면 none 출력 후 프로그램 종료.
print(1 in dictionary_1)
print(4 in dictionary_1) # key in dictionary : key 에 value 존재 여부(O : True / X : False)
# 사전 내용 수정
dictionary_1[3] = "CC" # 정의 안된 key 사용하여 추가
dictionary_1["str"] = "text" # 정의 된 key 사용하여 덮어쓰기
del dictionary_1[1] # del [key] : 정의 된 key 의 value 삭제
print(dictionary_1)
dictionary_1.clear() # 사전.clear() : 사전 비우기
print(dictionary_1)
# 사전 내용 출력
dictionary_2 = {"a":"AA", "b":"BB", "c":"CC"}
print(dictionary_2.keys()) # 사전.keys() : 사전 내 keys 출력
print(dictionary_2.values()) # 사전.values() : 사전 내 values 출력
print(dictionary_2.items()) # 사전.items() : 사전 내 key 와 value 모두 출력

