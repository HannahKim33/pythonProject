import seaborn as sns
import matplotlib.pyplot as plt

# var =['a','b','a','a','c','b']
# sns.countplot(x=var)

df=sns.load_dataset('titanic')
# print(df)

# sns.countplot(data=df, x='sex')

# sns.countplot(data=df, x="class")

# sns.countplot(data=df, x='class', hue='alive')
sns.countplot(data=df, y='class', hue='alive')

# plt.show()
help(sns.countplot())