# 이곳은 문제를 풀며 자유롭게 코드를 짜볼 수 있는 공간입니다.
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0  

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        num_of_dogs += 1
        birth_of_dogs += 1
        
    def __del__(self):
        num_of_dogs -= 1
        print("RIP")
    
    def bark(self):
        print("크르를르르르으릉르릉....컹컹!")
        
    def get_status(num_of_dogs, birth_of_dogs):
        print(f'Birth: {birth_of_dogs}, Current: {num_of_dogs}')
    # 아래에 코드를 작성하시오.