from pyrogram import filters
from pyrogram.types import Message

from SoloCloud import app
from SoloCloud.core.call import AyushSolo

welcome = 20
close = 30


@app.on_message(filters.video_chat_started, group=welcome)
@app.on_message(filters.video_chat_ended, group=close)
async def welcome(_, message: Message):
    await AyushSolo.stop_stream_force(message.chat.id)
