# Guide de contribution

Nous sommes ravis que vous souhaitiez contribuer au bot de tickets Discord ! Voici quelques lignes directrices pour faciliter votre contribution.

## Comment contribuer

1. **Signaler des bugs**
   - Vérifiez d'abord que le bug n'a pas déjà été signalé
   - Utilisez le modèle de rapport de bug pour fournir toutes les informations nécessaires
   - Incluez des étapes détaillées pour reproduire le problème

2. **Proposer des fonctionnalités**
   - Décrivez clairement la fonctionnalité et son cas d'utilisation
   - Expliquez comment cette fonctionnalité bénéficierait à tous les utilisateurs

3. **Soumettre des pull requests**
   - Forkez le dépôt
   - Créez une branche pour votre fonctionnalité (`git checkout -b feature/amazing-feature`)
   - Committez vos changements (`git commit -m 'Add some amazing feature'`)
   - Poussez vers la branche (`git push origin feature/amazing-feature`)
   - Ouvrez une Pull Request

## Standards de code

- Respectez les conventions PEP 8 pour le code Python
- Ajoutez des commentaires et des docstrings pour documenter votre code
- Écrivez des messages de commit clairs et descriptifs
- Maintenez une couverture de tests pour votre code

## Structure du projet

```
discord-ticket-bot/
├── main.py              # Point d'entrée principal
├── bot.py               # Définition de la classe TicketBot
├── cogs/                # Modules de commandes
│   ├── ticket_commands.py  # Commandes administratives
│   └── ticket_system.py    # Système de tickets (boutons, interactions)
├── utils/               # Utilitaires et helpers
│   ├── database.py      # Gestion de la base de données
│   ├── config.py        # Gestion de la configuration
│   ├── embeds.py        # Création d'embeds Discord
│   ├── permissions.py   # Gestion des permissions
│   ├── panel_embeds.py  # Embeds pour les panels
│   └── ticket_utils.py  # Utilitaires pour les tickets
└── ...
```

## Processus de développement

1. **Choisir une issue** - Regardez les issues ouvertes ou créez-en une nouvelle
2. **Discuter** - Discutez de votre approche dans l'issue avant de commencer à coder
3. **Développer** - Écrivez votre code et testez-le soigneusement
4. **Soumettre** - Créez une PR et attendez la review

Merci de contribuer à améliorer ce projet !