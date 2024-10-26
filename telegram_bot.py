
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext
import requests

# ضع التوكن الخاص بك هنا
API_TOKEN = '7658230517:AAErZp5QSugGryx9TEr0drNcw92GRpRq1fg'

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text('مرحبًا! أرسل لي رابط لتحميل الفيديو.')

async def download_video(update: Update, context: CallbackContext):
    url = update.message.text.strip()
    try:
        response = requests.get(url)
        with open('video.mp4', 'wb') as f:
            f.write(response.content)
        await update.message.reply_video(video=open('video.mp4', 'rb'))
    except Exception as e:
        await update.message.reply_text('حدث خطأ أثناء التنزيل. تأكد من صحة الرابط.')

if __name__ == '__main__':
    # إنشاء التطبيق باستخدام التوكن
    app = ApplicationBuilder().token(API_TOKEN).build()

    # إضافة الأوامر ومعالجات الرسائل
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download_video))

    # تشغيل البوت
    app.run_polling()
