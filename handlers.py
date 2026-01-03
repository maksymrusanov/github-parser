from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
from parser import take_info


class Reg(StatesGroup):
    language = State()


@router.message(CommandStart())
async def test(message: Message):
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="Yes", callback_data="Yes"),
        InlineKeyboardButton(text="No", callback_data="No"),
    )
    keyboard.adjust(2)

    await message.answer(
        "Do you want to specify programming language?",
        reply_markup=keyboard.as_markup(),
    )


@router.callback_query(F.data == "Yes")
async def ask_language(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Reg.language)
    await callback.message.answer("Enter your language:")


@router.message(Reg.language)
async def set_language(message: Message, state: FSMContext):
    await state.update_data(language=message.text)
    data = await state.get_data()

    repos = take_info(data["language"])
    for i in repos:
        await message.answer(
            f"Owner: {i['owner']}\n"
            f"Repo: {i['repo']}\n"
            f"Link: {i['url']}\n"
            f"Language: {i['language']}\n"
            f"Desc: {i['desc']}"
        )

    await state.clear()


@router.callback_query(F.data == "No")
async def all_repos(callback: CallbackQuery):
    await callback.answer()

    repos = take_info()
    for i in repos:
        await callback.message.answer(
            f"Owner: {i['owner']}\n"
            f"Repo: {i['repo']}\n"
            f"Link: {i['url']}\n"
            f"Language: {i['language']}\n"
            f"Desc: {i['desc']}"
        )
