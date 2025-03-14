    @app_commands.command(name="help", description="Show all available ticket commands with detailed panel information")
    async def help(self, interaction: discord.Interaction):
        """Show all available ticket commands with detailed panel information"""
        await interaction.response.defer(ephemeral=True)
        
        # Check if user is staff
        is_staff = await self.permissions.is_ticket_staff(interaction.guild, interaction.user)
        is_admin = interaction.user.guild_permissions.administrator
        
        # Import panel colors and info
        panel_embeds = PanelEmbeds()
        
        # Use the support color for help
        embed = discord.Embed(
            title="📚 Ticket System Help",
            description="**Système avancé de tickets avec panels par catégorie**\n\nVoici les commandes disponibles :",
            color=panel_embeds.colors.get('SUPPORT', discord.Color.blue())
        )
        
        # User commands
        embed.add_field(
            name="🧑‍💼 Commandes Utilisateur",
            value=(
                "`/openticket <raison>` - Ouvrir manuellement un ticket\n"
                "`/close` - Fermer le ticket actuel\n"
                "`/help` - Afficher cette aide"
            ),
            inline=False
        )
        
        # Staff commands
        if is_staff:
            embed.add_field(
                name="👮 Commandes Staff",
                value=(
                    "`/forceclose <ticket>` - Forcer la fermeture d'un ticket\n"
                    "`/add <utilisateur>` - Ajouter un utilisateur au ticket\n"
                    "`/remove <utilisateur>` - Retirer un utilisateur du ticket\n"
                    "`/rename <nouveau_nom>` - Renommer un ticket\n"
                    "`/transfer <staff>` - Transférer un ticket à un autre membre du staff\n"
                    "`/listtickets` - Lister tous les tickets ouverts"
                ),
                inline=False
            )
        
        # Admin commands
        if is_admin:
            embed.add_field(
                name="🔧 Commandes Admin",
                value=(
                    "`/setup` - Configurer le système de tickets\n"
                    "`/setstaff <role>` - Définir le rôle staff\n"
                    "`/setcategory <nom>` - Définir la catégorie de tickets\n"
                    "`/setlogchannel <salon>` - Définir le salon des logs\n"
                    "`/setarchivechannel <salon>` - Définir le salon d'archives\n"
                    "`/addpanel <nom> <catégorie> <question>` - Ajouter un nouveau panel de tickets\n"
                    "`/setpanel <catégorie> <question>` - Personnaliser le panel par défaut\n"
                    "`/addtemplate <nom> <catégorie> <message>` - Créer un modèle de ticket\n"
                    "`/addfield <modèle> <nom> <label> <type>` - Ajouter un champ à un modèle\n"
                    "`/listtemplates` - Lister tous les modèles de tickets"
                ),
                inline=False
            )
            
        # Get panels from database
        panels = await self.db.get_all_panels(interaction.guild.id)
        
        # Categories section
        if panels:
            categories = {}
            for panel in panels:
                category = panel.get('category', 'default')
                if category not in categories:
                    categories[category] = []
                categories[category].append(panel)
            
            # Add field for each category
            for category, category_panels in categories.items():
                emoji = panel_embeds.emoji.get(category, panel_embeds.emoji['default'])
                panel_names = ", ".join([f"`{p['name']}`" for p in category_panels])
                
                embed.add_field(
                    name=f"{emoji} Catégorie: {category}",
                    value=(
                        f"{panel_embeds.descriptions.get(category, '')}\n\n"
                        f"**Panels disponibles:** {panel_names}"
                    ),
                    inline=False
                )
        else:
            embed.add_field(
                name="🎫 Panels de Tickets",
                value="Aucun panel configuré. Utilisez `/setup` pour configurer le système avec les panels par défaut.",
                inline=False
            )
        
        embed.set_footer(text="Les utilisateurs peuvent créer des tickets via les boutons dans le salon de création de tickets")
        await interaction.followup.send(embed=embed)