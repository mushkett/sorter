import os
import shutil
import piexif

list_of_month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                 'Ноябрь', 'Декабрь']


# создаем папки годов/месяцев
def d():
    for x in enumerate(list_of_month):
        month = f"{x[0]+1}. {x[1]}"
        if not os.path.exists(month):
            os.makedirs(month)


def get_date_taken(path):
    exif_dict = piexif.load(path)
    try:
        return exif_dict['Exif'][36867][:10]
    except:
        pass


p = input('Скопируйте сюда путь к фото. Например: E:/\1')
os.chdir(p)


def sort_photos():

    for root, dirs, files in os.walk(p):
        for file in files:
            try:
                year = get_date_taken(file)[:4].decode('utf-8')
                if not os.path.exists(year):
                    os.makedirs(year)
                os.chdir(f'{p}\{year}')
                d()
                os.chdir(p)
            except:
                continue

            try:
                number_of_month = int(get_date_taken(file)[5:7].decode('utf-8'))
                year = get_date_taken(file)[:4].decode('utf-8')
                month = f'{number_of_month}. {list_of_month[number_of_month - 1]}'  # месяц создания фото
                try:
                    shutil.copy(file, f'{year}\\{month}')  # перенос файла в папку
                except:
                    print('error')
                else:
                    os.remove(file)
            except:
                continue


sort_photos()
