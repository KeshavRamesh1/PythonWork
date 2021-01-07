###########
#### All the pure python code from the class_04 slides. 
###########



############

import pandas as pd
import os

# Change the working directory to where the datasets are stored.
os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\DataSets') 
no_show_01 = pd.read_csv("no_show_10.csv", index_col=0) # The read_csv command. Use the first column as index.
print(no_show_01)

############

no_show_02 = pd.read_html("no_show_10.htm",index_col=0)[0] # The [0] pulls off the first (and only) data frame.
no_show_02.index.name = 'Patient ID' # Give the index a name.
print(no_show_02)

############

no_show_03 = pd.read_json('no_show_10.json') 
no_show_03.index.name = 'Patient ID' # Give the index a name.
print(no_show_03)

############

no_show_04 = pd.read_csv("http://mathmba.com/data/no_show_10.csv", index_col=0)
print(no_show_04.shape) # "shape" gives you the dimensions of the data frame, the number of rows and columns.
no_show_05 = pd.read_html("http://mathmba.com/data/no_show_10.htm",index_col=0)[0]
print(no_show_05.shape)
no_show_06 = pd.read_json("http://mathmba.com/data/no_show_10.json")
print(no_show_06.shape)


############

from sqlalchemy import create_engine # The database toolkit.

# An "engine" is set up to establish a connection to the database when the time comes.
sqlEngine = create_engine('mysql://stat705_student:$[h0CC*TtKO~@mathmba.com/STAT705X')

# The connect method makes the connection.
dbConnection = sqlEngine.connect()

# The key pandas command to put the results from the query right into a data frame is "read_sql".
# It sends the query "SELECT * FROM RESPONSES" over the connection.
survey_from_db = pd.read_sql("SELECT * FROM RESPONSES", dbConnection, index_col='MYID')
print(type(survey_from_db)) # Confirm we have a data frame.
dbConnection.close() # Close the connection to conserve resources.

############

print(survey_from_db.head(10))

############


dbConnection = sqlEngine.connect()

# The key pandas command to put the results from the query right into a data frame.
# It sends the query over the connection.
db_summary = pd.read_sql("SELECT Q1, COUNT(Q1) FROM RESPONSES GROUP BY Q1", dbConnection)
dbConnection.close() # Close the connection to conserve resources.

print(db_summary)

############

survey_from_db.Q1.value_counts()

############

# Read in the data sets using pandas. They are both csv files, residing on the web.
import pandas as pd
x_data = pd.read_csv("http://mathmba.com/richardw/x_var_join.csv")
y_data = pd.read_csv("http://mathmba.com/richardw/y_var_join.csv")
print(x_data.head(3))
print("Rows and columns are ",  x_data.shape)
print(y_data.head(3))
print("Rows and columns are ",  y_data.shape)

############

pd.merge(x_data,y_data, on = 'ACCOUNTID')

############

# Below we specify the name of the key in each data frame with "left_on" and "right_on".
inner_join_data = pd.merge(x_data,y_data, left_on = 'ACCOUNTID', right_on = 'AccountID')
print(inner_join_data)
print("Rows and columns are",  inner_join_data.shape)

############

# Note the 'how="left"' argument.
left_join_data = pd.merge(x_data,y_data, left_on = 'ACCOUNTID', right_on = 'AccountID', how="left")
print(left_join_data)
print("Rows and columns are",  left_join_data.shape)


############

# Note the 'how="right"' argument.
right_join_data = pd.merge(x_data,y_data, left_on = 'ACCOUNTID', right_on = 'AccountID', how="right")
print(right_join_data)
print("Rows and columns are",  right_join_data.shape)


############

# Note the 'how="outer"' argument.
outer_join_data = pd.merge(x_data,y_data, left_on = 'ACCOUNTID', right_on = 'AccountID', how="outer")
print(outer_join_data)
print("Rows and columns are ",  outer_join_data.shape)


############

# Insert a new row in the data frame with the .append method.
new_x_data = x_data.append({'SocialMediaIndex': 0, 'WordPress': 'NO','ACCOUNTID':'INF85'}, ignore_index=True)

# Now do an inner join and note how "INF85" is the new data frame twice.:
print(pd.merge(new_x_data,y_data, left_on = 'ACCOUNTID', right_on = 'AccountID')) 

############

# Rename a column. The "inplace" overwrites the existing data frame.
# The axis argument specifies if it is the rows or column index you wish to change. 0 = rows, 1 = columns.
# The old and new names are specified in a dict structure.
y_data.rename({'AccountID': 'ACCOUNTID'}, axis = 1, inplace = True) 
print(y_data)


############

# pandas looks for the common column name and uses that as the key automatically.
print(pd.merge(x_data, y_data)) 

############

from datetime import datetime, date, time

today = date.today()
print("Today's date:", today)

now = datetime.now()
print("Now =", now)


############

# The the .timestamp method returns the number of seconds since 1970-1-1 00:00:00
epoch_time = datetime.now().timestamp()
print(epoch_time)

############

time_one = pd.to_datetime('03211989', format="%m%d%Y")
print(time_one)
print(type(time_one)) # It is of type "Timestamp" 

time_two = pd.to_datetime('07132020', format="%m%d%Y")
print(time_two)

############

print(time_two - time_one) 
print(type(time_two - time_one)) # It is of type "Timedelta" 

############

# The time format used by Yahoo Finance stock data downlaods (see homework 2).
time_three = pd.to_datetime('Jan 13, 2020', format="%b %d, %Y")
print(time_three)

############

import os
os.chdir('C:\\Users\\richardw\\Dropbox (Penn)\\Teaching\\477s2020\\DataSets') 
outpatient_data = pd.read_csv("Outpatient.csv", )

# Basic top level data summaries.
print(outpatient_data.shape) # Rows and columns.
print(outpatient_data.columns) # Column names.
print(outpatient_data.dtypes) # Column data types.

############

outpatient_data = pd.read_csv("Outpatient.csv", parse_dates=['SchedDate', 'ApptDate']) # Pass in the date columns.
print(outpatient_data.dtypes) # This looks better!

############

outpatient_data['ScheduleLag']  = outpatient_data['ApptDate'] - outpatient_data['SchedDate']

# What is the average schedule lag? It is about a month.
outpatient_data['ScheduleLag'].mean()


############

outpatient_data['ApptDayOfWeek'] =  outpatient_data['ApptDate'].dt.day_name(locale='fr')
outpatient_data['ApptMonthOfYear'] =  outpatient_data['ApptDate'].dt.month_name(locale='fr')
print(outpatient_data.columns)

############

outpatient_data['ApptDayOfWeek'].value_counts()

############

# This will count the number of appointments in each Status level. 
print(outpatient_data.Status.value_counts())

############

# Using groupby gives the value counts by day of the week.
outpatient_data.groupby('ApptDayOfWeek').Status.value_counts()

############

# The optional argument, "normalize" will return a proportion. They add to 1 for each day of the week.
outpatient_data.groupby('ApptDayOfWeek').Status.value_counts(normalize=True)

############

# Save the result into a Series object with a MultiIndex.
category_props = outpatient_data.groupby('ApptDayOfWeek').Status.value_counts(normalize=True)
print(type(category_props))
print(category_props.index)

############

# xs stands for "cross section" and 'level' specifies which level of the MultiIndex to look in. 
category_props.xs('Cancelled', level=1)

############

pd.set_option('precision', 3) # Control output formatting for floats to 3 digits of precision.
print(pd.crosstab(index = outpatient_data.Status, columns = outpatient_data.ApptDayOfWeek, normalize = 'columns'))

############

