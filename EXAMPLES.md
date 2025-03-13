# Exemples d'utilisation

Ce document présente des exemples pratiques pour configurer et utiliser le bot de tickets.

## Mise en place initiale

### Étape 1: Configurer le système de tickets

```
/setup
```

Cette commande crée automatiquement:
- Les catégories Discord pour chaque type de ticket
- Un canal pour les logs de tickets
- Un canal pour les archives

### Étape 2: Définir le rôle staff

```
/setstaff @Support
```

Cette commande donne au rôle "Support" l'accès aux fonctionnalités d'administration du bot.

### Étape 3: Configurer les catégories (optionnel si vous utilisez /setup)

```
/setcategorychannel recrutement RECRUTEMENT
/setcategorychannel signalement SIGNALEMENT
/setcategorychannel support SUPPORT
/setcategorychannel giveaway GIVEAWAY
```

## Création de panels de tickets

### Exemple 1: Panel de support simple

```
/createticketmessage support Besoin d'aide ? Cliquez sur le bouton ci-dessous pour ouvrir un ticket.
```

### Exemple 2: Panel personnalisé avec question spécifique

```
/addpanel probleme-technique support Comment pouvons-nous vous aider avec votre problème technique ?
```

Puis créer un message pointant vers ce panel:
```
/createticketmessage support Pour les problèmes techniques, utilisez ce bouton.
```

## Gestion des tickets

### Fermer un ticket

Depuis un canal de ticket:
```
/close
```

Le bot demandera une raison de fermeture obligatoire.

### Ajouter un utilisateur à un ticket

```
/add @Utilisateur
```

### Retirer un utilisateur d'un ticket

```
/remove @Utilisateur
```

### Renommer un ticket

```
/rename probleme-urgent
```

## Utilisation de templates

### Créer un template pour les recrutements

```
/addtemplate recrutement-staff recrutement Bienvenue dans votre candidature pour rejoindre notre équipe!
```

### Ajouter des champs au template

```
/addfield recrutement-staff experience Quelle est votre expérience? paragraphe true
/addfield recrutement-staff age Quel âge avez-vous? court true
/addfield recrutement-staff disponibilite Quelles sont vos disponibilités? paragraphe true
```

## Exemples de personnalisation avancée

### Configuration de nombre maximum de tickets par utilisateur

```
/setmaxtickets 3
```

### Création d'un panel pour signalements avec question spécifique

```
/addpanel signalement-membre signalement Quel membre souhaitez-vous signaler et pourquoi ?
```

### Création d'un panel pour les candidatures

```
/addpanel recrutement-admin recrutement Pourquoi souhaitez-vous rejoindre notre équipe d'administration ?
```