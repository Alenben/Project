class Netflix:
    def catagories(self,movies,series,lang):
        self.movies=movies
        self.series=series
        self.lang=lang
n1=Netflix()
n1.catagories("red notice","witcher","english")
n2=Netflix()
n2.catagories("mirage","la ca sa papel","spanish")
print(n1.series)
print(n2.lang)