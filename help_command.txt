    @app_commands.command(name="help", description="Show all available ticket commands")
    async def help(self, interaction: discord.Interaction):
        """Show all available ticket commands"""
        await interaction.response.defer(ephemeral=True)
        
        # Check if user is staff
        is_staff = await self.permissions.is_ticket_staff(interaction.guild, interaction.user)
        is_admin = interaction.user.guild_permissions.administrator
        
        # Importer les couleurs des panels
        from utils.panel_embeds import PanelEmbeds
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
                    "`/setcategory <name>` - Set the ticket category\n"
                    "`/setlogchannel <channel>` - Set the log channel\n"
                    "`/setarchivechannel <channel>` - Set the archive channel"
                ),
                inline=False
            )
        
        await interaction.followup.send(embed=embed)
