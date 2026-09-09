import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("✅ Bot đã sẵn sàng, thưa cậu chủ!")

@bot.command()
async def ping(ctx):
    await ctx.send("Xin chào cậu chủ! Tôi sẵn sàng ạ.")

@bot.command()
async def hello(ctx):
    await ctx.send("Chào cậu chủ! Có gì cần tôi giúp không ạ?")

@bot.command()
async def helpme(ctx):
    embed = discord.Embed(title="📋 Danh sách lệnh", color=0x00ff00)
    embed.add_field(name="!ping", value="Kiểm tra bot", inline=False)
    embed.add_field(name="!hello", value="Chào bot", inline=False)
    embed.add_field(name="!shop", value="Xem cửa hàng", inline=False)
    embed.add_field(name="!buy [ID]", value="Mua sản phẩm", inline=False)
    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))

