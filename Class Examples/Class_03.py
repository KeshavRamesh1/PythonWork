###########
#### All the pure python code from the class_03 slides. 
###########

# This will be the standard way of importing the pandas library and aliasing it to "pd" 
import pandas as pd

# Create some data in place (later we will import from various sources).
# These are median house prices from various locations around Philadelphia.
house_data = pd.Series([66803, 104923, 114233, 114572, 112471, 99843, 74308, 147176, 199065, 130953],
                      index =['Collindale','Downingtown', 'Falls Town', 'Hatboro', 'Lansdale',
                              'Norwood', 'Sharon Hill', 'Springfield', 'Upper Darby', 'Yardley'])

############

print(house_data)

############

house_data.values # Look at the values in the Series

############

house_data.index # Look at the index itself

############

house_data[[0,7,3]] # Identify elements in positions 0, 7 and 3 (note the [[]] brackets).

############

list_a = list(range(10)) # Make a list
list_a[[0,7,3]] # This does not work!

############

house_data[2:5] # Recall the slice notation and note the single [] bracket.

############

house_data['Downingtown'] # Returns just the value of the Downingtown element.

############

house_data[['Downingtown']] # returns a Series containing the Downingtown element.

############

house_data[['Downingtown', 'Lansdale', 'Upper Darby', 'Falls Town']]

############

raw_data = pd.Series([31,16,12,27,28,9],
                      index =['a','b', 'c', 'd', 'e','f'])
logic_filter = [False, True, True, False, False, True]

print(raw_data[logic_filter])

############

# A list containing Trues in positions, 0,3,7,8
logical_list = [True, False, False, True, False, False, False, True, True, False]

house_data[logical_list]

############

expensive = house_data > 110000 # A logical comparison returning another Series, but this time of logicals.
print(expensive)

############

type(expensive)

############

house_data[expensive] # Just those rows where the price is greater than $110,000.

############

house_data[(house_data > 90000) & (house_data < 110000)]

############

house_data.mean() # The average of the prices.


############

house_data.median() # The median of the prices.

############

house_data.quantile([.25, .5, .75]) # The 25th, 50th and 75 percentiles.

############

house_data[2] = 123456 # Overwrite a single element.
print(house_data)

############

house_data[4:6] = [999999, 8888888] # Overwrite using a slice,
print(house_data)

############

house_data[house_data < 100000] = 0 # Overwrite using a logical filter to identify, and a repeated value to populate.
print(house_data)

############

#A dict structure containing the raw data and column names: 
raw_data = {'Sex': ['male','female','female','male','female','male','male','female','female','male'],
           'Age': [4,40,23,22,60,50,55,70,58,28],
           'Schedule lag': [41,29,5,18,1,17,29,3,4,2],
           'Schedule minutes':[30,15,30,30,15,10,30,30,15,30],
           'Status': ['No show', 'No show', 'No show', 'No show', 'Show', 'Show', 'No show', 'No show', 'Show', 'No show']}

############

patient_data = pd.DataFrame(data = raw_data) # pd.DataFrame() when passed the raw data will create the new data frame.  
print(patient_data) 

############

patient_data.shape # The number of rows and columns (.shape).

############

patient_data.dtypes # The data types in the data frame (.dtypes).

############

## Get just the names of the columns in the data frame with the .columns attribute.
print( patient_data.columns) 

############

# Get the Age column by name as we would if the data structure were a dict.
print(patient_data['Age'])

############

print(patient_data.Age) # This gets at the same column, but by "attribute" name.

############

print(patient_data.index) # This shows the index: by default here the numbers 0 through 9.

############

patient_ids = ['P456', 'P126','P563', 'P884','P102', 'P067','P120', 'P943','P496', 'P805'] # Patient identifiers.
patient_data.index = patient_ids # Assign a new index.
patient_data.index.name = 'Patient ID' # Give the new index a name.
print(patient_data) # Check out the data frame.

############

print(patient_data[3:6]) # Use the slice operator to identify by row number.

############

print(patient_data[:6:-1]) # Use the slice operator to identify by row number.

############

print(patient_data[['Sex', 'Status']]) # Identifying a set of columns.

############

print(patient_data.loc[['P120', 'P805']])  # Identify the rows by name.

############

print(patient_data.loc[['P120', 'P805'],  ['Sex', 'Status']]) # Identify rows and columns by name.

############

print(patient_data.iloc[1]) # The second row returned as a Series, with index of column names. 

############

print(patient_data.iloc[[1]]) # The second row returned as a DataFrame. 

############

print(patient_data.iloc[[0,-1]])

############

print(patient_data.iloc[[1,3,5],[2,3]]) # Rows 2, 4 and 6, with columns 3 and 4.

############

print(patient_data.iloc[:2,3:]) # Slice notation works too.

############

patient_data.Sex == "female" # A series where the trues are for females and the falses for males.
print(patient_data.Sex == "female")

############

print(patient_data[patient_data.Sex == "female"]) # Select only the females

############

# A compound selection of females who showed up. The "&" here performs the logical "and". 
# It works elementwise on the two boolean Series. 
print(patient_data[(patient_data.Sex == "female") & (patient_data.Status == "Show")])

############

# Get the schedule lag for females who showed up. 
print(patient_data[(patient_data.Sex == "female") & (patient_data.Status == "Show")].iloc[:, [2]])

############

print(patient_data.iloc[2,0]) # Sex of the third patient.
patient_data.iloc[2,0] = 'male' # Overwrite from female to male.
print(patient_data.iloc[2,0])

############

patient_data.iloc[2:4,1] = 19
print(patient_data)

############

patient_data.loc[['P456', 'P884'],['Sex', 'Age']] = [['NA',99],['NA',99]]
print(patient_data)

############

