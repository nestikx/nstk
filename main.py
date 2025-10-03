from pyrogram import Client, filters
from dotenv import load_dotenv
import os
import funcs, ns

load_dotenv()

users = ["console", "ChatGPT"]

app = Client(
    name = "/etc/secrets/nstk.session",
    api_id = os.getenv("API_ID"),
    api_hash = os.getenv("API_HASH")
)

funcs.main(app, users)

app.run()