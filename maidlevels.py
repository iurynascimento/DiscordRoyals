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
  users[f'{user.id}']['experience'] += 25
  print(f"{user.name}")
  print(f"{users[f'{user.id}']['level']}")
  print(f"{users[f'{user.id}']['experience']}")
  print("")

async def level_up(users, user, message):
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 6))

  if lvl_start < lvl_end:
    responses = [
                ' Incrivel, esse é seu level',
                ' Parabens, seu level agora é esse:',
                ]
  
    await message.channel.send(f" {user.mention} ```🔥 {random.choice(responses)} {lvl_end}. 🔥```")
    users[f'{user.id}']["level"] = lvl_end
   
    
  
  


  # LEVELS ROLES

  infinitylord = 901917714208157746
  divinitylord = 902622489027444846
  demigodlord = 902622489828524103
  infinityvoid = 903285176015130685
  divinityvoid = 902924872412446840
  demigodvoid = 902733455270486086
  abyssallord = 902730715869892678
  abyssalsavior = 902622495906086982
  dimenlord = 902622496661053550
  dimemvoid = 902622498011635736
  dimemsavior = 902624168514813973
  sorclord = 902622499160883220
  sorcvoid = 902622500683386901
  sorcsavior = 902622500813414410
  sorcapprentice = 902623978743545947




  if experience == 500: #ROLE LVL 1
    role = user.guild.get_role(sorcapprentice)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if experience == 1000: #ROLE LVL 1
    role = user.guild.get_role(sorcsavior)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if experience == 2000: #ROLE LVL 1
    role = user.guild.get_role(sorcvoid)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if experience == 5000: #ROLE LVL 2
    role = user.guild.get_role(sorclord)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")
  
  if experience == 10000: #ROLE LVL 3
    role = user.guild.get_role(dimemsavior)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if experience == 25000: #ROLE LVL 4
    role = user.guild.get_role(dimemvoid)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")
  
  if experience == 50000: #ROLE LVL 5
    role = user.guild.get_role(dimenlord)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if experience == 80000: #ROLE LVL 6
    role = user.guild.get_role(abyssalsavior)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")
  
  if experience == 100000: #ROLE LVL 7
    role = user.guild.get_role(abyssallord)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if experience == 200000: #ROLE LVL 8
    role = user.guild.get_role(demigodvoid)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")

  if experience == 250000: #ROLE LVL 9
    role = user.guild.get_role(divinityvoid)
    await user.add_roles(role)
    #print(f"{user.name, user.id} ADD ROLE")  
#-----------------------------------#
  if experience == 260000: #ROLE LVL 10
    role = user.guild.get_role(infinityvoid)
    await user.add_roles(role)

  if experience == 270000: #ROLE LVL 11
    role = user.guild.get_role(divinityvoid)
    await user.add_roles(role)

  if experience == 280000: #ROLE LVL 12
    role = user.guild.get_role(demigodlord)
    await user.add_roles(role)

  if experience == 290000: #ROLE LVL 12
    role = user.guild.get_role(divinitylord)
    await user.add_roles(role)

  if experience == 300000: #ROLE LVL 13
    role = user.guild.get_role(infinitylord)
    await user.add_roles(role)


#-----------------------------------------------------------------------#


@bot.command(name="rank")
async def rank(ctx, member: discord.Member = None):
  if member == None:
    userlvl = users[f'{ctx.author.id}']['level']
    await ctx.send(f'{ctx.author.mention} Esse é seu Nivel Atual,  {userlvl}!')
  else:
    userlvl2 = users[f'{member.id}']['level']
    await ctx.send(f'{member.mention} is at level {userlvl2}!')


  xp = f"{users[f'{ctx.author.id}']['experience']}"
  lvl = f"{users[f'{ctx.author.id}']['level']}"

  embed = discord.Embed(title=ctx.author.name,
  description ="Você de fato pertence a Elite do poder, e agora está buscando mais, já que usar o poder dessa dimensão não lhe é suficiente que nem antes.",
  colour= 00000)
  
  embed.set_author(name="Status",icon_url="https://www.tibiawiki.com.br/images/7/74/Majestic_Shield.gif")
  embed.add_field(name="Name", value=ctx.author.mention, inline=False)
  embed.add_field(name="XP",value=f"Você tem {xp} de XP .", inline=False)
  embed.add_field(name="Level", value=f"Seu level atual é {lvl} .", inline=True)
  embed.set_thumbnail(url=ctx.author.avatar_url)
  embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Request By {ctx.author}')
  await ctx.send(embed=embed)
