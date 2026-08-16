import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.pdfgen import canvas

class NexaPurpleHeaderCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_nexa_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_nexa_decorations(self, page_count):
        self.saveState()
        
        # BANDEAU VIOLET HEADER (Couleur HEX exacte prélevée sur le logo #6f2f9f)
        c_purple_bg = colors.HexColor("#6f2f9f")
        self.setFillColor(c_purple_bg)
        self.rect(0, 782, 595.27, 60, fill=True, stroke=False)
        
        # Texte Blanc Gauche du bandeau
        self.setFont("Helvetica-Bold", 11)
        self.setFillColor(colors.white)
        self.drawString(36, 820, "BACHELOR DATA & BUSINESS INTELLIGENCE")
        self.setFont("Helvetica", 9)
        self.drawString(36, 802, "Chef de projet web – RNCP40857")
        
        # IMAGE EMBARQUÉE DU LOGO OFFICIEL NEXA DIGITAL SCHOOL (#6f2f9f)
        logo_path = r"C:\Users\user\OneDrive\Documents\web-rayane-ourad-main\nexa_logo.png"
        if os.path.exists(logo_path):
            self.drawImage(logo_path, 445, 786, width=120, height=50, mask='auto')
        else:
            self.setFont("Helvetica-Bold", 15)
            self.drawRightString(559, 818, "NEXA")
            self.setFont("Helvetica", 8.5)
            self.drawRightString(559, 804, "Digital School")
        
        # PIED DE PAGE (Conforme guide Nexa)
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 22, "Campus de Paris | Pedagogie-ia@nexa.fr | Apprenant : Rayane OURAD")
        
        page_str = f"Page {self._pageNumber} sur {page_count}"
        self.drawRightString(559, 22, page_str)
        
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 32, 559, 32)
        
        self.restoreState()

