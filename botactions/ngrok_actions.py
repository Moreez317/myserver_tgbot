import os
from pyngrok import ngrok


NGROK_TOKEN = os.environ.get("NGROK_TOKEN")

ngrok.set_auth_token(NGROK_TOKEN)


def make_new_tunnel(port, protocol):  # 22, "tcp"
    tunnel = ngrok.connect(port, protocol)
    return tunnel


def get_active_tunnel():
    return ngrok.get_tunnels()


def kill_active_tunnel(tunnel):
    ngrok.disconnect(tunnel.public_url)
