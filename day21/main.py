class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print('inhale, exhale')
    
class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breath(sef):
        super().breath()
        print('doing this under water')

    def swim(self):
        print('moving in water')
    

nemo = Fish()

nemo.breath()
nemo.swim()
print(f'fish have {nemo.num_eyes} eyes')