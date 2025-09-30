#!/usr/bin/env python3
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton # pyright: ignore[reportMissingImports]
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes  # pyright: ignore[reportMissingImports]

with open('token.txt', 'r') as f:
    BOT_TOKEN = f.read().strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [KeyboardButton("Кнопка 1"), KeyboardButton("Кнопка 2")],
        [KeyboardButton("Кнопка 3")]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)

    await update.message.reply_text("Выберите кнопку:", reply_markup=keyboard)

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "Кнопка 1":
        await update.message.reply_text("Вы нажали кнопку 1! ✅")
    elif text == "Кнопка 2":
        await update.message.reply_text("Вы нажали кнопку 2! ✅")
    elif text == "Кнопка 3":
        await update.message.reply_text("Вы нажали кнопку 3! ✅")
    else:
        await update.message.reply_text("Используйте кнопки ниже 👇")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_buttons))

    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
