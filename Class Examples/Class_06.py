###########
#### All the pure python code from the class_06 slides. 
###########

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime, date

# Read in some data
os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\DataSets') 
op_data = pd.read_csv("Outpatient.csv", parse_dates=['SchedDate', 'ApptDate'])
op_data['ScheduleLag']  = op_data['ApptDate'] - op_data['SchedDate']
op_data.columns


############

sns.set() # The default theme.
op_data['SL'] = op_data['ScheduleLag'].dt.days # Create a new variable that has schedule lag in days.
sns.boxplot(x='SL', data = op_data); # Create a default boxplot. The colon is a trick to stop unwanted output on the terminal. 

############

# Note below that the data argument is not quoted, but the x argument is quoted.
# "Flier" is the name for the outliers.
sns.boxplot(x='SL', data = op_data, orient='v', color='red', fliersize=1.0);  


############

g = sns.boxplot(x='SL', data = op_data, orient='v', color='red', fliersize=1.0, notch=True, sym=""); 
print(type(g))

############

g = sns.catplot(x='SL', data = op_data, kind="box") # A boxplot, from the "catplot" figure level command. 
print(type(g))
g.set_xlabels("Schedule lag") # You can tweak these plots using built in methods.
g.fig.suptitle('Distribution of schedule lags');

############

g = sns.catplot(x='SL', data = op_data, kind="violin") # A boxplot, from the "catplot" figure level command. 
g.set_xlabels("Schedule lag") # You can tweak these plots using built in methods.
g.fig.suptitle('Distribution of schedule lags');

############

sns.distplot(op_data['SL']);

############

sns.distplot(op_data['SL'], kde=False, rug=True); # Remove the kernel density estimate and add a rug plot.

############

from scipy import stats # Get access to some statistical functionality

sns.distplot(op_data['SL'], kde=False, fit=stats.lognorm); 

############

sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.distplot(op_data['SL'], kde=False, fit=stats.lognorm); 


############

import os
os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\Images') 
sns.set(rc={'figure.figsize':(6,4)})
sns.distplot(op_data['SL'], kde=False, fit=stats.lognorm); 
plt.savefig("output_{0}.png".format('OP')) # savefig method for png format.
plt.savefig("output_{0}.jpeg".format('OP')) # savefig method for jpeg format.
plt.savefig("output_{0}.svg".format('OP')) # savefig method for svg format.


############

sns.catplot(x='Dept', kind="count", data=op_data);

############

#### Prep the data
top_dept = op_data['Dept'].value_counts()[:5] # Identify the top 5 Departments
new_dept = op_data.loc[op_data['Dept'].isin(top_dept.index)]['Dept'] # Subset using '.isin'.
new_dept = pd.DataFrame(data=new_dept) # Cast the Series to a DataFrame.

############

#### Build the plot
g = sns.catplot(x='Dept', kind="count", palette="ch:.25", data=new_dept, height=6, aspect=2) #ch stands for a "cube-helix" color palette.
g.set_xticklabels(rotation=45, horizontalalignment='right')
plt.subplots_adjust(bottom=0.4) # This adds more white space to the bottom of the plot.
plt.savefig("output_{0}.png".format('Dept')) # savefig method.

############

new_dept = op_data.loc[op_data['Dept'].isin(top_dept.index)] # Keep all of the columns now.
g = sns.catplot(x='Dept', kind="count", palette="ch:.25", data=new_dept, 
                col="Sex", height=6, aspect=1.5) # Note the 'col' argument.
g.set_xticklabels(rotation=45, horizontalalignment='right');

############

g = sns.catplot(x='Dept', kind="count", palette="ch:.25", data=new_dept, 
                row = 'Sex', col="Status", height=2, aspect=1.5) # Note the 'col' argument.
g.set_xticklabels(rotation=45, horizontalalignment='right');

############

dept_counts = op_data['Dept'].value_counts()[:5] # Just work with the  frequencies here.
dept_counts.plot.pie(figsize=(6, 6)); # This is a pandas plot.

############

current_palette = sns.color_palette()
sns.palplot(current_palette)

############

sns.palplot(sns.color_palette("Paired")) # The paired palette.

############

sns.palplot(sns.color_palette("Blues"))

