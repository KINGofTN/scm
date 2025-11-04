import plotly.express as px
df = px.data.gapminder()
df = df[df['country'].isin(['India', 'China', 'United States'])]

fig = px.line(
    df,
    x='year',
    y='lifeExp',
    color='country',
    animation_frame='year',
    title='Life Expectancy Growth (Animated Line)'
)
fig.show()
