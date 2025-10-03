from pyrogram import Client, filters
from time import sleep
import requests

import data
import gpt


def main(app, users):
    @app.on_message(filters.command("help", prefixes=".") & filters.me)
    def help(_, msg):
        msg.edit(data.help_text)
    
    @app.on_message(filters.command("anim", prefixes=".") & filters.me)
    def anim(_, msg):
        text = msg.text.split(".anim ", maxsplit=1)[1]
        a = ""
        for i in text:
            a = a + i
            msg.edit(a + "_")
            sleep(0.1)
        msg.edit(a)

    @app.on_message(filters.command("flip", prefixes=".") & filters.me)
    def flip(_, msg):
        text = msg.text.split(".flip ", maxsplit=1)[1]
        final_str = ""
        for char in text:
            if char in data.reversed_text.keys():
                new_char = data.reversed_text[char]
            else:
                new_char = char
            final_str += new_char
        if text != final_str:
            msg.edit(final_str)
        else:
            msg.edit(text)

    @app.on_message(filters.command("calc", prefixes=".") & filters.me)
    def calc(_, msg):
        text = msg.text.split(".calc ", maxsplit=1)[1]
        try:
            msg.edit(f"[{app.name}]: {str(text)}={str(eval(text))}")
        except:
            msg.edit(f"[{app.name}: command error!")

    @app.on_message(filters.command("ipinfo", prefixes=".") & filters.me)
    def ipinfo(_, msg):
        ip = msg.text.split(".ipinfo ", maxsplit=1)[1]
        search_resul = ""
        try:
            response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
            for key, value in response.items():
                search_resul = f"{key}: {value}\n" + search_resul
                msg.edit(f"[{app.name}]: {str(ip)}\n{str(search_resul)}")

        except requests.exceptions.ConnectionError:
            msg.edit(f"[{app.name}]: Please check your connection!")
    
    @app.on_message(filters.command("gpt", prefixes="."))
    def chat_gpt(client, msg):
        try:
            send_message = client.send_message(
                chat_id = msg.chat.id,
                text = "...")
            client.edit_message_text(
                chat_id = msg.chat.id,
                message_id = send_message.id,
                text = f"[{users[1]}]:\n{gpt.question(msg.text.split(".gpt ", maxsplit=1)[1])}")
    
        except Exception as e:
            client.send_message(
                chat_id = msg.chat.id,
                text = f"[{users[0]}]: {e}")
            print(f"[{users[0]}]: {e}")
    
    @app.on_message(filters.command("spam", prefixes=".") & filters.me)
    def spam(client, msg):
        text = msg.text.split(".spam ", maxsplit=1)[1]
        text = text.split(" ", maxsplit=1)
        for i in range(int(text[0])):
            client.send_message(
                chat_id = msg.chat.id,
                text = text[1])