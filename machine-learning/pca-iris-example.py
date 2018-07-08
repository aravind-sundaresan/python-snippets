import pandas as pd

# Load the Iris dataset
iris_df = pd.read_csv(filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None)

iris_df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
print(iris_df.head())
