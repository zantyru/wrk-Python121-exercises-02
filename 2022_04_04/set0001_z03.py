ticket = input("Вв серийный номер билета ABxxxxx: ")

n = int(ticket[2:])

START_VALUE = 1643
COLS = 15  # Кол-во мест в ряду

row = (n - START_VALUE) // COLS + 1
col = (n - START_VALUE) % COLS + 1  #@BONUS
m = n - START_VALUE + 1  #@BONUS

print(f"Номер ряда: {row}")
print(f"Номер места (колонка): {m} ({col})")  #@BONUS


