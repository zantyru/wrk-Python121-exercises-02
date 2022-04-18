class Stack:

    class EmptyError(Exception):
        pass

    class OverflowError(Exception):
        pass

    def __init__(self, max_size):
        self.__max_size = int(max_size)
        if self.__max_size < 1:
            raise ValueError("Stack size can not be less than 1.")
        self.__body = []

    def push(self, item):
        if len(self.__body) < self.__max_size:
            self.__body.append(item)
        else:
            raise Stack.OverflowError("Stack is full.")

    def pop(self):
        try:
            item = self.__body.pop()
        except IndexError:
            raise Stack.EmptyError("Stack is empty.")

        return item


if __name__ == '__main__':

    # Создаём стек на 10 элементов
    s = Stack(10)  # Стек пуст!

    # Кладём в стек три объекта
    s.push("3434")
    s.push(3)
    s.push([1, 2, 4])

    # Вынимаем из стека объект и выводим его на экран
    obj = s.pop()  # После этой операции в стеке остаётся только 2 объекта!
    print(obj) # [1, 2, 4]

    # Тест на переполнение
    for n in range(11):
        try:
            s.push(n)
        except Stack.OverflowError:
            print(f"В стеке нет места для {n}!")