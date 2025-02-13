import pickle

# with를 쓰면 close를 안해도 됨
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("studying python")

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read()) 