# Projet Scouting OL - Rayane Ourad

Projet réalisé dans le cadre du Bachelor 3 DBI (2025-2026).

C'est une application web de recrutement développée pour la cellule de scouting de l'Olympique Lyonnais. Elle permet de filtrer des joueurs selon plusieurs critères, d'analyser leurs performances avec des graphiques en radar et de trouver des profils similaires grâce à un algorithme k-NN.

## Organisation du projet

- `backend/` : API FastAPI en Python, base de données SQLite (`recruitment_app.db`) et algorithme k-NN.
- `Frontend/` : Interface web en React (Vite) avec du CSS sur mesure.

## Comment démarrer le projet

### 1. Récupérer le projet
```bash
git clone https://github.com/L3-WEB-2026/web-rayane-ourad.git
cd web-rayane-ourad
```

### 2. Lancer le backend
```bash
cd backend
pip install -r requirements.txt
python main.py
```
L'API tourne sur `http://127.0.0.1:8000`.

### 3. Lancer le frontend
Dans un nouveau terminal :
```bash
cd Frontend
npm install
npm run dev
```
L'application s'ouvre sur `http://localhost:5173`.

## Ce que fait l'application

- **Recherche & Filtres** : par nom, poste, âge, valeur marchande max et note globale.
- **Fiches Joueurs & Radars** : graphique à 6 axes (Finition, Dribble, Passes, Vitesse, Défense, Physique).
- **Jumeaux statistiques (KNN)** : affichage des 4 joueurs les plus proches sur le plan statistique et du standing.
- **Accès par rôle (RBAC)** :
  - `scout1` : accès aux stats sportives (valeurs financières masquées).
  - `directeur` / `rayane` : accès complet avec gestion du budget mercato (45 M€) et simulateur de salaire.

## Données utilisées
Base contenant 2 854 joueurs professionnels des 5 grands championnats (saison 2024-2025).
