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

# Отображение средней оценки внизу (без надписи "Средняя оценка")
average_score = round(sum(scores) / len(scores), 1)
st.markdown(f"<h2 style='text-align: center; font-size: 50px;'>{average_score}</h2>", unsafe_allow_html=True)

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
        grouped = df.groupby("Трек")["Средняя оценка"].mean().round(1).reset_index()
        
        st.write("### Результаты по трекам:")
        for track in grouped["Трек"].unique():
            st.write(f"**{track}**")
            filtered_df = df[df["Трек"] == track][["Имя", "Средняя оценка"]]
            st.dataframe(filtered_df)
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")
