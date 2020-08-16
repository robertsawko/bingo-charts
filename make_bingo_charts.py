from pandas import read_excel
from numpy.random import choice
from pandas import DataFrame

CHART_SIZE = 5
NO_OF_CHARTS = 10


class BingoChart:
    def __init__(self, selected_items):
        self.items = selected_items
        self.chart = DataFrame(columns=[
            '{0}'.format(i) for i in range(CHART_SIZE)])
        for row_i in range(CHART_SIZE):
            new_row = {
                column:
                    selected_items.iloc[row_i*CHART_SIZE + column_i]['Pytanie']
                for column_i, column in enumerate(self.chart.columns)}
            self.chart = self.chart.append(new_row, ignore_index=True)


questions_and_answers = read_excel('test.xlsx')
for _ in range(NO_OF_CHARTS):
    index = choice(
        len(questions_and_answers),
        size=CHART_SIZE**2,
        replace=False)
    bc = BingoChart(questions_and_answers.loc[index])
    print(bc.chart.to_latex(
        index=False,
        header=False,
        column_format='|C{2cm}|C{2cm}|C{2cm}|C{2cm}|C{2cm}|'))
