username=input("введите ваше имя")
title=[]
temp_title=str
title_count=0
stop_word=""
stop_word2="none"
#цикл для ввода названий заголовков со стоп словом none  и пустым значением(энтер)
while temp_title !=stop_word and temp_title!=stop_word2:
   temp_title=input("введите название заметки"+str(title_count+1))
   title.append(temp_title)
  # print(temp_title)
   title_count+=1
title_count=len(title)
#print(title_count)
content_count=0
content=[]
status=[]
created_date=[]
issue_date=[]
# цикл для ввода информации (содержание, статус, дата создания, дата окончания)в зависимости от кол-ва названий(title)
while content_count!=title_count:
    content_count +=1
    content.append(  input("введите описание заметки"+str(content_count)))
    status.append(input("введите статус заметки" + str(content_count)))
    created_date.append(  input("введите дату создания заметки"+str(content_count)+" в формате 00.00.0000"))
    issue_date.append( input("введите дату предполагаемого окончания заметки"+str(content_count)+" в формате 00.00.0000"))

print("имя:"+username)
print_count=0
# цикл для вывода всей информации(имя заметки, описание заметки, статус заметки, дата созданий, дата окончания) по очереди в зависимости от колва названий заметки
while print_count!=title_count:
    print("название заметки" +str(print_count+1)+":"+ title[print_count])
    print("описание заметки" +str(print_count+1)+":" +content[print_count])
    print("статус заметки" +str(print_count+1)+":" +status[print_count])
    print("дата создания заметки" +str(print_count+1)+":"+ created_date[print_count])
    print("дата окончания заметки" +str(print_count+1)+":"+ issue_date[print_count])
    print_count += 1


