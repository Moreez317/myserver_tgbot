import subprocess
import shlex


def execute_command(command):
    try:
        execute = subprocess.run(shlex.split(command),
                                 stdout=subprocess.PIPE).stdout.decode('utf-8')
        return execute
                
    except Exception:
        return "Failed!"
