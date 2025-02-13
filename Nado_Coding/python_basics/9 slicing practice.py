jumin = "980523-1234567" # 필요한 것만 잘라서 가져오는게 슬라이싱

print("sex: " + jumin[7])
print("year: " + jumin[0:2]) # a 부터 b 앞까지
print("month: " + jumin[2:4])
print("date: " + jumin[4:6])

print("date of birth: " + jumin[:6]) # 처음부터
print("back number: " + jumin[7:]) # 끝까지
print("back number(from backside): " + jumin[-7:]) # 맨뒤에서 7번째 자리부터 끝까지