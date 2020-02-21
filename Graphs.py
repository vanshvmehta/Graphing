"""
1. Display a line chart
2. Display a bar chart
3. Display a pie chart
"""

import matplotlib.pyplot as pyplot


def line():
    x1, y1 = [1, 2, 3, 4, 5, 6], [1, 3, 5, 7, 9, 11]
    x2, y2 = [1, 2, 3, 4, 5, 6], [1, 4, 9, 16, 25, 36]
    x3, y3 = [1, 2, 3, 4, 5, 6], [1, 8, 27, 64, 125, 216]
    pyplot.xlabel = 'x Values'
    pyplot.ylabel = 'y Values'
    pyplot.plot(x1, y1, color='g')
    pyplot.plot(x2, y2, color='r')
    pyplot.plot(x3, y3)
    pyplot.show()


def bar():
    pyplot.title = "India's Per Capita GDP"
    year = [2014, 2015, 2016, 2017, 2018]
    gdp = [1640.2, 1751.7, 1874.2, 1987.3, 2104.2]
    pyplot.xlabel = 'Years'
    pyplot.ylabel = 'Per Capita GDP($)'
    pyplot.bar(year, gdp, color=['r', 'b', 'g', 'c', 'k'])
    pyplot.show()


def pie():
    pyplot.title = "Marks of Jatin Munjal"
    mark = [84, 91, 63, 75, 98]
    subj = ['English', 'German', 'Sociology', 'Home Science', 'Geography']
    pyplot.pie(mark, labels=subj, explode=[0, 0, 0.1, 0, 0.1], autopct='%1.2f')
    pyplot.show()


print('''
1. Display a line chart
2. Display a bar chart
3. Display a pie chart
4. Exit the menu
''')
opt = 0
while opt != 4:
    opt = int(input('Enter your option: '))
    if opt == 1:
        line()
    elif opt == 2:
        bar()
    elif opt == 3:
        pie()
