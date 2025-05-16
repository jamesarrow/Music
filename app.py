import streamlit as st
import pandas as pd
import os

# Название приложения
st.title("Ебать какое жюри")

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
st.markdown(f"## Средняя оценка: {average_score}")

# Кнопка "Сохранить оценку"
if st.button("Сохранить оценку"):
    if name:  # Проверяем, что имя введено
        result = [name, track] + scores + [average_score]
        df = pd.DataFrame([result], columns=["Имя", "Трек"] + criteria + ["Средняя оценка"])
        df.to_csv("music_scores.csv", mode='a', header=not os.path.isfile("music_scores.csv"), index=False)
        st.success(f"Оценка сохранена! Спасибо, {name}!")
    else:
        st.error("Введите имя перед сохранением!")

# Кнопка "Посмотреть результаты"
if st.button("Посмотреть результаты"):
    try:
        df = pd.read_csv("music_scores.csv")
        st.write("### Все оценки:")
        for track_name in df['Трек'].unique():
            st.write(f"#### Трек: {track_name}")
            filtered_df = df[df['Трек'] == track_name][["Имя", "Средняя оценка"]]
            # Убираем левую колонку с индексами
            st.dataframe(filtered_df.reset_index(drop=True))
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")

# Кнопка "Обнулить результаты"
if st.button("Обнулить результаты"):
    if os.path.exists("music_scores.csv"):
        os.remove("music_scores.csv")
        st.success("Все результаты успешно обнулены!")
    else:
        st.warning("Файл с результатами не найден.")
