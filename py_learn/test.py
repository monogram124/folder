class Banknote:
    def __init__(self, value: int):
        self.value = value
    
    def __repr__(self): # типо для програмистов
        return f"Banknote({self.value})"
    
    def __str__(self): # для людей
        return f"Банкнота номиналом в {self.value} рублей"
    
    def __eq__(self, other): # без реализации этого метода питон будет сравнивать ссылки в памяти и выведет True только если это один и тот же объект
        # return self.value == other.value
        pass
    def __lt__(self, other):
        return self.value < other.value 
    
    def __gt__(self, other):
        return self.value > other.value 
    
    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value
    
class Wallet:
    def __init__(self, *banknotes:Banknote):
        self.container = []
        self.container.append(banknotes)
        self.index = 0
        
    def __repr__(self) -> str:
        return f"Wallet({self.container})"

    def __contains__(self, item):
        return item in self.container
    
    def __bool__(self):
        return self.container
    
    def __len__(self):
        return len(self.container)
    
    def __call__(self):
        return f"{sum(e.value for e in self.container)} рублей"

    def __iter__(self): # возвращает итерратор
        return Iterator(self.container)

    def __next__(self):
        while self.index <= self.index < len(self.container):
            value = self.container[self.index]

            self.index += 1
            
            return value
        raise StopIteration
    
class Iterator: # новый класс создал для того чтобы можно было несклоько раз итератор использовать и перезапускать его
    def __init__(self, container):
        self.container = container
        self.index = 0

    def __next__(self): # если класс реализует этот метод то он итератор но не итерабл
        if self.index <= self.index < len(self.container):
            value = self.container[self.index]
            # тут просто реализиация метода next чтобы сделать этот класс итератором
            self.index += 1
            
            return value
        raise StopIteration # если выходит за пределы длины объекта бросаем исключение, если не прописывать это исключение не будет работать 
        # for под копотом проверяет это исключение он будет просит у кошелька содержимое пока не поймает это исключение

# iterable некоторый объект который возвращает итератор 
# итерратор это тот объект который при вызове метода next возвращает один из своих элементов
if __name__ == "__main__":
    fifty = Banknote(50) 
    hundred = Banknote(100)
    print(f"{fifty!r}") # Banknote(50)
    print(fifty) # Банкнота номиналом в 50 рублей

    wallet = Wallet(fifty, hundred)
    print(hundred in wallet) # True

    print(f"{wallet!r}") # Wallet([Banknote(50), Banknote(100)])

    for item in wallet:
        print(item)