############

custom_palette = sns.color_palette("Reds", 4)
sns.palplot(custom_palette)


############

custom_palette = sns.color_palette("Greens", 6)
sns.palplot(custom_palette)

############

g = sns.catplot(x='Dept', kind="count", palette=custom_palette, data=new_dept)
g.set_xticklabels(rotation=45, horizontalalignment='right');

############

sns.palplot(sns.cubehelix_palette(n_colors = 8, start=0.8, rot=.4))

############

wharton_colors = ["#004785", "#262460", "#A90533", "#A8204E"]
sns.set_palette(sns.color_palette(wharton_colors)) # Set the custom color palette.


############

g = sns.catplot(x='Dept', kind="count", palette=wharton_colors, data=new_dept, height=6, aspect=2)
g.set_xticklabels(rotation=45, horizontalalignment='right');

############

sns.set_palette(sns.color_palette("cubehelix_r")) # Use a different palette.
new_dept = op_data.loc[op_data['Dept'].isin(top_dept.index)] #Subset the data.
g = sns.catplot(x = 'Dept', y = "SL", data = new_dept) # The default "catplot"
g.set_xticklabels(rotation=45, horizontalalignment='right');

############

g = sns.catplot(x='Dept',y="SL", kind="box", data=new_dept) # The comparison boxplots
g.set_xticklabels(rotation=45, horizontalalignment='right');

############

g = sns.catplot(x ='Dept', y="SL", kind="violin", data=new_dept) # The default "catplot"
g.set_xticklabels(rotation=45, horizontalalignment='right');

############

sns.catplot(x = 'Status', y = "SL", hue ='Dept', kind="box", data = new_dept, height=4, aspect=3); # Note the 'hue' argument.

############

f, ax = plt.subplots(1, 1, figsize = (12, 6)) # Set the size of the plot.
sns.boxplot(x = 'Status', y = "SL", hue = 'Dept', data = new_dept, ax=ax); # Note we are back to boxplot.
plt.savefig("output_{0}.png".format('Comps')) # savefig method for png format.


############

g = sns.catplot(x = 'Dept', y = "SL", kind= "bar", hue = 'Status', data = new_dept,height=4,aspect=3) # The 'bar' kind.
g.set_ylabels("Average Schedule lag");

############

os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\DataSets') 
car_data = pd.read_csv("Car08_just_499.csv")
print(car_data.columns)

############

sns.relplot(x="Weight(lb)", y="GP1000M_City", data=car_data,color="red");

############

sns.relplot(x="Weight(lb)", y="GP1000M_City", hue="Transmission", data=car_data);

############

sns.relplot(x="Weight(lb)", y="GP1000M_City", hue = "Transmission", style="Cylinders", data=car_data);

############

sns.relplot(x="Weight(lb)", y="GP1000M_City", hue="Transmission", style="Cylinders", palette="copper", data=car_data);

############

sns.relplot(x="Weight(lb)", y="GP1000M_City", hue = "Transmission", size = "Horsepower", 
            sizes=(20, 200), style="Cylinders", palette="Reds", data=car_data, height=6, aspect=1.5);

############

sns.jointplot(x="Weight(lb)", y="GP1000M_City", data=car_data, color="red");

############

sns.jointplot(x="Weight(lb)", y="GP1000M_City", data=car_data, color="red", kind="kde");

############

sns.set(style="whitegrid", font_scale=1.5) # Change the style
tmp_data = car_data[['GP1000M_City', 'Weight(lb)', 'Horsepower', 'Length', 'Transmission']]
sns.pairplot(tmp_data, hue="Transmission");
plt.savefig("output_{0}.png".format('Cars')) # savefig method for png format


############

from statsmodels.graphics.mosaicplot import mosaic
mosaic(op_data, ['Sex', 'Status']);

############

op_data['SL_8Cut'] = pd.qcut(op_data['SL'], 8) # Create 8 levels with equal numbers in each category.

fig, ax1 = plt.subplots(figsize=(16, 7)) # Controlling plot size using matplotlib. This returns a figure to plot on.

mosaic(op_data, ['SL_8Cut', 'Status'], ax=ax1); # Plots the mosaic plot on the axes "ax1".


############

