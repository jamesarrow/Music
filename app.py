import streamlit as st
import pandas as pd

# Название приложения
st.markdown(
    """
    <style>
    .main {
        background-color: #1c1c1c;
        color: #ffffff;
    }
    .stSlider > div {
        background-color: #2e2e2e;
        border-radius: 5px;
    }
    .stSlider > div > div {
        color: #ffffff;
    }
    .stNumberInput input {
        background-color: #2e2e2e;
        color: #ffffff;
    }
    .score-display {
        font-size: 50px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
    }
    .track-display {
        font-size: 20px;
        color: #a1a1a1;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎵 Музыкальная оценка на тусовке")

name = st.text_input("Введите имя:")

# Треки для выбора
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
scores = [st.slider(crit, 1, 10, 5, key=crit) for crit in criteria]

# Автоматический подсчет оценки
average_score = round(sum(scores) / len(scores), 2)

# Отображение трека и средней оценки
st.markdown(f"<div class='track-display'>Трек: {track}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='score-display'>Средний балл: {average_score}</div>", unsafe_allow_html=True)

# Сохранение данных
if name:
    df = pd.DataFrame([[name, track, average_score]], columns=["Name", "Track", "Average Score"])
    df.to_csv("music_scores.csv", mode='a', header=False, index=False)
    st.success("Оценка сохранена!")
