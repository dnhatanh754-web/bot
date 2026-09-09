import discord
from discord.ext import commands
import sqlite3
from datetime import datetime
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("✅ Bot đã sẵn sàng, boss man!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

bot.run(os.getenv("TOKEN"))
