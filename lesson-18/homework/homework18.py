import pandas as pd
import numpy as np
import pyodbc

# data = {
#     'id': [332289, 2051744, 2225995, 5486226, 5515021],
#     'creationdate': ['2008-12-01 21:24:44', '2010-01-12 19:31:47', '2010-02-09 00:51:38', '2011-03-30 12:26:50', '2011-04-01 14:50:44'],
#     'score': [3184, 420, 51, 7, 10],
#     'viewcount': [5962784, 587728, 59922, 6393, 13744],
#     'title': [
#         'How do I change the size of figures drawn with...',
#         'How to invert the x or y axis',
#         'How can I create stacked line graph?',
#         'Rolling median in python',
#         'Compute a compounded return series in Python'
#     ],
#     'answercount': [14, 10, 4, 5, 3],
#     'commentcount': [1, 3, 0, 4, 6],
#     'favoritecount': [0.0, 0.0, 0.0, 0.0, 0.0],
#     'quest_name': ['tatwright', 'DarkAnt', 'David Underhill', 'yueerhu', 'Demitri'],
#     'quest_rep': [37837.0, 4211.0, 15936.0, 175.0, 13369.0],
#     'ans_name': [None, 'Demitri', 'doug', 'Mike Pennington', 'Mike Pennington'],
#     'ans_rep': [None, 13369.0, 69290.0, 42288.0, None]
# }


# df = pd.DataFrame(data)


# Find all questions that were created before 2014
# df['creationdate'] = pd.to_datetime(df['creationdate'])
# filtered_df = df[df['creationdate'].dt.year < 2014]
# print(filtered_df)


# Find all questions with a score more than 50
# a = df[df['score'] > 50]
# print(a)

# Find all questions with a score between 50 and 100
# a = df[df['score'].between(50,100)]
# print(a)

# Find all questions answered by Scott Boston
# a = df[df['ans_name'] == 'Scott Boston']
# print(a)

# Find all questions answered by the following 5 users
# users = [None, 'Demitri', 'doug', 'Mike Pennington', None]
# a = df[df['ans_name'].isin(users)]
# print(a)

# Find all questions that were created between March, 2014 and October 2014 that were answered by Unutbu and have score less than 5.
# a = df[df['creationdate'].between('2014-03-01','2014-10-31')]
# b = a[a['ans_name'] = 'Unutbu']
# c = b[b['score'] < 5]
# print(c)



# Find all questions that have score between 5 and 10 or have a view count of greater than 10,000
# a = df[df['score'].between(5,10)]
# b = a[a['viewcount'] > 10000]
# print(b)

# Find all questions that are not answered by Scott Boston
# a = df[df['ans_name'] != 'Scott Boston']
# print(a)



data = {
    "PassengerId": [1, 2, 3, 4, 5],
    "Survived": [0, 1, 1, 1, 0],
    "Pclass": [3, 1, 3, 1, 3],
    "Name": [
        "Braund, Mr. Owen Harris",
        "Cumings, Mrs. John Bradley (Florence Briggs Th.)",
        "Heikkinen, Miss. Laina",
        "Futrelle, Mrs. Jacques Heath (Lily May Peel)",
        "Allen, Mr. William Henry"
    ],
    "Sex": ["male", "female", "female", "female", "male"],
    "Age": [22.0, 38.0, 26.0, 35.0, 35.0],
    "SibSp": [1, 1, 0, 1, 0],
    "Parch": [0, 0, 0, 0, 0],
    "Ticket": ["A/5 21171", "PC 17599", "STON/O2. 3101282", "113803", "373450"],
    "Fare": [7.25, 71.2833, 7.925, 53.1, 8.05],
    "Cabin": [None, "C85", None, "C123", None],
    "Embarked": ["S", "C", "S", "S", "S"]
}

df1 = pd.DataFrame(data)
# print(df1)
# Select Female Passengers in Class 1 with Ages between 20 and 30: Extract a DataFrame containing female passengers in Class 1 with ages between 20 and 30.
# a = df1[df1['Pclass'] == 1]
# b = a[a['Age'].between(20,30)]
# print(b)


# Filter Passengers Who Paid More than $100: Create a DataFrame with passengers who paid a fare greater than $100.
# a = df1[df1['Fare']>100]
# print(a)

# Select Passengers Who Survived and Were Alone: Filter passengers who survived and were traveling alone (no siblings, spouses, parents, or children).
# a = df1[df1['Survived']== 0]
# b = a[a['SibSp'] == 0]
# print(b)


# Filter Passengers Embarked from 'C' and Paid More Than $50: Create a DataFrame with passengers who embarked from 'C' and paid more than $50.
# a = df1[df1['Embarked'] == 'C']
# b = a[a['Fare'] > 50]
# print(b)


# Select Passengers with Siblings or Spouses and Parents or Children: Extract passengers who had both siblings or spouses aboard and parents or children aboard.
# a = df1[df1['SibSp']== 1]
# print(a)


# Filter Passengers Aged 15 or Younger Who Didn't Survive: Create a DataFrame with passengers aged 15 or younger who did not survive.
# a = df1[df1['Age']<= 15]
# b = a[a['Survived'] == 1]
# print(b)


# Select Passengers with Cabins and Fare Greater Than $200: Extract passengers with known cabin numbers and a fare greater than $200.
# a = df1[df1['Cabin']!= 'None']
# b = a[a['Fare'] > 200]
# print(b)

# Filter Passengers with Odd-Numbered Passenger IDs: Create a DataFrame with passengers whose PassengerId is an odd number.
# a = df1[df1['PassengerId'].isin([1,3,5])]
# print(a)


# Select Passengers with Unique Ticket Numbers: Extract a DataFrame with passengers having unique ticket numbers.


# Filter Passengers with 'Miss' in Their Name and Were in Class 1: Create a DataFrame with female passengers having 'Miss' in their name and were in Class 1.
a = df1[(df1["Sex"] == "female") & (df1["Pclass"] == 1) & (df1["Name"].str.contains("Miss"))]
print(a)
