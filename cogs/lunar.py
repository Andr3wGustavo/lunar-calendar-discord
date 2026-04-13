import discord
from discord import app_commands
from discord.ext import commands, tasks
from utils.db import get_guild_channel, set_guild_channel, get_all_guilds
from utils.lunar_calc import lunar_calc
from datetime import datetime, time, timezone

class PainelView(discord.ui.View):
    def __init__(self, bot, target_channel):
        super().__init__(timeout=None)
        self.bot = bot
        self.target_channel = target_channel

    @discord.ui.button(label="Force Matrix Drop", style=discord.ButtonStyle.blurple, emoji="🌌")
    async def force_drop(self, interaction: discord.Interaction, button: discord.ui.Button):
        # We fetch the lunar cog and call the raw create embed function
        cog = self.bot.get_cog('LunarCog')
        if cog:
            embed = cog.create_lunar_embed()
            await self.target_channel.send(embed=embed)
            await interaction.response.send_message("Matrix Drop successfully forced to the channel.", ephemeral=True)
        else:
            await interaction.response.send_message("Error communicating with Lunar Engine.", ephemeral=True)

class LunarCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.daily_lunar_update.start()

    def cog_unload(self):
        self.daily_lunar_update.cancel()

    def create_lunar_embed(self):
        data = lunar_calc.get_lunar_data()
        
        # Color mapping based on waxing or waning
        color = discord.Color.dark_theme()
        if data['illumination'] > 90:
            color = discord.Color.light_grey()
        elif data['illumination'] < 10:
            color = discord.Color.darker_grey()

        embed = discord.Embed(
            title=f"🌙 Daily Lunar Matrix Report - {data['phase_name']}",
            description="Aligning 3D Maya with celestial frequencies.",
            color=color,
            timestamp=datetime.now(timezone.utc)
        )

        embed.add_field(name="Illumination", value=f"{data['illumination']}%", inline=True)
        embed.add_field(name="Current Zodiac (Tropical)", value=f"**{data['zodiac_sign']}**", inline=True)
        embed.add_field(name="Vedic Nakshatra (Sidereal)", value=f"**{data['nakshatra']}**", inline=True)

        embed.add_field(
            name="Spiritual Geometry (Maya 3D)", 
            value=f"Earth Distance: {data['distance_km']} km\nSun-Moon Angle: {data['angle_diff']}°\nVedic Cycle: {data['tithi_paksha']} (Tithi {data['tithi_number']})",
            inline=False
        )

        val_spiritual = f"*{data['spiritual_message']}*"
        if data['tithi_event']:
             val_spiritual += f"\n\n{data['tithi_event']}"
        if data['eclipse_alert']:
             val_spiritual += f"\n\n{data['eclipse_alert']}"
        if data['retrograde_alert']:
             val_spiritual += f"\n\n{data['retrograde_alert']}"

        embed.add_field(
            name="Mystic Yogi Alignment",
            value=val_spiritual,
            inline=False
        )

        embed.set_footer(text="Perfect Lunar Bot • Astrological Precision")
        return embed

    # Task runs every day at 12:00 PM UTC
    @tasks.loop(time=time(hour=12, minute=0, tzinfo=timezone.utc))
    async def daily_lunar_update(self):
        guilds = await get_all_guilds()
        embed = self.create_lunar_embed()
        
        for guild_id, channel_id in guilds:
            channel = self.bot.get_channel(channel_id)
            if channel:
                try:
                    await channel.send(embed=embed)
                except discord.Forbidden:
                    pass

    @daily_lunar_update.before_loop
    async def before_lunar_update(self):
        await self.bot.wait_until_ready()

    @app_commands.command(name="painel", description="Configure the Discord Lunar Matrix Engine Panel")
    @app_commands.describe(channel="Select the channel for daily lunar drops")
    @app_commands.default_permissions(manage_guild=True)
    async def painel(self, interaction: discord.Interaction, channel: discord.TextChannel = None):
        target_channel = channel or interaction.channel
        await set_guild_channel(interaction.guild_id, target_channel.id)
        
        embed = discord.Embed(
            title="🌌 Lunar Engine Admin Panel",
            description=f"Matrix coordinates synced. Daily drops will be deployed to {target_channel.mention} at 12:00 PM UTC.",
            color=discord.Color.brand_green()
        )
        
        # Displaying System Sensors
        sensors = (
            "✅ **Orbital Distance (Maya 3D)**\n"
            "✅ **Vedic Nakshatras & Yogic Map**\n"
            "✅ **Tithi Scanner (Ekadashi/Purnima)**\n"
            "✅ **Ocult Node Eclipses (Rahu/Ketu)**\n"
            "✅ **Planetary Retrogrades (Geocentric)**"
        )
        embed.add_field(name="Active Cyber-Mystic Sensors", value=sensors, inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        embed.set_footer(text="System fully operational.")
        
        view = PainelView(self.bot, target_channel)
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

    @app_commands.command(name="moon", description="Get the exact current lunar state instantly")
    async def moon(self, interaction: discord.Interaction):
        embed = self.create_lunar_embed()
        await interaction.response.send_message(embed=embed)

    @app_commands.command(name="nakshatra", description="Query the ancient Vedic mystic meaning of a Lunar Mansion")
    @app_commands.describe(mansion="Name of the Nakshatra (e.g., Ashwini)")
    async def nakshatra(self, interaction: discord.Interaction, mansion: str):
        mansion = mansion.title().strip()
        if mansion not in lunar_calc.nakshatra_meanings:
            await interaction.response.send_message(f"❌ Nakshatra '{mansion}' not found in the Maya Matrix. Try checking spelling.", ephemeral=True)
            return
            
        desc = lunar_calc.nakshatra_meanings[mansion]
        # Calculate roughly which order it is
        index = lunar_calc.nakshatras.index(mansion) + 1
        
        embed = discord.Embed(
            title=f"🌌 Jyotish Matrix: {mansion}",
            description=f"**Mansion #{index} of 27**\n\n*Spiritual Blueprint:*\n{desc}",
            color=discord.Color.purple()
        )
        embed.set_footer(text="Mystic Yogi Alignment • Maya 3D Engine")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(LunarCog(bot))
