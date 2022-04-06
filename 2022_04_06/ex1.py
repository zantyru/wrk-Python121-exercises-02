class FloatMatrix:
    """Row-oriented numeric 2d table."""

    def __init__(self, rows=None, columns=None):

        try:
            self.__rows = int(rows)
            self.__cols = int(columns)
        except (ValueError, TypeError) as _:
            raise ValueError("Matrix dimensions are wrong.")

        self.__data = tuple(
            [0.0] * self.__cols
            for _ in range(self.__rows)
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} rows={self.__rows} columns={self.__cols}>"

    def __getitem__(self, rowcol):
        row, col = self._unpack_coordinates(rowcol)
        return self.__data[row][col]

    def __setitem__(self, rowcol, value):
        row, col = self._unpack_coordinates(rowcol)
        self.__data[row][col] = float(value)

    def _unpack_coordinates(self, rowcol):
        if not isinstance(rowcol, tuple):
            raise TypeError(
                f"Coordinates must be tuple,"
                f" not '{type(rowcol).__class__.__name__}'"
            )

        try:
            row, col = rowcol
        except ValueError:
            raise ValueError(
                f"Expected 2 values, not {len(rowcol)}."
            )

        try:
            row = int(float(row))
            col = int(float(col))
        except (TypeError, ValueError) as _:
            raise ValueError(
                "Coordinates can be integers, floats"
                " or strings represent integers or floats."
            )

        if row < 0 or row >= self.__rows or col < 0 or col >= self.__cols:
            raise IndexError("Out of bounds.")

        return row, col

    @property
    def rows(self):
        return self.__rows

    @property
    def columns(self):
        return self.__cols


if __name__ == '__main__':

    m = FloatMatrix(rows=7, columns=10)
    print(m)
    print(f"m.rows={m.rows}, m.columns={m.columns}")

    m[3, 4] = 12
    print(m[3, 4])

