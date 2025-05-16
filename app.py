import streamlit as st
import pandas as pd
import os

# Название приложения
st.title("Ебать какие жюри")

# Список треков
tracks = [
    "Австралия - Милкшейкмэн", "Азербайджан - Солист Илюха в коже",
    "Бельгия - Красный Себастьян", "Грузия - Шансон и белые флаги",
    "Ирландия - Песня про Лайку", "Кипр - Парень на строительных лесах",
    "Сербия - Мужик с хвостом про Милу", "Словения - Про жену и рак",
    "Хорватия - Вунш-пунш", "Чехия - Кис-кис"
]

# Ввод имени и выбор трека
name = st.text_input("Введите имя:")
track = st.selectbox("Выберите трек:", tracks)

# Критерии оценки
criteria = ["Вокал", "Стилевость", "Костюмы", "Оформление сцены", "Харизма", "Номер", "Общее впечатление"]
scores = [st.slider(crit, 1, 10, 5) for crit in criteria]

# Автоматический подсчет средней оценки
average_score = round(sum(scores) / len(scores), 1)
st.markdown(f"## {average_score}")

# Кнопка "Сохранить оценку"
if st.button("Сохранить оценку"):
    result = [name, track] + scores + [average_score]
    df = pd.DataFrame([result], columns=["Имя", "Трек"] + criteria + ["Средняя оценка"])
    df.to_csv("music_scores.csv", mode='a', header=False, index=False)
    st.success(f"Оценка сохранена!")

# Кнопка "Посмотреть результаты"
if st.button("Посмотреть результаты"):
    try:
        df = pd.read_csv("music_scores.csv", names=["Имя", "Трек"] + criteria + ["Средняя оценка"])
        st.write("### Все оценки:")
        results = df.groupby("Трек")["Средняя оценка"].mean().reset_index()
        st.dataframe(results)
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")

# Кнопка "Обнулить результаты"
if st.button("Обнулить результаты"):
    if os.path.exists("music_scores.csv"):
        os.remove("music_scores.csv")
        st.success("Все результаты успешно обнулены!")
    else:
        st.warning("Файл с результатами не найден.")
