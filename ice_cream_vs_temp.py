import plotly.express as px
import csv

with open("icecreamvstemp.csv")as csv_files:
    df=csv.DictReader(csv_file)
    fig=px.scatter(df,x="Temperature",y="Ice-Cream Sales(₹)")
    fig.show()

  