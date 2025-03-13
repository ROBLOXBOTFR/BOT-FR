# Discord Ticket Bot

Un bot Discord avancé de gestion de tickets écrit en Python avec discord.py, offrant une personnalisation complète et une gestion efficace des requêtes utilisateurs.

## Fonctionnalités

- Système de tickets multi-catégories (RECRUTEMENT, SIGNALEMENT, SUPPORT, GIVEAWAY)
- Fermeture de ticket avec raison obligatoire
- Notification automatique par DM lors de la fermeture d'un ticket
- Archivage complet des conversations de tickets
- Panels personnalisables avec questions spécifiques
- Système de rôles staff pour la gestion des permissions
- Limite configurable de tickets simultanés par utilisateur
- Commandes d'administration complètes

## Installation

1. Cloner ce dépôt
   ```
   git clone https://github.com/VOTRE-NOM/discord-ticket-bot.git
   cd discord-ticket-bot
   ```

2. Installer les dépendances
   ```
   pip install -r requirements.txt
   ```

3. Configurer le token dans un fichier `.env` ou une variable d'environnement
   ```
   DISCORD_TOKEN=votre_token_discord
   ```

4. Lancer le bot
   ```
   python main.py
   ```

## Configuration

Le bot peut être configuré avec la commande `/setup` qui créera automatiquement les catégories et canaux nécessaires.

Utilisez `/setstaff @role` pour définir le rôle staff qui aura accès aux commandes d'administration.

## Commandes principales

- `/setup` - Configure les canaux et catégories pour le système de tickets
- `/setstaff @role` - Définit le rôle staff pour la gestion des tickets
- `/setmaxtickets nombre` - Définit le nombre maximum de tickets par utilisateur
- `/setcategorychannel type nom` - Définit la catégorie pour un type de ticket spécifique
- `/openticket raison [catégorie]` - Ouvre un ticket manuellement
- `/close` - Ferme le ticket actuel avec demande de raison obligatoire
- `/forceclose #channel` - Force la fermeture d'un ticket avec raison obligatoire
- `/add @utilisateur` - Ajoute un utilisateur au ticket actuel
- `/remove @utilisateur` - Retire un utilisateur du ticket actuel
- `/listtickets` - Affiche la liste de tous les tickets ouverts

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.