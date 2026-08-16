import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT

def generate_bloc4():
    pdf_path = r"C:\Users\user\OneDrive\Documents\OURAD_RAYANE_BLOC4_CONCEPTION_DEVELOPPEMENT.pdf"
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    c_purple = colors.HexColor('#5b21b6')
    c_dark = colors.HexColor('#0f172a')
    c_ol_blue = colors.HexColor('#0b2c5c')
    c_ol_red = colors.HexColor('#d31115')
    c_text = colors.HexColor('#334155')

    title_main = ParagraphStyle(
        'CoverTitle', parent=styles['Heading1'], fontSize=22, leading=26,
        textColor=c_dark, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=10
    )

    subtitle_main = ParagraphStyle(
        'CoverSubTitle', parent=styles['Normal'], fontSize=12, leading=16,
        textColor=c_purple, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=16
    )

    h1_style = ParagraphStyle(
        'SectionH1', parent=styles['Heading1'], fontSize=14, leading=18,
        textColor=c_dark, fontName='Helvetica-Bold', spaceBefore=14, spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'SectionH2', parent=styles['Heading2'], fontSize=11.5, leading=15,
        textColor=c_ol_blue, fontName='Helvetica-Bold', spaceBefore=10, spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyCustom', parent=styles['Normal'], fontSize=9, leading=13,
        textColor=c_text, alignment=TA_JUSTIFY, fontName='Helvetica', spaceAfter=5
    )

    bullet_style = ParagraphStyle(
        'BulletCustom', parent=styles['Normal'], fontSize=8.5, leading=12.5,
        textColor=c_text, fontName='Helvetica', spaceAfter=3, leftIndent=12
    )

    code_style = ParagraphStyle(
        'CodeStyle', parent=styles['Normal'], fontSize=8, leading=11,
        textColor=colors.HexColor('#0f172a'), fontName='Courier', spaceBefore=3, spaceAfter=5
    )

    story = []

    # =========================================================================
    # PAGE DE GARDE : BLOC DE COMPÉTENCE 4
    # =========================================================================
    story.append(Spacer(1, 20))
    story.append(Paragraph("NEXA DIGITAL SCHOOL — CAMPUS DE PARIS", ParagraphStyle('SchoolH', parent=styles['Normal'], fontSize=11, textColor=c_purple, alignment=TA_CENTER, fontName='Helvetica-Bold')))
    story.append(Paragraph("BACHELOR DATA & BUSINESS INTELLIGENCE (RNCP40857)", ParagraphStyle('DegreeH', parent=styles['Normal'], fontSize=13, textColor=c_dark, alignment=TA_CENTER, fontName='Helvetica-Bold')))
    
    story.append(Spacer(1, 25))
    story.append(HRFlowable(width="100%", thickness=2.5, color=c_purple, spaceAfter=15))
    story.append(Paragraph("BLOC DE COMPÉTENCE 4 : CONCEVOIR ET DÉVELOPPER DES SOLUTIONS WEB", title_main))
    story.append(Paragraph("DOSSIER TECHNIQUE DE CONCEPTION & DÉVELOPPEMENT FULL-STACK", subtitle_main))
    story.append(Paragraph("Projet : Recruitment Match — Olympique Lyonnais 🔴🔵", ParagraphStyle('AppSub', parent=styles['Normal'], fontSize=11, textColor=c_ol_red, alignment=TA_CENTER, fontName='Helvetica-Bold')))
    story.append(HRFlowable(width="100%", thickness=2.5, color=c_purple, spaceBefore=15, spaceAfter=25))

    meta_table = [
        [Paragraph("<b>Apprenant :</b>", body_style), Paragraph("Rayane OURAD", body_style)],
        [Paragraph("<b>Intitulé du Bloc :</b>", body_style), Paragraph("Bloc 4 — Concevoir et développer des solutions web", body_style)],
        [Paragraph("<b>Application Web :</b>", body_style), Paragraph("Recruitment Match OL (React 18 / FastAPI / SQLite)", body_style)],
        [Paragraph("<b>URL Déploiement :</b>", body_style), Paragraph("https://recruitment-match-pro.vercel.app", body_style)],
        [Paragraph("<b>Dépôt GitHub :</b>", body_style), Paragraph("https://github.com/L3-WEB-2026/web-rayane-ourad.git", body_style)],
        [Paragraph("<b>Date de rendu :</b>", body_style), Paragraph("Août 2026", body_style)]
    ]
    t_meta = Table(meta_table, colWidths=[140, 350])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 5)
    ]))
    story.append(t_meta)
    story.append(PageBreak())

    # =========================================================================
    # SECTION A : L'ARCHITECTURE TECHNIQUE (2 PAGES)
    # =========================================================================
    story.append(Paragraph("a. L'Architecture Technique (Modulaire, Scalable & Brique Data)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=10))

    story.append(Paragraph(
        "L'architecture technique retenue pour le projet <b>Recruitment Match OL</b> est une architecture découplée de type <b>Client / Serveur (API REST)</b>. "
        "Elle garantit une séparation stricte des responsabilités entre la brique Data Engineering (ETL), le serveur d'API REST Python (FastAPI) et l'interface utilisateur réactive (React 18).", body_style
    ))

    arch_table = [
        [Paragraph("<b>Couche Architecture</b>", body_style), Paragraph("<b>Composant / Techno</b>", body_style), Paragraph("<b>Spécifications & Rôle Technique</b>", body_style)],
        [Paragraph("<b>Front-Office UI</b>", body_style), Paragraph("React 18 / Vite", body_style), Paragraph("Interface réactive (Single Page Application), gestion d'état Hooks, rendu Canvas SVG vectoriel.", body_style)],
        [Paragraph("<b>Back-Office API</b>", body_style), Paragraph("Python 3.12 / FastAPI", body_style), Paragraph("API REST asynchrone (Uvicorn), middleware CORS, validation Pydantic, déserialisation JSON.", body_style)],
        [Paragraph("<b>Sécurité & Auth</b>", body_style), Paragraph("PyJWT & Passlib (Bcrypt)", body_style), Paragraph("Authentification par jetons JWT Bearer, hachage irréversible des mots de passe, contrôle RBAC.", body_style)],
        [Paragraph("<b>Base de données</b>", body_style), Paragraph("SQLite3 (`recruitment_app.db`)", body_style), Paragraph("Stockage relationnel indexé des 2 854 joueurs Opta 2024-2025 et des utilisateurs.", body_style)],
        [Paragraph("<b>Brique Data ETL</b>", body_style), Paragraph("Python / `soccerdata` (FBref)", body_style), Paragraph("Pipeline d'extraction, nettoyage Pandas et étalonnage des 6 attributs Opta (0 à 100).", body_style)]
    ]
    t_arch = Table(arch_table, colWidths=[100, 110, 280])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_ol_blue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(t_arch)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Brique Data & Pipeline de Collecte ETL :</b>", h2_style))
    story.append(Paragraph("• <b>Source des données :</b> Extraction via la bibliothèque Python `soccerdata` interrogeant la base officielle FBref pour la saison 2024-2025 (2 854 joueurs enregistrés dans les 5 grands championnats).", bullet_style))
    story.append(Paragraph("• <b>Fonction de nettoyage `extract_scalar()` :</b> Isole l'élément brut Pandas (`iloc[0]`) pour éradiquer la pollution de texte issue des Series MultiIndex (ex: `Name: 1053, dtype: str`).", bullet_style))
    story.append(Paragraph("• <b>Étalonnage des 6 axes Opta (0 à 100) :</b> Calcul des attributs de Finition, Dribble, Passes, Vitesse, Défense et Physique basés sur les statistiques réelles par 90 minutes ($Gls/90$, $Ast/90$, $PrgP/90$, $PrgC/90$).", bullet_style))

    story.append(PageBreak())

    # =========================================================================
    # SECTION B : MAQUETTES ET PROTOTYPES (UX/UI)
    # =========================================================================
    story.append(Paragraph("b. Les Maquettes et Prototypes (UX/UI & Design System OL)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=10))

    story.append(Paragraph(
        "Le design system de l'application a été élaboré selon les principes du <b>Glassmorphism</b> et de la charte visuelle officielle de l'Olympique Lyonnais. "
        "Les interfaces ont été testées pour répondre aux normes d'ergonomie (critères heuristiques de Bastien & Scapin).", body_style
    ))

    ux_table = [
        [Paragraph("<b>Interface / Écran</b>", body_style), Paragraph("<b>Principes Ergonomiques & Choix UX/UI</b>", body_style)],
        [
            Paragraph("<b>Page d'Accueil & Connexion</b>", body_style),
            Paragraph("Formulaire épuré avec cartes translucides, logo officiel OL tricolore et rappels des comptes de démonstration autorisés (`rayane`, `directeur`, `scout1`).", body_style)
        ],
        [
            Paragraph("<b>Scouting & Radar Opta</b>", body_style),
            Paragraph("Panneau latéral de filtres compacts avec sliders dynamiques, barre d'autocomplétion directe et affichage en grille réactive des fiches de joueurs.", body_style)
        ],
        [
            Paragraph("<b>Effectif OL & Comparateur</b>", body_style),
            Paragraph("Présentation des joueurs lyonnais sous forme de cartes cliquables ouvrant la fenêtre modal de similarité $k$-NN (Jumeaux statistiques) et comparateur dual radar face-à-face.", body_style)
        ],
        [
            Paragraph("<b>Espace Budget Mercato</b>", body_style),
            Paragraph("Tableau de bord financier avec indicateurs en temps réel (Enveloppe 45 M€) et sliders interactifs de simulation d'impact salarial et de transfert.", body_style)
        ]
    ]
    t_ux = Table(ux_table, colWidths=[140, 350])
    t_ux.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_purple),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))
    story.append(t_ux)

    story.append(PageBreak())

    # =========================================================================
    # SECTION C : PRÉSENTATION DU DÉVELOPPEMENT FRONT-END (2 PAGES)
    # =========================================================================
    story.append(Paragraph("c. Présentation du Développement Front-End (React 18 & Mobile-First)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=10))

    story.append(Paragraph(
        "Le développement front-end s'appuie sur la bibliothèque <b>React 18</b> associée à l'outil de build ultra-rapide <b>Vite</b>. "
        "Le code est découpé en composants réutilisables et isolés afin de maximiser la maintenabilité.", body_style
    ))

    story.append(Paragraph("<b>Formule Trigonométrique du Radar Vectoriel Canvas SVG (`RadarChartCanvas.jsx`) :</b>", h2_style))
    story.append(Paragraph(
        "Le graphique en toile d'araignée divise un cercle complet (360°) en 6 angles égaux de 60° ($\\theta_i = \\frac{2\\pi}{6} \\times i - \\frac{\\pi}{2}$). "
        "Pour chaque attribut Opta (Finition, Dribble, Passes, Vitesse, Défense, Physique), les coordonnées géométriques $(X, Y)$ du sommet du polygone sont calculées en SVG :", body_style
    ))

    code_svg = """// Calcul des coordonnées X et Y pour chaque axe du radar SVG
const angle = (Math.PI * 2 / 6) * index - (Math.PI / 2);
const x = centerX + (radius * (statValue / 100)) * Math.cos(angle);
const y = centerY + (radius * (statValue / 100)) * Math.sin(angle);

// Rendu du polygone SVG translucide OL
<polygon points={pointsString} fill="rgba(211, 17, 21, 0.45)" stroke="#d31115" strokeWidth="2" />"""
    story.append(Paragraph(code_svg, code_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Approche Mobile-First et Responsive Web Design :</b>", h2_style))
    story.append(Paragraph("• <b>Curseurs tactiles adaptés (20px) :</b> Ajustement de la taille des sliders et inputs (`min-height: 44px`) pour une manipulation facile au pouce.", bullet_style))
    story.append(Paragraph("• <b>Media Queries (`@media (max-width: 768px)`) :</b> Réorganisation automatique des grilles en 1 seule colonne et conversion du radar en modal coulissante (*Sheet*).", bullet_style))

    story.append(PageBreak())

    # =========================================================================
    # SECTION D : PRÉSENTATION DU DÉVELOPPEMENT BACK-END (3 PAGES)
    # =========================================================================
    story.append(Paragraph("d. Présentation du Développement Back-End (FastAPI & SQLite)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=10))

    story.append(Paragraph(
        "Le serveur back-end est développé en <b>Python 3.12</b> avec le framework <b>FastAPI</b>. "
        "Les données sont stockées dans une base relationnelle <b>SQLite3</b> optimisée.", body_style
    ))

    story.append(Paragraph("<b>Endpoints de l'API REST FastAPI (`backend/main.py`) :</b>", h2_style))
    
    api_table = [
        [Paragraph("<b>Méthode & Route</b>", body_style), Paragraph("<b>Accès RBAC</b>", body_style), Paragraph("<b>Description & Rôle de l'Endpoint</b>", body_style)],
        [Paragraph("`POST /login`", body_style), Paragraph("Public", body_style), Paragraph("Vérification des identifiants (Bcrypt) et émission d'un jeton JWT d'accès Bearer.", body_style)],
        [Paragraph("`GET /players/search`", body_style), Paragraph("Scout / Directeur", body_style), Paragraph("Recherche multicritère sécurisée via requêtes SQL paramétrées (`WHERE`).", body_style)],
        [Paragraph("`GET /players/{id}/similar`", body_style), Paragraph("Scout / Directeur", body_style), Paragraph("Calcul de la distance euclidienne $k$-NN pour trouver les 4 jumeaux statistiques réels.", body_style)],
        [Paragraph("`GET /director/budget`", body_style), Paragraph("Directeur / Admin", body_style), Paragraph("Endpoint confidentiel renvoyant le budget de 45 M€. Renvoie HTTP 403 pour le rôle Scout.", body_style)]
    ]
    t_api = Table(api_table, colWidths=[130, 100, 260])
    t_api.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_ol_blue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 5),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(t_api)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Algorithme des $k$-Plus Proches Voisins ($k$-NN) et Pénalité de Standing :</b>", h2_style))
    story.append(Paragraph(
        "Pour garantir que Kylian Mbappé soit associé à des stars de standing mondial (Erling Haaland, Barcola, Dembélé) et non à des remplaçants, "
        "l'algorithme applique une pénalité logarithmique basée sur l'écart de valeur marchande :", body_style
    ))

    code_knn_full = """# Distance euclidienne pondérée k-NN (Opta Stats + Log Market Value Tier)
valDiffSq = Math.pow((Math.log10(player.market_value) - Math.log10(candidate.market_value)) * 14, 2);
statDiffSq = (
  Math.pow(player.stat_finishing - candidate.stat_finishing, 2) +
  Math.pow(player.stat_dribbling - candidate.stat_dribbling, 2) +
  Math.pow(player.stat_passing - candidate.stat_passing, 2) +
  Math.pow(player.stat_pace - candidate.stat_pace, 2) +
  Math.pow(player.stat_defending - candidate.stat_defending, 2) +
  Math.pow(player.stat_physical - candidate.stat_physical, 2)
) / 6;

distance = Math.sqrt(statDiffSq + valDiffSq);
similarityScore = Math.round(Math.max(0, 100 - distance) * 10) / 10;"""
    story.append(Paragraph(code_knn_full, code_style))

    story.append(PageBreak())

    # =========================================================================
    # SECTION E : LES TESTS, RGPD & ACCESSIBILITÉ (4 PAGES)
    # =========================================================================
    story.append(Paragraph("e. Stratégie de Tests, Conformité RGPD & Accessibilité W3C", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=10))

    story.append(Paragraph(
        "Une batterie complète de tests a été exécutée pour valider la robustesse, la sécurité et la conformité légale de la plateforme.", body_style
    ))

    test_table = [
        [Paragraph("<b>Type de Test</b>", body_style), Paragraph("<b>Périmètre & Scénario de Test</b>", body_style), Paragraph("<b>Résultat de Validation</b>", body_style)],
        [Paragraph("Tests Unitaires", body_style), Paragraph("Validation des calculs de distance $k$-NN et d'extraction scalaires Pandas.", body_style), Paragraph("100% de succès", body_style)],
        [Paragraph("Tests d'Intégration", body_style), Paragraph("Flux complet Authentification JWT ➔ Requête SQL ➔ Rendu React.", body_style), Paragraph("100% de succès", body_style)],
        [Paragraph("Tests de Sécurité RBAC", body_style), Paragraph("Tentative d'accès à la route `/director/budget` avec un token Scout.", body_style), Paragraph("Blocage HTTP 403 vérifié", body_style)],
        [Paragraph("Test de Fallback Vercel", body_style), Paragraph("Simulation de rupture de connexion avec le serveur API Python.", body_style), Paragraph("Basculement client en 0 ms", body_style)]
    ]
    t_test = Table(test_table, colWidths=[120, 250, 120])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_purple),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))
    story.append(t_test)
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>Conformité RGPD & Accessibilité Web W3C/ARIA :</b>", h2_style))
    story.append(Paragraph("• <b>Protection des données (RGPD) :</b> Hachage irréversible Bcrypt des mots de passe, absence de cookies traceurs tiers et sessions temporaires sécurisées.", bullet_style))
    story.append(Paragraph("• <b>Accessibilité W3C :</b> Conformité aux normes WCAG AA (contrastes de texte 4.5:1), balises HTML5 sémantiques et attributs ARIA pour lecteurs d'écran.", bullet_style))

    story.append(PageBreak())

    # =========================================================================
    # SECTION F & G : MAINTENANCE, GESTION DES INCIDENTS & BILAN
    # =========================================================================
    story.append(Paragraph("f & g. Maintenance Post-Déploiement, Gestion des Incidents & Bilan", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=10))

    story.append(Paragraph(
        "L'application est déployée en production et dispose d'une procédure de maintenance continue intégrant les mises à jour de données réelles Opta.", body_style
    ))
    story.append(Paragraph("• <b>Déploiement Continu (CI/CD) :</b> Intégration Git & Vercel redéployant l'application en moins de 15 secondes à chaque commit.", bullet_style))
    story.append(Paragraph("• <b>Procédure de gestion des incidents :</b> Basculement automatique en mode démo client-side en cas d'interruption du service API local Python.", bullet_style))

    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=2, color=c_purple, spaceAfter=10))
    story.append(Paragraph("<b>Validation Officielle du Bloc de Compétence 4 :</b> Ce dossier certifie la capacité à concevoir et développer une solution web robuste, sécurisée, performante et adaptée aux besoins de l'Olympique Lyonnais.", ParagraphStyle('EndingText2', parent=styles['Normal'], fontSize=9.5, leading=13.5, textColor=c_dark, alignment=TA_CENTER, fontName='Helvetica-Bold')))

    doc.build(story)
    print(f"Document d'évaluation spécifique Bloc 4 généré avec succès : {pdf_path}")

if __name__ == "__main__":
    generate_bloc4()
