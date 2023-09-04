

class Person():

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        result = "my name is " + self.name + ", and age is " + str(self.age)
        return result
    
    def to_dict(self):
        return self.__dict__
    
    @classmethod
    def from_dict(cls, dict_obj):
        return cls(dict_obj['name'], dict_obj['age'])