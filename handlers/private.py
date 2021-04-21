from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJc2Rgf4VDc3yFwhYxUoFgx8bYabZclQACfwgAAr-MkAQpURMT4hK2dh8E")
    await message.reply_text(
        f"""*Halo, nama aku {bn} 🎶

Saya dapat memutar musik di dalam voice chat group kamu. Saya diciptakan oleh [ms.vina](https://t.me/levinachannel).

Note: Silahkan gunakan bot ini dengan baik & bijak, Jika terjadi kendala silahkan hubungi [levina](https://t.me/dlwrml).
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 daftar dan penjelasan perintah", url="https://telegra.ph/command-04-21")
                  ],[
                    InlineKeyboardButton(
                        "📣 Group Support", url="https://t.me/gcsupportbots"
                    ),
                    InlineKeyboardButton(
                        "📣 Channel Support", url="https://t.me/levinachannel"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📣 Channel Support", url="https://t.me/levinachannel")
                ]
            ]
        )
   )