##### END LEVEL COMMAND #####

@bot.event
async def on_member_join(member):
  canalwc = bot.get_channel(900869518287581194)
  regras = bot.get_channel(900817880239706192)
  mensagem = await canalwc.send(f" ► Bem vindo a Royals, {member.mention}\n► Leia as regras em {regras.mention}")
  
  await asyncio.sleep(3000)

  await mensagem.delete()


@bot.command(name="roles")
async def roles1(ctx):

  administrador = discord.utils.get(ctx.guild.roles, id=901917067492618250)
  infinitylord = discord.utils.get(ctx.guild.roles, id=901917714208157746)
  divinitylord = discord.utils.get(ctx.guild.roles, id=902622489027444846)
  demigodlord = discord.utils.get(ctx.guild.roles, id=902622489828524103)
  infinityvoid = discord.utils.get(ctx.guild.roles, id=903285176015130685)
  divinityvoid = discord.utils.get(ctx.guild.roles, id=902924872412446840)
  demigodvoid = discord.utils.get(ctx.guild.roles, id=902733455270486086)
  abyssallord = discord.utils.get(ctx.guild.roles, id=902730715869892678)
  abyssalsavior = discord.utils.get(ctx.guild.roles, id=902622495906086982)
  dimenlord = discord.utils.get(ctx.guild.roles, id=902622496661053550)
  dimemvoid = discord.utils.get(ctx.guild.roles, id=902622498011635736)
  dimemsavior = discord.utils.get(ctx.guild.roles, id=902624168514813973)
  sorclord = discord.utils.get(ctx.guild.roles, id=902622499160883220)
  sorcvoid = discord.utils.get(ctx.guild.roles, id=902622500683386901)
  sorcsavior = discord.utils.get(ctx.guild.roles, id=902622500813414410)
  sorcapprentice = discord.utils.get(ctx.guild.roles, id=902623978743545947)


  embed = discord.Embed(
    description = "Esses São os Cargos por XP\n\n"
        f"╭─ ❖  Cargos Lendarios  ❖ ─╮\n\n"
        f"► Não deixem que lhe façam pensar que você não é capaz de fazer algo porque essa pessoa não consegue fazer. Se você deseja alguma coisa, se quer realmente, lute por isso e ponto final. \n\n"
        f"300.000 XP+ ➤{infinitylord.mention}\n290.000 XP+  ➤{divinitylord.mention}\n280.000 XP+ ➤{demigodlord.mention}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"► Se quiser que eu mate Lords, eu mato Lords, se quiser que eu mato Divindades eu mato Divindades, Abyssais e todos, mas lembre se de um coisa adoraria te matar de graça\n\n"
        f"270.000 XP+ ➤{infinityvoid.mention}\n260.000 XP+ ➤{divinityvoid.mention}\n250.000XP+ ➤{demigodvoid.mention}\n\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"► Eu sou um guerreiro que sonhou com a paz. Às vezes ela demora pra acontecer, às vezes não acontece. Mas você tem que acordar\n\n"
        f"200.000 XP+ ➤{abyssallord.mention}\n100.000 XP+ ➤{abyssalsavior.mention}\n80.000 XP+ ➤{dimenlord.mention}\n50.000 XP+ ➤{dimemvoid.mention}\n25.000XP+ ➤{dimemsavior.mention}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"► Haverá um dia que você desejará fazer um pouco de mal, para alcançar um bem maior.\n\n"
        f"10.000 XP+ ➤{sorclord.mention}\n5.000 XP+ ➤{sorcvoid.mention}\n1.000 XP+ ➤{sorcsavior.mention}\n500 XP+ ➤{sorcapprentice.mention}\n\n"
        "━━━━━━━━━━━━━━━━━━━━━\n\n",
    colour = 00000
  )

  embed.set_author(name="Roles", icon_url="https://www.tibiawiki.com.br/images/1/1b/Paper.gif")
  embed.set_thumbnail(url="https://www.tibiawiki.com.br/images/2/2b/Divine_Plate.gif")
  embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Request By {ctx.author}')
  await ctx.send(embed=embed)
  



@bot.command(name="test")
async def test(ctx):
  moderator = discord.utils.get(ctx.guild.roles, id=901917067492618250)
  await ctx.send(f'Hello {moderator.mention}')


TOKEN = config("TOKEN") 
bot.run(TOKEN)