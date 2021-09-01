import pandas
url = "iris.data"
names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"]
dataset = pandas.read_csv(url,names=names)
print(dataset.describe)