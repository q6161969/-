class Magic:
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def __str__(self):
        return '%s:威力%d,%(self.name,self.power)'

class MagicBook():
    book=[]
    def __init__(self):
        magic1=Magic('重击',60)
        magic2=Magic('火球',80)
        book=[magic1,magic2]

    def show_book(self):
        pass
