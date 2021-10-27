import discord
from discord import colour
from discord.ext import commands
import asyncio
import os
import json
from decouple import config
from discord.flags import Intents 
from rich import print
import random


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=">", case_intensitive = True, intents = intents)

@bot.event
async def on_ready():
  print("[red]================================[/]")
  print(f"    ----{bot.user}----")
  print("[red]================================[/]")
  print("        Online and Ready  ")
  print("[green]================================[/]")
  print("   [green][bold]READY TO THIS![/][/]")
  print(f"[green][bold]   {bot.user.name}[/][/]")
  print(f"[green]   {bot.user.id}[/]")
  print("[green]================================[/]")
##### END #####




##### START LEVEL COMMAND #####
 
with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass
 
with open('users.json', 'r') as f:
  users = json.load(f)
 
@bot.event    
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_experience(users, message.author)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)
            await bot.process_commands(message)
 
async def add_experience(users, user):
  if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
  users[f'{user.id}']['experience'] += 6
  print(f"{user.name}")
  print(f"{users[f'{user.id}']['level']}")
  print(f"{users[f'{user.id}']['experience']}")
  print("")

async def level_up(users, user, message):
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 3))
  if lvl_start < lvl_end:
    responses = [
                ' Incrivel, esse é seu level ',
                ' Parabens, seu level agora é esse: ',
                ]
    

    await message.channel.send(f" {user.mention} ```🔥 {random.choice(responses)} {lvl_end}. 🔥```")
    users[f'{user.id}']["level"] = lvl_end
   
    
  
  # LEVELS ROLES

  encasseract = 901917714208157746
  magohexeract = 902622489027444846
  metamago = 902622489828524103
  lendamaxima = 902622495906086982
  supremomestre = 902622496661053550
  diretordemagia = 902622498011635736
  arquimago = 902624168514813973
  bruxo = 902622499160883220
  mago = 902622500683386901
  sacerdote = 902622500813414410
  aprendiz = 902623978743545947


  if lvl_end == 1: #ROLE LVL 1
    role = user.guild.get_role(aprendiz)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if lvl_end == 3: #ROLE LVL 1
    role = user.guild.get_role(sacerdote)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if lvl_end == 5: #ROLE LVL 1
    role = user.guild.get_role(mago)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if lvl_end == 15: #ROLE LVL 2
    role = user.guild.get_role(bruxo)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")
  
  if lvl_end == 25: #ROLE LVL 3
    role = user.guild.get_role(arquimago)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if lvl_end == 35: #ROLE LVL 4
    role = user.guild.get_role(diretordemagia)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")
  
  if lvl_end == 45: #ROLE LVL 5
    role = user.guild.get_role(supremomestre)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if lvl_end == 55: #ROLE LVL 6
    role = user.guild.get_role(lendamaxima)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")
  
  if lvl_end == 65: #ROLE LVL 7
    role = user.guild.get_role(metamago)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if lvl_end == 75: #ROLE LVL 8
    role = user.guild.get_role(magohexeract)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if lvl_end == 300: #ROLE LVL 9
    role = user.guild.get_role(encasseract)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")  
#-----------------------------------#
 


@bot.command(name="rank")
async def rank(ctx, member: discord.Member = None):
  if member == None:
    userlvl = users[f'{ctx.author.id}']['level']
    await ctx.send(f'{ctx.author.mention} Esse é seu Nivel Atual,  {userlvl}!')
  else:
    userlvl2 = users[f'{member.id}']['level']
    await ctx.send(f'{member.mention} is at level {userlvl2}!')

  embed = discord.Embed(title="{} LEVEL STATUS".format(ctx.author.name))
  embed.add_field(name="Name", value=ctx.author.mention, inline=False)
  embed.add_field(name="XP", value=f"{users[f'{ctx.author.id}']['experience']}", inline=True)
  embed.add_field(name="Level", value=f"{users[f'{ctx.author.id}']['level']}", inline=True)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  await ctx.send(embed=embed)
