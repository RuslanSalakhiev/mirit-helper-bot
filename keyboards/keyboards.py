from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import emoji


def navigation_buttons(previous_step):
    buttons = [
        InlineKeyboardButton(text=emoji.emojize(":right_arrow_curving_up:") + " В меню",
                             callback_data='navi_main_menu'),
        InlineKeyboardButton(text=emoji.emojize(":left_arrow:") + " Назад",
                             callback_data='navi_' + previous_step),
    ]
    return buttons


def navigation_only_keyboard(previous_step):
    buttons = [
        InlineKeyboardButton(text=emoji.emojize(":right_arrow_curving_up:") + " В меню",
                             callback_data='navi_main_menu'),
        InlineKeyboardButton(text=emoji.emojize(":left_arrow:") + " Назад",
                             callback_data='navi_' + previous_step),
    ]
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*buttons)
    return keyboard


def main_menu_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=emoji.emojize(":police_car_light:") + " Конвертер", callback_data="converter"),
    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard


def converter_keyboard(previous_step, selected_amount, selected_currency) -> InlineKeyboardMarkup:
    buttons = [
        InlineKeyboardButton(text=f"{emoji.emojize(':right_arrow_curving_up:')} USD",
                             callback_data='amount_USD'),
        InlineKeyboardButton(text=f"{emoji.emojize(':right_arrow_curving_up:')} EUR",
                             callback_data='amount_EUR'),
        InlineKeyboardButton(text=f"{emoji.emojize(':right_arrow_curving_up:')} GEL",
                             callback_data='amount_GEL'),
        InlineKeyboardButton(text=f"{emoji.emojize(':right_arrow_curving_up:')} TRY",
                             callback_data='amount_TRY'),
        InlineKeyboardButton(text=emoji.emojize(":right_arrow_curving_up:") + " В меню",
                             callback_data='navi_main_menu'),
        InlineKeyboardButton(text=emoji.emojize(":left_arrow:") + " Назад",
                             callback_data='navi_' + previous_step),

    ]
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    return keyboard