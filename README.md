# Recruitment Match - Olympique Lyonnais 🔴🔵

Application web de scouting et d'aide au recrutement réalisée dans le cadre du projet d'évaluation Bachelor 3 DBI (2025-2026).

L'objectif de l'application est d'assister la cellule de recrutement et la direction sportive de l'Olympique Lyonnais dans la détection de profils compatibles, l'analyse comparative de performances (données Opta) et la simulation budgétaire du mercato.

---

## 🛠️ Stack Technique

### Backend (Python & FastAPI)
- **FastAPI** : API REST pour la recherche, l'authentification et le calcul de similarité.
- **SQLite** : Base de données relationnelle locale (`recruitment_app.db`).
- **Passlib & PyJWT** : Gestion des jetons d'accès et sécurité RBAC (Role-Based Access Control).
- **scikit-learn & pandas** : Algorithme des k plus proches voisins (k-NN) et calculs de distance euclidienne pondérée.

### Frontend (React & Vite)
- **React** (avec Hooks `useState`, `useEffect`) : Interface utilisateur réactive.
- **Vanilla CSS** : Design personnalisé sombre (style glassmorphism).
- **Canvas HTML5 / SVG** : Graphiques radars interactifs à 6 axes (Finition, Dribble, Passes, Vitesse, Défense, Physique).

---

## 🔑 Rôles & Authentification (RBAC)

L'application intègre 3 niveaux d'accès distincts :

1. **Recruteur (Scout)** : 
   - Recherche multicritère de joueurs.
   - Visualisation des radars de performance et recherche de jumeaux statistiques (k-NN).
   - *Données financières confidentielles masquées.*

2. **Directeur Sportif** :
   - Accès complet aux fiches joueurs avec valeurs de marché et salaires.
   - Espace **Budget Mercato** : suivi de l'enveloppe globale de transfert (45 M€) et de la masse salariale.
   - Simulateur d'impact financier d'un recrutement en temps réel.

3. **Administrateur** :
   - Accès global et gestion des permissions.

---

## 🚀 Installation & Lancement en local

### 1. Cloner le projet
```bash
git clone https://github.com/L3-WEB-2026/web-rayane-ourad.git
cd web-rayane-ourad
```

### 2. Lancer le Backend (Python FastAPI)
```bash
cd backend
pip install -r requirements.txt
python main.py
```
Le serveur démarre sur `http://127.0.0.1:8000`.

### 3. Lancer le Frontend (React)
```bash
cd ../Frontend
npm install
npm run dev
```
L'application est accessible sur `http://localhost:5173`.

---

## 📊 Jeu de données

La base de données contient **2 854 joueurs professionnels** issus des championnats européens majeurs, enrichis de leurs statistiques réelles de la saison 2024-2025 (données brutes Opta / FBref) :
- Vrais âges et nationalités à jour.
- Statistiques de performance calibrées sur 90 minutes.
- Valeurs de marché réelles et fin de contrats.

---

## 👥 Auteur
Projet réalisé par **Rayane Ourad** — Bachelor 3 Data & Business Intelligence.
