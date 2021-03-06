#cogs--------------------------------------------------------------------------------------------  
import cogs.gif_gen as EMOTES
import cogs.help as HELP
import cogs.sticky as sticky
import cogs.react as react
import cogs.bingus as BINGUS_MEME
import cogs.mod as SPECIAL
import cogs.bio as bio
import cogs.dev as dev
import cogs.levels as LEVELS
#async_run---------------------------------------------------------------------------------------
import asyncio
def run(run):
  asyncio.run(run)
#import------------------------------------------------------------------------------------------  
import random as RANDOM
import os
import discord
import time
import traceback
from discord.ext import tasks, commands
from discord import app_commands
from pytz import timezone
TZX = timezone('EST')
from zoneinfo import ZoneInfo
import datetime as DT
import sys
sys.path.append('../..')
from passcodes import main
sys.path.append('busboy/bot')
import LIBS.A_change as DEBUG_CHANGE
key=main.fenne.key
import motor.motor_asyncio
from db.dbc import client as connection_url
from db.mongo import Document
#EXTRA_IMPORTS----------------------------------------------------------------------------------
from extras.text_zone import BIG as b
from extras.text_zone import all_id as id_0
import extras.IDS as ID
#EXTRA_TEXT--------------------------------------------------------------------------------------
cafe = ID.cafe
Fenne = 474984052017987604 
Luna = 599059234134687774
r1 = id_0.fenne
rcheck = id_0.check
r3 = id_0.heart
r4 = id_0.P_heart
r5 = id_0.thumb_up
null = None
botuser = 966392608895152228
#intents----------------------------------------------------------------------------------------

intents = discord.Intents.all()
ACTIVITY=discord.Activity(type=discord.ActivityType.watching, name="discord.gg/FemboyCafe")
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.', '. '), intents=intents, activity=ACTIVITY, case_insensitive=True, tree_cls=app_commands.CommandTree)
bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(connection_url))
bot.db = bot.mongo["Pybot00"]
bot.inbox = Document(bot.db, "inbox")
bot.bio = Document(bot.db, "bio")
bot.config = Document(bot.db, "level_config")
bot.levels = Document(bot.db, "levels") # users levels
bot.verifies = Document(bot.db, "verifications")
#-----------------------------------------------------------------------------------------------
@tasks.loop(time=[DT.time(hour=0, minute=0, second=0, tzinfo=ZoneInfo("US/Eastern"))])
async def purge():
  array=[cafe.friends.connect, cafe.friends.inbox]
  for channel in array:
    cha = bot.get_channel(channel) or await bot.fetch_channel(channel)
    await cha.purge(limit=500)
    if channel == cafe.friends.connect:
      await cha.send("Connect Post Example:\n```Topics:\nMood:\nActivities & Interests:```\n\nMust be text only, you can delete your status at any time!")
  
  entries = await bot.inbox.get_all()
  for entry in entries:
    await bot.inbox.delete(entry["_id"])
  
@bot.event
async def on_member_join(mem):
  try:
    await mem.send(f"""??? Welcome <@!{mem.id}> {b.wd()}""")
  except:
    return
  finally:
    welcomed= discord.Object(id=889011345712894002)
    reg= discord.utils.get(mem.guild.roles, name="Regular")
    if reg not in mem.roles:
      return

    await mem.remove_roles(welcomed)
    
@bot.event
async def on_member_remove(mem): 
  bot.db.bio.delete_many({"_id": mem.id})
  cha= await bot.fetch_channel(cafe.friends.bio) or bot.get_channel(cafe.friends.bio)
  def check(msg):
    return msg.author.id == mem.id 
  await cha.purge(check=check)
  
@bot.event
async def on_guild_channel_create(cha):
  if cha.category.id == cafe.cats.home and "ticket" in str(cha.name):
    await asyncio.sleep(3)
    await cha.send("Hey there, how can we help you?")

  elif cha.id != cafe.verify:
    if cha.category_id != cafe.cats.verify:
      return
    await asyncio.sleep(2.5)
    await cha.send(f"""Welcome! 
To verify for the server please answer the survey.
  ```
  1. How did you find the server? 
  2. Why did you join?
  3. Do you identify as LGBTQ+?```
You must have <#889009278088773632> and a profile picture.
Please put all answers in one message and do not close the ticket!""")

async def main_start(run):
    async with bot:
        purge.start()
        await bot.add_cog(DEBUG_CHANGE.CHANGED(bot))
        await bot.add_cog(EMOTES.gifs(bot))
        await bot.add_cog(SPECIAL.mod(bot))
        await bot.add_cog(BINGUS_MEME.bingus(bot))
        await bot.add_cog(sticky.sticky(bot))
        await bot.add_cog(react.auto_react(bot))
        await bot.add_cog(bio.Bios(bot))
        await bot.add_cog(HELP.Help(bot))
        await bot.add_cog(dev.Dev(bot))
        await bot.add_cog(LEVELS.Levels(bot))

        try:
          await bot.start(str(key))
        except KeyboardInterrupt:
          await bot.close()
          sys.exit()
          
        
run(main_start(run))
####
