import streamlit as st
import pandas as pd
import os

# Название приложения
st.title("Ебать какое жюри")

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

# Проверка на дублирование оценки
def is_duplicate(name, track):
    if os.path.exists("music_scores.csv"):
        df = pd.read_csv("music_scores.csv")
        if not df[(df['Имя'] == name) & (df['Трек'] == track)].empty:
            return True
    return False

# Кнопка "Сохранить оценку"
if st.button("Сохранить оценку"):
    if is_duplicate(name, track):
        st.warning(f"Оценка для трека '{track}' от '{name}' уже существует!")
    else:
        result = [name, track] + scores + [average_score]
        df = pd.DataFrame([result], columns=["Имя", "Трек"] + criteria + ["Средняя оценка"])
        df.to_csv("music_scores.csv", mode='a', header=not os.path.isfile("music_scores.csv"), index=False)
        st.success(f"Оценка сохранена!")

# Кнопка "Посмотреть результаты"
if st.button("Посмотреть результаты"):
    try:
        df = pd.read_csv("music_scores.csv")
        st.write("### Все оценки:")
        for trk in df['Трек'].unique():
            st.write(f"#### Трек: {trk}")
            filtered_df = df[df['Трек'] == trk][["Имя", "Средняя оценка"]]
            st.dataframe(filtered_df.reset_index(drop=True))
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")

# Кнопка "Топ 10 треков на основе всех оценок"
if st.button("Топ 10 треков на основе всех оценок"):
    try:
        df = pd.read_csv("music_scores.csv")
        track_scores = df.groupby("Трек")["Средняя оценка"].sum().reset_index()
        top_tracks = track_scores.sort_values("Средняя оценка", ascending=False).head(10)
        st.write("### Топ 10 треков по сумме всех оценок:")
        st.dataframe(top_tracks.reset_index(drop=True))
    except FileNotFoundError:
        st.warning("Нет данных для отображения.")

# Кнопка и выбор участника для топ-10 треков
st.write("### Топ 10 треков участника")
try:
    df = pd.read_csv("music_scores.csv")
    names = df['Имя'].unique().tolist()

    # Появляется выбор участника из списка
    selected_name = st.selectbox("Выберите участника:", [""] + names)

    if selected_name:
        user_tracks = df[df['Имя'] == selected_name][["Трек", "Средняя оценка"]]
        top_user_tracks = user_tracks.sort_values("Средняя оценка", ascending=False).head(10)
        st.write(f"### Топ 10 треков участника {selected_name}:")
        st.dataframe(top_user_tracks.reset_index(drop=True))
except FileNotFoundError:
    st.warning("Нет данных для отображения.")

# Функция для обнуления данных
def reset_results():
    if os.path.exists("music_scores.csv"):
        os.remove("music_scores.csv")
        st.success("Все результаты успешно обнулены!")
    else:
        st.warning("Нет данных для обнуления.")

# Галочка подтверждения рядом с кнопкой
st.write("### Обнулить все результаты")
confirm_reset = st.checkbox("Подтверждаю обнуление данных")
st.button("Обнулить результаты", on_click=reset_results, disabled=not confirm_reset)
