import csv
 
def csv_reader(file_obj): #читаем csv файл
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
        r = (line["Рабочий email"]) 
        l = (line["Личный email"])
    # объединяем в один список личные и рабочие емайлы
        base = r+l

        #удаляем пустые строки и пробелы
        base = ''.join(base.split())
        if not base.strip(): 
            continue

	#разделяем, если в одной строке 2 адреса
        stace = base.split(',')        
        
    #записываем результат в файл
        with open('mail_data.txt', "a") as file:
            for line in stace:              
                file.write(line+'\n')    
                
if __name__ == "__main__":
    csv_path = "1.csv"	#название файла из которого считываем информацию
    with open(csv_path, "r", encoding='utf-8') as f_obj:
        csv_reader(f_obj)
	# а это просто так ))
input("А мы уже закончили....Нажмите Enter для выхода") 
 
 
