# Copyright ©️ 2022 Sanila Ranatunga. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [feedback-bot] (https://github.com/sanila2007/feedback-bot)

# Read GNU General Public License v3.0: https://github.com/sanila2007/feedback-bot/blob/mai/LICENSE
# Don't forget to follow github.com/sanila2007 because I'm doing these things for free and open source
# Star and fork and enjoy!


from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ForceReply, InputMediaPhoto

from helper import buttons, messages
from plugins import date_info, ratings, quotes_text
from Captcha import captcha_buttons, captcha_text
from pyrogram import Client, filters
from config import Config
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

bot = Client(
    "bot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)


@bot.on_inline_query()
def inlinequery(client, inline_query):
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Telegraph Uploader Bot",
                description="A telegram bot which can upload media such as images, videos & animations to the telegra.ph",
                thumb_url="https://telegra.ph/file/8edc5c1131bcc8a691a3c.jpg",
                input_message_content=InputTextMessageContent(
                    "**Telegraph Uploader**\n\nA telegram bot which can upload media such as images, videos & animations to the telegra.ph"
                ),
                url="https://t.me/telegraph200_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.ne/telegraph200_bot")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Feedback Bot",
                thumb_url="https://telegra.ph/file/e997ee0ea8bc354e77d3d.jpg",
                description="Multi functional bot that can give & collect feedbacks from users and broadcast replies to them with cool functions such as rating bots, completing captchas & etc...",
                input_message_content=InputTextMessageContent(
                    "**Feedback Bot**\n\nMulti functional bot that can give & collect feedbacks from users and broadcast replies to them with cool functions such as rating bots, completing captchas & etc...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/sanilaassistant_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/sanilaassistant_bot")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Song Downloader Bot",
                thumb_url="https://telegra.ph/file/79f269c5db774fb4e732d.jpg",
                description="One of the most powerful song download bot found on Telegram...",
                input_message_content=InputTextMessageContent(
                    "**Music Download Bot**\n\nOne of the most powerful Song download bot found on Telegram...\n\nDeveloper : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/songdownload597_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/songdownload597_bot")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Text to File Bot",
                thumb_url="https://telegra.ph/file/cc1c4c375f60c649a70a7.jpg",
                description="Send any code or text message to this bot then it will convert it into file...",
                input_message_content=InputTextMessageContent(
                    "**Text to File Bot**\n\nTEXT TO FILE BOT JUST SENT YOUR CODE OR TEXT MESSAGE THEN I WILL CONVERT IT INTO FILE\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/hb_text_to_file_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/hb_text_to_file_bot")
                        ]
                    ]
                ),
            ),

            InlineQueryResultArticle(
                title="QR Code Generator Bot",
                thumb_url="https://telegra.ph/file/cc1c4c375f60c649a70a7.jpg",
                description="Telegram Bot that can generate QR codes",
                input_message_content=InputTextMessageContent(
                    "**QR Code Generator Bot**\n\nTelegram Bot that can generate QR codes\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/HB_QR_CODE_BOT",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/HB_QR_CODE_BOT")
                        ]
                    ]
                ),
            ),

            InlineQueryResultArticle(
                title="Youtube Video Downloader Bot",
                thumb_url="https://telegra.ph/file/c846b61802788f8d6af86.jpg",
                description="Telegram bot that can download videos, thumbnail and playlist videos from Youtube",
                input_message_content=InputTextMessageContent(
                    "**Youtube Video Bot**\n\nTelegram bot that can download videos, thumbnail and playlist videos from Youtube VERY QUICKLY.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/HB_YOUTUBE_BOT",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/HB_YOUTUBE_BOT")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Torrent Search Bot",
                thumb_url="https://telegra.ph/file/89639d2a177ba4a4e8ea3.jpg",
                description="Telegram Bot that can search & download torrents from YTS, Piratebay, Anime, etc...",
                input_message_content=InputTextMessageContent(
                    "**Torrent Search Bot**\n\nTelegram Bot that can search & download torrents from YTS, Piratebay, Anime, etc...\n\nDEVELOPER : <a href=https://github.com/sanila2007>Sanila Ranatunga</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/torrentdownload88_bot",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/torrentdownload88_bot")
                        ]
                    ]
                ),
            ),
            InlineQueryResultArticle(
                title="Random Name Generator Bot",
                thumb_url="https://telegra.ph/file/cc1c4c375f60c649a70a7.jpg",
                description="A bot that can generate random name for you",
                input_message_content=InputTextMessageContent(
                    "**Random Name Generator Bot**\n\nTelegram bot that can generate random names for their users.\n\nDEVELOPER : <a href=https://github.com/hbbots>Amal Mohan</a>",
                    disable_web_page_preview=True
                ),
                url="https://t.me/HB_RANDOM_NAME_GENERATOR_BOT",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Reach the Bot", url="https://t.me/HB_RANDOM_NAME_GENERATOR_BOT")
                        ]
                    ]
                ),
            )
        ],
        cache_time=1
    )


