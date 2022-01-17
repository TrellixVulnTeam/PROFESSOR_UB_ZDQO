from datetime import datetime
from telethon import events
from telethon.utils import get_display_name
from math import ceil
from re import compile
import asyncio
import html
import os
import re
import sys
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest

from Professor import *
#from d3vilbot.cmdhelp import *
from Professor.utils import *
from Professor.config import Config
YOUR_NAME = Config.YOUR_NAME
D3VIL_row = Config.BUTTONS_IN_HELP
D3VIL_emoji = Config.EMOJI_IN_HELP

from . import *
# main menu for api setting


@tgbot.on(callbackquery.CallbackQuery(data=compile(b"apiset")))
async def apiset(event):
    await event.edit(
        get_string("ast_1"),
        buttons=[
            [Button.inline("Remove.bg API", data="rmbg")],
            [Button.inline("DEEP API", data="dapi")],
            [Button.inline("OCR API", data="oapi")],
            [Button.inline("« Back", data="setter")],
        ],
    )


@tgbot.on(callbackquery.CallbackQuery(data=compile(b"rmbgapi")))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "RMBG_API"
    name = "Remove.bg API Key"
    async with event.client.conversation(pru) as conv:
        await conv.send_message(get_string("ast_2"))
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{name} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )


@tgbot.on(callbackquery.CallbackQuery(data=compile(b"dapi")))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "DEEP_API"
    name = "DEEP AI API Key"
    async with event.client.conversation(pru) as conv:
        await conv.send_message("Get Your Deep Api from deepai.org and send here.")
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{YOUR_NAME} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )


@tgbot.on(callbackquery.CallbackQuery(data=compile(b"oaspi")))
async def rmbgapi(event):
    await event.delete()
    pru = event.sender_id
    var = "OCR_API"
    name = "OCR API Key"
    async with event.client.conversation(pru) as conv:
        await conv.send_message("Get Your OCR api from ocr.space Send Send Here.")
        response = conv.wait_event(events.NewMessage(chats=pru))
        response = await response
        themssg = response.message.message
        if themssg == "/cancel":
            return await conv.send_message(
                "Cancelled!!",
                buttons=get_back_button("apiset"),
            )
        else:
            await setit(event, var, themssg)
            await conv.send_message(
                f"{YOUR_NAME} changed to {themssg}",
                buttons=get_back_button("apiset"),
            )
