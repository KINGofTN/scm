import plotly.express as px

"""
#basic setup
fig = px.bar(x=["a","b","c","d"],y=[10,20,30,40])
fig.show()
"""


"""
important types
1.bar
fig = px.bar(x=["a","b","c","d"],y=[10,20,30,40])

2.scatter
fig = px.scatter(x=["a","b","c","d"],y=[10,20,30,40])

3.line

fig = px.line(x=["a","b","c","d"],y=[10,20,30,40])
"""


"""
setting titile & labels
1.title
fig = px.bar(x=["a","b","c","d"],y=[10,20,30,40],title="title")

2.
"""
fig = px.bar(x=["a","b","c","d"],y=[10,20,30,40])
fig.show()