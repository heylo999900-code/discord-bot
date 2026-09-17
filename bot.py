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
        f"👋 Hello {member.mention}!\n\n"
        f"💙 Welcome to **{member.guild.name}**! We're thrilled you've decided to join us.\n\n"
        f"🌟 This server is all about building a friendly, active, "
        f"and respectful community where everyone feels welcome.\n\n"
        f"✨ **Here's how to get started:**\n"
        f"• 📜 Read the server rules.\n"
        f"• 🎮 Pick your notification and game roles.\n"
        f"• 🙋 Introduce yourself.\n"
        f"• 💬 Join the conversation and have fun!\n\n"
        f"💬 **Chat Zone** → #general-chat\n"
        f"📜 **Rules** → #rules\n\n"
        f"❓ If you have any questions or need assistance, "
        f"our staff team is always happy to help.\n\n"
        f"❤️ Enjoy your stay and have fun with the community!\n\n"
        f"🎉 Once again, **welcome to the family!**"
    ),
    color=discord.Color.blue()
)

# 👤 New member's profile picture
embed.set_thumbnail(url=member.display_avatar.url)

# 🏠 Server icon
if member.guild.icon:
    embed.set_author(
        name=member.guild.name,
        icon_url=member.guild.icon.url
    )

# 👥 Member count
embed.add_field(
    name="👥 Members",
    value=f"**{member.guild.member_count}**",
    inline=True
)

# 👤 New member
embed.add_field(
    name="👤 New Member",
    value=f"**{member.name}**",
    inline=True
)

# 🏠 Server icon in footer
if member.guild.icon:
    embed.set_footer(
        text=f"Welcome to {member.guild.name}",
        icon_url=member.guild.icon.url
    )
else:
    embed.set_footer(
        text=f"Welcome to {member.guild.name}"
    )

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
