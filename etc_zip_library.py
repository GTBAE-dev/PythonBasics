# zip : 여러 list 내 객체를 index 별로 튜플 형태로 묶는 작업
lst_big = ["AA", "BB", "CC"]
lst_small = ["aa", "bb", "cc"]
print(zip(lst_big, lst_small))
print(list(zip(lst_big, lst_small))) # 리스트로 감싸줘야 zip 으로 합친 리스트 확인 가능

# *을 통해 리스트 내 여러 튜플 객체를 index 별로 분리
lst_zip = [('AA', 'aa'), ('BB', 'bb'), ('CC', 'cc')]
print(list(zip(*lst_zip))) 

lst_big, lst_small = zip(*lst_zip)
print(lst_big)
print(lst_small)