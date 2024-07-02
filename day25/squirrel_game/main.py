import pandas

squirrel_census = pandas.read_csv("squirrel_census.csv")
squirrel_color_count = {}

unique_fur_color = list(set(squirrel_census["Primary Fur Color"].dropna().to_list()))

for color in unique_fur_color:
    squirrel_color_count[color] = len(squirrel_census[squirrel_census["Primary Fur Color"] == color][["Primary Fur Color"]])

df = pandas.DataFrame(squirrel_color_count.items(), columns=['Fur color', 'Count'])
df.to_csv("squirrel_count.csv")
