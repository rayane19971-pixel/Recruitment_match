import os
import sys
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

def build_pdf():
    # Enregistrement dans Mes Documents
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
        fontSize=22,
        leading=26,
        textColor=colors.HexColor('#0f172a'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0284c7'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold',
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor('#1e293b'),
        fontName='Helvetica-Bold',
        spaceBefore=12,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Heading3'],
        fontSize=11,
        leading=15,
        textColor=colors.HexColor('#0369a1'),
        fontName='Helvetica-Bold',
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#334155'),
        alignment=TA_LEFT,
        fontName='Helvetica',
        spaceAfter=5
    )

    story = []

    # En-tête
    story.append(Paragraph("PROJECT RECRUITMENT MATCH - OLYMPIQUE LYONNAIS", title_style))
    story.append(Paragraph("GUIDE TECHNIQUE ET EXPLICATION DÉTAILLÉE DU CODE SOURCE (FRONTEND & BACKEND)", subtitle_style))
    story.append(Paragraph("<b>Auteur :</b> Rayane Ourad — <b>Formation :</b> Bachelor 3 DBI (Data & Business Intelligence)", body_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#0284c7'), spaceAfter=12))

    # Introduction & Architecture
    story.append(Paragraph("1. ARCHITECTURE GLOBALE ET FONCTIONNEMENT DE L'APPLICATION", h1_style))
    story.append(Paragraph(
        "L'application <b>Recruitment Match OL</b> est une plateforme full-stack orientée Data Scouting. "
        "Elle repose sur une architecture découplée Client / Serveur :", body_style
    ))

    arch_data = [
        [Paragraph("<b>Composant</b>", body_style), Paragraph("<b>Technologie</b>", body_style), Paragraph("<b>Rôle principal</b>", body_style)],
        [Paragraph("<b>Backend</b>", body_style), Paragraph("Python / FastAPI", body_style), Paragraph("API REST, Authentification JWT, Sécurité RBAC, Calcul KNN SQL.", body_style)],
        [Paragraph("<b>Base de données</b>", body_style), Paragraph("SQLite (relational)", body_style), Paragraph("Stockage local des 2 854 joueurs Opta 2024-2025 et des utilisateurs.", body_style)],
        [Paragraph("<b>Frontend</b>", body_style), Paragraph("React 18 / Vite", body_style), Paragraph("Interface dynamique, Canvas SVG Radar, Filtres et autocomplétion.", body_style)],
        [Paragraph("<b>Déploiement Web</b>", body_style), Paragraph("Vercel (Stand-alone)", body_style), Paragraph("Hébergement en ligne avec calcul KNN autonome côté client (fallback).", body_style)]
    ]

    t_arch = Table(arch_data, colWidths=[85, 105, 320])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0f2fe')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0369a1')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 10))

    # PARTIE BACKEND
    story.append(Paragraph("2. LE BACKEND (PYTHON & FASTAPI)", h1_style))
    story.append(Paragraph(
        "Le répertoire <code>backend/</code> contient toute la logique métier, la gestion des accès et l'interaction avec la base de données SQLite.", body_style
    ))

    # main.py
    story.append(Paragraph("📄 Fichier 1 : <code>backend/main.py</code> (Serveur d'API REST FastAPI)", h2_style))
    story.append(Paragraph("• <code>@app.post('/login')</code> : Récupère les identifiants tapés par l'utilisateur, vérifie leur validité en base SQLite et génère un jeton sécurisé JWT contenant le rôle (<i>scout</i>, <i>director</i>, <i>admin</i>).", body_style))
    story.append(Paragraph("• <code>@app.get('/players/search')</code> : Filtre les joueurs selon la recherche textuelle, le poste, l'âge et la valeur marchande maximale via une requête SQL paramétrée.", body_style))
    story.append(Paragraph("• <code>@app.get('/players/{id}/similar')</code> : Exécute l'algorithme des k Plus Proches Voisins (k-NN) en calculant la distance euclidienne pondérée entre le joueur sélectionné et les candidats du même poste.", body_style))
    story.append(Paragraph("• <code>@app.get('/director/budget')</code> : Endpoint confidentiel réservé au rôle <i>director</i> ou <i>admin</i> renvoyant l'enveloppe budgétaire du club.", body_style))

    # database.py
    story.append(Paragraph("📄 Fichier 2 : <code>backend/database.py</code> (Gestion SQLite & Requêtes SQL)", h2_style))
    story.append(Paragraph("• <code>create_db()</code> : Initialise la base SQLite si elle n'existe pas et crée la structure des tables <code>users</code> et <code>players</code>.", body_style))
    story.append(Paragraph("• <code>search_players_matching()</code> : Construit dynamiquement la clause <code>WHERE SQL</code> de manière paramétrée pour éviter toute injection SQL.", body_style))

    # import_real_fbref_2025_full.py
    story.append(Paragraph("📄 Fichier 3 : <code>backend/import_real_fbref_2025_full.py</code> (Extraction Opta/FBref 2024-2025)", h2_style))
    story.append(Paragraph("• <code>extract_scalar()</code> : Isole les valeurs scalaires brutes de Pandas pour éliminer la pollution de texte.", body_style))
    story.append(Paragraph("• Étalonnage des 6 attributs Opta (0-100) : Notes de Finition, Dribble, Passes, Vitesse, Défense et Physique calculées d'après les performances réelles sur 90 minutes (buts <i>Gls</i>, passes dé <i>Ast</i>, minutes <i>Min</i>).", body_style))

    story.append(PageBreak())

    # PARTIE FRONTEND
    story.append(Paragraph("3. LE FRONTEND (REACT & VITE)", h1_style))
    story.append(Paragraph(
        "Le répertoire <code>Frontend/src/</code> contient tous les composants d'interface réactifs développés en React.", body_style
    ))

    # App.jsx
    story.append(Paragraph("📄 Fichier 1 : <code>Frontend/src/App.jsx</code> (Composant Racine & État Global)", h2_style))
    story.append(Paragraph("• Gestion de l'état local (<code>useState</code>) : Stocke le jeton JWT (<code>token</code>), le rôle (<code>role</code>), les filtres et la liste des joueurs.", body_style))
    story.append(Paragraph("• Fallback Vercel Stand-alone : Bascule automatiquement sur <code>players_dataset.json</code> si le serveur local Python n'est pas joignable.", body_style))

    # LoginModal.jsx
    story.append(Paragraph("📄 Fichier 2 : <code>Frontend/src/components/LoginModal.jsx</code> (Page de Connexion RBAC)", h2_style))
    story.append(Paragraph("• Contrôle l'accès selon les droits utilisateur (Admin: <code>rayane</code>, Directeur: <code>directeur</code>, Scout: <code>scout1</code>) et bloque les saisies erronées.", body_style))

    # ScoutingFilters.jsx & PlayerSearchBar.jsx
    story.append(Paragraph("📄 Fichiers 3 & 4 : <code>ScoutingFilters.jsx</code> & <code>PlayerSearchBar.jsx</code> (Filtres & Autocomplétion)", h2_style))
    story.append(Paragraph("• <code>ScoutingFilters.jsx</code> : Filtres par poste, âge, note minimale et slider de valeur marchande max (5 M€ à 200 M€ / Illimitée).", body_style))
    story.append(Paragraph("• <code>PlayerSearchBar.jsx</code> : Autocomplétion instantanée dès 2 caractères tapés pour ouvrir directement la fiche d'un joueur.", body_style))

    # RadarChartCanvas.jsx & PlayerRadarModal.jsx
    story.append(Paragraph("📄 Fichiers 5 & 6 : <code>RadarChartCanvas.jsx</code> & <code>PlayerRadarModal.jsx</code> (Radar Canvas & KNN)", h2_style))
    story.append(Paragraph("• <code>RadarChartCanvas.jsx</code> : Trigonométrie SVG divisant un cercle en 6 angles de 60° pour dessiner le polygone rouge des performances.", body_style))
    story.append(Paragraph("• <code>PlayerRadarModal.jsx</code> : Calcule la distance euclidienne pondérée (Stats Opta + Standing) pour afficher les 4 jumeaux statistiques réels (ex: Mbappé est associé à Haaland, Kvaratskhelia, Barcola et Dembélé).", body_style))

    # BudgetDashboard.jsx
    story.append(Paragraph("📄 Fichier 7 : <code>Frontend/src/components/BudgetDashboard.jsx</code> (Espace Direction & Simulateur)", h2_style))
    story.append(Paragraph("• Restreint l'accès aux comptes non autorisés (Scout). Propose deux sliders interactifs pour tester le montant d'un transfert et l'impact sur l'enveloppe globale de 45 M€.", body_style))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=8))
    story.append(Paragraph("<b>Synthèse :</b> Document d'accompagnement technique pour l'évaluation Bachelor 3 Data & Business Intelligence.", body_style))

    doc.build(story)
    print(f"PDF généré avec succès dans Mes Documents : {pdf_path}")

if __name__ == "__main__":
    build_pdf()
