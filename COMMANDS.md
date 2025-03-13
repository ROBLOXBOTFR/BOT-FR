# Liste des commandes

Ce document liste toutes les commandes disponibles dans le bot de tickets avec leurs descriptions et usages.

## Commandes de configuration

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/setup` | Configure le système de tickets | `/setup` |
| `/setstaff @role` | Définit le rôle staff | `/setstaff @Support Team` |
| `/setmaxtickets nombre` | Définit le nombre max de tickets par utilisateur | `/setmaxtickets 3` |
| `/setcategory nom` | Définit la catégorie par défaut (legacy) | `/setcategory Tickets` |
| `/setcategorychannel type nom` | Définit la catégorie pour un type de ticket | `/setcategorychannel recrutement Recrutements` |
| `/setlogchannel #channel` | Définit le canal de logs | `/setlogchannel #ticket-logs` |
| `/setarchivechannel #channel` | Définit le canal d'archives | `/setarchivechannel #archives` |

## Commandes de tickets

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/openticket raison [catégorie]` | Ouvre un ticket manuellement | `/openticket J'ai besoin d'aide avec mon achat support` |
| `/close` | Ferme le ticket actuel | `/close` |
| `/forceclose #channel` | Force la fermeture d'un ticket | `/forceclose #ticket-user-123` |
| `/add @user` | Ajoute un utilisateur au ticket | `/add @User123` |
| `/remove @user` | Retire un utilisateur du ticket | `/remove @User123` |
| `/rename nouveau_nom` | Renomme le ticket | `/rename urgent-support` |
| `/transfer @staff` | Transfère le ticket à un autre staff | `/transfer @Admin123` |
| `/listtickets` | Liste tous les tickets ouverts | `/listtickets` |

## Commandes de panels

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/setpanel catégorie question` | Définit une question pour une catégorie | `/setpanel support Quel est votre problème ?` |
| `/addpanel nom catégorie question` | Ajoute un nouveau panel | `/addpanel bug-report signalement Décrivez le bug rencontré` |
| `/listpanels` | Liste tous les panels | `/listpanels` |
| `/removepanel nom` | Supprime un panel | `/removepanel bug-report` |

## Commandes de templates

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/addtemplate nom catégorie message` | Crée un template | `/addtemplate recrutement-staff recrutement Bienvenue dans votre candidature` |
| `/addfield nom label type requis` | Ajoute un champ à un template | `/addfield recrutement-staff experience Quelle est votre expérience ? paragraphe true` |
| `/listtemplates` | Liste tous les templates | `/listtemplates` |
| `/removetemplate nom` | Supprime un template | `/removetemplate recrutement-staff` |
| `/removefield nom champ` | Supprime un champ d'un template | `/removefield recrutement-staff experience` |

## Autres commandes

| Commande | Description | Exemple |
|----------|-------------|---------|
| `/createticketmessage catégorie message` | Crée un message avec bouton de ticket | `/createticketmessage support Cliquez pour ouvrir un ticket de support` |
| `/help` | Affiche l'aide et toutes les commandes | `/help` |
| `/cleanserver` | Nettoie le serveur (attention !) | `/cleanserver` |