def build_pages1_to_4():
    pdf_path = r"C:\Users\user\OneDrive\Documents\OURAD_RAYANE_PROJET.pdf"
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=70,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    c_purple = colors.HexColor('#6f2f9f')
    c_dark = colors.HexColor('#0f172a')
    c_ol_blue = colors.HexColor('#0b2c5c')
    c_ol_red = colors.HexColor('#d31115')
    c_text = colors.HexColor('#334155')

    title_cover = ParagraphStyle(
        'CoverTitle', parent=styles['Heading1'], fontSize=24, leading=29,
        textColor=c_dark, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=10
    )

    subtitle_black_cover = ParagraphStyle(
        'CoverSubBlack', parent=styles['Normal'], fontSize=15, leading=19,
        textColor=c_dark, alignment=TA_CENTER, fontName='Helvetica-Bold', spaceAfter=14
    )

    desc_cover = ParagraphStyle(
        'CoverDesc', parent=styles['Normal'], fontSize=11.5, leading=16,
        textColor=c_purple, alignment=TA_CENTER, fontName='Helvetica-Oblique', spaceAfter=18
    )

    h1_style = ParagraphStyle(
        'SecH1', parent=styles['Heading1'], fontSize=13.5, leading=16.5,
        textColor=c_dark, fontName='Helvetica-Bold', spaceBefore=6, spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'SecH2', parent=styles['Heading2'], fontSize=11, leading=14.5,
        textColor=c_ol_blue, fontName='Helvetica-Bold', spaceBefore=6, spaceAfter=4
    )

    h3_style = ParagraphStyle(
        'SecH3', parent=styles['Heading3'], fontSize=9.8, leading=13.5,
        textColor=c_ol_red, fontName='Helvetica-Bold', spaceBefore=5, spaceAfter=3
    )

    body_style = ParagraphStyle(
        'BodyTxt', parent=styles['Normal'], fontSize=9, leading=13,
        textColor=c_text, alignment=TA_JUSTIFY, fontName='Helvetica', spaceAfter=6
    )

    swot_bullet = ParagraphStyle(
        'SwotBullet', parent=styles['Normal'], fontSize=8.5, leading=12,
        textColor=c_text, fontName='Helvetica', spaceAfter=3
    )

    meta_label = ParagraphStyle(
        'MetaLbl', parent=styles['Normal'], fontSize=9.5, leading=13.5,
        textColor=c_ol_blue, fontName='Helvetica-Bold'
    )

    meta_val = ParagraphStyle(
        'MetaVal', parent=styles['Normal'], fontSize=9.5, leading=13.5,
        textColor=c_text, fontName='Helvetica'
    )

    toc_title = ParagraphStyle(
        'TocTitle', parent=styles['Normal'], fontSize=9.5, leading=13.5,
        textColor=c_text, fontName='Helvetica'
    )

    toc_page = ParagraphStyle(
        'TocPage', parent=styles['Normal'], fontSize=9.5, leading=13.5,
        textColor=c_ol_blue, alignment=TA_CENTER, fontName='Helvetica-Bold'
    )

    story = []

    # =========================================================================
    # PAGE 1 : PAGE DE GARDE OFFICIELLE NEXA
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("DOSSIER DE PROJET ANNUEL CERTIFICATIF", title_cover))
    story.append(Paragraph("RECRUITMENT MATCH — OLYMPIQUE LYONNAIS 🔴🔵", subtitle_black_cover))
    story.append(Paragraph("Plateforme Full-Stack Data Scouting, Matching Opta (k-NN) & Gestion de Budget Mercato", desc_cover))
    story.append(HRFlowable(width="100%", thickness=2.5, color=c_purple, spaceBefore=8, spaceAfter=18))

    meta_t = [
        [Paragraph("Nom et Prénom de l'apprenant :", meta_label), Paragraph("Rayane OURAD", meta_val)],
        [Paragraph("Intitulé du Diplôme :", meta_label), Paragraph("Bachelor Data & Business Intelligence", meta_val)],
        [Paragraph("Titre RNCP Officiel :", meta_label), Paragraph("RNCP40857 — Chef de projet web", meta_val)],
        [Paragraph("Blocs de compétences évalués :", meta_label), Paragraph("Bloc 1 (Analyse des besoins) & Bloc 4 (Concevoir & Développer)", meta_val)],
        [Paragraph("Établissement de Formation :", meta_label), Paragraph("Nexa Digital School (Campus de Paris - Pedagogie-ia@nexa.fr)", meta_val)],
        [Paragraph("Entreprise / Client Sponsor :", meta_label), Paragraph("Olympique Lyonnais (Cellule de Scouting & Direction Sportive)", meta_val)],
        [Paragraph("URL du projet déployé :", meta_label), Paragraph("https://recruitment-match-pro.vercel.app", meta_val)],
        [Paragraph("Dépôt Git Officiel :", meta_label), Paragraph("https://github.com/L3-WEB-2026/web-rayane-ourad.git", meta_val)],
        [Paragraph("Date de réalisation :", meta_label), Paragraph("Août 2026", meta_val)]
    ]
    t_m = Table(meta_t, colWidths=[165, 325])
    t_m.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 6.5)
    ]))
    story.append(t_m)
