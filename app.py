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

# Обновленные критерии
criteria = [
    "Живой Вокал", "Стиль/Трендовость", "Костюмы", 
    "Оформление сцены", "Харизма", "Номер", "Общее впечатление"
]

# Ввод имени и выбор трека
name = st.text_input("Введите имя:")
track = st.selectbox("Выберите трек:", tracks)

# Критерии оценки
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

# Кнопка "Топ 10 треков"
if st.button("Топ 10 треков на основе всех оценок"):
    try:
        df = pd.read_csv("music_scores.csv")
        track_scores = df.groupby("Трек")["Средняя оценка"].sum().reset_index()
        top_tracks = track_scores.sort_values("Средняя оценка", ascending=False).head(10)
        st.write("### Топ 10 треков по сумме всех оценок:")
        st.dataframe(top_tracks)
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")

# Подтверждающее окно при нажатии на "Обнулить результаты"
if st.button("Обнулить результаты"):
    if st.checkbox("Подтвердите обнуление данных"):
        try:
            open("music_scores.csv", "w").close()
            st.success("Все результаты обнулены!")
        except FileNotFoundError:
            st.warning("Нет данных для обнуления.")
