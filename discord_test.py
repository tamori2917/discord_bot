# coding=utf-8
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
from time import sleep
import time
import random
import datetime
import asyncio

bot = commands.Bot(command_prefix="+", intents = discord.Intents.default())
lot_channel_id = "925747753072619600"
lot_result_channel = "925747753072619600"

work_channel_id = "925773152901013504"
work_result_channel = "925773152901013504"
def __init__(self, bot):
  self.bot = bot

@bot.event
async def on_ready():
  print("Logged in as {0.user}.".format(bot))


# メッセージの送信時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):


  if message.content.startswith("こつこつ"): #こんにちはから始まるメッセージ
      
    #指定したチャンネルとメッセージを送ったチャンネルが同じIDなら実行
    if int(message.channel.id) == int(lot_channel_id):
        while True:
            ran = random.randint(60,300)
            ran2 = random.randint(1,100)
            wait_time = ran + 300
            print("waiting..." + str(wait_time))
            print(datetime.datetime.now())
            await asyncio.sleep(1)
            time.sleep(wait_time)
            if wait_time % 2 == 0:
                if ran2  % 2 == 0:
                    send_message = f'こつこつ'
                    await message.channel.send(send_message)
                else:
                    send_message = f'れべあげ'
                    await message.channel.send(send_message)
            else:
                if ran2  % 2 == 0:
                    send_message = f'あげかつ'
                    await message.channel.send(send_message)
                else:
                    send_message = f'あげあげ'
                    await message.channel.send(send_message)

    else:
        print("not hit")
        pass


@bot.event
async def on_massage(massage):

  if massage.content.startswith("!work"): #こんにちはから始まるメッセージ
      
    #指定したチャンネルとメッセージを送ったチャンネルが同じIDなら実行
    if int(massage.channel.id) == int(work_channel_id):
        while True:
            ran = random.randint(60,300)
            wait_time = ran + 300
            print("waiting...work" + str(wait_time))
            print(datetime.datetime.now())
            await asyncio.sleep(1)
            time.sleep(wait_time)
            send_massage = f'!work'
            await massage.channel.send(send_massage)


    else:
        print("not hit")
        pass

bot.run("ODc0MTU2NTM1NDk5MDgzODQ3.YeKPAg.omzjGfw_9y6ELk8Y48kuGJuDgEg", bot=False)

