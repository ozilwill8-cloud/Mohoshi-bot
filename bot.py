import telebot
from telebot import types

# التوكن الخاص بك
API_TOKEN = "8888686040:AAFD-athjq8fw5lYNrltXBZzPBaob0JIKbI"
bot = telebot.TeleBot(API_TOKEN)

# محافظ الشحن الخاصة بك
USDT_TRC20 = "TQfB72wi3MZgi7Gz4eoRBnRvw3StNG3XCx"
USDT_EVM = "0x29c19b2b9de886fe1706dd74db46bd1acf3af757"

# يوزر الدعم الفني
SUPPORT_USER = "@Sa_87i"

user_wallets = {}

# القائمة الرئيسية للأزرار بنفس النمط الاحترافي
def main_menu_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("🛒 شراء رقم جديد", callback_data="services")
    btn2 = types.InlineKeyboardButton("💳 تعبئة رصيد (إيداع)", callback_data="wallet")
    btn3 = types.InlineKeyboardButton("📞 التواصل والدعم", callback_data="support")
    btn4 = types.InlineKeyboardButton("ℹ️ معلومات الحساب", callback_data="account_info")
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id not in user_wallets:
        user_wallets[user_id] = 0.00

    # التصميم بدون رتبة الحساب مع الآيدي والرصيد واسم "الطوهشي"
    text = (
        f"👑 *الطوهشي | Buy and Sell Numbers* 🌐\n"
        f"────────────────────────\n"
        f"• *إيدي حسابك:* `{user_id}`\n"
        f"• *رصيد حسابك:* `USD {user_wallets[user_id]:.2f}`\n"
        f"────────────────────────\n"
        f"👇 *اختر من القائمة أدناه للبدء:*"
    )
    bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=main_menu_keyboard())

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    if user_id not in user_wallets:
        user_wallets[user_id] = 0.00

    if call.data == "main_menu":
        text = (
            f"👑 *الطوهشي | Buy and Sell Numbers* 🌐\n"
            f"────────────────────────\n"
            f"• *إيدي حسابك:* `{user_id}`\n"
            f"• *رصيد حسابك:* `USD {user_wallets[user_id]:.2f}`\n"
            f"────────────────────────\n"
            f"👇 *اختر من القائمة أدناه:*"
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=main_menu_keyboard())

    elif call.data == "services":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("✈️ أرقام تيليجرام", callback_data="tg_menu"),
            types.InlineKeyboardButton("💬 أرقام واتساب", callback_data="wa_menu"),
            types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")
        )
        text = "📂 *قسم الخدمات المتاحة:*\n\nيرجى اختيار التطبيق المراد تفعيل رقمه:"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "tg_menu":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("🇸🇦 السعودية ⟵ 0.70$", callback_data="buy_tg_sa"),
            types.InlineKeyboardButton("🇰🇼 الكويت ⟵ 0.65$", callback_data="buy_tg_kw"),
            types.InlineKeyboardButton("🇦🇪 الإمارات ⟵ 0.75$", callback_data="buy_tg_ae"),
            types.InlineKeyboardButton("🔙 رجوع للأقسام", callback_data="services")
        )
        bot.edit_message_text("✈️ *أرقام تيليجرام المتاحة:*\nاختر الدولة المطلوبة:", call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "wa_menu":
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(
            types.InlineKeyboardButton("🇸🇦 السعودية ⟵ 0.50$", callback_data="buy_wa_sa"),
            types.InlineKeyboardButton("🇰🇼 الكويت ⟵ 0.50$", callback_data="buy_wa_kw"),
            types.InlineKeyboardButton("🇦🇪 الإمارات ⟵ 0.55$", callback_data="buy_wa_ae"),
            types.InlineKeyboardButton("🇾🇪 اليمن ⟵ 0.40$", callback_data="buy_wa_ye"),
            types.InlineKeyboardButton("🇪🇬 مصر ⟵ 0.35$", callback_data="buy_wa_eg"),
            types.InlineKeyboardButton("🇯🇴 الأردن ⟵ 0.40$", callback_data="buy_wa_jo"),
            types.InlineKeyboardButton("🇮🇶 العراق ⟵ 0.35$", callback_data="buy_wa_iq"),
            types.InlineKeyboardButton("🌍 باقي الدول العربية ⟵ 0.45$", callback_data="buy_wa_arab"),
            types.InlineKeyboardButton("🔙 رجوع للأقسام", callback_data="services")
        )
        bot.edit_message_text("💬 *أرقام واتساب لجميع الدول العربية:*\nاختر الدولة:", call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    elif call.data.startswith("buy_"):
        prices = {
            "buy_tg_sa": 0.70, "buy_tg_kw": 0.65, "buy_tg_ae": 0.75,
            "buy_wa_sa": 0.50, "buy_wa_kw": 0.50, "buy_wa_ae": 0.55,
            "buy_wa_ye": 0.40, "buy_wa_eg": 0.35, "buy_wa_jo": 0.40,
            "buy_wa_iq": 0.35, "buy_wa_arab": 0.45
        }
        price = prices.get(call.data, 0.50)
        
        if user_wallets[user_id] >= price:
            user_wallets[user_id] -= price
            markup = types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("🏠 العودة للرئيسية", callback_data="main_menu"))
            success_text = f"✅ *تم شراء الرقم بنجاح!*\n\n📱 الرقم: `+9665XXXXXXXX`\n💵 التكلفة: `{price}$`\n⏳ *جاري انتظار وصول الكود...*"
            bot.edit_message_text(success_text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        else:
            bot.answer_callback_query(call.id, "⚠️ رصيدك غير كافي لشراء هذا الرقم!", show_alert=True)

    elif call.data == "wallet" or call.data == "account_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("💳 عرض عناوين الشحن (USDT)", callback_data="wallets_info"),
            types.InlineKeyboardButton("📞 التواصل لإرسال إيصال الشحن", url=f"https://t.me/{SUPPORT_USER.replace('@', '')}"),
            types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")
        )
        text = (
            f"👤 *معلومات الحساب والرصيد*\n"
            f"────────────────────────\n"
            f"• *إيدي حسابك:* `{user_id}`\n"
            f"• *رصيد حسابك:* `USD {user_wallets[user_id]:.2f}`\n"
            f"────────────────────────\n"
            f"لشحن رصيدك، قم بالتحويل عبر إحدى المحافظ ثم راسل الدعم بالإيصال."
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "wallets_info":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("📞 إرسال الإيصال للدعم", url=f"https://t.me/{SUPPORT_USER.replace('@', '')}"),
            types.InlineKeyboardButton("🔙 رجوع", callback_data="wallet")
        )
        text = (
            f"💎 *عناوين الشحن والإيداع المعتمدة:*\n\n"
            f"🔹 *USDT (TRC20):*\n`{USDT_TRC20}`\n\n"
            f"🔹 *USDT / EVM Wallet:*\n`{USDT_EVM}`\n\n"
            f"⚠️ *ملاحظة:* بعد إتمام التحويل، يرجى إرسال صورة الإيصال مع الآيدي الخاص بك (`{user_id}`) إلى الدعم الفني ({SUPPORT_USER}) ليتم إضافة الرصيد لحسابك فوراً."
        )
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)

    elif call.data == "support":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(
            types.InlineKeyboardButton("💬 مراسلة الدعم المباشر", url=f"https://t.me/{SUPPORT_USER.replace('@', '')}"),
            types.InlineKeyboardButton("🔙 العودة للقائمة الرئيسية", callback_data="main_menu")
        )
        text = f"📞 *الدعم الفني والخدمات (الطوهشي):*\n\nلأي استفسار أو مشكلة أو لشحن الرصيد، تواصل معنا مباشرة عبر المعرف:\n👉 `{SUPPORT_USER}`"
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, parse_mode="Markdown", reply_markup=markup)

print("البوت يعمل الآن بدون رتبة الحساب وبشكل أنيق...")
bot.infinity_polling()
