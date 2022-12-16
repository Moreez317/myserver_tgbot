# Список ID telegram аккаунтов, которые могут иметь доступ к боту
ALLOWED_USER_ID_LIST = (398446346,)

# Команды для выполнения в модуле terminal_actions.py
SHUTDOWN_COMMAND = "sudo shutdown now"
REBOOT_COMMAND = "sudo reboot now"

AUTHORIZED_USER_MESSAGE = "Congratulations! You are in list of allowed ID's! Type /actions to show avaliable actions..."

# не используется, поскольку cli_emulation закомментированна
CLI_ENTER_MESSAGE = """
This is terminal emulator. Some commands will work, some...
Enter commands:
"""

AVALIABLE_COMMANDS_MESSAGE = """
show avaliable commands: /actions
add new torrent: /add_torrent
shutdown: /halt
reboot: /reboot
make new ngrok tunnel: /make_tunnel
drop tunnel: /kill_tunnel
"""
