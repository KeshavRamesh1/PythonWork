###########
#### All the pure python code from the class_05 slides. 
###########

def tconvert(x):
    y = 32 + 9/5 * x
    return y

# Call the function a couple of times 
print(tconvert(22))
print(tconvert(100)) 

############

def tconvert(x):
    '''Takes in a number x, returns the converted temperature of x.'''
    y = 32 + 9/5 * x
    return y

print(tconvert.__doc__)

############

print(tconvert("It's hot!"))

############

def tconvert(x):
    '''Takes in a number x, returns the converted temperature of x.'''
    if( isinstance(x, (int, float)) and not isinstance(x, (bool))):  #Booleans are also ints! 
        y = 32 + 9/5 * x
        return y
    else:
        return "This function only works with numbers."

print(tconvert(3))
print(tconvert(21.2))
print(tconvert(True))
print(tconvert("It's hot!"))

############

def tconvert(x, direction):
    '''Takes in a number x, returns the converted temperature of x.'''
    
    if not ( (direction == "f2c") or (direction == "c2f")):
        return "Direction must be 'c2f' or 'f2c'."
    if not ( isinstance(x, (int, float)) and not isinstance(x, (bool))): # Booleans are also ints! 
        return "This function only works with numbers."
      
    if direction == "c2f":
        y = 32 + 9/5 * x
        return y
    if direction == "f2c":
        y = (x - 32) * 5/9
        return y     

############

print(tconvert(0.0, "c2f"))
print(tconvert(71, "f2c"))
print(tconvert(71, "a2b")) # Break it on purpose.
print(tconvert(225,"c2f"))

############

print(tconvert(direction = "f2c", x = 21))

############

print(tconvert(direction = "f2c", 212)) # This is illegal.

############

def tconvert(x, direction = "c2f"):
    '''Takes in a number x, returns the converted temperature of x.'''
    
    if not ( (direction == "f2c") or (direction == "c2f")):
        return "Direction must be 'c2f' or 'f2c'."
    if not ( isinstance(x, (int, float)) and not isinstance(x, (bool))): # Booleans are also ints! 
        return "This function only works with numbers."
      
    if direction == "c2f":
        y = 32 + 9/5 * x
        return y
    if direction == "f2c":
        y = (x - 32) * 5/9
        return y

############

print(tconvert(10)) # No need for the direction parameter, if happy with 'c2f'
print(tconvert(200))

############

def top3(x):
    y = x.value_counts(sort=True) # Recall thatvalue_counts makes frequencies, and the sort argument will sort them.
    return y.index[0], y[0], y.index[1], y[1], y.index[2], y[2] # Return multiple values.


############

import pandas as pd
import numpy as np
np.random.seed(1234)
data = np.random.choice(['a','b','c','d','e','f','g','h','i','j'], size=1000, replace=True) # Random sampling with replacement.
data = pd.Series(data) # Store the data in a pandas Series.

############

top3(data)

############

import math
def data_transform(x, fn):
    return [fn(input) for input in x] # Notice that the function "fn" is being used in the comprehension.

data = [1,2,5,6,2,1]

print(data_transform(data, lambda y: y**2))
print(data_transform(data, lambda y: math.log(y)))


############

data = np.random.randint(10, size=10000) # Make some data, random integers between 0 and 9. 

############

list(map(lambda x: x**2 , data))[0:5] # Just look at the first 5 elements.

############

# Read in a data frame for illustration.
import os
os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\DataSets') 
op_data = pd.read_csv("Outpatient_to_clean.csv")
print(op_data.shape) # Track the dimensions.
op_data.drop(0, inplace=True) # Drop the first row.
print(op_data.shape) # Track the dimensions.
op_data.drop(len(op_data)-1, inplace=True) # Drop the last row.
print(op_data.shape) # Track the dimensions.

############

temp = op_data.loc[op_data['Status'] != "Bumped"] # The logical filter selects all rows, that are not Bumped.
temp['Status'].value_counts() # Note that "Bumped has gone".

############

# Notice the NaN's in the data frame.
op_data = pd.read_csv("Outpatient_to_clean.csv",  parse_dates = ['SchedDate', 'ApptDate']) 
print(op_data.head(5))

############

op_data.dropna(inplace=True) # '.dropna()' removes all rows with any missing data.
print(op_data.head(5)) # Note that some of the rows have disappeared.

############

op_data['Sex'] = op_data['Sex'].map({'F': 'F', 'M': 'M'}).fillna('Unknown')
print(op_data[0:7])

############

op_data['Dept'] = op_data['Dept'].str.strip()
print(op_data['Dept']) 

############

print(op_data[0:2])
op_data['Age'].mean() # This fails.

############

op_data['Age'] = pd.to_numeric(op_data['Age'], errors = 'coerce')
print(op_data['Age'].mean()) # Now we can calculate the mean.

############

print(op_data['Dept'].value_counts())


############

op_data.loc[op_data['Dept'] == "NEUROLOGICAL", 'Dept'] = "NEUROLOGY"  # The logical replacement filter.
op_data['Dept'].value_counts() # Now there are more rows in the NEUROLOGY column.

############

op_data.sort_values(by='Age', inplace = True)
print(op_data.head(3))

############

op_data.sort_values(by = ['PID', 'SchedDate'], inplace=True) # Sorting by two columns.
print(op_data.head(5))


############

op_data.groupby('PID')['PID'].count()

############

op_data.groupby('PID')['PID'].count() - 1 # Remove 1 from the count.


############

prev = lambda x: len (x) - 1 # A lambda function to count previous appointments.
prior_arrived = lambda x: sum(x[:-1] == "Arrived") if len(x) > 1 else 'NA'  # Counting the number of prior arrivals.
    
op_behave = op_data.groupby('PID').agg(PriorVisits=('PID', prev), 
                           PriorArrived=('Status', prior_arrived))
print(op_behave.head(3))

############

op_last_values = op_data.groupby('PID').last() # Obtain the last row for each patient
print(op_last_values.head(5))

############

op_last_values.loc['P10998']


############

final_op_data = pd.merge(op_last_values, op_behave, on = 'PID')
print(final_op_data.head(5))

############

