# Bingo chart making it LaTeX

To run on the test
```
python generate_test.py 
python make_bingo_charts.py > tables.tex
sed -i "s/\\\\\\\/\\\\\\\\\\\\midrule/" tables.tex
latexmk -pdf
```
