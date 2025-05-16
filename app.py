import streamlit as st
import pandas as pd

tracks = [
    "Австралия - Милкшейкмэн", "Азербайджан - Солист Илюха в коже",
    "Бельгия - Красный Себастьян", "Грузия - Шансон и белые флаги",
    "Ирландия - Песня про Лайку", "Кипр - Парень на строительных лесах",
    "Сербия - Мужик с хвостом про Милу", "Словения - Про жену и рак",
    "Хорватия - Вунш-пунш", "Чехия - Кис-кис"
]

st.title("Музыкальная оценка на тусовке")

name = st.text_input("Введите имя:")
track = st.selectbox("Выберите трек:", tracks)

criteria = ["Вокал", "Стилевость", "Костюмы", "Оформление сцены", "Харизма", "Номер", "Общее впечатление"]
scores = [st.slider(crit, 1, 10, 5) for crit in criteria]

if st.button("Сохранить оценку"):
    average_score = round(sum(scores) / len(scores), 2)
    df = pd.DataFrame([[name, track, average_score]], columns=["Name", "Track", "Average Score"])
    df.to_csv("music_scores.csv", mode='a', header=False, index=False)
    st.success(f"Оценка сохранена! Средний балл: {average_score}")

if st.button("Показать результаты"):
    try:
        df = pd.read_csv("music_scores.csv", names=["Name", "Track", "Average Score"])
        st.write(df)
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")
