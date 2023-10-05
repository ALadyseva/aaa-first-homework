import csv


my_file = 'C:/Users/ladys/OneDrive/Python2/Corp_Summary.csv'
my_encoding = 'utf-8'
my_delimiter = ';'


def menu():
    """
    Prints menu with following options:
    1. show the hierarchy of departments
    2. show the report of departments
    3. save the report of departments in csv-file
    4. exit
    """
    print('---Меню---')
    print('1) Иерархия команд')
    print('2) Отчёт по департаментам')
    print('3) Сохранить отчёт по департаментам в csv-файл')
    print('4) Выйти')
    option = ''
    options = {'1': 1, '2': 2, '3': 3, '4': 4}
    while option != '4':
        while option not in options:
            print('Выберите действие: {}/{}/{}/{}'.format(*options))
            option = input()
        if options[option] == 1:
            return department_n_units()
        elif options[option] == 2:
            return department_rep()
        elif options[option] == 3:
            return write_rep()


def convert_file(file_name: str, encod: str, delim: str):
    """
    Opens csv file.
    Parameters:
    file_name: name of the file to open
    encod: encoding of the file to open
    delim: delimiter that is used in the file
    """
    with open(my_file, encoding=my_encoding) as r_file:
        reader = csv.reader(r_file, delimiter=my_delimiter)
        names, departments, unit, post, mark, salary = [], [], [], [], [], []
        for line in reader:
            if line[0] != 'ФИО полностью':
                names.append(line[0])
                departments.append(line[1])
                unit.append(line[2])
                post.append(line[3])
                mark.append(line[4])
                salary.append(int(line[5]))
    return (names, departments, unit, post, mark, salary)


def hierarchy_print(dictionary: dict):
    """
    Prints dictionary the following way:
        key
        --> value_1
        ...
        --> value_n
    """
    for key in dictionary:
        print(key)
        for elem in dictionary[key]:
            print(f'--> {elem}')
        print('')


def department_n_units():
    """
    Prints hierarchy of departments and units.
    """
    departments = convert_file(my_file, my_encoding, my_delimiter)[1]
    units = convert_file(my_file, my_encoding, my_delimiter)[2]
    hierarchy = {}
    for dep in departments:
        hierarchy[dep] = []
    for i, dep in enumerate(departments):
        for j, unit in enumerate(units):
            if i == j and unit not in hierarchy[dep]:
                hierarchy[dep].append(unit)
    hierarchy_print(hierarchy)
    menu()


def report_print(dictionary: dict):
    """
    Prints dictionary the following way:
    name: key
    size: key['size']
    fork: key['min'] - key['max']
    average: key['avg']
    """
    for key in dictionary.keys():
        print(f'name: {key}')
        print('size:', dictionary[key]['size'])
        print('fork:', dictionary[key]['min'], '-', dictionary[key]['max'])
        print('avg:', dictionary[key]['avg'])
        print('')


def department_prerep():
    """
    Prepares information for department report.
    Output of this fucntion is dictionary:
        key of the dictionary is the name of department
        value is a dictionary of size, min, max and average salary
    """
    departments = convert_file(my_file, my_encoding, my_delimiter)[1]
    salary = convert_file(my_file, my_encoding, my_delimiter)[5]
    report = {}
    for dep in departments:
        report[dep] = {}
        report[dep]['size'] = 0
        report[dep]['min'] = 100000000000
        report[dep]['max'] = 0
        report[dep]['avg'] = 0
    for i, dep in enumerate(departments):
        report[dep]['size'] += 1
        report[dep]['min'] = min(salary[i], report[dep]['min'])
        report[dep]['max'] = max(salary[i], report[dep]['max'])
        report[dep]['avg'] += salary[i]
    for key in report.keys():
        report[key]['avg'] = round(report[key]['avg'] / report[key]['size'], 2)
    return report


def department_rep():
    """
    Prints report about departments:
    - name of department
    - size of department
    - min and max salary
    - average salary
    """
    report_print(department_prerep())
    menu()


def write_rep():
    """
    Saves departments report in csv-file, named 'report.csv'
    """
    report = department_prerep()
    with open('report.csv', mode='w', encoding=my_encoding) as w_file:
        f_wr = csv.writer(w_file, delimiter=';', lineterminator='\r')
        f_wr.writerow(['Название', 'Численность', 'Вилка з/п', 'Средняя з/п'])
        for key in report.keys():
            mas = []
            mas.append(key)
            mas.append(str(report[key]['size']))
            mas.append(str(report[key]['min'])+' - '+str(report[key]['max']))
            mas.append(str(report[key]['avg']))
            f_wr.writerow(mas)
    menu()


if __name__ == '__main__':
    menu()
