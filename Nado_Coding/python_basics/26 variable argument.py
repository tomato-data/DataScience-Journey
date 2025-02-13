def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    # 프린트 문이 끝날 때 줄바꿈이 아니라 어떻게 끝낼지 설정 가능 (end)
    print("name: {0}\t나이: {1}\t".format(name, age), end = " ")
    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("name: {0}\t나이: {1}\t".format(name, age), end = " ")
    for lang in language:
        print(lang, end = " ")
    print()

profile("a", 20, "python", "Java", "C", "C++", "C#", "Javascript")
profile("a", 20, "kotlin", "swift")

# 가변인자도 뒤에 일반인자가 올 수 없는지 확인