#     story.append(PageBreak())

    # =========================================================================
    # PAGE 2 : SOMMAIRE GÉNÉRAL PAGO-CENTRÉ
    # =========================================================================
    story.append(Paragraph("SOMMAIRE DÉTAILLÉ DU DOSSIER DE PROJET ANNUEL", h1_style))
    story.append(HRFlowable(width="100%", thickness=2, color=c_purple, spaceAfter=10))

    toc_items = [
        ("PAGE 1", "Page de garde officielle & informations administratives du projet", "Garde"),
        ("PAGE 2", "Sommaire général paginé du dossier de projet annuel (RNCP40857)", "Sommaire"),
        ("PAGES 3 - 4", "Contexte & Objectifs Stratégiques OL (Analyse SWOT)", "Partie 1"),
        ("PAGES 5 - 19", "Analyse des Besoins, Veille, MoSCoW, Risques & RSE (15 pages)", "Partie 1"),
        ("PAGES 20 - 29", "Cahier des Charges, Fonctionnalités, Gantt & Budget (10 pages)", "Partie 1"),
        ("PAGES 30 - 31", "Architecture Technique Modulaire & Data ETL (Bloc 4 - 2 pages)", "Partie 2"),
        ("PAGES 32 - 33", "Maquettes & Prototypes UX/UI Glassmorphism OL (Bloc 4)", "Partie 2"),
        ("PAGES 34 - 35", "Développement Front-End React 18, Canvas SVG & Mobile (Bloc 4 - 2 pages)", "Partie 2"),
        ("PAGES 36 - 38", "Développement Back-End FastAPI, SQLite & Algorithme k-NN (Bloc 4 - 3 pages)", "Partie 2"),
        ("PAGES 39 - 40", "Tests, RGPD, Accessibilité W3C, Maintenance & Bilan (Bloc 4 - 6 pages)", "Partie 2")
    ]

    t_toc_data = [
        [Paragraph("<b>Pages</b>", ParagraphStyle('ThSec', parent=meta_label, alignment=TA_CENTER, textColor=colors.white)), 
         Paragraph("<b>Intitulé Officiel des Chapitres (Cadrage RNCP40857)</b>", ParagraphStyle('ThTitle', parent=meta_label, textColor=colors.white)),
         Paragraph("<b>Section</b>", ParagraphStyle('ThPart', parent=meta_label, alignment=TA_CENTER, textColor=colors.white))]
    ]
    for row in toc_items:
        t_toc_data.append([
            Paragraph(row[0], toc_page),
            Paragraph(row[1], toc_title),
            Paragraph(f"<b>{row[2]}</b>", ParagraphStyle('TocBadge', parent=meta_label, alignment=TA_CENTER, textColor=c_purple))
        ])

    t_toc = Table(t_toc_data, colWidths=[85, 335, 70])
    t_toc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_purple),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 6),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#ffffff'), colors.HexColor('#f8fafc')])
    ]))
    story.append(t_toc)
