class Pet:
    def __init__(self , name ,weight , color ):
        self.name = name 
        self.weight = weight 
        self.color = color 
        
    def say_hello(self):
        return f'His name is {self.name} , weight is {self.weight} , and his color is {self.color}'
#p = Pet('ivan', '35', 'red')
#print(p.say_hello())
