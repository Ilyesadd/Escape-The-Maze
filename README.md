# Escape the Maze

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.5.2-green.svg)
![License](https://img.shields.io/badge/License-Open-brightgreen.svg)

Escape the Maze est un jeu vidéo en 2D où le joueur contrôle un personnage devant résoudre des labyrinthes complexes tout en évitant des obstacles et des ennemis. Le jeu utilise Python et Pygame pour gérer les graphismes, les collisions et les mécaniques de jeu.

## 🎮 Fonctionnalités

- **Mécaniques de jeu** :
  - Contrôle fluide du personnage à l'aide des touches directionnelles
  - Labyrinthes générés aléatoirement grâce à l'algorithme de backtracking
  - Éléments interactifs : clés, portes, ennemis, et objets bonus

- **Graphismes** :
  - Sprites 2D simples pour les personnages et les objets
  - Effets visuels gérés avec Pygame (animations, transitions entre niveaux)

- **Système de progression** :
  - Score dynamique affiché à l'écran, basé sur le temps et les bonus collectés
  - Déblocage progressif de niveaux avec des labyrinthes plus complexes

- **Sons et Musique** :
  - Sons interactifs (pas, ennemis, et ouverture de portes)
  - Musique de fond immersive

## 🚀 Installation

1. Assurez-vous d'avoir Python 3.6 ou supérieur installé sur votre système
2. Installez Pygame en utilisant pip :
   ```
   pip install pygame
   ```
3. Clonez ou téléchargez ce dépôt
   ```
   git clone https://github.com/ilyesadd/escape-the-maze.git
   cd escape-the-maze
   ```
4. Exécutez le jeu :
   ```
   python main.py
   ```

## 🎯 Comment jouer

- Utilisez les touches fléchées (↑, ↓, ←, →) pour déplacer votre personnage
- Collectez la clé pour pouvoir ouvrir la porte de sortie
- Évitez les ennemis rouges qui se déplacent dans le labyrinthe
- Ramassez les bonus verts pour augmenter votre score
- Atteignez la porte de sortie pour passer au niveau suivant
- Appuyez sur Échap pour mettre le jeu en pause
- Appuyez sur R pour redémarrer le niveau

## 📁 Structure du projet

```
Escape the Maze/
├── main.py                 # Point d'entrée du jeu
├── game/
│   ├── __init__.py        # Package game
│   ├── game_manager.py    # Gestionnaire de jeu
│   ├── maze.py            # Génération et rendu du labyrinthe
│   ├── player.py          # Classe du joueur
│   ├── entities/          # Entités du jeu
│   │   ├── __init__.py    # Package entities
│   │   ├── enemy.py       # Classe des ennemis
│   │   └── item.py        # Classes des objets (clé, porte, bonus)
│   └── states/            # États du jeu
│       ├── __init__.py    # Package states
│       ├── menu_state.py  # État du menu principal
│       ├── play_state.py  # État de jeu principal
│       └── game_over_state.py # État de fin de jeu
```



## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/amazing-feature`)
3. Committez vos changements (`git commit -m 'Add some amazing feature'`)
4. Poussez vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence libre, vous pouvez l'utiliser et le modifier comme bon vous semble.

---

Développé avec ❤️ en Python