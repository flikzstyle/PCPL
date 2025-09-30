#!/usr/bin/env python3
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

START, MENU, CALCULATOR, CONVERTER = range(4)

# Команда /start - начальное состояние
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Добро пожаловать! Я бот с конечным автоматом.\n"
        "Вы в начальном состоянии. Переходим в главное меню..."
    )
    return await main_menu(update, context)

async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🧮 Калькулятор"), KeyboardButton("🔄 Конвертер валют")],
        [KeyboardButton("❌ Выход")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🏠 Главное меню:\n"
        "Выберите режим работы:",
        reply_markup=reply_markup
    )
    return MENU

async def handle_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🧮 Калькулятор":
        return await calculator_mode(update, context)
    elif text == "🔄 Конвертер валют":
        return await converter_mode(update, context)
    elif text == "❌ Выход":
        return await cancel(update, context)
    else:
        await update.message.reply_text("Пожалуйста, используйте кнопки")
        return MENU

async def calculator_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("1"), KeyboardButton("2"), KeyboardButton("3"), KeyboardButton("+")],
        [KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6"), KeyboardButton("-")],
        [KeyboardButton("7"), KeyboardButton("8"), KeyboardButton("9"), KeyboardButton("*")],
        [KeyboardButton("0"), KeyboardButton("="), KeyboardButton("C"), KeyboardButton("/")],
        [KeyboardButton("🔙 Назад")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    context.user_data['calc_expression'] = ""

    await update.message.reply_text(
        "🧮 Режим калькулятора\n"
        "Введите выражение или используйте кнопки\n"
        f"Текущее: {context.user_data['calc_expression']}",
        reply_markup=reply_markup
    )
    return CALCULATOR

async def handle_calculator(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    expression = context.user_data.get('calc_expression', "")

    if text == "🔙 Назад":
        return await main_menu(update, context)
    elif text == "C":
        context.user_data['calc_expression'] = ""
        expression = ""
    elif text == "=":
        try:
            result = eval(expression)
            await update.message.reply_text(f"✅ Результат: {expression} = {result}")
            context.user_data['calc_expression'] = str(result)
            expression = str(result)
        except:
            await update.message.reply_text("❌ Ошибка в выражении!")
            context.user_data['calc_expression'] = ""
            expression = ""
    elif text in ["/","+", "-", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        context.user_data['calc_expression'] += text
        expression += text
    else:
        await update.message.reply_text("Используйте кнопки калькулятора")
        return CALCULATOR

    keyboard = [
        [KeyboardButton("1"), KeyboardButton("2"), KeyboardButton("3"), KeyboardButton("+")],
        [KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6"), KeyboardButton("-")],
        [KeyboardButton("7"), KeyboardButton("8"), KeyboardButton("9"), KeyboardButton("*")],
        [KeyboardButton("0"), KeyboardButton("="), KeyboardButton("C"), KeyboardButton("/")],
        [KeyboardButton("🔙 Назад")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        f"Текущее выражение: {expression}",
        reply_markup=reply_markup
    )
    return CALCULATOR

async def converter_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("USD → RUB"), KeyboardButton("EUR → RUB")],
        [KeyboardButton("RUB → USD"), KeyboardButton("RUB → EUR")],
        [KeyboardButton("🔙 Назад")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "🔄 Режим конвертера валют\n"
        "Выберите направление конвертации:\n"
        "💵 Курсы: USD = 82 RUB, EUR = 96 RUB",
        reply_markup=reply_markup
    )
    return CONVERTER

async def handle_converter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🔙 Назад":
        return await main_menu(update, context)

    rates = {'USD': 82, 'EUR': 96}

    if text == "USD → RUB":
        context.user_data['conversion'] = 'usd_rub'
        await update.message.reply_text("💵 Введите сумму в USD:")
        return CONVERTER
    elif text == "EUR → RUB":
        context.user_data['conversion'] = 'eur_rub'
        await update.message.reply_text("💶 Введите сумму в EUR:")
        return CONVERTER
    elif text == "RUB → USD":
        context.user_data['conversion'] = 'rub_usd'
        await update.message.reply_text("₽ Введите сумму в RUB:")
        return CONVERTER
    elif text == "RUB → EUR":
        context.user_data['conversion'] = 'rub_eur'
        await update.message.reply_text("₽ Введите сумму в RUB:")
        return CONVERTER
    else:

        try:
            amount = float(text)
            conversion = context.user_data.get('conversion', '')

            if conversion == 'usd_rub':
                result = amount * rates['USD']
                await update.message.reply_text(f"💵 ${amount} = {result:.2f} ₽")
            elif conversion == 'eur_rub':
                result = amount * rates['EUR']
                await update.message.reply_text(f"💶 €{amount} = {result:.2f} ₽")
            elif conversion == 'rub_usd':
                result = amount / rates['USD']
                await update.message.reply_text(f"₽ {amount} = ${result:.2f}")
            elif conversion == 'rub_eur':
                result = amount / rates['EUR']
                await update.message.reply_text(f"₽ {amount} = €{result:.2f}")
            else:
                await update.message.reply_text("Сначала выберите направление конвертации")

            return await converter_mode(update, context)

        except ValueError:
            await update.message.reply_text("Пожалуйста, введите число")
            return CONVERTER

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 До свидания! Чтобы начать снова, отправьте /start",
        reply_markup=ReplyKeyboardMarkup([[]], resize_keyboard=True)
    )
    return ConversationHandler.END

def main():

    BOT_TOKEN = "8191456089:AAFD_4h2BG_EO21P_N1IUcnTV80vMbQLhW4"

    app = Application.builder().token(BOT_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            START: [MessageHandler(filters.TEXT, start)],
            MENU: [MessageHandler(filters.TEXT, handle_menu)],
            CALCULATOR: [MessageHandler(filters.TEXT, handle_calculator)],
            CONVERTER: [MessageHandler(filters.TEXT, handle_converter)],
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    app.add_handler(conv_handler)

    print("🤖 Бот с конечным автоматом запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