# START MESSAGE

@bot.on_message(filters.command("start") & filters.private)
async def command1(bot, message):
    text = f"Hello {message.from_user.first_name}\n\n"+messages.START_TEXT_CAPTION_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
    await bot.send_message(Config.LOG_CHANNEL,
                           f"New User!\n\n◉ User - {message.from_user.first_name}\n◉ Joined time - {date_info.POSTED_TIME}\n◉ Joined date - {date_info.POSTED_DATE}")


# Learn bots section

@bot.on_message(filters.regex(pattern="Learn Bots"))
def reply_to_Learn_Bots(bot, message):
    text = messages.LEARN_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.LEARN_REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Restricted Stickers!!

@bot.on_message(filters.sticker)
async def restric_sticker(bot, message):
    await bot.send_chat_action(message.chat.id, enums.ChatAction.CANCEL)
    await bot.send_message(message.chat.id, "Oops!\n\nStickers has been restricted")


@bot.on_message(filters.regex(pattern="Song Download Bot🤖💖"))
def reply_to_utube(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
    bot.send_message(message.chat.id, "https://telegra.ph/How-to-use-Song-Downloader-Bot-07-09")


@bot.on_message(filters.regex(pattern="Torrent Download Bot🤖💖"))
def reply_to_s_on(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
    bot.send_message(message.chat.id, "https://telegra.ph/How-to-use-the-Torrent-Downloader-Bot-07-09")


@bot.on_message((filters.regex(pattern="Youtube Video Download Bot🤖💖")))
def reply_to_s_ong(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.UPLOAD_DOCUMENT)
    bot.send_message(message.chat.id, "https://telegra.ph/How-to-use-the-Youtube-Video-Downloader-Bot-07-09")


# About bot section

@bot.on_message(filters.regex(pattern="About Bot"))
def reply_to_AboutBot(bot, message):
    bot.send_message(message.chat.id, "<ins>**About Bot**</ins>\n\n"
                                      "Name: <a href=https://t.me/sanilaassistant_bot>Sanila's Assistant Bot</a>\n\n"
                                      "Created on: 11/21/2021\n\n"
                                      "Latest Version:  v0.8.4\n\n"
                                      "Language: <a href=www.python.org>Python</a>\n\n"
                                      "Framework: <a href=https://docs.pyrogram.org/>Pyrogram</a>\n\n"
                                      "Server: <a href=https://heroku.com>Heroku</a>\n\n"
                                      "Developer: <a href=https://github.com/sanila2007>Sanila Ranatunga\n\n</a>"
                                      "Source: 🔓\n\n", disable_web_page_preview=True)


# Contact section

@bot.on_message(filters.regex(pattern="Contact 📞"))
def reply_to_Contact(bot, message):
    bot.send_message(message.chat.id, messages.CONTACT_TEXT, reply_markup=ForceReply(message.chat.id))


# About Developer

@bot.on_message(filters.regex(pattern="About Developer"))
def reply_to_About(bot, message):
    bot.send_message(message.chat.id,
                     "**<ins>About Developer</ins>**\n\n""❖ Name : Sanila Ranatunga\n\n""❖ Age : 15 Years (2022)\n\n""❖ Birthday : 09.01.2007\n\n""❖ From : Sri Lanka\n\n""❖ Skills : Programmer , Developer\n\n""❖ Ambition : Be a software engineer\n\n""❖ Languages : Python, HTML, CSS, JS\n\n❖ Still Learning : C++, Java")


# Home

@bot.on_message(filters.regex(pattern="Home"))
def greet(bot, message):
    text = messages.REPLY_MESSAGE
    reply_markup = ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True

    )


@bot.on_message(filters.regex(pattern="Finish"))
def reply_finish(bot, message):
    bot.send_message(message.chat.id, messages.FEEDBACK_FINISH_TEXT,
                     reply_markup=ReplyKeyboardMarkup(buttons.REPLY_BUTTONS, resize_keyboard=True,
                                                      one_time_keyboard=False))


# Feedbacks section

@bot.on_message(filters.regex(pattern="Feedbacks"))
def reply_to_Feedback(bot, message):
    text = messages.FEEDBACK_REPLY_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.FEEDBACK_REPLY_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


# Credits

@bot.on_message(filters.regex(pattern="Credits"))
def reply_to_Credits(bot, message):
    text = messages.CREDITS_TEXT
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, one_time_keyboard=False, resize_keyboard=True)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Changelog Section

