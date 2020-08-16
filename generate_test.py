from random import choice
from string import ascii_uppercase, digits
from numpy import dtype, empty
from pandas import DataFrame


def generate_random_string(string_length):
    return ''.join(
        choice(ascii_uppercase + digits)
        for _ in range(string_length))


dtypes = dtype([
          ('Pytanie', str),
          ('Question', str),
          ('Odpowiedz', str),
          ('Answer', str)])
data = empty(0, dtype=dtypes)

df = DataFrame(data)
for _ in range(100):
    new_row = {
        column: generate_random_string(5)
        for column in df.columns}
    df = df.append(new_row, ignore_index=True)
df.to_excel('test.xlsx', index=False)
