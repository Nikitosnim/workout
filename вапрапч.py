class Number:
    def __init__(self):
        self.value = 0
    def add(self, a):
        self.value += a
    def div(self,a):
        if a==0:
            self.value = 'Error'
        else:
            self.value // a
