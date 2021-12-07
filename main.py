class demo:
    def _int_(self,name,place,age):
        self.name=name
        self.place=place
        self.age=age
    def _float_(self):
        return self.age
p1=demo("ocean","pondicherry",21)
print(p1.name)