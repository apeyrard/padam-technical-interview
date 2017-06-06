# Exercice :

- Sur la thématique de Padam, créer un système de réservation très simplifié permettant à un client de réserver une voiture pour effectuer un trajet.
- Pour vous faire gagner du temps, et parce que vous n'arriverez pas sur un projet vierge, une base de code vous est fournie. Elle est de mauvaise qualité, et vous avez carte blanche pour l'améliorer et la rendre 'production ready'. Cette étape de refactoring est une partie intégrante de l'exercice.


## Le site devra permettre à un client :

- de s'inscrire, se connecter, se déconnecter.
- de créer, voir, et supprimer des réservations.
- de connaître le temps de parcours de sa réservation


## Pour cadrer et simplifier l'exercice, on partira des principes suivants :

- Un trajet est possible avec n'importe quel point de départ/arrivée sur Terre, et est disponible à tout moment (cependant, la voiture doit bien sûr être disponible à ce moment là).
- Une voiture n'accepte qu'un seul client par trajet.
- Une réservation est gratuite (ne nécessite pas de paiement).
- Il n'est pas nécessaire de permettre la création de voitures via le site. A la place, on pourra par exemple en créer quelques unes directement via un script d’initialisation.


# Instructions et conseils généraux :

- Un projet Django, hébergé sur Github, avec une BDD sqlite (commitée), est attendu.
- Il n'y a pas de deadline, mais idéalement le projet ne devrait pas prendre plus de 2 jours à réaliser.
- Mettre l'accent sur le back-end. Le front-end est moins important pour le poste en question.
- Ne pas hésiter à utiliser des mécanismes propres à Django si besoin (ex : signaux, override de save(), CBVs, extensions, etc.).
- Ne pas hésiter à laisser des commentaires (ou un document) pour expliquer les choix techniques (eg: expliquer les bénéfices / contraintes de telle ou telle solution)
- Certains aspects sont volontairement vagues pour vous laisser une liberté de choix.
- Si vous ne disposez que de peu de temps pour réaliser l'exercice, concentrez-vous sur la qualité plutôt que la quantité. A l'inverse, si vous avez du temps, tout bonus sera apprécié.
- Ne pas hésiter à nous poser des questions si besoin (rafik@padam.io et/ou nathan@padam.io).
