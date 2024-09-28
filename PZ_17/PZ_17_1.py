import tkinter as tk
from tkinter import ttk

# Функция, вызываемая при нажатии кнопки "Отправить информацию"
def submit_form():
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    age = entry_age.get().strip()

    # Проверка обязательных полей
    if not name or not email or not age:
        print("Заполните обязательные поля!")
        return

    phone = entry_phone.get()
    gender = gender_var.get()
    qualities = entry_qualities.get("1.0", tk.END).strip()
    favorite_animals = [animal for animal, var in animal_vars.items() if var.get()]

    # Вывод введенной информации в консоль
    print(f"Имя: {name}")
    print(f"Телефон: {phone}")
    print(f"Email: {email}")
    print(f"Возраст: {age}")
    print(f"Пол: {gender}")
    print(f"Личные качества: {qualities}")
    print(f"Любимые животные: {favorite_animals}")


# Инициализация главного окна
root = tk.Tk()
root.title("Форма заявки на работу в зоопарке")
root.geometry("450x410")  # Задание фиксированного размера окна

# Контактная информация
frame_contact_info = tk.LabelFrame(root, text="Контактная информация", width=380)
frame_contact_info.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

tk.Label(frame_contact_info, text="Имя*").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_contact_info, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame_contact_info, text="Телефон").grid(row=1, column=0, sticky="w")
entry_phone = tk.Entry(frame_contact_info, width=30)
entry_phone.grid(row=1, column=1)

tk.Label(frame_contact_info, text="Email*").grid(row=2, column=0, sticky="w")
entry_email = tk.Entry(frame_contact_info, width=30)
entry_email.grid(row=2, column=1)

# Персональная информация
frame_personal_info = tk.LabelFrame(root, text="Персональная информация", width=380)
frame_personal_info.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

tk.Label(frame_personal_info, text="Возраст*").grid(row=0, column=0, sticky="w")
entry_age = tk.Entry(frame_personal_info, width=30)
entry_age.grid(row=0, column=1)

tk.Label(frame_personal_info, text="Пол").grid(row=1, column=0, sticky="w")
gender_var = tk.StringVar(value="Женщина")
gender_dropdown = ttk.Combobox(frame_personal_info, textvariable=gender_var, width=27)
gender_dropdown['values'] = ("Женщина", "Мужчина")
gender_dropdown.grid(row=1, column=1)

tk.Label(frame_personal_info, text="Перечислите личные качества").grid(row=2, column=0, sticky="nw")
entry_qualities = tk.Text(frame_personal_info, width=30, height=5)
entry_qualities.grid(row=2, column=1)

# Любимые животные
frame_favorite_animals = tk.LabelFrame(root, text="Выберите ваших любимых животных", width=380)
frame_favorite_animals.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Создание флажков для выбора любимых животных
animal_vars = {
    "Зебра": tk.BooleanVar(),
    "Слон": tk.BooleanVar(),
    "Кошка": tk.BooleanVar(),
    "Антилопа": tk.BooleanVar(),
    "Анаконда": tk.BooleanVar(),
    "Голубь": tk.BooleanVar(),
    "Человек": tk.BooleanVar(),
    "Краб": tk.BooleanVar()
}

for i, (animal, var) in enumerate(animal_vars.items()):
    tk.Checkbutton(frame_favorite_animals, text=animal, variable=var).grid(row=i // 4, column=i % 4, sticky="w")

# Кнопка отправки информации
submit_button = tk.Button(root, text="Отправить информацию", command=submit_form)
submit_button.grid(row=3, column=0, pady=10)

# Настройка столбцов для одинаковой ширины
root.grid_columnconfigure(0, weight=1)
frame_contact_info.grid_columnconfigure(0, weight=1)
frame_contact_info.grid_columnconfigure(1, weight=1)
frame_personal_info.grid_columnconfigure(0, weight=1)
frame_personal_info.grid_columnconfigure(1, weight=1)
frame_favorite_animals.grid_columnconfigure(0, weight=1)
frame_favorite_animals.grid_columnconfigure(1, weight=1)
frame_favorite_animals.grid_columnconfigure(2, weight=1)
frame_favorite_animals.grid_columnconfigure(3, weight=1)

# Запуск приложения
root.mainloop()
