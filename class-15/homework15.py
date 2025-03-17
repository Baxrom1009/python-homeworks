
# import requests
# import os
# url = 'https://www.freetestapi.com/api/v1/politicians'
# response = requests.get(url)
# data = response.json()

# for obj in data:
#     columns = 'id,name,dob,country,party,position,years_in_office' + '\n'
#     id = obj['id']
#     name = obj['name']
#     dob = obj['dob']
#     country = obj['country']
#     party = obj['party']
#     position = obj['position']
#     years_in_office = obj['years_in_office']
#     image_link = obj['image']
#     biography = obj['biography']
#     values = f'{id},{name},{dob},{country},{party},{position},{years_in_office}' + '\n'
#     path = r"C:\Users\envy\Desktop\Python\general python\homework15"
#     os.makedirs(path +"\\"+ name,exist_ok=True)
#     file_path = path +"\\"+ name + '\\'+ name
#     with open(file_path + '.csv', 'w',encoding="utf-8") as f:
#         f.write(columns)
#         f.write(values)
#     with open(file_path + '.jpg', 'wb') as f:
#         response = requests.get(image_link)
#         f.write(response.content)
#     with open(file_path + '.txt','w',encoding="utf-8") as f:
#         f.write(biography)




