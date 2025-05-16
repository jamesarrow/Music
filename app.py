import streamlit as st
import pandas as pd

# Темная тема оформления
st.set_page_config(page_title='Музыкальная оценка', page_icon='🎵', layout='centered')
st.markdown("""
    <style>
    body {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .stTextInput, .stSelectbox, .stButton, .stSlider {
        background-color: #333;
        color: #ffffff;
        border-radius: 8px;
    }
    .stSlider > div > div {
        height: 8px;
        background-color: #6a0dad;
    }
    .stButton > button {
        background-color: #6a0dad;
        color: #ffffff;
        border-radius: 12px;
    }
    .total-score {
        font-size: 50px;
        color: #ffd700;
        text-align: center;
        margin-top: 20px;
    }
    .result-table {
        margin-top: 20px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Название приложения
st.title("🎵 Музыкальная оценка на тусовке")

# Ввод имени
name = st.text_input("Введите имя:")

# Список треков
tracks = [
    "Австралия - Милкшейкмэн", "Азербайджан - Солист Илюха в коже",
    "Бельгия - Красный Себастьян", "Грузия - Шансон и белые флаги",
    "Ирландия - Песня про Лайку", "Кипр - Парень на строительных лесах",
    "Сербия - Мужик с хвостом про Милу", "Словения - Про жену и рак",
    "Хорватия - Вунш-пунш", "Чехия - Кис-кис"
]
track = st.selectbox("Выберите трек:", tracks)

# Критерии оценки
criteria = ["Вокал", "Стилевость", "Костюмы", "Оформление сцены", "Харизма", "Номер", "Общее впечатление"]
scores = {}

for criterion in criteria:
    score = st.slider(criterion, 1, 10, 5, key=criterion)
    scores[criterion] = score

# Подсчет средней оценки
average_score = round(sum(scores.values()) / len(scores), 2)
st.markdown(f'<div class="total-score">Средний балл: {average_score}</div>', unsafe_allow_html=True)

# Сохранение данных в CSV
if st.button("Сохранить оценку"):
    result = {"Имя": name, "Трек": track, **scores, "Средняя оценка": average_score}
    df = pd.DataFrame([result])
    df.to_csv("music_scores.csv", mode='a', header=False, index=False)
    st.success("Оценка сохранена!")

# Кнопка для просмотра всех результатов
if st.button("Посмотреть результаты"):
    try:
        df = pd.read_csv("music_scores.csv", names=["Имя", "Трек"] + criteria + ["Средняя оценка"])
        st.write(df)
    except FileNotFoundError:
        st.warning("Результаты пока не сохранены.")
