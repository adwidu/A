#import discord and my functions
from asyncio.windows_events import NULL
import discord
import essentialDiscordfunctions

#instantiates the imported libraries
edf = essentialDiscordfunctions.essentialDiscordFunctions
client = discord.Client()

#extra variables
loginchannel = client.get_channel(827260565805596672)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="lx? commands"))

@client.event   
async def on_message(ctx: discord.Message):
    if ctx.author.display_name == "lexiModBot": return

    #admin commands zone
    if ctx.content.lower().startswith("lx?") and edf.isAdmin(ctx):
        
        args = edf.getArgs(ctx, "lx?")
        command = edf.getCommand(ctx, "lx?")
        
        if command == "channel":
            if args[0] == "delete":
                if len(ctx.channel_mentions) != 0:
                    print(len(ctx.channel_mentions))
                    c = client.get_channel(int(ctx.channel_mentions[0].id))
                    await c.delete()

            if args[0] == "multidelete":
                if len(ctx.channel_mentions) != 0:
                    print(len(ctx.channel_mentions))
                    for i in range(len(ctx.channel_mentions)):
                        c = client.get_channel(int(ctx.channel_mentions[i].id))
                        await c.delete()

            if args[0] == "add":
                if args[1] == "voice" :
                    name = ""
                    for a in range(len(args) - 2):
                        name += args[a+2]+" "
                    newchannel = await ctx.guild.create_voice_channel(name, category=ctx.channel.category)

                if args[1] == "text":
                    name = ""
                    for a in range(len(args) - 2):
                        name += args[a+2]+"-"
                    newchannel = await ctx.guild.create_text_channel(name, category=ctx.channel.category)
            
    #non-admin commands zone
    if ctx.content.lower().startswith("lx?"):

        args = edf.getArgs(ctx, "lx?")
        command = edf.getCommand(ctx, "lx?")

        
        if command == "login":
            if ctx.channel == loginchannel:
                await ctx.author.add_roles(discord.utils.get(ctx.guild.roles,name="Usuario"))
                await ctx.delete()
            else:
                await ctx.channel.send("you are already loged into the server xD, what an idiot "+discord.utils.get(ctx.guild.roles,name="Usuario").mention)

    if len(ctx.content.split("vc[")) != 0:
        if ctx.content.split("vc[")[1].split("]")[0]:
            channel = discord.utils.get(ctx.guild.channels,name=ctx.content.split("vc[")[1].split("]")[0])
            content: str = ctx.content
            content = content.replace("vc[","<#")
            content = content.replace("]",">")
            content = content.replace(ctx.content.split("vc[")[1].split("]")[0], str(channel.id))
            await ctx.channel.send(str(ctx.author.display_name)+" says: " + content)
            await ctx.delete()

client.run("OTI5ODEyNjQ3ODU4Mjk4OTEy.Ydsxgg.mFbqbCzTZmz_BPKazZ8HB6N6mMc")