#     story.append(PageBreak())

    # =========================================================================
    # PAGE 3 : CONTEXTE DE L'ENTREPRISE (OL) & BESOIN À RÉSOUDRE
    # =========================================================================
    story.append(Paragraph("CONTEXTE DE L'ENTREPRISE (OL) & BESOINS À RÉSOUDRE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Présentation de l'Entreprise Sponsor : L'Olympique Lyonnais</b>", h2_style))
    story.append(Paragraph("L'Olympique Lyonnais est une institution emblématique du football professionnel français et européen. Fondé en 1950, le club a écrit l'une des plus belles pages du sport français en remportant sept titres consécutifs de Champion de France de Ligue 1 entre 2002 et 2008. Désormais intégré au groupe international <i>Eagle Football</i>, l'OL s'appuie sur une structure d'entreprise moderne et intégrée. Le club possède des infrastructures d'exception, notamment le Groupama Stadium d'une capacité de 59 186 places, la LDLC Arena, un centre médical de pointe ainsi que l'une des académies de formation les plus réputées au monde, ayant révélé des talents internationaux comme Karim Benzema, Alexandre Lacazette, Rayan Cherki et Corentin Tolisso.", body_style))

    story.append(Paragraph("L'analyse détaillée de l'organisation permet de caractériser l'entreprise selon cinq axes fondamentaux :", body_style))

    ol_info_data = [
        [Paragraph("<b>Axe d'Analyse</b>", meta_label), Paragraph("<b>Caractéristiques Rédigées de l'Entreprise Client (Olympique Lyonnais)</b>", meta_label)],
        [Paragraph("Secteur d'Activité", body_style), Paragraph("L'Olympique Lyonnais évolue à la croisée du sport professionnel de haut niveau, du spectacle vivant, des médias numériques et de la Data Intelligence appliquée à la performance.", body_style)],
        [Paragraph("Taille & Effectifs", body_style), Paragraph("En tant que groupe international, l'organisation emploie plus de 400 salariés permanents administratifs et techniques, ainsi que plus de 100 sportifs professionnels sous contrat.", body_style)],
        [Paragraph("Chiffre d'Affaires & Modèle", body_style), Paragraph("Le chiffre d'affaires annuel dépasse régulièrement 250 millions d'euros, généré par la billetterie, les droits télévisuels, le sponsoring corporate et le trading de joueurs.", body_style)],
        [Paragraph("Enjeux Stratégiques Actuels", body_style), Paragraph("Les priorités du club imposent d'assurer la soutenabilité financière post-crise des droits TV, de garantir une qualification européenne régulière et de moderniser le scouting.", body_style)],
        [Paragraph("Valeurs d'Entreprise", body_style), Paragraph("La philosophie de l'OL repose sur l'excellence de l'académie de formation, la rigueur d'ingénierie sportive, l'innovation technologique et un fort ancrage territorial.", body_style)]
    ]
    t_ol = Table(ol_info_data, colWidths=[135, 355])
    t_ol.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_ol_blue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 5)
    ]))
    story.append(t_ol)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2. Identification du Problème et Opportunité de Marché</b>", h2_style))
    story.append(Paragraph("Le marché mondial des transferts de football connaît actuellement une inflation spectaculaire, portée par la puissance financière de la Premier League anglaise et l'arrivée de fonds souverains. Dans ce contexte hyper-concurrentiel, l'Olympique Lyonnais doit composer avec une enveloppe budgétaire allouée au Mercato plafonnée à <b>45 millions d'euros</b>. Cette contrainte financière est strictement contrôlée par la Direction Nationale du Contrôle de Gestion (DNCG) ainsi que par la réglementation du <i>Squad Cost Ratio</i> fixée par l'UEFA, qui limite l'ensemble des dépenses salariales et d'indemnités à 70 % des revenus globaux du club.", body_style))
    story.append(Paragraph("<b>Le problème majeur identifié :</b> Historiquement, la cellule de scouting de l'Olympique Lyonnais souffrait d'une dispersion importante de ses rapports d'observation sur des fichiers Excel isolés, de biais d'évaluation subjective propres à chaque recruteur et d'une incapacité technique à tester en temps réel l'impact d'un nouveau salaire sur le budget global du club.", body_style))
    story.append(Paragraph("<b>L'opportunité de marché :</b> Pour répondre à cette problématique, une opportunité stratégique majeure réside dans l'exploitation des données de performance réelles Opta et FBref portant sur 2 854 joueurs professionnels des 5 grands championnats européens. L'implémentation de l'algorithme d'Intelligence Artificielle des k-Plus Proches Voisins (k-NN) permet à l'OL d'identifier scientifiquement des recrues à fort potentiel sous-évaluées sur le marché, offrant ainsi une alternative performante et financièrement soutenable face à la concurrence.", body_style))
