"""
Reaction Roles Cog
Features: Reaktionsrollen hinzufügen/entfernen, automatische Rollenvergabe
"""

import discord
from discord.ext import commands
import database as db


class ReactionRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def cog_load(self):
        print('✅ Reaction Roles Cog geladen')

    # ─── REAKTION HINZUFÜGEN ───────────────────────────────────────────────
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        if payload.user_id == self.bot.user.id:
            return
        if not payload.guild_id:
            return

        role_id = await db.get_reaction_role(payload.message_id, str(payload.emoji))
        if not role_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        role = guild.get_role(role_id)
        if not role:
            return

        try:
            await member.add_roles(role, reason='Reaction Role')
        except discord.Forbidden:
            pass

    # ─── REAKTION ENTFERNEN ────────────────────────────────────────────────
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        if not payload.guild_id:
            return

        role_id = await db.get_reaction_role(payload.message_id, str(payload.emoji))
        if not role_id:
            return

        guild = self.bot.get_guild(payload.guild_id)
        if not guild:
            return

        member = guild.get_member(payload.user_id)
        if not member or member.bot:
            return

        role = guild.get_role(role_id)
        if not role:
            return

        try:
            await member.remove_roles(role, reason='Reaction Role entfernt')
        except discord.Forbidden:
            pass

async def setup(bot):
    await bot.add_cog(ReactionRoles(bot))
