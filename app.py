import streamlit as st
import pandas as pd

# Название приложения
st.title("Музыкальная оценка на тусовке")

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

# Кнопка "Сохранить оценку"
if st.button("Сохранить оценку"):
    average_score = round(sum(scores) / len(scores), 2)
    result = [name, track] + scores + [average_score]
    df = pd.DataFrame([result], columns=["Имя", "Трек"] + criteria + ["Средняя оценка"])
    df.to_csv("music_scores.csv", mode='a', header=False, index=False)
    st.success(f"Оценка сохранена! Средний балл: {average_score}")

# Кнопка "Посмотреть результаты"
if st.button("Посмотреть результаты"):
    try:
        df = pd.read_csv("music_scores.csv", names=["Имя", "Трек"] + criteria + ["Средняя оценка"])
        st.write("### Все оценки:")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")
