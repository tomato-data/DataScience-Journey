class ThailandPackage:
    def detail(self):
        print("[3 days 5 nights Thailand Package]\
        Bangkok, Pataya (Night Market) $500")

# 모듈 내부인지 외부인지 확인 할 때 쓸 수 있음 
if __name__ == "__main__":
    print("executing directly from Thailand module")
    print("This sentence only appears if module is directly ran")
    trip_to = ThailandPackage()
    trip_to.detail()

else:
    print("executing outside from Thailand module")