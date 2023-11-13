import openai
import telebot

# openai.api_key = "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"
bot = telebot.TeleBot("6030967124:AAFDZUXO6VY3Udmf0BKRApW-fZ5LmGeiSLw")

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if(message.text == "/start"):
        return
    mytext = message.text;
    if("-/-" in message.text):
        mytext = "Проверь правописание и пунктуацию: " + mytext;
    # response = openai.Completion.create(
    #     engine="text-davinci-003",
    #     prompt=(f"{mytext}\n"),
    #     max_tokens=600,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    response = "ответ"
    bot.send_message(message.chat.id, response)
    #print(message)
    print(message.chat.id, ":@", message.from_user.username, ": ", message.from_user.first_name, " : ", message.text)

    if(message.chat.id !=468004165):
        a = message.from_user.first_name
        a+=": "
        a+=message.text
        bot.send_message(468004165, a)
bot.polling()