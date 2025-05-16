import streamlit as st
import pandas as pd

# Настройка страницы
st.set_page_config(page_title='Музыкальная оценка', page_icon='🎵', layout='centered')

# Темное оформление через CSS
st.markdown("""
    <style>
    body {
        background-color: #000000;
        color: #e0e0e0;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput, .stSelectbox, .stButton, .stSlider {
        background-color: #1e1e1e;
        color: #e0e0e0;
        border-radius: 12px;
        border: 1px solid #444;
    }
    .stSlider > div > div {
        height: 14px;
        background-color: #6a0dad;
        border-radius: 8px;
    }
    .stButton > button {
        background-color: #6a0dad;
        color: #ffffff;
        border-radius: 12px;
    }
    .total-score {
        font-size: 70px;
        color: #ffd700;
        text-align: center;
        margin-top: 20px;
        font-weight: bold;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #ffd700;
        margin-bottom: 20px;
    }
    .track-title {
        font-size: 22px;
        color: #b0b0b0;
        margin-bottom: 10px;
    }
    .result-table {
        margin-top: 20px;
        border-radius: 8px;
        background-color: #1e1e1e;
        color: #e0e0e0;
    }
    .stMarkdown {
        background-color: #1e1e1e;
    }
    </style>
    """, unsafe_allow_html=True)

# Название приложения
st.markdown('<div class="title">🎵 Музыкальная оценка на тусовке</div>', unsafe_allow_html=True)

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
st.markdown('<div class="track-title">Выберите трек:</div>', unsafe_allow_html=True)
track = st.selectbox("", tracks)

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
        st.markdown('<div class="track-title">Все оценки:</div>', unsafe_allow_html=True)
        st.dataframe(df.style.set_properties(**{'background-color': '#1e1e1e', 'color': '#e0e0e0'}))
    except FileNotFoundError:
        st.warning("Результаты пока не сохранены.")
