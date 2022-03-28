him = input( " ВВеди: " )
him = him.lower()                                              #---------------------приведение к нижнему регистру
him = him.split()                                              #---------------------РАСЩЕПЛЕНИЕ
him = [him.strip('.,!;()[]') for him in him]                   #---------------------УБИРАЕМ ЛИШНИЕ ЗНАКИ
him = [him.replace("'s", '') for him in him]                   #---------------------ЗАМЕНЯЕМ 'S НА ПУСТОТУ 
him = sorted(him)
print("Ответ: " + str(him))
