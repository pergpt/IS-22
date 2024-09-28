"""
Приложение АБИТУРИЕНТ для автоматизации работы
приемной комиссии, которая обеспечивает обработку
анкетных данных абитуриентов. Таблица Анкета
содержит следующие данные об абитуриентах:
Регистрационный номер, Фамилия, Имя, Отчество,
Дата Рождения, Награды (наличие кр. Диплома или
медали (да/нет)), Адрес, выбранная Специальность.
"""

import sqlite3

with sqlite3.connect("abiturient.db") as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS anketa (
        reg_num INTEGER PRIMARY KEY AUTOINCREMENT,
        l_name TEXT NOT NULL,
        f_name TEXT NOT NULL,
        m_name TEXT,
        b_date TEXT,
        awards TEXT,
        address TEXT,
        specialty TEXT
        )''')

# Добавление данных
def add(l_name, f_name, m_name, b_date, awards, address, specialty):
    with sqlite3.connect("abiturient.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO anketa (l_name, f_name, m_name, b_date, awards, address, specialty)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (l_name, f_name, m_name, b_date, awards, address, specialty))

# Поиск по фамилии
def search_by_last_name(l_name):
    with sqlite3.connect("abiturient.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM anketa WHERE l_name = ?
        ''', (l_name,))
        results = cursor.fetchall()
        return results

# Удаление по номеру регистрации
def delete(reg_num):
    with sqlite3.connect("abiturient.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
        DELETE FROM anketa WHERE reg_num = ?
        ''', (reg_num,))

# Замена значения
def update(reg_num, l_name, f_name, m_name, b_date, awards, address, specialty):
    with sqlite3.connect("abiturient.db") as conn:
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE anketa
        SET l_name = ?, f_name = ?, m_name = ?, b_date = ?, awards = ?, address = ?, specialty = ?
        WHERE reg_num = ?
        ''', (l_name, f_name, m_name, b_date, awards, address, specialty, reg_num))

# Вывод данных
def display_all():
    with sqlite3.connect('abiturient.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM anketa
        ''')
        results = cursor.fetchall()
        for row in results:
            print(row)

# add('Сидоров', 'Алексей', 'Сергеевич',
#     '1995-06-12', 'Победитель олимпиады',
#     'ул. Пушкина, 10', 'Математика')

# delete(1)

# update(1, 'Иванов', 'Иван', 'Иванович',
#              '2000-01-01', 'Золотая медаль',
#              'ул. Ленина, 1', 'Информатика')

# display_all()
