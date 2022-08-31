class node:
    def __init__(self, init_data):
        self.data=init_data
        self.next=None
        
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self, data):
        self.data=new_data
    def set_next(self, new_next):
        self.next=new_next
        
    def is_empty(self):
        return self.data == None 
        
temp=node(90)
#print(temp.get_data())
temp.set_next(57)
print(temp.get_next())
print(temp.get_data())
print(temp.is_empty())