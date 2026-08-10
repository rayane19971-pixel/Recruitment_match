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
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        leading=24,
        textColor=colors.HexColor('#0f172a'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0284c7'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=12
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0f172a'),
        fontName='Helvetica-Bold',
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0369a1'),
        fontName='Helvetica-Bold',
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor('#334155'),
        alignment=TA_LEFT,
        fontName='Helvetica',
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'CodeStyleCustom',
        parent=styles['Normal'],
        fontSize=8,
        leading=11,
        textColor=colors.HexColor('#0f172a'),
        fontName='Courier',
        spaceBefore=2,
        spaceAfter=4
    )

    story = []

    # En-tête
    story.append(Paragraph("DOSSIER TECHNIQUE D'EXPLICATION DU CODE SOURCE", title_style))
    story.append(Paragraph("PROJECT RECRUITMENT MATCH - OLYMPIQUE LYONNAIS (FULL-STACK & DATA SCOUTING)", subtitle_style))
    story.append(Paragraph("<b>Auteur :</b> Rayane Ourad — <b>Formation :</b> Bachelor 3 DBI (Data & Business Intelligence) — <b>Année :</b> 2025-2026", body_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284c7'), spaceAfter=10))

    # SECTION 1: ARCHITECTURE
    story.append(Paragraph("1. ARCHITECTURE TECHNIQUE ET FLUX DE DONNÉES", h1_style))
    story.append(Paragraph(
        "L'application est construite selon une architecture découplée <b>Client / Serveur (API REST)</b>. "
        "Le Frontend réactif en React échange avec le Backend Python FastAPI via des requêtes HTTP asynchrones au format JSON.", body_style
    ))

    arch_table = [
        [Paragraph("<b>Composant</b>", body_style), Paragraph("<b>Technologie</b>", body_style), Paragraph("<b>Description & Rôle Technique</b>", body_style)],
        [Paragraph("<b>Frontend UI</b>", body_style), Paragraph("React 18 / Vite", body_style), Paragraph("Gestionnaire d'état dynamique (`useState`, `useEffect`), composants modulaire, Canvas SVG.", body_style)],
        [Paragraph("<b>Backend API</b>", body_style), Paragraph("Python / FastAPI", body_style), Paragraph("Serveur ASGI rapide (Uvicorn), middleware CORS, gestion des routes et contrôles de sécurité.", body_style)],
        [Paragraph("<b>Base de données</b>", body_style), Paragraph("SQLite (relational)", body_style), Paragraph("Base locale `recruitment_app.db` stockant les 2 854 joueurs Opta 2024-2025 et les utilisateurs.", body_style)],
        [Paragraph("<b>Sécurité & RBAC</b>", body_style), Paragraph("PyJWT & Passlib", body_style), Paragraph("Hachage bcrypt des mots de passe, génération et vérification des jetons d'accès Bearer JWT.", body_style)],
        [Paragraph("<b>Algorithme Data</b>", body_style), Paragraph("scikit-learn / JS", body_style), Paragraph("Algorithme des k-NN avec distance euclidienne pondérée par la valeur marchande.", body_style)]
    ]

    t_arch = Table(arch_table, colWidths=[80, 95, 335])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0f2fe')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0369a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('TOPPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 10))

    # SECTION 2: BACKEND
    story.append(Paragraph("2. EXPLICATION DÉTAILLÉE DU BACKEND (PYTHON & FASTAPI)", h1_style))

    # main.py
    story.append(Paragraph("📄 Fichier 1 : `backend/main.py` (Point d'entrée et Serveur d'API REST)", h2_style))
    story.append(Paragraph("Ce fichier configure le serveur Web Uvicorn, la sécurité et l'ensemble des endpoints HTTP exposés au client :", body_style))
    story.append(Paragraph("• <b>Configuration CORS (`CORSMiddleware`) :</b> Autorise le navigateur web du Frontend (port 5173 ou domaine Vercel) à communiquer avec l'API Python sans être bloqué par les règles de sécurité cross-origin.", body_style))
    story.append(Paragraph("• <b>Route `@app.post('/login')` :</b> Récupère le nom d'utilisateur et le mot de passe via un formulaire OAuth2. Il appelle `database.get_user()`, compare le mot de passe hashé avec `CryptContext(schemes=['bcrypt'])`, puis renvoie un token d'accès JWT signé contenant le rôle de l'utilisateur (`scout`, `director`, `admin`).", body_style))
    story.append(Paragraph("• <b>Route `@app.get('/players/search')` :</b> Reçoit les paramètres de recherche (nom `query`, poste `position`, filtres `min_age`, `max_age`, `max_value`, `min_overall`). Il exécute la requête SQL sécurisée et renvoie la liste paginée des joueurs compatibles.", body_style))
    story.append(Paragraph("• <b>Route `@app.get('/players/{id}/similar')` :</b> Exécute l'algorithme des <i>k Plus Proches Voisins</i> (k-NN). Il calcule la distance euclidienne sur les 6 attributs Opta et applique une pénalité logarithmique sur l'écart de valeur marchande pour éviter d'associer des stars avec des remplaçants :", body_style))
    story.append(Paragraph("$$Distance = \\sqrt{\\frac{1}{6}\\sum_{i=1}^6 (Stat_{target,i} - Stat_{candidat,i})^2 + \\left(14 \\cdot (\\log_{10}(Val_{target}) - \\log_{10}(Val_{candidat}))\\right)^2}$$", code_style))
    story.append(Paragraph("• <b>Route `@app.get('/director/budget')` (Contrôle RBAC) :</b> Inspecte le jeton JWT transmis dans le header `Authorization: Bearer <token>`. Si le rôle est `scout`, l'API lève immédiatement une exception `HTTPException(status_code=403, detail='Accès refusé')`. Si le rôle est `director` ou `admin`, elle renvoie l'enveloppe de 45 M€.", body_style))
    story.append(Spacer(1, 6))

    # database.py
    story.append(Paragraph("📄 Fichier 2 : `backend/database.py` (Gestion de la base SQLite & Requêtes SQL)", h2_style))
    story.append(Paragraph("• <code>get_connection()</code> : Ouvre la connexion vers `data/recruitment_app.db` et définit `conn.row_factory = sqlite3.Row`. Cela permet d'accéder aux colonnes SQL par leur nom sous forme de dictionnaire Python au lieu d'index numériques.", body_style))
    story.append(Paragraph("• <code>search_players_matching()</code> : Construit dynamiquement la clause SQL `WHERE` selon les critères choisis par le recruteur :", body_style))
    story.append(Paragraph("<code>SELECT * FROM players WHERE position = ? AND age >= ? AND age <= ? AND market_value <= ? ORDER BY overall DESC</code>", code_style))
    story.append(Paragraph("L'utilisation de requêtes paramétrées avec les points d'interrogation `?` garantit une protection absolue contre les attaques par injection SQL.", body_style))
    story.append(Spacer(1, 6))

    # import_real_fbref_2025_full.py
    story.append(Paragraph("📄 Fichier 3 : `backend/import_real_fbref_2025_full.py` (Scraper & Étalonnage Opta)", h2_style))
    story.append(Paragraph("• <b>Scraping via `soccerdata` :</b> Télécharge les statistiques de la saison 2024-2025 pour les 5 grands championnats européens (Ligue 1, Premier League, LaLiga, Serie A, Bundesliga).", body_style))
    story.append(Paragraph("• <code>extract_scalar()</code> : Extrait proprement les valeurs brutes de Pandas en isolant les éléments `iloc[0]` pour éliminer toute pollution de chaîne de caractères (comme les métadonnées `Name: 1053, dtype: str`).", body_style))
    story.append(Paragraph("• <b>Étalonnage des 6 axes Opta (0 à 100) :</b> Évalue la Finition, le Dribble, les Passes, la Vitesse, la Défense et le Physique d'après les statistiques par 90 minutes (buts réels `Gls`, passes dé réelles `Ast`, passes progressives `PrgP`, percussions `PrgC` et minutes jouées `Min`).", body_style))
    story.append(Paragraph("• <b>Ajustement par le temps de jeu :</b> Applique un facteur correcteur sur la valeur marchande selon le temps de jeu réel (`min_played > 800`), permettant de ramener les jeunes remplaçants sans buts à leur juste valeur (1-3 M€) et d'isoler le standing des stars (30-180 M€).", body_style))

    story.append(PageBreak())

    # SECTION 3: FRONTEND
    story.append(Paragraph("3. EXPLICATION DÉTAILLÉE DU FRONTEND (REACT & VITE)", h1_style))

    # App.jsx
    story.append(Paragraph("📄 Fichier 1 : `Frontend/src/App.jsx` (Composant Racine & Gestion d'État)", h2_style))
    story.append(Paragraph("`App.jsx` est le composant central qui conserve l'état global de la session et orchestre les vues :", body_style))
    story.append(Paragraph("• <b>États locaux (`useState`) :</b>", body_style))
    story.append(Paragraph("  - `token` / `role` / `username` : Conservent les informations de session authentifiée.", body_style))
    story.append(Paragraph("  - `players` : Tableau d'objets contenant les résultats des joueurs filtrés.", body_style))
    story.append(Paragraph("  - `activeTab` : Contrôle la navigation entre l'onglet 'Scouting' et 'Budget Mercato'.", body_style))
    story.append(Paragraph("  - `selectedPlayer` : Détermine quel joueur est actuellement affiché dans la fenêtre modal radar.", body_style))
    story.append(Paragraph("• <b>Fallback Vercel Stand-alone :</b> En cas d'indisponibilité du serveur Python local (lors du déploiement Vercel), la méthode `fetch()` capture l'erreur et bascule automatiquement sur le fichier client `players_dataset.json` pour exécuter le filtrage et les calculs KNN directement dans le navigateur sans rupture de service.", body_style))
    story.append(Spacer(1, 6))

    # LoginModal.jsx
    story.append(Paragraph("📄 Fichier 2 : `Frontend/src/components/LoginModal.jsx` (Authentification RBAC)", h2_style))
    story.append(Paragraph("Formulaire de connexion qui soumet les identifiants vers l'API. En mode Vercel, il effectue une vérification stricte des rôles autorisés (Admin: `rayane`, Directeur: `directeur`, Scout: `scout1`). Si les identifiants sont erronés, il affiche un message d'erreur rouge sans ouvrir la session.", body_style))
    story.append(Spacer(1, 6))

    # ScoutingFilters.jsx & PlayerSearchBar.jsx
    story.append(Paragraph("📄 Fichiers 3 & 4 : `ScoutingFilters.jsx` & `PlayerSearchBar.jsx` (Filtres & Autocomplétion)", h2_style))
    story.append(Paragraph("• `ScoutingFilters.jsx` : Propose les filtres réactifs par poste, âge, note globale et le <b>slider de valeur marchande maximale</b> (de 5 M€ à 200 M€ / Illimitée). Chaque changement de slider déclenche immédiatement une ré-évaluation de la recherche.", body_style))
    story.append(Paragraph("• `PlayerSearchBar.jsx` : Barre de recherche avec autocomplétion instantanée. Dès que l'utilisateur tape 2 caractères, le composant filtre le dataset local et affiche une liste déroulante de suggestions. Un clic sur une suggestion ouvre directement la fiche détaillée du joueur.", body_style))
    story.append(Spacer(1, 6))

    # RadarChartCanvas.jsx
    story.append(Paragraph("📄 Fichier 5 : `Frontend/src/components/RadarChartCanvas.jsx` (Trigonométrie SVG)", h2_style))
    story.append(Paragraph("Ce composant génère le graphique en toile d'araignée à 6 axes. Il divise un cercle complet (360°) en 6 angles égaux de 60° ($\\theta = 0^\\circ, 60^\\circ, 120^\\circ, 180^\\circ, 240^\\circ, 300^\\circ$) et calcule les coordonnées géométriques $(X, Y)$ de chaque attribut :", body_style))
    story.append(Paragraph("<code>X = Center_X + (Radius * (Stat_Value / 100)) * cos(Angle)</code>", code_style))
    story.append(Paragraph("<code>Y = Center_Y + (Radius * (Stat_Value / 100)) * sin(Angle)</code>", code_style))
    story.append(Paragraph("Ces 6 points sont ensuite reliés par un élément SVG `<polygon>` rempli d'une couleur rouge translucide (`rgba(239, 68, 68, 0.45)`).", body_style))
    story.append(Spacer(1, 6))

    # PlayerRadarModal.jsx
    story.append(Paragraph("📄 Fichier 6 : `Frontend/src/components/PlayerRadarModal.jsx` (Modal Détaillée & KNN Client)", h2_style))
    story.append(Paragraph("Affiche la fiche complète du joueur sélectionné (âge, nationalité, fin de contrat, salaire, valeur marchande) et exécute l'algorithme des Jumeaux Statistiques ($k$-NN). Il applique la formule de distance pondérée par la valeur marchande pour proposer les 4 équivalents réels (ex: Mbappé est associé à Haaland, Kvaratskhelia, Barcola et Dembélé).", body_style))
    story.append(Spacer(1, 6))

    # BudgetDashboard.jsx
    story.append(Paragraph("📄 Fichier 7 : `Frontend/src/components/BudgetDashboard.jsx` (Simulateur Financier Mercato)", h2_style))
    story.append(Paragraph("Tableau de bord financier réservé aux rôles `director` et `admin` :", body_style))
    story.append(Paragraph("• <b>Contrôle d'accès RBAC :</b> Si l'utilisateur connecté possède le rôle `scout`, le composant retourne immédiatement un écran de blocage rouge (<i>Accès Restreint RBAC</i>).", body_style))
    story.append(Paragraph("• <b>Simulateur de recrutement :</b> Deux sliders interactifs permettent de régler l'indemnité de transfert estimée (ex: 15 M€) et le salaire annuel proposé (ex: 2.5 M€/an). Le composant calcule dynamiquement l'enveloppe restante sur les 45 M€ attribués et alerte en cas de dépassement budgétaire.", body_style))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=8))
    story.append(Paragraph("<b>Conclusion :</b> Ce document résume l'intégralité du fonctionnement technique du projet Recruitment Match OL. Il démontre la maîtrise des concepts d'architecture web full-stack, de sécurité RBAC, de traitement de données et d'algorithmique appliquée au sport intelligence.", body_style))

    doc.build(story)
    print(f"PDF détaillé généré avec succès : {pdf_path}")

if __name__ == "__main__":
    build_pdf()
