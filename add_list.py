
username=input("введите ваше имя")
title=input("введите название заметки")
content=input("введите описание заметки")
status=input("введите статус заметки")
created_date=input("введите дату создания заметки в формате 00.00.0000")
issue_date=input("введите дату предполагаемого окончания заметки в формате 00.00.0000")
title_title = [input("введите название заголовка1"), input("введите название заголовка2"),
               input("введите название заголовка3")]
temp_created_date=created_date[0:5]
temp_issue_date=issue_date[0:5]

print ("имя пользователя: "+username)
print("имя заметки: "+title)
print("краткое описание заметки: "+status)
print(created_date[0:5])
print(issue_date[0:5])
print("название заголовков:  ")
print(title_title)