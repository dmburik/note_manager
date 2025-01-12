username=input("введите ваше имя")
title=[]
title.append(input("введите название заметки"))
title.append(input("введите название заметки2"))
title.append(input("введите название заметки3"))
title_count=len(title)
print(title_count)
content_count=0
content=[]
status=[]
created_date=[]
issue_date=[]
while content_count!=title_count:
    content_count +=1
    content.append(input("введите описание заметки"+str(content_count)))
    status.append(input("введите статус заметки" + str(content_count)))
    created_date.append(input("введите дату создания заметки"+str(content_count)+" в формате 00.00.0000"))
    issue_date.append(input("введите дату предполагаемого окончания заметки"+str(content_count)+" в формате 00.00.0000"))

print("имя:"+username)
print_count=0
while print_count!=title_count:
    print("название заметки: " + title[print_count])
    print("описание заметки:" + content[print_count])
    print("статус заметки:" + status[print_count])
    print("дата создания заметки:" + created_date[print_count])
    print("дата окончания заметки:" + issue_date[print_count])
    print_count += 1


