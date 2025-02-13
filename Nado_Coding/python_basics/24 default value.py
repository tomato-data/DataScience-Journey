def profile(name, age, language):
    print("name: {0}\tage: {1}\tlangauge: {2}" \
        .format(name, age, language))

profile("a", 20, "python")
profile("b", 20, "Java")

def profile(name, age = 17, language = "python"):
    print("name: {0}\tage: {1}\tlangauge: {2}" \
        .format(name, age, language))

profile("a")
profile("b", 20, "Java")
# 기본값이 첫 전달값이 아닐 경우에는?