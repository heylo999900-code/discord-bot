import discord
from discord.ext import commands
import config

# Bot permissions
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# When bot comes online
@bot.event
async def on_ready():
    print(f"Bot is Ready! Logged in as {bot.user}")


# Welcome message
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(
        member.guild.text_channels,
        name="welcome"
    )

    if channel:
        embed = discord.Embed(
            title="👋 Welcome to the Server!",
            description=(
                f"Welcome {member.mention} to "
                f"**{member.guild.name}**! 🎉\n\n"
                f"👤 **Username:** {member.name}\n"
                f"🆔 **Member:** #{member.guild.member_count}\n"
                f"👥 **Total Members:** {member.guild.member_count}"
            ),
            color=discord.Color.blue()
        )

        # Member profile picture
        embed.set_author(
            name=member.name,
            icon_url=member.display_avatar.url
        )

        # Server profile picture
        if member.guild.icon:
            embed.set_thumbnail(url=member.guild.icon.url)

        # Footer
        embed.set_footer(
            text=f"{member.guild.name} • Member #{member.guild.member_count}"
        )

        await channel.send(embed=embed)


# Leave message
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(
        member.guild.text_channels,
        name="welcome"
    )

    if channel:
        embed = discord.Embed(
            title="😢 Member Left",
            description=(
                f"**{member.name}** has left **{member.guild.name}**.\n\n"
                f"👥 **Total Members:** {member.guild.member_count}"
            ),
            color=discord.Color.red()
        )

        # Member profile picture
        embed.set_author(
            name=member.name,
            icon_url=member.display_avatar.url
        )

        # Server profile picture
        if member.guild.icon:
            embed.set_thumbnail(url=member.guild.icon.url)

        embed.set_footer(
            text=f"{member.guild.name} • Members: {member.guild.member_count}"
        )

        await channel.send(embed=embed)


# Test command
@bot.command()
async def ping(ctx):
    await ctx.send("pong")


# Run bot
print("Starting bot...")
bot.run(config.DISCORD_TOKEN)