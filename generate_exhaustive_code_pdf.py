import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

def build_pdf():
    pdf_path = r"C:\Users\user\OneDrive\Documents\Guide_Explication_Code_Projet_OL.pdf"
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#0f172a'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#0284c7'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=10
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontSize=12,
        leading=15,
        textColor=colors.HexColor('#0f172a'),
        fontName='Helvetica-Bold',
        spaceBefore=10,
        spaceAfter=4
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#0369a1'),
        fontName='Helvetica-Bold',
        spaceBefore=8,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#334155'),
        alignment=TA_LEFT,
        fontName='Helvetica',
        spaceAfter=3
    )

    code_style = ParagraphStyle(
        'CodeStyleCustom',
        parent=styles['Normal'],
        fontSize=7.5,
        leading=10,
        textColor=colors.HexColor('#0f172a'),
        fontName='Courier',
        spaceBefore=2,
        spaceAfter=3
    )

    story = []

    # En-tête
    story.append(Paragraph("DÉCRYPTAGE LIGNE PAR LIGNE DU CODE SOURCE (BACKEND & FRONTEND)", title_style))
    story.append(Paragraph("PROJECT RECRUITMENT MATCH - OLYMPIQUE LYONNAIS", subtitle_style))
    story.append(Paragraph("<b>Auteur :</b> Rayane Ourad — <b>Bachelor 3 Data & Business Intelligence</b> (2025-2026)", body_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284c7'), spaceAfter=8))

    # SECTION BACKEND
    story.append(Paragraph("PARTIE 1 : DÉCRYPTAGE DU BACKEND (PYTHON / FASTAPI / SQLITE)", h1_style))

    # main.py
    story.append(Paragraph("📄 Fichier : <code>backend/main.py</code>", h2_style))
    main_lines = [
        ("L. 1 - 7", "import fastapi, jwt, datetime...", "Importation des modules requis : FastAPI pour créer le serveur Web, PyJWT pour générer les jetons d'accès sécurisés, et Passlib pour hacher les mots de passe."),
        ("L. 9 - 12", "app = FastAPI(title='Recruitment OL')", "Instanciation de l'application FastAPI. C'est l'objet `app` qui recevra toutes les requêtes HTTP envoyées par React."),
        ("L. 14 - 21", "app.add_middleware(CORSMiddleware...)", "Configuration CORS. Autorise le navigateur web (localhost:5173 ou Vercel) à envoyer des requêtes AJAX au serveur sans être bloqué par la sécurité Same-Origin Policy."),
        ("L. 23 - 25", "pwd_context = CryptContext(schemes=['bcrypt'])", "Initialisation de l'algorithme de hachage Bcrypt. Aucun mot de passe n'est stocké en clair dans la base de données SQLite."),
        ("L. 27 - 35", "def create_access_token(data, expires_delta)", "Fonction qui fabrique le jeton JWT. Elle encode l'identifiant et le rôle de l'utilisateur avec une clé secrète et une date d'expiration (ex: 30 min)."),
        ("L. 37 - 55", "@app.post('/login')", "Endpoint de connexion. Reçoit `username` et `password` via formulaire. Il cherche l'utilisateur avec `database.get_user()`, valide le mot de passe hashé avec `pwd_context.verify()` et renvoie le jeton JWT Bearer."),
        ("L. 57 - 78", "@app.get('/players/search')", "Endpoint de recherche des joueurs. Lit les paramètres HTTP de l'URL (`query`, `position`, `min_age`, `max_age`, `max_value`, `min_overall`) et appelle `database.search_players_matching()`."),
        ("L. 80 - 105", "@app.get('/players/{player_id}/similar')", "Endpoint de l'algorithme KNN (k-NN). Récupère le joueur cible, filtre les candidats du même poste et calcule la distance euclidienne pondérée sur les 6 axes Opta et la valeur marchande."),
        ("L. 107 - 120", "@app.get('/director/budget')", "Endpoint d'accès restreint au budget. Inspecte le token JWT. Si `role == 'scout'`, renvoie `HTTP 403 Forbidden`. Si `role == 'director'`, renvoie l'enveloppe de 45 M€.")
    ]

    t_main = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in main_lines], colWidths=[55, 150, 305])
    t_main.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_main)
    story.append(Spacer(1, 6))

    # database.py
    story.append(Paragraph("📄 Fichier : <code>backend/database.py</code>", h2_style))
    db_lines = [
        ("L. 1 - 5", "import sqlite3", "Importation du pilote natif SQLite3 pour interagir avec la base de données locale."),
        ("L. 7 - 12", "def get_connection()", "Ouvre la connexion vers `data/recruitment_app.db` et active `conn.row_factory = sqlite3.Row` pour pouvoir accéder aux colonnes par leur nom (ex: `row['name']`)."),
        ("L. 14 - 35", "def create_db()", "Crée les tables SQL `users` (id, username, password_hash, role) et `players` (id, name, club, position, age, market_value, stat_finishing, stat_pace...) si elles n'existent pas encore."),
        ("L. 37 - 60", "def get_user(username)", "Exécute `SELECT * FROM users WHERE username = ?` de manière paramétrée pour récupérer le compte utilisateur sans risque d'injection SQL."),
        ("L. 62 - 95", "def search_players_matching(...)", "Construit dynamiquement la requête SQL `WHERE` selon les filtres renseignés par l'utilisateur (`position = ?`, `age <= ?`, `market_value <= ?`) et renvoie les résultats triés par note globale.")
    ]

    t_db = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in db_lines], colWidths=[55, 150, 305])
    t_db.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_db)
    story.append(Spacer(1, 6))

    # import_real_fbref_2025_full.py
    story.append(Paragraph("📄 Fichier : <code>backend/import_real_fbref_2025_full.py</code>", h2_style))
    etl_lines = [
        ("L. 1 - 10", "import soccerdata as sd, pandas as pd", "Importation du scraper `soccerdata` pour extraire la base FBref officielle de la saison 2024-2025."),
        ("L. 12 - 50", "ELITE_PLAYERS_STATS = {...}", "Dictionnaire de référence répertoriant les 30 stars mondiales (Mbappé, Haaland, Cherki, Saliba) avec leurs vrais 6 attributs Opta et valeurs de marché réelles."),
        ("L. 52 - 60", "def extract_scalar(val)", "Isole l'élément brut d'une Series Pandas (`iloc[0]`) pour empêcher toute corruption de texte du type `Name: 1053, dtype: str`."),
        ("L. 62 - 120", "def import_fbref_2025_real_data()", "Scrape les 2 854 joueurs des 5 championnats européens. Pour chaque joueur, il lit son vrai âge, son temps de jeu réels `Min`, ses buts réels `Gls` et ses passes dé `Ast`."),
        ("L. 122 - 160", "Calcul des 6 axes & Insertion SQL", "Calcule les notes de Finition, Dribble, Passes, Vitesse, Défense et Physique (0-100) et insère les lignes dans la base SQLite via `cursor.execute()`.")
    ]

    t_etl = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in etl_lines], colWidths=[55, 150, 305])
    t_etl.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_etl)

    story.append(PageBreak())

    # SECTION FRONTEND
    story.append(Paragraph("PARTIE 2 : DÉCRYPTAGE DU FRONTEND (REACT 18 / VITE)", h1_style))

    # App.jsx
    story.append(Paragraph("📄 Fichier : <code>Frontend/src/App.jsx</code>", h2_style))
    app_lines = [
        ("L. 1 - 6", "import React, { useState, useEffect }", "Importation des Hooks réactifs de React et des sous-composants (LoginModal, ScoutingFilters, PlayerSearchBar, PlayerRadarModal, BudgetDashboard)."),
        ("L. 8 - 15", "const [token, setToken] = useState(...)", "Déclaration des états réactifs globaux : jeton JWT `token`, rôle `role`, nom d'utilisateur `username`, liste des joueurs `players`, onglet actif `activeTab` et joueur sélectionné `selectedPlayer`."),
        ("L. 17 - 35", "useEffect(() => { handleSearch() }, [])", "Hook d'effet exécuté au chargement de la page. Il déclenche la première recherche de joueurs."),
        ("L. 37 - 75", "const handleSearch = async () => {...}", "Fonction qui tente d'interroger l'API FastAPI local (`http://127.0.0.1:8000/players/search`). En cas d'échec (ex: sur Vercel), elle bascule sur le fichier `players_dataset.json` et effectue le filtrage côté client."),
        ("L. 77 - 110", "renderTabContent()", "Affiche conditionnellement la vue 'Scouting' ou le composant 'BudgetDashboard' selon l'onglet cliqué par l'utilisateur."),
        ("L. 112 - 145", "Structure JSX de la Navbar & Layout", "Rendu HTML de la barre supérieure avec le logo PRO / OL, l'indicateur de rôle utilisateur connecté et le bouton de déconnexion.")
    ]

    t_app = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in app_lines], colWidths=[55, 150, 305])
    t_app.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_app)
    story.append(Spacer(1, 6))

    # LoginModal.jsx
    story.append(Paragraph("📄 Fichier : <code>Frontend/src/components/LoginModal.jsx</code>", h2_style))
    login_lines = [
        ("L. 1 - 8", "export default function LoginModal()", "Déclaration du composant modal d'authentification. Reçoit la callback `onLoginSuccess`."),
        ("L. 10 - 25", "const handleSubmit = async (e)", "Intercepte la soumission du formulaire (`e.preventDefault()`). Envoie les identifiants à l'API via `fetch('/login')` avec `URLSearchParams`."),
        ("L. 27 - 50", "Vérification stricte Vercel / Error state", "Si l'API n'est pas joignable, vérifie strictement les 3 comptes pré-remplis (`rayane`, `directeur`, `scout1`). En cas d'erreur, modifie l'état `error` pour afficher l'alerte rouge."),
        ("L. 52 - 80", "Rendu Formulaire JSX", "Génère les champs `username` et `password` avec gestion dynamique de la valeur saisie (`onChange`).")
    ]

    t_login = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in login_lines], colWidths=[55, 150, 305])
    t_login.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_login)
    story.append(Spacer(1, 6))

    # ScoutingFilters.jsx & PlayerSearchBar.jsx
    story.append(Paragraph("📄 Fichiers : <code>ScoutingFilters.jsx</code> & <code>PlayerSearchBar.jsx</code>", h2_style))
    filter_lines = [
        ("ScoutingFilters", "maxMarketValue Slider", "Gère le slider de valeur marchande maximale (de 5 M€ à 200 M€ / Illimitée). Dès qu'il est déplacé, l'événement `onFilterChange` transmet la nouvelle valeur à `App.jsx`."),
        ("PlayerSearchBar", "Autocomplétion temps réel", "Barre de recherche réactive. Dès que 2 caractères sont tapés, il exécute `ALL_PLAYERS.filter(p => p.name.toLowerCase().includes(query))` et affiche les suggestions. Un clic sur une option déclenche `onSelectPlayer(p)` pour ouvrir le radar.")
    ]

    t_filter = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in filter_lines], colWidths=[80, 125, 300])
    t_filter.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_filter)
    story.append(Spacer(1, 6))

    # RadarChartCanvas.jsx & PlayerRadarModal.jsx
    story.append(Paragraph("📄 Fichiers : <code>RadarChartCanvas.jsx</code> & <code>PlayerRadarModal.jsx</code>", h2_style))
    radar_lines = [
        ("RadarChartCanvas", "Trigonométrie SVG 6 axes", "Calcule les angles de 60° (Math.PI / 3) et détermine les coordonnées X et Y de chaque sommet : `X = Cx + R * (Val/100) * cos(angle)`. Génère la toile rouge `<polygon>`."),
        ("PlayerRadarModal", "Algorithme KNN & Jumeaux", "Calcule la distance euclidienne pondérée par le statut de la valeur marchande. Renvoye les 4 jumeaux statistiques réels (Mbappé ➔ Haaland, Kvaratskhelia, Barcola, Dembélé).")
    ]

    t_radar = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in radar_lines], colWidths=[80, 125, 300])
    t_radar.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_radar)
    story.append(Spacer(1, 6))

    # BudgetDashboard.jsx
    story.append(Paragraph("📄 Fichier : <code>Frontend/src/components/BudgetDashboard.jsx</code>", h2_style))
    budget_lines = [
        ("L. 1 - 15", "Vérification du rôle RBAC", "Si `role === 'scout'`, stoppe le rendu et affiche immédiatement la carte rouge `⛔ Accès Restreint (RBAC)`."),
        ("L. 17 - 45", "Simulateur financier interactif", "Gère deux sliders réactifs (`simulatedTransfer` et `simulatedSalary`). Recalcule en temps réel l'enveloppe restante sur les 45 M€ et ajuste la couleur (Bleu si valide, Rouge si dépassement).")
    ]

    t_budget = Table([[Paragraph(f"<b>{r[0]}</b>", body_style), Paragraph(f"<code>{r[1]}</code>", code_style), Paragraph(r[2], body_style)] for r in budget_lines], colWidths=[55, 150, 305])
    t_budget.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('TOPPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_budget)

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=6))
    story.append(Paragraph("<b>Synthèse :</b> Ce décryptage détaillé offre une maîtrise complète ligne par ligne de la structure full-stack du projet Recruitment Match OL.", body_style))

    doc.build(story)
    print(f"PDF décryptage ligne par ligne généré avec succès : {pdf_path}")

if __name__ == "__main__":
    build_pdf()
