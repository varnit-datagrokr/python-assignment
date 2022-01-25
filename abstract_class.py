from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_gender(self) -> str:
        pass

class Male(Person):
    def __init__(self) -> None:
        super().__init__()

    def get_gender(self) -> str:
        return "Male"

class Female(Person):
    def __init__(self) -> None:
        super().__init__()

    def get_gender(self) -> str:
        return "Female"

if __name__ == '__main__':
    try:
        P = Person()
    except Exception as e:
        print(e)

    M = Male()
    print(M.get_gender())

    F = Female()
    print(F.get_gender())
