import streamlit as st
from PIL import Image
import base64
import time

# Настройка страницы
st.set_page_config(
    page_title="Для самой лучшей Риты ❤️ (по дружески) )))",
    page_icon="❤️",
    layout="centered"
)

# Стили CSS для красоты
st.markdown("""
<style>
    /* Фон с повторяющимся узором сердец */
    .stApp {
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120' viewBox='0 0 120 120'%3E%3Cpath fill='%23e7548020' d='M60,20 C75,5 95,10 95,30 C95,45 75,60 60,75 C45,60 25,45 25,30 C25,10 45,5 60,20 Z'/%3E%3C/svg%3E");
        background-size: 120px;
        background-repeat: repeat;
        background-color: #fff9fb;
    }

    .title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        text-align: center;
        color: #e75480;
        font-size: 2.8em;
        margin-top: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .message {
        font-family: 'Georgia', serif;
        font-size: 1.4em;
        line-height: 1.6;
        color: #5a1846;
        text-align: center;
        padding: 25px;
        background: rgba(255, 255, 255, 0.85);
        border-radius: 20px;
        box-shadow: 0 6px 20px rgba(231, 84, 128, 0.3);
        margin: 25px auto;
        max-width: 620px;
        backdrop-filter: blur(2px);
    }
    .heart {
        animation: beat 1.2s infinite;
        display: inline-block;
        font-size: 2em;
        color: #e75480;
    }
    @keyframes beat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .footer {
        text-align: center;
        margin-top: 40px;
        color: #9c27b0;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# Заголовок с анимированными сердечками
st.markdown('<div class="title">💌 Для Риты, с любовью 💖</div>', unsafe_allow_html=True)

# Основное сообщение
message = """
Дорогая Рита! 💕
Ты — как солнечный луч в самый пасмурный день и уютное тепло в самый холодный вечер.
Твоя улыбка делает мир ярче, а твоя доброта — мягче и добрее.
Пусть этот День святого Валентина напомнит тебе,
как ты обожаема — не только мной, но всеми, кто тебя знает!
И знай: ты важна, ценна и любима — не только сегодня, а каждый день! 🌸

С Днём Святого Валентина! 🌹 Бэсти
"""

st.markdown(f'<div class="message">{message}</div>', unsafe_allow_html=True)

# Анимированные сердечки
cols = st.columns(7)
hearts = ["❤️", "💖", "💗", "💓", "💕", "💘", "💝"]
for i, col in enumerate(cols):
    with col:
        st.markdown(f'<div class="heart">{hearts[i]}</div>', unsafe_allow_html=True)

# Интерактивная кнопка "Получить поцелуй"
if st.button("💋 Нажми, чтобы получить поцелуй в лобик"):
    st.balloons()
    st.success("💋 Поцелуй отправлен! Он уже летит к тебе...")

# Подпись
st.markdown('<div class="footer">Сделано с теплом и заботой • 14 февраля 2026</div>', unsafe_allow_html=True)