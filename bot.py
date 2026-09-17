import os
import discord
from discord.ext import commands

# Discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Bot setup
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Bot is Ready! Logged in as {bot.user}")


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(
        member.guild.text_channels,
        name="『👋』・server-join"
    )

    if channel is None:
        print("Welcome channel not found.")
        return

    embed = discord.Embed(
        title="╭━━━〔 👋 WELCOME 〕━━━╮",
        description=(
            f"🎉 **Welcome {member.mention}!**\n\n"
            f"💙 Welcome to **{member.guild.name}**!\n"
            f"✨ We're happy to have you here.\n\n"
            f"📜 Please read the rules and enjoy your stay!\n"
            f"🌟 Have fun with the community! 🎊"
        ),
        color=discord.Color.green()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    if member.guild.icon:
        embed.set_author(
            name=member.guild.name,
            icon_url=member.guild.icon.url
        )

    embed.add_field(
        name="👥 Members",
        value=f"**{member.guild.member_count}**",
        inline=True
    )

    embed.add_field(
        name="👤 New Member",
        value=f"**{member.name}**",
        inline=True
    )

    if member.guild.icon:
        embed.set_footer(
            text=f"Welcome to {member.guild.name}",
            icon_url=member.guild.icon.url
        )
    else:
        embed.set_footer(text=f"Welcome to {member.guild.name}")

    await channel.send(embed=embed)


@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(
        member.guild.text_channels,
        name="『🚪』・server-left"
    )

    if channel is None:
        print("Leave channel not found.")
        return

    embed = discord.Embed(
        title="😢 Member Left",
        description=(
            f"**{member.name}** has left the server.\n\n"
            f"We currently have **{member.guild.member_count}** members."
        ),
        color=discord.Color.red()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    if member.guild.icon:
        embed.set_author(
            name=member.guild.name,
            icon_url=member.guild.icon.url
        )

    embed.set_footer(
        text=f"{member.guild.name} • Member Leave"
    )

    await channel.send(embed=embed)


@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")


# Railway Variable बाट token लिने
token = os.getenv("DISCORD_TOKEN")

if not token:
    raise RuntimeError(
        "DISCORD_TOKEN is missing. Add it in Railway Variables."
    )

print("Starting bot...")
bot.run(token)
