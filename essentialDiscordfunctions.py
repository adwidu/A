import discord

class essentialDiscordFunctions:
    def getArgs(ctx: discord.Message, prefix: str):
        tempArgs = ctx.content.split(" ")
        tempArgs[0] = tempArgs[0].split(prefix)[1]
        args = []
        for i in range(len(tempArgs) -1):
            args = args + [tempArgs[i+1]]
        return args

    def getCommand(ctx: discord.Message, prefix: str):
        tempArgs = ctx.content.split(" ")
        tempArgs[0] = tempArgs[0].split(prefix)[1]
        return tempArgs[0]

    def isAdmin(ctx: discord.Message):
        adminRole = discord.utils.get(ctx.guild.roles,name="Admin")
        if adminRole in ctx.author.roles:
            return True
        else:
            return False
