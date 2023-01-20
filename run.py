import logging
import os
import telebot

from datetime import datetime

import botactions
from botactions.constants import SHUTDOWN_COMMAND, REBOOT_COMMAND, AUTHORIZED_USER_MESSAGE, AVALIABLE_COMMANDS_MESSAGE

TELEGRAM_API_TOKEN = os.environ.get("TELEGRAM_API_TOKEN")
TORRENT_FILES_DIR = os.environ.get("TORRENT_FILES_DIR")
LOG_DIR = os.environ.get("LOGS_DIR")
#LOG_DIR = 'logs/'

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)


def start_bot():
    logging.info("bot started!")
    try:
        bot.infinity_polling(timeout=123)

    except Exception as exception:
        logging.error(exception)


def download_file(message):
    file_name = message.document.file_name
    file_info = bot.get_file(message.document.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    if file_name[-8::] == '.torrent':
        with open(TORRENT_FILES_DIR + "/" + file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

        logging.info("Added torrent: " + file_name)

    else:
        bot.send_message(message.from_user.id, "Incorrect file format!")


# Закомментировано поскольку не используется cli_emulation
# def read_command(message):
#   command = message.text
#   bot.send_message(message.from_user.id, str(botactions.execute_command(command)))
#
#   logging.info(str(datetime.now()) + "/id:" +
#                str(message.from_user.id) + "/command:" + str(command))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    logging.info("id:" + str(message.from_user.id) + " trying to start")

    if botactions.verify_user(message.from_user.id) == True:
        bot.send_message(message.from_user.id, AUTHORIZED_USER_MESSAGE)


@bot.message_handler(commands=['actions'])
def send_avaliable_actions(message):
    if botactions.verify_user(message.from_user.id) == True:
        bot.send_message(message.from_user.id, AVALIABLE_COMMANDS_MESSAGE)


# Закомментировано поскольку не хочется иметь возможность исполнять
# команды из под SUDO прям в телеге
# @bot.message_handler(commands=['enter_cli'])
# def cli_emulation(message):
#   if botactions.verify_user(message.from_user.id) == True:
#       bot.send_message(message.from_user.id, CLI_ENTER_MESSAGE)
#       bot.register_next_step_handler(message, read_command)


@bot.message_handler(commands=['add_torrent'])
def add_torrent(message):
    if botactions.verify_user(message.from_user.id) == True:
        bot.register_next_step_handler(message, download_file)


@bot.message_handler(commands=['halt'])
def shutdown(message):
    if botactions.verify_user(message.from_user.id) == True:
        botactions.execute_command(SHUTDOWN_COMMAND)


@bot.message_handler(commands=['reboot'])
def reboot(message):
    if botactions.verify_user(message.from_user.id) == True:
        botactions.execute_command(REBOOT_COMMAND)


@bot.message_handler(commands=['make_tunnel'])
def ngrok_create(message):
    if botactions.verify_user(message.from_user.id) == True:
        tunnel = botactions.get_active_tunnel()

        if tunnel:
            bot.send_message(message.from_user.id, str(tunnel))
            logging.info("Made new tunnel: " + str(tunnel))
        else:
            tunnel = botactions.make_new_tunnel(22, "tcp")
            bot.send_message(message.from_user.id, str(tunnel))
            logging.info("Tunnel already exists: " + str(tunnel))


@bot.message_handler(commands=['kill_tunnel'])
def ngrok_kill(message):
    if botactions.verify_user(message.from_user.id) == True:
        try:
            tunnel = botactions.get_active_tunnel()[0]
            botactions.kill_active_tunnel(tunnel)
            bot.send_message(message.from_user.id, "Closed!")

            logging.info("Closed! " + str(tunnel))

        except IndexError:
            bot.send_message(message.from_user.id, "Tunnel already closed!")


if __name__ == "__main__":
    log_format = "%(asctime)s - %(message)s"
    logging.basicConfig(filename=LOG_DIR + str(datetime.now()) +
                        ".log", filemode='w', level=logging.INFO, format=log_format)
    start_bot()