@bot.on_message(filters.regex(pattern="Changelog"))
def reply_to_Changelog(bot, message):
    reply_markup = ReplyKeyboardMarkup(buttons.HOME_BUTTON_CR, resize_keyboard=True, one_time_keyboard=False)
    bot.send_message(message.chat.id, messages.CHANGELOG_TEXT, disable_web_page_preview=True, reply_markup=reply_markup)


# Assistant Bot Feedback/Report bugs centre

@bot.on_message(filters.regex(pattern="Sanila Assistant Bot"))
async def reply_to_Assistant(bot, message):
    reply_markup = ForceReply(message.chat.id)
    await bot.send_message(message.chat.id, messages.SANILA_ASSISTANT_TEXT,
                           reply_markup=reply_markup
                           , disable_web_page_preview=True)


# Reporting area - Song Downloader bot

@bot.on_message(filters.regex(pattern="Song Downloader Bot"))
def reply_to_Song(bot, message):
    reply_markup = ForceReply(message.chat.id)
    text = messages.SONG_DOWNLOADER_TEXT
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Rating bots

@bot.on_message(filters.regex(pattern="Rate Bot"))
def reply_to_rate_bots(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.SPEAKING)
    text = ratings.RATINGS_TEXT
    reply_markup = ReplyKeyboardMarkup(ratings.RATINGS_BUTTONS, resize_keyboard=True, one_time_keyboard=False)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


RATING_BOT = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⭐", callback_data="one_star")
        ],
        [
            InlineKeyboardButton("⭐⭐", callback_data="two_star")
        ],
        [
            InlineKeyboardButton("⭐⭐⭐", callback_data="three_star")],
        [
            InlineKeyboardButton("⭐⭐⭐⭐", callback_data="four_star")

        ],
        [

            InlineKeyboardButton("⭐⭐⭐⭐⭐", callback_data="five_star")
        ]
    ]
)


# Rating bots

@bot.on_message(filters.regex(pattern="Assistant Bot"))
def reply_to_rating_assistant(bot, message):
    reply_markup = RATING_BOT
    bot.send_message(message.chat.id,
                     f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",
                     reply_markup=reply_markup)
    bot.send_message(Config.FEEDBACK_CHANNEL,
                     f"**New user entered rating area**\n\nUser - {message.from_user.first_name}\nUsername - @{message.chat.username}\nBot - {message.text}")


@bot.on_message(filters.regex(pattern="Torrent Bot"))
def reply_to_rating_assistant(bot, message):
    reply_markup = RATING_BOT
    bot.send_message(message.chat.id,
                     f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",
                     reply_markup=reply_markup)
    bot.send_message(Config.FEEDBACK_CHANNEL,
                     f"**New user entered rating area**\n\nUser - {message.from_user.first_name}\nUsername - @{message.chat.username}\nBot - {message.text}")


@bot.on_message(filters.regex(pattern="Youtube Bot"))
def reply_to_rating_assistant(bot, message):
    reply_markup = RATING_BOT
    bot.send_message(message.chat.id,
                     f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",
                     reply_markup=reply_markup)
    bot.send_message(Config.FEEDBACK_CHANNEL,
                     f"**New user entered rating area**\n\nUser - {message.from_user.first_name}\nUsername - @{message.chat.username}\nBot - {message.text}")


@bot.on_message(filters.regex(pattern="Song Bot"))
async def reply_to_rating_assistant(bot, message):
    reply_markup = RATING_BOT
    await bot.send_message(message.chat.id,
                           f"How many stars would you like to give to **{message.text}**??\n\n<i>*Note - These ratings will be reset after you rate but these ratings will share with the admin(developer)</i>",
                           reply_markup=reply_markup)
    await bot.send_message(Config.FEEDBACK_CHANNEL,
                           f"**New user entered rating area**\n\nUser - {message.from_user.first_name}\nUsername - @{message.chat.username}\nBot - {message.text}")


# Reporting area - Torrent downloader bot

@bot.on_message(filters.regex(pattern="Torrent Downloader Bot"))
async def reply_to_Torrent(bot, message):
    reply_markup = ForceReply(message.chat.id)
    text = messages.TORRENT_DOWNLOADER_TEXT
    await message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


# Reporting area - Youtube video downloader bot

@bot.on_message(filters.regex(pattern="Youtube Video Downloader Bot"))
def reply_to_Youtube(bot, message):
    text = messages.YOUTUBE_VIDEO_DOWNLOADER_TEXT
    reply_markup = ForceReply(message.chat.id)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )


