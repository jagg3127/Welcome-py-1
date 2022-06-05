import discord
from discord.ext import commands
from extras.IDS import cafe

class bio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bio(self, ctx, member: discord.Member=None):
        """Posts someones bio."""
        data = await self.bot.bio.find(member.id)
        if not data:
            if member == ctx.author:
                return await ctx.send("You don't have a bio stored.")
            else:
                return await ctx.send("They don't have a bio stored.")
        
        bio_channel = self.bot.get_channel(cafe.friends.bio)
        msg = await bio_channel.fetch_message(data["msg_id"])

        view = discord.ui.View()
        view.add_item(discord.ui.Button(label="Go to bio post", url=msg.jump_url))

        await ctx.send(discord.utils.escape_mentions(f"**Bio for {member.name}**\n{data['bio']}"), view=view)