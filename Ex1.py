import pandas as pd
data = pd.read_csv('Salaries.csv')
#1.Display Top 10 Rows of The Dataset
print(data.head(10))
#2. Check Last 10 Rows of The Dataset
print(data.tail())
#3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
print(data.shape)
print("Number of Rows:",data.shape[0])
print("Number of Columns:",data.shape[1])
#4. Getting Information About Our Dataset Like Total Number Rows,
#Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(data.info())
#5.Check Null Values In The Dataset
print(data.isnull())
#6. Drop ID, Notes, Agency and Status Columns
print(data.columns)
data=data.drop(['Id','Notes','Agency','Status'],axis=1)#0 for rows,1 for colums
print(data.columns)
#7. Get Overall Statistics About The Dataframe
print(data.describe())#explain numerical columns
#if we want all
print(data.describe(include(all))
#8. Find Occurrence of The Employee Names  (Top 5)
print(data.columns) #to get exact column name
print(data['EmployeeName'].value_counts())#will give occurance in descending order
print(data['EmployeeName'].value_counts().head())#will print first 5 
9. Find The Number of Unique Job Titles
print(data['JobTitle'].nunique()) 
#10. Total Number of Job Titles Contain Captain
print(len(data[data['JobTitle'].str.contains('CAPTAIN',case=False)])) 
print(data[data['JobTitle'].str.contains('CAPTAIN',case=False)].count())
#11. Display All the Employee Names From Fire Department
print(data[data['JobTitle'].str.contains('fire',case=False)]['EmployeeName'])
#12. Find Minimum, Maximum and Average BasePay
print(data['BasePay'].describe())
#13. Replace 'Not Provided' in EmployeeName' Column to NaN
import numpy as np
data['EmployeeName']=data['EmployeeName'].replace('Not provided',np.nan)
print(data['EmployeeName'])
 
 
 
