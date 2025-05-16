import streamlit as st
import pandas as pd

# Стилизация через CSS
st.markdown(
    """
    <style>
    .slider {{
        background-color: #222;
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }}
    .title {{
        font-size: 30px;
        color: #fff;
        margin-bottom: 20px;
    }}
    .track-title {{
        background-color: #333;
        padding: 15px;
        border-radius: 10px;
        color: #fff;
        margin-bottom: 15px;
    }}
    .total-score {{
        font-size: 60px;
        font-weight: bold;
        color: #fff;
        text-align: center;
    }}
    .track-info {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    .icon {{
        font-size: 40px;
        color: #fff;
    }}
    .button {{
        background-color: #555;
        color: #fff;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
        text-align: center;
        cursor: pointer;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Заголовок приложения
st.markdown('<div class="title">🎵 Музыкальная оценка на тусовке</div>', unsafe_allow_html=True)

# Ввод имени
name = st.text_input("Введите имя:")

# Список треков
tracks = [
    "Австралия - Милкшейкмэн", "Азербайджан - Солист Илюха в коже", "Бельгия - Красный Себастьян",
    "Грузия - Шансон и белые флаги", "Ирландия - Песня про Лайку", "Кипр - Парень на строительных лесах",
    "Сербия - Мужик с хвостом про Милу", "Словения - Про жену и рак", "Хорватия - Вунш-пунш",
    "Чехия - Кис-кис", "Черногория - Костюм ватного диска", "Норвегия - Чувак в доспехах"
]

# Выбор трека
track = st.selectbox("Выберите трек:", tracks)

# Критерии оценки
criteria = ["Вокал", "Стилевость", "Костюмы", "Оформление сцены", "Харизма", "Номер", "Общее впечатление"]
scores = {}

# Слайдеры для оценок
for criterion in criteria:
    score = st.slider(criterion, 1, 10, 5, key=criterion)
    scores[criterion] = score

# Подсчет среднего балла
average_score = sum(scores.values()) / len(scores)
st.markdown(f'<div class="total-score">Итог: {round(average_score, 1)}</div>', unsafe_allow_html=True)

# Сохранение результата
if st.button("Сохранить оценку"):
    result = {"Имя": name, "Трек": track, **scores, "Средняя оценка": round(average_score, 1)}
    df = pd.DataFrame([result])
    df.to_csv("results.csv", mode="a", header=False, index=False)
    st.success("Оценка сохранена!")
