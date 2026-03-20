"""
===========================================
  ULTIMATE DISCORD BOT - by Claude
  Features: Moderation, AutoMod, Tickets,
  Games, Leveling, Welcome, Logging,
  Economy, Music, Giveaways, Reaction Roles
===========================================
"""

import discord
from discord.ext import commands
import asyncio
import json
import os
import logging
from datetime import datetime

# ─── Logging Setup ───────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler('data/bot.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('DiscordBot')

# ─── Config laden ──────────────────────────────────────────
def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

config = load_config()

# ─── Intents ──────────────────────────────────────────────────────────────────
intents = discord.Intents.all()

# ─── Bot-Klasse ───────────────────────────────────────────────────────────────
class UltimateBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or config.get('prefix', '!'),
            intents=intents,
            help_command=None,    # Eigenes Helf-System
            case_insensitive=True,
            strip_after_prefix=True,
        )
        self.config = config
        self.start_time = datetime.utcnow()

    async def setup_hook(self):
        """Wird beim Start ausgeführt - lädt alle Cogs"""
        # Datenordner erstellen
        os.makedirs('data', exist_ok=True)

        cogs = [
            'cogs.moderation',
            'cogs.automod',
            'cogs.tickets',
            'cogs.games',
            'cogs.leveling',
            'cogs.welcome',
            'cogs.logging_cog',
            'cogs.utility',
            'cogs.fun',
            'cogs.economy',
            'cogs.music',
            'cogs.giveaway',
            'cogs.reaction_roles',
        ]

        loaded = 0
        failed = 0
        for cog in cogs:
            try:
                await self.load_extension(cog)
                logger.info(f'✅ Cog geladen: {cog}')
                loaded += 1
            except Exception as e:
                logger.error(f'❌ Fehler beim Laden von {cog}: {e}')
                failed += 1

        logger.info(f'Cogs: {loaded} geladen, {failed} fehlgeschlagen')

        # Slash Commands synchronisieren
        try:
            synced = await self.tree.sync()
            logger.info(f'✅ {len(synced)} Slash Commands synchronisiert')
        except Exception as e:
            logger.error(f'❌ Fehler beim Sync: {e}')

    async def on_ready(self):
        logger.info(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        logger.info(f'  Bot gestartet: {self.user.name}')
        logger.info(f'  Bot ID: {self.user.id}')
        logger.info(f'  Server: {len(self.guilds)}')
        logger.info(f'  Discord.py Version: {discord.__version__}')
        logger.info(f'━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

        # Aktivität setzen
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name=f"{config.get('prefix', '!')}help | {len(self.guilds)} Server"
            ),
            status=discord.Status.online
        )

    async def on_command_error(self, ctx, error):
        """Globaler Error-Handler"""
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title='❌ Keine Berechtigung',
                description='Du hast nicht die nötigen Berechtigungen für diesen Befehl.',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=5)
        elif isinstance(error, commands.BotMissingPermissions):
            embed = discord.Embed(
                title='❌ Bot-Berechtigungen fehlen',
                description=f'Mir fehlen folgende Berechtigungen: `{", ".join(error.missing_permissions)}`',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=5)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                title='❌ Fehlende Argumente',
                description=f'Fehlendes Argument: `{error.param.name}`\nNutze `{self.command_prefix}help {ctx.command.name}` für Hilfe.',
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed, delete_after=8)
        elif isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                title='❌ Ung÷ltiges Argument',
                description=str(error),
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed, delete_after=8)
        elif isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                title='⏱️ Cooldown',
                description=f'Warte noch **{error.retry_after:.1f}** Sekunden.',
                color=discord.Color.orange()
            )
            await ctx.send(embed=embed, delete_after=5)
        elif isinstance(error, commands.CheckFailure):
            return
        else:
            logger.error(f'Unbehandelter Fehler in {ctx.command}: {error}', exc_info=error)
            embed = discord.Embed(
                title='❌ Unerwarteter Fehler',
                description=f'Ein Fehler ist aufgetreten: `{str(error)[:200]}`',
                color=discord.Color.red()
            )
            await ctx.send(embed=embed, delete_after=10)

    async def on_guild_join(self, guild):
        """Bot tritt einem neuen Server bei"""
        logger.info(f'Server beigetreten: {guild.name} ({guild.id})')
        # Willkommensnachricht an Systemkanal
        if guild.system_channel:
            embed = discord.Embed(
                title='👋 Hallo! Danke für die Einladung!',
                description=(
                    f'Ich bin **{self.user.name}**, euer Ultimate Discord Bot!\n\n'
                    f'**Prefix:** `{config.get("prefix", "!")}`\n'
                    f'**Help:** `{config.get("prefix", "!")}help`\n\n'
                    f'Nutze `{config.get("prefix", "!")}setup` um mich einzurichten!'
                ),
                color=discord.Color.blue()
            )
            embed.set_thumbnail(url=self.user.display_avatar.url)
            try:
                await guild.system_channel.send(embed=embed)
            except:
                pass

# ─── Bot starten ──────────────────────────────────────────────────────────────
async def main():
    bot = UltimateBot()

    token = config.get('token')
    if not token or token == 'DEIN_BOT_TOKEN_HIER':
        logger.error("�� Kein Bot-Token in config.json! Bitte trage deinen Token ejȸ�')
        return

    async with bot:
        await bot.start(token)

if __name__ == '__main__':
    asyncio.run(main())
