# 프로그램상에서 사용하는 데이터를 파일형태로 저장

import pickle
# b = binary, pickle을 쓸 때는 항상 binary를 정의해줘야 함, encoding 설정 불필요
profile_file = open("profile.pickle", "wb")
profile = {"name" : "A", "age" : 30, \
    "hobby" : ["football", "baseball", "basketball"]}

print(profile)
pickle.dump(profile, profile_file) # profile 의 정보를 profile_file에 저장
# pickle을 이용해서 이 데이터를 파일에다 입력
profile_file.close()