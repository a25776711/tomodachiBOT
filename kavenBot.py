import discord
from discord.ext import commands
import todo
import json

with open('data/item.json', "r", encoding="utf8") as file:
    data = json.load(file)

bot = commands.Bot(command_prefix='k.')

@bot.event
async def on_ready():
    print(f'目前登入身分:{bot.user}')

@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    else:
        temp=todo.save(ctx.author)
        if todo.mch(ctx.content):
            await ctx.channel.send("你好兇喔")
        if temp:
            await ctx.channel.send(f"喔 <@{ctx.author.id}>升級了")
        await bot.process_commands(ctx)

@bot.command()
async def join(ctx):
    if ctx.author == bot.user:
        return
    if ctx.author.voice is None:
        await ctx.send("你要進語音阿")
    else:
        tmp = ctx.author.voice.channel
        await tmp.connect()
@bot.command()
async def lv(ctx):
    print(ctx)
    await ctx.send(todo.lvch(ctx.author))
@bot.command()
async def leave(ctx):
    if ctx.voice_client is not None:
        await ctx.voice_client.disconnect()
        await ctx.send("88")
    else:
        await ctx.send("你是要我去哪裡")

@bot.command()
async def hi(ctx):
    await ctx.send(f"Hi <@{ctx.author.id}>")

@bot.command()
async def hp(ctx):
    await ctx.send(todo.helps())
@bot.command()
async def r(ctx):
    todo.save(ctx.author)
    await ctx.send(todo.helps())

bot.run(data['token'])
