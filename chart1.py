import plotly.express as px
import pandas as pd
data = pd.DataFrame({
    'Role': ['Data Scientist', 'Data Analyst', 'Software Engineer', 'Machine Learning Engineer'],
    'Salary': [110000, 85000, 105000, 115000],
    'Experience': [5, 3, 7, 6]
})
fig = px.scatter(data, x='Experience', y='Salary', color='Role', size='Salary',
                 title='Salary vs. Years of Experience')
fig.update_layout(xaxis_title='Years of Experience', yaxis_title='Salary')
fig.show()
languages = ['Python', 'R', 'Java', 'SQL', 'JavaScript']
usage = [80, 45, 60, 75, 55]
fig = px.bar(x=languages, y=usage, title='Programming Language Usage')
fig.update_layout(xaxis_title='Programming Languages', yaxis_title='Usage (%)')
fig.show()
