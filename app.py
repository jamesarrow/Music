import streamlit as st
import pandas as pd
import os

# Название приложения
st.title("Музыкальная оценка на тусовке")

# Список треков
tracks = [
    "Австралия", "Азербайджан", "Бельгия", "Грузия", "Ирландия", "Кипр", "Сербия", "Словения",
    "Хорватия", "Чехия", "Черногория", "Норвегия", "Люксембург", "Эстония", "Израиль", 
    "Литва", "Испания", "Украина", "Великобритания", "Австрия", "Исландия", "Латвия", 
    "Нидерланды", "Финляндия", "Италия", "Польша", "Германия", "Греция", "Армения", 
    "Швейцария", "Мальта", "Португалия", "Дания", "Швеция", "Франция", "Сан-Марино", "Албания"
]

# Ввод имени и выбор трека
name = st.text_input("Введите имя:")
track = st.selectbox("Выберите трек:", tracks)

# Критерии оценки
criteria = ["Вокал", "Стилевость", "Костюмы", "Оформление сцены", "Харизма", "Номер", "Общее впечатление"]
scores = [st.slider(crit, 1, 10, 5) for crit in criteria]

# Средняя оценка
average_score = round(sum(scores) / len(scores), 1)
st.markdown(f"### Итоговая оценка: {average_score}")

# Кнопка "Сохранить оценку"
if st.button("Сохранить оценку"):
    result = [name, track] + scores + [average_score]
    df = pd.DataFrame([result], columns=["Имя", "Трек"] + criteria + ["Средняя оценка"])
    df.to_csv("music_scores.csv", mode='a', header=not os.path.isfile("music_scores.csv"), index=False)
    st.success(f"Оценка сохранена!")

# Кнопка "Посмотреть результаты"
if st.button("Посмотреть результаты"):
    try:
        df = pd.read_csv("music_scores.csv")
        for trk in df['Трек'].unique():
            st.write(f"### Трек: {trk}")
            st.dataframe(df[df['Трек'] == trk][["Имя", "Средняя оценка"]])
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")

# Подтверждающий чекбокс перед обнулением
confirm_reset = st.checkbox("Подтверждаю обнуление результатов")

# Кнопка "Обнулить результаты" активна только при подтверждении
if st.button("Обнулить результаты") and confirm_reset:
    if os.path.exists("music_scores.csv"):
        os.remove("music_scores.csv")
        st.success("Результаты успешно обнулены!")
    else:
        st.warning("Нет данных для обнуления.")
elif st.button("Обнулить результаты"):
    st.warning("Подтвердите обнуление, установив галочку.")
