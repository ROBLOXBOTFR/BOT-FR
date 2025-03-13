import discord
from discord import app_commands
from discord.ext import commands
import logging
import asyncio
from typing import Optional, Union

from utils.database import DatabaseManager
from utils.ticket_utils import TicketUtils
from utils.embeds import Embeds
from utils.permissions import PermissionHelper
from utils.panel_embeds import PanelEmbeds

logger = logging.getLogger(__name__)

class TicketCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = DatabaseManager()
        self.ticket_utils = TicketUtils(bot)
        self.embeds = Embeds()
        self.permissions = PermissionHelper(bot)
        
    @app_commands.command(name="help", description="Show all available ticket commands")
    async def help(self, interaction: discord.Interaction):
        """Show all available ticket commands with detailed panel information"""
        await interaction.response.defer(ephemeral=True)
        
        # Check if user is staff
        is_staff = await self.permissions.is_ticket_staff(interaction.guild, interaction.user)
        is_admin = interaction.user.guild_permissions.administrator
        
        # Importer les couleurs des panels
        panel_embeds = PanelEmbeds()
        
        # Utiliser une couleur par défaut ou celle du support
        embed = discord.Embed(
            title="Ticket System Help",
            description="Here are all the available commands:",
            color=panel_embeds.colors.get('SUPPORT', discord.Color.blue())
        )
        
        # User commands
        embed.add_field(
            name="User Commands",
            value=(
                "`/openticket <reason>` - Manually open a ticket\n"
                "`/close` - Close the current ticket\n"
                "`/help` - Show this help message"
            ),
            inline=False
        )
        
        # Staff commands
        if is_staff:
            embed.add_field(
                name="Staff Commands",
                value=(
                    "`/forceclose <ticket>` - Force close a ticket\n"
                    "`/add <user>` - Add a user to a ticket\n"
                    "`/remove <user>` - Remove a user from a ticket\n"
                    "`/rename <new_name>` - Rename a ticket\n"
                    "`/transfer <staff>` - Transfer a ticket to another staff member\n"
                    "`/listtickets` - List all open tickets"
                ),
                inline=False
            )
        
        # Admin commands
        if is_admin:
            embed.add_field(
                name="Admin Commands",
                value=(
                    "`/setup` - Setup the ticket system\n"
                    "`/setstaff <role>` - Set the staff role\n"
                    "`/setcategory <n>` - Set the ticket category\n"
                    "`/setlogchannel <channel>` - Set the log channel\n"
                    "`/setarchivechannel <channel>` - Set the archive channel"
                ),
                inline=False
            )
            
            # Template and panel commands
            embed.add_field(
                name="Template & Panel Commands",
                value=(
                    "`/setpanel <category> <question>` - Set default panel for a category\n"
                    "`/addpanel <n> <category> <question>` - Create a custom panel\n"
                    "`/addtemplate <n> <category> <welcome>` - Create a ticket template\n"
                    "`/addfield <template> <n> <label> <type>` - Add field to a template\n"
                    "`/listtemplates` - List all ticket templates"
                ),
                inline=False
            )
        
        # Ajouter des informations sur les catégories disponibles
        embed.add_field(
            name="📋 Available Categories",
            value=(
                f"{panel_embeds.emoji.get('RECRUTEMENT')} **RECRUTEMENT** - Pour candidater à un poste\n"
                f"{panel_embeds.emoji.get('SIGNALEMENT')} **SIGNALEMENT** - Pour signaler un problème ou un utilisateur\n"
                f"{panel_embeds.emoji.get('SUPPORT')} **SUPPORT** - Pour demander de l'aide technique\n"
                f"{panel_embeds.emoji.get('GIVEAWAY')} **GIVEAWAY** - Pour proposer un cadeau à la communauté"
            ),
            inline=False
        )
        
        # Ajouter des informations sur le fonctionnement des panels
        embed.add_field(
            name="🔍 About Panels",
            value=(
                "Les panels sont des interfaces personnalisées pour créer des tickets.\n"
                "- Chaque catégorie peut avoir plusieurs panels\n"
                "- Les panels adaptent les questions aux besoins spécifiques\n"
                "- Les administrateurs peuvent créer de nouveaux panels avec `/addpanel`\n"
                "- Chaque panel a un design visuel adapté à sa catégorie"
            ),
            inline=False
        )
        
        embed.set_footer(text="Ticket System v1.0 | Developed with ❤️")
        
        await interaction.followup.send(embed=embed)
async def setup(bot):
    await bot.add_cog(TicketCommands(bot))