@bot.on_message(filters.private & filters.command("captcha"))
def captch(bot, message):
    text = captcha_text.CAPTCHA_TEX_T
    reply_markup = InlineKeyboardMarkup(captcha_buttons.CAPTCHA_BUTT_ONS)
    bot.send_photo(message.chat.id, "https://telegra.ph/file/f54447d286c02e3f18070.jpg")
    message.reply(
        text=text,
        reply_markup=reply_markup
    )


@bot.on_message(filters.reply)
def fbb(bot, message):
    bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    tet = f"**<u>Feedback Information</u>**\n\nMessage - `{message.text}`\nWord count - {len(message.text.split())}\nPosted by - {message.from_user.first_name}\nUser ID - {message.from_user.id}\nUsername - @{message.chat.username}\nLanguage - {message.from_user.language_code}\nChat type - {message.chat.type}\nPosted date - {date_info.POSTED_DATE}\nPosted time - {date_info.POSTED_TIME}\nDate of reply - {date_info.DATE_OF_REPLY}\n\n<i>*Note: Add more feedbacks or click finish</i>"
    reply_markup = ReplyKeyboardMarkup(buttons.FINISH_FEEDBACK_BUTTONS, one_time_keyboard=True, resize_keyboard=True)
    message.reply(
        text=tet,
        reply_markup=reply_markup,
        quote=True
    )
    bot.send_message(Config.FEEDBACK_CHANNEL, "**New feedback available!**\n\n" + tet)



@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
    global a
    if CallbackQuery.data == "🧊":
        CallbackQuery.edit_message_text(
            captcha_text.PASS_CAPTCHA
        )

    elif CallbackQuery.data == "❌":
        CallbackQuery.edit_message_text(
            captcha_text.MULTY_FAIL,
            reply_markup=InlineKeyboardMarkup(captcha_buttons.RELOAD_CAPTCHA)
        ),

    elif CallbackQuery.data == "📩" or "🔥" or "🌭" or "🚑" or "🚡" or "💡" or "🔎" or "📈" or "🎆" or "🎎" or "🍧" or "⛑" or "🪀" or "🧸":
        CallbackQuery.edit_message_text(
            captcha_text.FAIL_CAPTCHA,
            reply_markup=InlineKeyboardMarkup(captcha_buttons.WRONG_CAPTCHA)
        )

    if CallbackQuery.data == "one_star":
        e = CallbackQuery.edit_message_text(
            "**Your ratings**\n\nGiven Stars - ⭐(1 star)\n\n<i>*Your ratings have been sent to the admin.</i>\n\nThank you for your support."
        )
        bot.send_message(Config.FEEDBACK_CHANNEL, f"**<u>New user has been rated a bot</u>**\n\n{e.text}")


    elif CallbackQuery.data == "two_star":
        d = CallbackQuery.edit_message_text(
            "**Your ratings**\n\nGiven Stars - ⭐⭐(2 star)\n\n<i>*Your ratings have been sent to the admin.</i>\n\nThank you for your support."
        )
        bot.send_message(Config.FEEDBACK_CHANNEL, f"**<u>New user has been rated a bot</u>**\n\n{d.text}")

    if CallbackQuery.data == "three_star":
        c = CallbackQuery.edit_message_text(
            "**Your ratings**\n\nGiven Stars - ⭐⭐⭐(3 star)\n\n<i>*Your ratings have been sent to the admin.</i>\n\nThank you for your support."
        )
        bot.send_message(Config.FEEDBACK_CHANNEL, f"**<u>New user has been rated a bot</u>**\n\n{c.text}")

    elif CallbackQuery.data == "four_star":
        b = CallbackQuery.edit_message_text(
            "**Your ratings**\n\nGiven Stars - ⭐⭐⭐⭐(4 star)\n\n<i>*Your ratings have been sent to the admin.</i>\n\nThank you for your support."
        )
        bot.send_message(Config.FEEDBACK_CHANNEL, f"**<u>New user has been rated a bot</u>**\n\n{b.text}")

    if CallbackQuery.data == "five_star":
        a = CallbackQuery.edit_message_text(
            "**Your ratings**\n\nGiven Stars - ⭐⭐⭐⭐⭐(5 star)\n\n<i>*Your ratings have been sent to the admin.</i>\n\nThank you for your support."
        )
        bot.send_message(Config.FEEDBACK_CHANNEL, f"**<u>New user has been rated a bot</u>**\n\n{a.text}")


print("Bot is alive📶✨")

bot.run()
