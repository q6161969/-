class Magic:
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def __str__(self):
        return '%s:威力%d,%(self.name,self.power)'

class MagicBook():
    magicbook=[]
    def __init__(self):
        magic1=Magic('重击',60)
        magic2=Magic('火球',80)
        self.magicbook=[magic1,magic2]

    def show_magic(self):
        for magic in self.magicbook:
            for i in range(len(self.magicbook)):
                if magic == self.magicbook[i]:
                    print('%d.%s'%(i+1,magic.name))


#mb=MagicBook()
#mb.show_magic()