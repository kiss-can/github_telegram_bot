import telebot
import requests

bot = telebot.TeleBot('6417948984:AAGMMiEurNS9Zy8wVLF_fan4VdyzBXSDrn0')

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, '¡Hola! Envía /buscar y luego el nombre del repositorio que quieres encontrar.')

@bot.message_handler(commands=['buscar'])
def buscar_repositorio(message):
    bot.reply_to(message, "Ingresa el nombre del proyecto que deseas buscar:")
    bot.register_next_step_handler(message, process_search_query)

def process_search_query(message):
    nombre_repositorio = message.text
    url = f"https://api.github.com/search/repositories?q={nombre_repositorio}"
    response = requests.get(url)

    if response.status_code == 200:
        resultados = response.json()['items']

        if resultados:
            mensaje = "Resultados de la búsqueda:\n"
            for resultado in resultados:
                mensaje += f"- {resultado['name']} ({resultado['html_url']})\n"
            bot.reply_to(message, mensaje)
        else:
            bot.reply_to(message, "No se encontraron resultados para tu búsqueda.")
    else:
        bot.reply_to(message, "Error al realizar la búsqueda. Por favor, inténtalo nuevamente.")
bot.polling()