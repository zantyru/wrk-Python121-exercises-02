#  ....  .....
#  .A..--.B...--....
#  ....  .....  .E..
#   -      -      -       ...
#  ..     .Z.------       .W.
#  .C     ...             ...

# Представление графа через словарь списков
rooms = {
    'W': [],
    'A': ['B', 'C'],
    'C': ['A'],
    'B': ['A', 'Z', 'E'],
    'E': ['B', 'Z'],
    'Z': ['B', 'E'],
}

def get_next_vertex(r, cv):
    # r - структура, описывающая граф комнат; словарь
    # списков узлов
    # cv - текущий узел; комната, в которой мы находимся
    indices = {}
    for i, next_room in enumerate(r[cv]):
        indices[i] = next_room

    while True:
        print(f"Вы в комнате '{cv}'.")
        for i, next_room in indices.items():
            print(i+1, '-', next_room)
        print(0, '- прекратить прогулку')

        try:
            answer = int(input("Номер комнаты: "))
            if answer == 0:
                next_vertex = 0
            else:
                next_vertex = indices[answer-1]
            break
        except (ValueError, TypeError, KeyError) as _:
            pass

    return next_vertex


current_vertex = 'A'
while True:
    next_vertex = get_next_vertex(rooms, current_vertex)
    if next_vertex == 0:
        print("Конец прогулки. До свидания.")
        break
    current_vertex = next_vertex