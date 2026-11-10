import tkinter as tk
import random


def generate_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    blocks = []

    for i in range(3): # создаём три блока ключа
        symbols = []

        # в каждом блоке ровно три буквы и две цифры
        for j in range(3):
            symbols.append(random.choice(letters)) # один случайный эл
        for j in range(2):
            symbols.append(random.choice(digits))
        # ["F", "X", "N", "2", "6"]

        random.shuffle(symbols) # перемешивает элементы списка symbols в случайном порядке
        block = "".join(symbols)
        blocks.append(block)

    return "-".join(blocks)


def show_key():
    key = generate_key()
    entry_key.delete(0, tk.END) # очищает поле entry_key от предыдущего ключа
    entry_key.insert(0, key) # вставляет новый ключ в поле, начиная с позиции 0
    status.config(text="Ключ готов") # меняет текст надписи status на «Ключ готов» 



def main(a, b=1):
    global window, entry_key, status

    window = tk.Tk() # Создаёт главное окно приложения и сохраняет ссылку на него в window
    window.title("Chicken gun/генератор ключей")
    window.geometry("800x445")
    window.resizable(False, False) # Запрещает пользователю изменять ширину и высоту окна. Поэтому расположение элементов и фона остаётся фиксированным

    background = tk.PhotoImage(file="ch.png") # загружает картинку из файла и сохраняет объект изображения
    background_label = tk.Label(window, image=background) # создаёт элемент для отображения изображения
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # размещает элемент с фоновой картинкой на всю площадь окна

    panel = tk.Frame(window, bg="#213326", padx=25, pady=20) # Frame контейнер для других элементов. На этой панели размещаются надписи, поле ключа и кнопки
    panel.place(relx=0.5, rely=0.5, anchor="center") # располагаем по центру

    title = tk.Label(panel, text="CHICKEN GUN", font=("Arial", 24, "bold"), bg="#29683B", fg="#a8d879") # создаёт элемент для отображения текста
    title.pack(pady=5) # Размещает надпись в панели и добавляет внешние вертикальные отступы по 5 пикселей
    rule = tk.Label(panel, text="В каждом блоке: 3 буквы A–Z и 2 цифры 0–9", font=("Arial", 11), bg="#213326", fg="white")
    rule.pack(pady=5) # pack() размещает надпись внутри этого контейнера (panel)

    entry_key = tk.Entry(panel, font=("Consolas", 24), width=19, justify="center") # tk.Entry создаёт однострочное текстовое поле
    entry_key.pack(pady=10) # pady=10 добавляет внешний отступ сверху и снизу поля по 10 пикселей

    generate_button = tk.Button(panel, text="Сгенерировать", command= lambda x: show_key(x), font=("Arial", 13), bg="#a8d879") # создаёт кнопку в интерфейсе/ command=show_key — функция, которая вызывается при нажатии
    generate_button.pack(fill="x", pady=5) # Размещает кнопку и растягивает её по доступной ширине панели


    status = tk.Label(panel, text="Учебный ключ", font=("Arial", 10), bg="#213326", fg="white")
    status.pack(pady=5)
    window.mainloop()

if __name__ == "__main__":
    main()