##### END LEVEL COMMAND #####

@bot.event
async def on_member_join(member):
  canalwc = bot.get_channel(900869518287581194)
  regras = bot.get_channel(900817880239706192)
  mensagem = await canalwc.send(f"WELCOME {member.mention}, Leia as regras em {regras.mention}")

  await asyncio.sleep(3000)

  await mensagem.delete()


@bot.command(name="roles")
async def roles1(ctx):
  administrador = discord.utils.get(ctx.guild.roles, id=901917067492618250)
  encasseract = discord.utils.get(ctx.guild.roles, id=901917714208157746)
  magohexeract = discord.utils.get(ctx.guild.roles, id=902622489027444846)
  metamago = discord.utils.get(ctx.guild.roles, id=902622489828524103)
  lendamaxima = discord.utils.get(ctx.guild.roles, id=902622495906086982)
  supremomestre = discord.utils.get(ctx.guild.roles, id=902622496661053550)
  diretordemagia = discord.utils.get(ctx.guild.roles, id=902622498011635736)
  arquimago = discord.utils.get(ctx.guild.roles, id=902624168514813973)
  bruxo = discord.utils.get(ctx.guild.roles, id=902622499160883220)
  mago = discord.utils.get(ctx.guild.roles, id=902622500683386901)
  sacerdote = discord.utils.get(ctx.guild.roles, id=902622500813414410)
  aprendiz = discord.utils.get(ctx.guild.roles, id=902623978743545947)



  embed = discord.Embed(
    description = "Esses São os Cargos por Level\n\n"
        f"❖  Cargos Lendarios  ❖\n"
        f"Esses são os primeiros cargos, você começará na caminhada como um invocador de magias.\n\n"
        f"Level 300+ ➤{encasseract.mention}\nLevel 95+  ➤{magohexeract.mention}\nLevel 85+ ➤{metamago.mention}\n\n",
    colour = 00000
  )
  embed2 = discord.Embed(
      description =
          f"Deixando de ser um novato, um mago finalmente consegue dominar habilidades próprias, para treinar seus movimento é cada vez mais necessário persistência.\n\n"
          f"Level 75+ ➤{lendamaxima.mention}\nLevel 65+ ➤{supremomestre.mention}\nLevel 55+ ➤{diretordemagia.mention}\nLevel 45+ ➤{arquimago.mention}\n\n",          
      colour = 00000
  )
  embed3 = discord.Embed(
      description =
          f"Você de fato pertence a Elite do poder, e agora está buscando mais, já que usar o poder dessa dimensão não lhe é suficiente que nem antes.\n\n"
          f"Level 35+ ➤{bruxo.mention}\nLevel 25+ ➤{mago.mention}\nLevel 15+ ➤{sacerdote.mention}\nLevel 5+ ➤{aprendiz.mention}\n\n",
      colour = 00000
  )

  embed.set_author(name="CARGOS", icon_url="https://www.tibiawiki.com.br/images/1/1f/Blessed_Shield.gif")
  embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/6/63/Icone7.png")
  embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Request By {ctx.author}')

  embed2.set_thumbnail(url="https://www.tibiawiki.com.br/images/f/f8/Eldritch_Tome.gif")
  embed2.set_footer(icon_url=ctx.author.avatar_url, text=f'Request By {ctx.author}')

  embed3.set_thumbnail(url="https://www.tibiawiki.com.br/images/0/00/Book_of_Lies.gif")
  embed3.set_footer(icon_url=ctx.author.avatar_url, text=f'Request By {ctx.author}')

  await ctx.send(embed=embed)
  await ctx.send(embed=embed2)
  await ctx.send(embed=embed3)

@bot.command(name="test")
async def test(ctx):
  moderator = discord.utils.get(ctx.guild.roles, id=901917067492618250)
  await ctx.send(f'Hello {moderator.mention}')


TOKEN = config("TOKEN") 
bot.run(TOKEN)