#     story.append(PageBreak())

    # =========================================================================
    # PAGE 4 : OBJECTIFS STRATÉGIQUES ET MATRICE SWOT AVEC TIRETS POINT PAR POINT
    # =========================================================================
    story.append(Paragraph("OBJECTIFS STRATÉGIQUES DU PROJET & MATRICE SWOT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Définition des Objectifs Stratégiques du Projet</b>", h2_style))
    story.append(Paragraph("Afin d'apporter une réponse globale aux enjeux identifiés, le projet <b>Recruitment Match OL</b> s'articules autour de trois objectifs stratégiques majeurs parfaitement reliés aux priorités d'entreprise de l'Olympique Lyonnais :", body_style))
    story.append(Paragraph("• <b>Centralisation Data & Matching k-NN :</b> Centraliser l'ensemble des données de performance réelles de 2 854 joueurs européens et calculer en moins de 15 millisecondes des jumeaux statistiques grâce à l'algorithme des k-Plus Proches Voisins (k-NN).", body_style))
    story.append(Paragraph("• <b>Pilotage Financier Mercato DNCG :</b> Offrir un outil de simulation budgétaire en temps réel à la Direction Sportive afin d'arbitrer les indemnités de transfert et de respecter scrupuleusement l'enveloppe de 45 millions d'euros.", body_style))
    story.append(Paragraph("• <b>Sécurité & Rôles Applicatifs RBAC :</b> Garantir la sécurité et la confidentialité des données salariales grâce à un contrôle d'accès strict basé sur les rôles (RBAC) et une authentification sécurisée par jetons JWT Bearer.", body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2. Matrice d'Analyse Stratégique SWOT (Présentation Point par Point)</b>", h2_style))
    story.append(Paragraph("L'analyse SWOT ci-dessous structure le positionnement stratégique du projet point par point avec des puces claires :", body_style))

    # Matrice SWOT point par point avec tirets / puces
    swot_data_bullets = [
        [Paragraph("<b>FORCES INTERNES (Strengths)</b>", meta_label), Paragraph("<b>FAIBLESSES INTERNES (Weaknesses)</b>", meta_label)],
        [
            Paragraph("• Académie de formation d'élite (Génération Lyon) produisant des pépites à haute valeur marchande.<br/>"
                      "• Infrastructures technologiques de pointe au Groupama Stadium (OL Play & Data Center).<br/>"
                      "• Marque internationale forte et attractivité historique auprès des joueurs sud-américains.<br/>"
                      "• Réseau étendu de recruteurs seniors possédant une solide expertise du terrain.", swot_bullet),
            Paragraph("• Enveloppe budgétaire allouée au Mercato plafonnée à 45 millions d'euros.<br/>"
                      "• Encadrement strict de la masse salariale par la DNCG et les règles UEFA.<br/>"
                      "• Dispersion historique des rapports de scouting sur des fichiers Excel isolés.<br/>"
                      "• Retards d'arbitrage lors des clôtures de Mercato en l'absence d'outils unifiés.", swot_bullet)
        ],
        [Paragraph("<b>OPPORTUNITÉS EXTERNES (Opportunities)</b>", meta_label), Paragraph("<b>MENACES EXTERNES (Threats)</b>", meta_label)],
        [
            Paragraph("• Jeux de données réels Opta et FBref disponibles sur 2 854 joueurs professionnels.<br/>"
                      "• Machine Learning (k-NN) pour détecter scientifiquement des recrues sous-évaluées.<br/>"
                      "• Numérisation des simulations budgétaires pour accélérer les décisions de la direction.<br/>"
                      "• Architecture cloud React 18 et Python FastAPI garantissant une haute réactivité.", swot_bullet),
            Paragraph("• Inflation constante des prix du marché portée par les clubs de Premier League.<br/>"
                      "• Surenchère salariale lors des négociations de contrats avec les agents.<br/>"
                      "• Risque de biais statistique si les métriques ne sont pas étalonnées sur 90 min réelles.<br/>"
                      "• Risque de fuite de données budgétaires confidentielles en l'absence de sécurité RBAC.", swot_bullet)
        ]
    ]
    t_swot = Table(swot_data_bullets, colWidths=[245, 245])
    t_swot.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#dcfce7')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#fee2e2')),
        ('BACKGROUND', (0,2), (0,2), colors.HexColor('#e0f2fe')),
        ('BACKGROUND', (1,2), (1,2), colors.HexColor('#fef3c7')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))
    story.append(t_swot)
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>3. Alignement des Résultats SWOT avec la Solution Web</b>", h3_style))
    story.append(Paragraph("En croisant les forces internes de l'Olympique Lyonnais avec les opportunités offertes par les technologies web modernes, le projet transforme une contrainte budgétaire stricte (45 M€) en un avantage concurrentiel majeur. Grâce à l'architecture modulaire découpée associant React 18 et Python FastAPI, la plateforme sécurise l'ensemble des investissements financiers du club tout en maximisant la performance sportive.", body_style))

    doc.build(story, canvasmaker=NexaPurpleHeaderCanvas)
    print("SWOT point par point avec tirets généré avec succès !")

if __name__ == "__main__":
    build_pages1_to_4()
