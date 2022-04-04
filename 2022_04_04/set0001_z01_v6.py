N = int(input("Вв ц число: "))


def compute_loops_in_digit_glyphs(n):
    return sum(
        {"0": 1, "6": 1, "8": 2, "9": 1}.get(digit, 0)
        for digit in str(n)
    )


K = compute_loops_in_digit_glyphs(N)
print(f"Кол-во замкнутых обл в знаках цифр: {K}")