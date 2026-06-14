class Parent:
    def __int__(self):
        self.data = 'parent data'

    def details(self):
        print(self.data)

class child(Parent) :
    def __int__(self):
        self.data = 'parent data'

    def details(self):
        print(self.data)
        
# p = Parent()     
# p.details()  


c=child()
c.details()