import pyodbc 

connection = pyodbc.connect( 
                               'DRIVER={SQL Server};'
                               'Server=DESKTOP-OM4IIFB;'
                               'Database=AdventureWorksDW2022;'
                               'trusted_Connection=yes;'
                               )
print('Connected Succesfully')


cursor = connection.cursor()
query = 'SELECT TOP (10) [EmployeeKey],[FirstName],[LastName],[MiddleName],[Title],[HireDate],[BirthDate],[MaritalStatus],[Gender],[DepartmentName]FROM [AdventureWorksDW2022].[dbo].[DimEmployee]'


cursor.execute(query)


columns = [column[0] for column in cursor.description]

data = [dict(zip(columns, row)) for row in cursor.fetchall()]

with open('employee.csv','w',encoding='utf-8') as f:
    columns = 'EmployeeKey,FirstName,LastName,MiddleName,Title,HireDate,BirthDate,MaritalStatus,Gender,DepartmentName' + '\n'
    f.write(columns)

    for obj in data:
        columns = 'EmployeeKey,FirstName,LastName,MiddleName,Title,HireDate,BirthDate,MaritalStatus,Gender,DepartmentName' + '\n'
        employee_key = obj['EmployeeKey']
        first_name = obj['FirstName']
        last_name = obj['LastName']
        midlle_name = obj['MiddleName']
        title = obj['Title']
        hire_date = obj['HireDate']
        birth_date = obj['BirthDate']
        Marital_status = obj['MaritalStatus']
        gender = obj['Gender']
        deparment_name = obj['DepartmentName']
        values = f'{employee_key},{first_name},{last_name},{midlle_name},{title},{hire_date}.{birth_date},{Marital_status},{gender},{deparment_name}' + '\n'
        f.write(values)


