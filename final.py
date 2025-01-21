
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
note=[username,title,content,status,temp_created_date,temp_issue_date,title_title]
print("Имя: "+note[0])
print("Название заметки: "+note[1])
print("Описание: "+note[2])
print("Статус заметки: "+note[3])
print("Дата создания: "+note[4])
print("Дата окончания: "+note[5])
print("Заголовки: "+title_title[0]+", "+title_title[1]+", "+title_title[2])
print(note)
