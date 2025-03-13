# Guide de démarrage rapide

Ce guide vous aidera à configurer et utiliser rapidement le bot de tickets Discord.

## Configuration initiale

1. **Inviter le bot sur votre serveur**
   - Utilisez le lien d'invitation généré dans le [portail des développeurs Discord](https://discord.com/developers/applications)
   - Assurez-vous de donner les permissions nécessaires (gestion des canaux, rôles, messages, etc.)

2. **Configuration du système de tickets**
   - Utilisez la commande `/setup` pour créer automatiquement les catégories et canaux nécessaires
   - Définissez le rôle staff avec `/setstaff @role`
   - Configurez le nombre maximum de tickets par utilisateur avec `/setmaxtickets nombre` (par défaut: 5)

## Configuration des catégories

Le bot supporte quatre catégories principales:
- **RECRUTEMENT**: Pour les candidatures de recrutement
- **SIGNALEMENT**: Pour signaler des problèmes ou des utilisateurs
- **SUPPORT**: Pour obtenir de l'aide
- **GIVEAWAY**: Pour les concours et distributions

Configurez les catégories avec:
```
/setcategorychannel type nom
```
Où "type" est le type de ticket (recrutement, signalement, support, giveaway) et "nom" est le nom de la catégorie Discord.

## Création de panels de tickets

Vous pouvez créer des messages avec des boutons pour ouvrir des tickets:

```
/createticketmessage catégorie message
```

Cela créera un message avec un bouton qui, lorsqu'il est cliqué, ouvrira un ticket dans la catégorie spécifiée.

## Gestion quotidienne

- `/close` - Ferme le ticket actuel (demande une raison)
- `/add @utilisateur` - Ajoute un utilisateur au ticket
- `/remove @utilisateur` - Retire un utilisateur du ticket
- `/rename nouveau_nom` - Renomme le ticket
- `/listtickets` - Liste tous les tickets ouverts

## Personnalisation avancée

Pour personnaliser davantage votre système de tickets, consultez le fichier README.md pour des commandes plus avancées comme:
- Création de panels personnalisés
- Configuration de templates
- Ajout de champs personnalisés
- Et plus encore!