import pandas as pd


"""
#Its a data handling and analysis tools

important data types
1.Series
2.DataFrame

# Create from column/series

s = pd.Series([10, 20, 30, 40])
print(s)

#index name
s=pd.Series([10,20,30,40,50],index=["day1","day2","day3","day4","day5"])
print(s)

s=pd.Series([10,20,30,40,50],index=["day1","day2","day3","day4","day5"])
print(s)

#acces by index
print(s["day1"])

#add,sub,mul,div
print(s*2)

#max,min
print(s.max())

#filter
print(s[s>30])

data = {'Math': 90, 'Physics': 80, 'Chemistry': 85}
marks = pd.Series(data)
print(marks)

print(marks.mean())    # Average
print(marks.max())     # Maximum
print(marks.min())     # Minimum
print(marks[marks > 80])  # Filtering

"""

"""
dataframe
"""

s=pd.Series([str(i) +"day" for i in range(1,6)],name="x_axis",index=[i for i in range(1,6)])
#print(s)


data = {
    "x":[i for i in range(1,10)],
    "y":[i*2 for i in range(1,10)],
    "day":["Day"+str(i) for i in range(1,10)]
}
r=pd.DataFrame(data)
#print(r["x"])
#print(r[["y","x"]])
#print(r.iloc[0])
#print(r.loc[0,"x"])

#print(r["x"]*2)

r["z"]=r["x"]+r["y"]

print(r)