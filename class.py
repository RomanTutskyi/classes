class Pet:
    def __init__(self , name ,weight , color , your_name):
        self.name = name 
        self.weight = weight 
        self.color = color 
        self.your_name = your_name
        
    def say_hello(self):
        return f'His name is {self.name} , weight is {self.weight} , and his color is {self.color}'

class Person(Pet):
    def name(self):
        return f'Your name is {self.your_name} '
p = Pet('ivan', '35', 'red' 'mukola')
print(p.say_hello())
m = Pet()
print(m.name())