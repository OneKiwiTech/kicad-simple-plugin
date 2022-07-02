from ..observable.observable import Observable

class Model:
    def __init__(self):
        self.status1 = Observable('')
        self.status2 = Observable('')

    def set_status1(self, value):
        self.status1.set(value)
    
    def set_status2(self, value):
        self.status2.set(value)