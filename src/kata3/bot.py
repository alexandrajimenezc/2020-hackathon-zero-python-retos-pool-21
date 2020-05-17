import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    return update.message.reply_text('Hola , soy creado por javi y Alex!')

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    return update.message.reply_txt('Ayudame!')

def mayus(update, context):
    """Renvia el msj en mayuscula /mayus."""
    return update.message.reply_text(update.message.text.upper())

def alreves(update, context):
    """Repite el mensaje del usuario y lo devuleve al reves."""
    return update.message.reply_text(update.message.text[::-1])

def repite(update, context):
    """Repite el mensaje del usuario /echo"""
    update.message.reply_text(update.message.text) 

def comandos(update, context):
    """Te dice los comandos disponibles"""
    update.message.reply_text('Hola , estos son los comando disponibles:\n/start : inicia el bot\n/help\n/mayus : convierte el texto en mayúscular \n/alreves : Te devuelve el texto alreves\n /repite : Repite lo que escribes ')

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("1100105888:AAHwcgDxQ7l7jwC2if1mNzeTFHCbweQQxx", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("help",help))
    dp.add_handler(CommandHandler("mayus",mayus))
    dp.add_handler(CommandHandler("alreves",alreves))
    dp.add_handler(CommandHandler("repite",repite))
    dp.add_handler(CommandHandler("comandos",comandos))

    #

    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
