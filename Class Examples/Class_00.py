###########
#### All the pure python code from the class_00 slides. 
###########

import pandas as pd
import os
from sklearn import tree

# This is where the data lives:
os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\DataSets')
print(os.getcwd())

carTable = pd.read_csv("Car08_just_499.csv")
print(carTable)


############

import mysql.connector as mysq

mydb = mysq.connect(
  host="mathmba.com",
  user="stat705_student",
  passwd="$[h0CC*TtKO~",
  database = "STAT705X"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM RESPONSES")
myresult = mycursor.fetchall()
mydb.close()

for x in myresult:
  print(x)
  

############

# Recode the levels of a categorical variable
print(carTable['Transmission'].value_counts())
recodes = {'A':'Automatic','AS':'Automatic','AV':'Automatic', 'M':'Manual'}
carTable['Transmission'] = carTable['Transmission'].map(recodes)
print(carTable.Transmission.value_counts())

############

import matplotlib.pyplot as plt
import seaborn as sns

sns.boxplot(x = 'Transmission', y = 'GP1000M_City', data = carTable)
plt.title('Fuel economy by transmission type')

############

sns.scatterplot(x = 'Weight(lb)', y = 'GP1000M_City', hue='Transmission', data=carTable, style='Transmission', 
                    palette=['green','orange'], legend='full')


############

# A scatterplot with the linear regression line and confidence bands
sns.regplot(carTable['Weight(lb)'], carTable['GP1000M_City'], color ='blue')

############

from sklearn.tree import DecisionTreeClassifier, plot_tree

X = carTable[['Weight(lb)', 'Displacement', 'Horsepower']]
y = carTable['GP1000M_City']
regtree = tree.DecisionTreeRegressor(max_leaf_nodes = 7)
regtree = regtree.fit(X, y,)

############

os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\Notes')
fig = plt.figure(num=None, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
plot_tree(regtree, filled=True, feature_names=X.columns)
plt.savefig('images/tree_01.png',  bbox_inches='tight')
plt.close(fig)

############

