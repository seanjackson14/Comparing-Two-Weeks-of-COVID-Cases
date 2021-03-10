import plotly.graph_objs as go
from plotly.offline import iplot
import pandas as pd
import datetime


df = pd.read_csv('all-states-history.csv')

def week1():
    date1 = input('Enter the first week for comparison (in YYYY-MM-DD form please): ')
    year, month, day = (int(x) for x in date1.split('-'))
    answer = datetime.date(year, month, day).weekday()
    if answer == 0:
        return date1
    while answer != 0:
        print('Please enter a date that corresponds to a Monday')
        date1 = input('Enter the first week for comparison (in YYYY-MM-DD form please): ')
        year, month, day = (int(x) for x in date1.split('-'))
        answer = datetime.date(year, month, day).weekday()
    return str(date1)

def week2():
    date2 = input('Enter the second week for comparison (in YYYY-MM-DD form please): ')
    year, month, day = (int(x) for x in date2.split('-'))
    answer = datetime.date(year, month, day).weekday()
    if answer == 0:
        return date2
    while answer != 0:
        print('Please enter a date that corresponds to a Monday')
        date2 = input('Enter the second week for comparison (in YYYY-MM-DD form please): ')
        year, month, day = (int(x) for x in date2.split('-'))
        answer = datetime.date(year, month, day).weekday()
    return str(date2)

date1 = week1()
date2 = week2()


def endWeek1(date1):

    endDate = pd.to_datetime(date1) + pd.DateOffset(days=6)
    return str(endDate.date())
def endWeek2(date2):
    endDate = pd.to_datetime(date2) + pd.DateOffset(days=6)
    return str(endDate.date())

endWeekOne = endWeek1(date1)
endWeekTwo = endWeek2(date2)

wk1df = df[(df['date'] >= date1) & (df['date'] <= endWeekOne)]

groupByState = wk1df.groupby(['state'])['positiveIncrease'].sum()

wk2df = df[(df['date'] >= date2) & (df['date'] <= endWeekTwo)]

groupByState2 = wk2df.groupby(['state'])['positiveIncrease'].sum()



dataweek1 = dict(type = 'choropleth',
            colorscale = 'orrd',
            locations = wk1df['state'],
            z = groupByState,
            locationmode='USA-states',
            text = 'Total COVID cases for your first selected week',
            geo = 'geo',
            colorbar={'title': f"Covid Cases for week of {date1}",'x':-.1})

dataweek2 = dict(type = 'choropleth',
            colorscale = 'orrd',
            locations = wk2df['state'],
            z = groupByState2,
            locationmode='USA-states',
            text = 'Total COVID cases for your second selected week',
            geo = 'geo2',
            colorbar={'title': f'Covid cases for week of {date2}'})

layout = dict()
layout['geo'] = dict(
        scope = 'usa',
        showland = True,
        domain = dict(x = [0, .5], y = [0, 1]))
layout['geo2'] = dict(
        scope = 'usa',
        showland = True,
        domain = dict(x = [0.5, 1.0], y = [0, 1]))


choromap = go.Figure([dataweek1,dataweek2], layout)

iplot(choromap)