class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def sleep(self):
        print('zzzzzzz')

class GuardDog(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 5)
        self.aggressive = True

    def rrr(self):
        print('stay away!')

# inheritance
class Puppy(Dog):
    # 메서드의 첫 번째 argument == self
    # 모든 `__`로 시작하는 메서드(매직메서드)는 자기 자신을 참조한다.
    # 클래스의 초기값을 설정하는 메서드

    def __init__(self, name, breed):
        # supper: parent class 참조
        super().__init__(name, breed, 0.1)
        self.spoiled = True

    # print 시 호출되는 메서드
    def __str__(self):
        return f"Hi, {self.name}"

    def woof(self):
        print("WOOF!")


# 클래스 초기화, 클래스의 instance 생성
ruffus = Puppy(name="Ruffus", breed="Beagle")
bibi = GuardDog(name="Bibi", breed="Dalmatian")

ruffus.woof()
bibi.rrr()

bibi.sleep()
