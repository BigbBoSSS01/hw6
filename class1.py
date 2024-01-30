from art import tprint
class Hello:
    def _init_(self, string):
        self.string = string


class Hi(Hello):
    def art(self):
        tprint('HI' + self.string)


obj = GoodMorning ('PYTHON')