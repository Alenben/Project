class Demo:
    def display(self,a=None,b=None,c=None):
        self.a=a
        self.b=b
        self.c=c
        if(a!=None and b!=None and c!=None):
            result=self.a+self.b+self.c
            print(result)
        elif(a != None and b != None):
            result=self.a+self.b
            print(result)
        else:
            result=self.a
            print(result)
d=Demo()
d.display(4)