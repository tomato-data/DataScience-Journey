import pickle

profile_file = open("profile.pickle", "rb") 
profile = pickle.load(profile_file) # 파일에 있는 정보를 프로필에 불러오기
print(profile)
profile_file.close

# 가지고 있는 데이터를 피클을 이용해서 파일에 저장, 파일에 있는 내용을 로드로 변수로 
# 저장하는거를 도와주는 유용한 라이브러리