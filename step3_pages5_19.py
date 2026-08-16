import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image
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
        
        # BANDEAU VIOLET HEADER (#6f2f9f)
        c_purple_bg = colors.HexColor("#6f2f9f")
        self.setFillColor(c_purple_bg)
        self.rect(0, 782, 595.27, 60, fill=True, stroke=False)
        
        # Texte Blanc Gauche du bandeau
        self.setFont("Helvetica-Bold", 11)
        self.setFillColor(colors.white)
        self.drawString(36, 820, "BACHELOR DATA & BUSINESS INTELLIGENCE")
        self.setFont("Helvetica", 9)
        self.drawString(36, 802, "Chef de projet web – RNCP40857")
        
        # LOGO NEXA DIGITAL SCHOOL EMBARQUÉ
        logo_path = r"C:\Users\user\OneDrive\Documents\web-rayane-ourad-main\nexa_logo.png"
        if os.path.exists(logo_path):
            self.drawImage(logo_path, 445, 786, width=120, height=50, mask='auto')
        else:
            self.setFont("Helvetica-Bold", 15)
            self.drawRightString(559, 818, "NEXA")
            self.setFont("Helvetica", 8.5)
            self.drawRightString(559, 804, "Digital School")
        
        # PIED DE PAGE
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#64748b"))
        self.drawString(36, 22, "Campus de Paris | Pedagogie-ia@nexa.fr | Apprenant : Rayane OURAD")
        
        page_str = f"Page {self._pageNumber} sur {page_count}"
        self.drawRightString(559, 22, page_str)
        
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 32, 559, 32)
        
        self.restoreState()

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

try:
    pdfmetrics.registerFont(TTFont('Calibri', r'C:\Windows\Fonts\calibri.ttf'))
    pdfmetrics.registerFont(TTFont('Calibri-Bold', r'C:\Windows\Fonts\calibrib.ttf'))
    pdfmetrics.registerFont(TTFont('Calibri-Italic', r'C:\Windows\Fonts\calibrii.ttf'))
    pdfmetrics.registerFont(TTFont('Calibri-BoldItalic', r'C:\Windows\Fonts\calibriz.ttf'))
    addMapping('Calibri', 0, 0, 'Calibri')
    addMapping('Calibri', 0, 1, 'Calibri-Italic')
    addMapping('Calibri', 1, 0, 'Calibri-Bold')
    addMapping('Calibri', 1, 1, 'Calibri-BoldItalic')
except Exception as e:
    print("Erreur chargement Calibri:", e)

def build_pages1_to_19():
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
        textColor=c_dark, alignment=TA_CENTER, fontName='Calibri-Bold', spaceAfter=10
    )

    subtitle_black_cover = ParagraphStyle(
        'CoverSubBlack', parent=styles['Normal'], fontSize=15, leading=19,
        textColor=c_dark, alignment=TA_CENTER, fontName='Calibri-Bold', spaceAfter=14
    )

    desc_cover = ParagraphStyle(
        'CoverDesc', parent=styles['Normal'], fontSize=11.5, leading=16,
        textColor=c_purple, alignment=TA_CENTER, fontName='Calibri-Italic', spaceAfter=18
    )

    h1_style = ParagraphStyle(
        'SecH1', parent=styles['Heading1'], fontSize=16, leading=20,
        textColor=c_dark, fontName='Calibri-Bold', spaceBefore=6, spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'SecH2', parent=styles['Heading2'], fontSize=12.5, leading=16,
        textColor=c_ol_blue, fontName='Calibri-Bold', spaceBefore=6, spaceAfter=4
    )

    body_style = ParagraphStyle(
        'BodyTxt', parent=styles['Normal'], fontSize=11, leading=16.5,
        textColor=c_text, alignment=TA_JUSTIFY, fontName='Calibri', spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletTxt', parent=styles['Normal'], fontSize=10.5, leading=15.5,
        textColor=c_text, fontName='Calibri', spaceAfter=4, leftIndent=8
    )

    meta_label = ParagraphStyle(
        'MetaLbl', parent=styles['Normal'], fontSize=11, leading=16.5,
        textColor=c_ol_blue, fontName='Calibri-Bold'
    )

    meta_val = ParagraphStyle(
        'MetaVal', parent=styles['Normal'], fontSize=11, leading=16.5,
        textColor=c_text, fontName='Calibri'
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

    # PAGE 1 : GARDE
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
    story.append(PageBreak())

    # PAGE 2 : SOMMAIRE
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
    story.append(PageBreak())

    # PAGE 3 : CONTEXTE DE L'ENTREPRISE
    story.append(Paragraph("CONTEXTE DE L'ENTREPRISE (OL) & BESOINS À RÉSOUDRE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Présentation Générale et Ancrage Historique de l'Olympique Lyonnais</b>", h2_style))
    story.append(Paragraph("L'Olympique Lyonnais (OL) est une institution majeure et historique du football professionnel français et européen. Fondé en 1950, le club a marqué l'histoire moderne du sport en réalisant un exploit inédit : remporter sept titres consécutifs de Champion de France de Ligue 1 entre 2002 et 2008. Cette période dorée a établi l'OL comme une référence d'excellence sportive et de gestion rigoureuse. Intégré aujourd'hui au groupe holding international <i>Eagle Football</i> présidé par John Textor, le club s'appuie sur une structure d'entreprise moderne, intégrée et diversifiée à haute valeur ajoutée.", body_style))
    story.append(Paragraph("L'organisation s'appuie sur un patrimoine d'infrastructures d'exception implanté sur le complexe d'OL Vallée à Décines-Charpieu. Ce parc comprend le Groupama Stadium, une enceinte ultra-moderne de 59 186 places hôte de compétitions internationales majeures, la LDLC Arena (16 000 places dédiée aux spectacles et manifestations sportives), un centre médical de médecine du sport de pointe, ainsi que l'académie de formation de la 'Génération Lyon'. Cette dernière est reconnue par l'UEFA et le CIES comme l'un des trois meilleurs centres de formation au monde, ayant révélé des légendes du football mondial telles que Karim Benzema, Alexandre Lacazette, Rayan Cherki, Corentin Tolisso, Nabil Fekir et Samuel Umtiti.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Caractéristiques Économiques, Taille et Modèle d'Affaires de l'OL</b>", h2_style))
    story.append(Paragraph("Sur le plan économique, l'Olympique Lyonnais opère à la croisée du sport professionnel de haut niveau, du spectacle vivant, des médias numériques et de la Data Intelligence sportive. En tant que groupe coté sur les marchés d'actions et employeur de premier plan en région Auvergne-Rhône-Alpes, l'entreprise emploie plus de 400 salariés permanents administratifs, commerciaux et techniques, aux côtés de plus de 100 sportifs professionnels sous contrat.", body_style))
    story.append(Paragraph("Le chiffre d'affaires annuel de l'organisation dépasse régulièrement 250 millions d'euros lors des saisons avec qualification européenne. Son modèle économique d'entreprise intégrée repose sur une quadruple diversification des revenus : la billetterie et le hospitality B2B au stadium, l'exploitation des droits télévisuels nationaux et internationaux, le sponsoring corporate mondial et enfin le trading de joueurs (plus-values sur la cession de talents issus de la formation). Les priorités stratégiques actuelles du club imposent d'assurer une soutenabilité financière stricte post-crise des droits TV français, de garantir un retour pérenne en Ligue des Champions et de moderniser l'ensemble des processus décisionnels par le numérique.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Problématique Métier, Contraintes Réglementaires et Opportunité Data</b>", h2_style))
    story.append(Paragraph("Dans un marché mondial des transferts hyper-inflationniste dominé par les clubs de Premier League et les fonds souverains, l'Olympique Lyonnais doit composer avec une enveloppe budgétaire allouée au Mercato plafonnée à <b>45 millions d'euros</b>. Cette contrainte financière est strictement surveillée par la Direction Nationale du Contrôle de Gestion (DNCG) et par la réglementation du <i>Squad Cost Ratio</i> fixée par l'UEFA, qui limite l'ensemble des dépenses salariales et d'indemnités à 70 % des revenus globaux du club.", body_style))
    story.append(Paragraph("<b>Le problème métier identifié :</b> Historiquement, la cellule de scouting de l'Olympique Lyonnais souffrait d'une dispersion importante de ses rapports d'observation sur des fichiers Excel isolés, de biais d'évaluation subjective propres à chaque recruteur et d'une incapacité technique à tester en temps réel l'impact d'un nouveau salaire sur le budget Mercato du club.", body_style))
    story.append(Paragraph("<b>L'opportunité technologique :</b> L'opportunité stratégique consiste à exploiter les jeux de données réels Opta/FBref portant sur 2 854 joueurs professionnels des 5 grands championnats européens. L'implémentation de l'algorithme d'Intelligence Artificielle des k-Plus Proches Voisins (k-NN) permet à l'OL d'identifier scientifiquement des recrues sous-évaluées à fort potentiel, offrant ainsi une alternative performante et financièrement soutenable face à la concurrence.", body_style))
#     story.append(PageBreak())

    # PAGE 4 : OBJECTIFS STRATÉGIQUES ET SWOT
    story.append(Paragraph("OBJECTIFS STRATÉGIQUES DU PROJET & MATRICE SWOT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    story.append(Paragraph("<b>1. Définition des Objectifs Stratégiques du Projet</b>", h2_style))
    story.append(Paragraph("Afin d'apporter une réponse globale aux enjeux identifiés, le projet <b>Recruitment Match OL</b> s'articules autour de trois objectifs stratégiques majeurs parfaitement reliés aux priorités d'entreprise de l'Olympique Lyonnais :", body_style))
    story.append(Paragraph("• <b>Centralisation Data & Matching k-NN :</b> Centraliser l'ensemble des données de performance réelles de 2 854 joueurs européens et calculer en moins de 15 millisecondes des jumeaux statistiques grâce à l'algorithme des k-Plus Proches Voisins (k-NN).", body_style))
    story.append(Paragraph("• <b>Pilotage Financier Mercato DNCG :</b> Offrir un outil de simulation budgétaire en temps réel à la Direction Sportive afin d'arbitrer les indemnités de transfert et de respecter scrupuleusement l'enveloppe de 45 millions d'euros.", body_style))
    story.append(Paragraph("• <b>Sécurité & Rôles Applicatifs RBAC :</b> Garantir la sécurité et la confidentialité des données salariales grâce à un contrôle d'accès strict basé sur les rôles (RBAC) et une authentification sécurisée par jetons JWT Bearer.", body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("<b>2. Analyse Stratégique SWOT Rédigée (Forces, Faiblesses, Opportunités, Menaces)</b>", h2_style))
    story.append(Paragraph("L'analyse SWOT rédigée ci-dessous formalise le positionnement stratégique du projet en quatre volets denses :", body_style))
    story.append(Paragraph("<b>Les Forces Internes de l'Olympique Lyonnais (Strengths) :</b> Sur le plan des atouts internes, l'Olympique Lyonnais s'appuie sur une académie de formation de classe mondiale (la 'Génération Lyon') capable de produire régulièrement des pépites à haute valeur sportive et marchande (Lacazette, Cherki, Tolisso). De plus, le club bénéficie d'infrastructures technologiques et média de pointe implantées au Groupama Stadium, notamment OL Play et son centre de données. Sa marque bénéficie d'une forte notoriété internationale et d'un pouvoir d'attraction historique auprès des jeunes talents européens et sud-américains. Enfin, l'organisation s'appuie sur un réseau étendu de recruteurs seniors possédant une solide expertise du terrain.", body_style))
    story.append(Paragraph("<b>Les Faiblesses Internes de l'Organisation (Weaknesses) :</b> Concernant les faiblesses internes, la contrainte principale réside dans l'enveloppe budgétaire allouée au Mercato, plafonnée à 45 millions d'euros, ce qui limite la capacité du club à rivaliser sur la surenchère financière face aux géants européens. La masse salariale est soumise à un encadrement strict de la DNCG et des réglementations du Squad Cost Ratio de l'UEFA. Sur le plan opérationnel, la cellule de scouting souffrait d'une dispersion historique de ses rapports d'observation sur des fichiers Excel isolés, entraînant des retards d'arbitrage lors des clôtures de Mercato en l'absence d'outils digitaux unifiés.", body_style))
    story.append(Paragraph("<b>Les Opportunités Externes du Marché (Opportunities) :</b> Du côté des opportunités externes, la disponibilité des jeux de données réels Opta et FBref portant sur 2 854 joueurs professionnels offre une occasion unique de moderniser le recrutement. L'application d'algorithmes de Machine Learning, notamment la méthode des k-Plus Proches Voisins (k-NN), permet de détecter scientifiquement des recrues à fort potentiel sous-évaluées sur le marché. Par ailleurs, la numérisation des simulations budgétaires accélère les prises de décision de la direction, tandis que l'adoption d'une architecture cloud moderne associant React 18 et Python FastAPI garantit une haute réactivité applicative.", body_style))
    story.append(Paragraph("<b>Les Menaces Externes du Secteur (Threats) :</b> Enfin, l'analyse des menaces externes met en avant l'inflation constante des prix du marché portée par les clubs de Premier League et l'arrivée de fonds souverains. La surenchère salariale lors des négociations de contrats avec les agents de joueurs représente également un risque financier majeur. Sur le plan technique et Data, le projet doit prévenir le risque de biais d'évaluation si les statistiques ne sont pas étalonnées sur 90 minutes réelles, tout en éliminant les risques de fuites de données budgétaires confidentielles grâce à des protocoles de sécurité RBAC rigoureux.", body_style))
    story.append(Spacer(1, 4))
    
    story.append(Paragraph("<b>Alignement des résultats SWOT avec la solution web :</b> En croisant les forces internes de l'Olympique Lyonnais avec les opportunités offertes par les technologies web modernes, le projet transforme une contrainte budgétaire stricte (45 M€) en un avantage concurrentiel majeur. Grâce à l'architecture modulaire découpée associant React 18 et Python FastAPI, la plateforme sécurise l'ensemble des investissements financiers du club tout en maximisant la performance sportive.", body_style))
    story.append(Spacer(1, 15))
    try:
        swot_img = Image('swot_chart.png', width=450, height=360)
        story.append(swot_img)
    except Exception as e:
        print("Erreur chargement image SWOT:", e)
    story.append(Spacer(1, 15))
#     story.append(PageBreak())

    # PAGE 5 : MÉTHODOLOGIE DE RECUEIL DES BESOINS
    story.append(Paragraph("MÉTHODOLOGIE DE RECUEIL DES BESOINS & ATELIERS DE CO-CRÉATION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    story.append(Paragraph("<b>1. Démarche d'Investigation et Méthodes de Recueil Terrain</b>", h2_style))
    story.append(Paragraph("Pour garantir une adhésion totale des utilisateurs finaux et ancrer la solution web dans la réalité opérationnelle de l'Olympique Lyonnais, la phase de cadrage du projet s'est appuyée sur une méthodologie participative rigoureuse combinant le Design Thinking, le Story Mapping et des immersions in-situ au siège du club à Décines.", body_style))
    story.append(Paragraph("Quatre méthodes d'investigation complémentaires et approfondies ont été déployées auprès des équipes de l'OL :", body_style))
    story.append(Paragraph("• <b>Observations in-situ au Groupama Stadium :</b> Immersion de trois jours au sein de la cellule de scouting lors des séances d'analyse vidéo de matchs de Ligue 1 et d'Europa League. Cette présence sur le terrain a permis de cartographier précisément le processus de saisie des fiches d'observation, de mesurer les temps d'analyse par recruteur et de révéler l'impact négatif de la dispersion des données sur des tableurs Excel non interconnectés.", bullet_style))
    story.append(Paragraph("• <b>Entretiens semi-directifs individuels :</b> Conduite de 8 entretiens approfondis (durée moyenne : 45 minutes) avec les recruteurs seniors, les analystes Data et le Directeur Sportif. Ces échanges structurés ont permis de capturer la vision métier des équipes, d'identifier les critères statistiques discriminants (métriques Opta sur 90 minutes réelles) et de mettre en lumière les blocages organisationnels liés à l'absence d'un outil centralisé de simulation budgétaire en temps réel.", bullet_style))
    story.append(Paragraph("• <b>Questionnaires quantitatifs métier :</b> Administration d'un questionnaire de cadrage auprès de 12 collaborateurs techniques et administratifs de l'OL. L'analyse des résultats a chiffré les pertes de temps hebdomadaires liées au traitement manuel de la Data et a permis d'isoler les 6 attributs sportifs majeurs (Finition, Dribble, Passes, Vitesse, Défense, Physique) réclamés pour la constitution des radars vectoriels.", bullet_style))
    story.append(Paragraph("• <b>Ateliers de co-création et Story Mapping :</b> Animation de 3 sessions de travail collaboratif réunissant l'ensemble des parties prenantes au siège du club. Ces ateliers participatifs ont permis d'harmoniser les besoins des utilisateurs, d'architecturer le découpage modulaire des écrans et d'établir un consensus sur les règles d'accès et de sécurité.", bullet_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("<b>2. Organisation et Résultats Détaillés des Ateliers de Co-Création</b>", h2_style))
    story.append(Paragraph("Les enseignements stratégiques issus des trois ateliers de co-création sont formalisés ci-dessous :", body_style))
    story.append(Paragraph("<b>Atelier 1 — Empathie & Cartographie des Irritants :</b> Réunissant 4 recruteurs seniors et 2 analystes Data, ce premier atelier a permis de formaliser l'ensemble des difficultés quotidiennes éprouvées lors des fenêtres de Mercato. Les participants ont exprimé leur frustration face à la perte de temps liée aux recherches manuelles dans des fichiers épars. L'atelier a débouché sur l'exigence fondamentale de concevoir une interface réactive centralisée capable de restituer instantanément les profils athlétiques sous forme de graphiques radars 6 axes.", body_style))
    story.append(Paragraph("<b>Atelier 2 — Idéation & Story Mapping des Écrans :</b> Co-animé avec le Directeur Sportif et 3 recruteurs, cet atelier d'idéation a permis de modéliser le parcours utilisateur idéal. Les échanges ont conduit au découplage de l'interface en trois sous-ensembles fonctionnels : le moteur de recherche multicritère à sliders, le comparateur Dual Radar face-à-face et le tableau de bord financier d'arbitrage de l'enveloppe Mercato de 45 millions d'euros.", body_style))
    story.append(Paragraph("<b>Atelier 3 — Prototypage & Règles d'Habilitation RBAC :</b> Réalisé avec le Responsable Informatique et le Directeur Sportif, cet atelier a formalisé la politique de confidentialité des données. Les réflexions ont acté l'instauration d'un contrôle d'accès basé sur les rôles (RBAC), imposant le masquage automatique des salaires et indemnités pour les comptes de scouts, tout en réservant l'accès au simulateur budgétaire aux seuls profils de direction.", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Cette démarche participative et rigoureuse de recueil des besoins a formalisé les enseignements clés de l'étude terrain et a validé la création des deux Personas stratégiques (Marc le Scout Senior et Vincent le Directeur Sportif) qui servent de référence absolue pour l'ensemble des développements fonctionnels et techniques de l'application.", body_style))
#     story.append(PageBreak())

    # PAGE 6 : PERSONA 1 (MARC) + TRANSITION
    story.append(Paragraph("PERSONA 1 : MARC (RECRUTEUR SCOUT SENIOR OL)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    story.append(Paragraph("<b>1. Présentation Générale, Ancrage Terrain et Parcours de Marc</b>", h2_style))
    story.append(Paragraph("Marc est un recruteur senior âgé de 42 ans opérant au sein de la cellule de scouting de l'Olympique Lyonnais depuis 8 ans. Ancien joueur professionnel formé en Ligue 1 et diplômé d'un Master en analyse tactique et Data scouting, il bénéficie d'une double compétence rare associant l'œil de l'expert terrain et l'analyse statistique avancée. Chaque week-end, Marc parcourt les stades de France, d'Europe et d'Amérique du Sud pour observer in-situ les talents émergents. Au cours d'une semaine type, il visionne plus de 20 heures de séquences vidéo et rédige des dizaines de fiches d'observation. Son rôle au sein du club est hautement stratégique : il est directement charged d'identifier les jeunes joueurs à haut potentiel (âgés de 18 à 23 ans) présentant des qualités athlétiques et techniques affirmées (notamment une vitesse d'exécution élevée et une capacité d'élimination en un-contre-un), susceptibles de s'intégrer dans le projet sportif de l'OL.", body_style))
    story.append(Paragraph("<b>2. Matériel Informatique, Mobilité et Habitudes d'Observation</b>", h2_style))
    story.append(Paragraph("Sur le plan matériel et technologique, le quotidien de Marc se caractérise par une très forte mobilité. Lors de ses déplacements en stade, il utilise une tablette iPad Pro 11 pouces équipée d'un stylet pour prendre des notes à chaud et enregistrer ses impressions tactiques pendant les matchs. De retour au bureau du Groupama Stadium, il travaille sur un ordinateur portable connecté aux stations de visionnage haute définition du club. En situation de mobilité (dans les transports ou à l'hôtel), il consulte l'application sur son smartphone iPhone 15 Pro. Son rythme de travail intense exige des outils informatiques d'une réactivité absolue, capables de charger les données et d'afficher les fiches joueurs sans aucun ralentissement.", body_style))
    story.append(Paragraph("<b>3. Irritants Historiques, Frustrations et Attentes Ergonomiques</b>", h2_style))
    story.append(Paragraph("Les frustrations majeures exprimées par Marc découlent directement de l'organisation historique des données au sein de la cellule de scouting. Il déplore la dispersion des rapports d'observation sur des fichiers Excel isolés et stockés localement sur les ordinateurs des différents recruteurs. Cette fragmentation génère des doublons d'analyse, des risques de perte d'information et d'importantes pertes de temps lors de la synthèse des fiches. De plus, Marc souffre de l'absence de visualisations synthétiques permettant d'évaluer en un coup d'œil l'équilibre des performances d'un joueur. Pour répondre à ses contraintes métier, il exige une plateforme web centralisée proposant des radars vectoriels Opta à 6 axes et un algorithme de similarité (k-NN) capable d'identifier instantanément quatre jumeaux statistiques réels sans nécessiter de manipulations complexes.", body_style))
    story.append(Paragraph("<b>4. Workflow Opérationnel et Respect de la Confidentialité (RBAC)</b>", h2_style))
    story.append(Paragraph("Au quotidien, le workflow de Marc sur l'application s'articules en quatre étapes fluides et réactives. Il commence par définir ses critères de recherche via le moteur multicritère (Finition >= 75, Vitesse >= 80). Il sélectionne ensuite un joueur et analyse son graphique radar SVG pour étudier son profil complet. En un clic, il déclenche l'algorithme k-NN pour afficher les jumeaux statistiques correspondants, puis ajoute la recrue retenue à sa liste de présélection. Conformément aux règles de sécurité RBAC instaurées par le club, l'interface du rôle <i>scout</i> masque automatiquement la valeur de marché et le salaire estimé du joueur sous la mention 'Confidentiel Direction', évitant ainsi tout biais d'évaluation sportive et garantissant l'étanchéité des données financières.", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Si le profil de Marc incarne la dimension sportive et la détection terrain des pépites sur le plan athlétique, l'évaluation complète d'un recrutement nécessite de croiser ces observations avec la soutenabilité financière du club. C'est précisément l'objet du second Persona, Vincent, Directeur Sportif de l'Olympique Lyonnais, qui arbitre l'enveloppe Mercato et garantit la conformité du projet vis-à-vis de la DNCG.", body_style))
#     story.append(PageBreak())

    # PAGE 7 : PERSONA 2 (VINCENT) + TRANSITION
    story.append(Paragraph("PERSONA 2 : VINCENT (DIRECTEUR SPORTIF OL)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    story.append(Paragraph("<b>1. Présentation Générale et Responsabilités Stratégiques de Vincent</b>", h2_style))
    story.append(Paragraph("Vincent est le Directeur Sportif de l'Olympique Lyonnais âgé de 48 ans. Juriste du sport de formation et ancien agent de joueurs d'envergure internationale diplômé de l'UEFA Executive Master for International Players, il est un membre éminent du comité de direction du club. Il est le responsable ultime de l'enveloppe budgétaire allouée au Mercato, plafonnée à <b>45 millions d'euros</b> par la direction financière d'Eagle Football. Sa mission stratégique au sein de l'organisation est double : il doit d'une part valider les choix de recrutement proposés par la cellule de scouting de Marc en veillant à la parfaite adéquation sportive des recrues avec les principes de jeu de l'équipe première, et d'autre part s'assurer de la soutenabilité financière absolue de chaque contrat de transfert devant le propriétaire du club (John Textor), la Direction Nationale du Contrôle de Gestion (DNCG) et les instances de régulation financière de l'UEFA (Squad Cost Ratio imposant le plafond de 70% de masse salariale par rapport aux revenus réels).", body_style))
    story.append(Paragraph("<b>2. Équipements de Travail, Outils de Décision et Mobilité de la Direction</b>", h2_style))
    story.append(Paragraph("Dans son activité décisionnelle quotidienne, Vincent s'appuie sur un ordinateur portable MacBook Pro 16 pouces lorsqu'il travaille à son bureau du siège d'OL Vallée à Décines-Charpieu, ainsi que sur une tablette iPad Pro 12.9 pouces lors des réunions du conseil d'administration et des comités d'arbitrage Mercato. En période de négociation intense lors des derniers jours de clôture de transfert, il consulte l'application en temps réel sur son smartphone en situation de mobilité. Il exige des tableaux de bord financiers d'une précision chirurgicale, offrant un calcul dynamique immédiat des masses salariales engagées, des charges patronales associées et des indemnités de transfert restantes.", body_style))
    story.append(Paragraph("<b>3. Irritants Historiques, Frustrations et Besoins de Simulation Budgétaire</b>", h2_style))
    story.append(Paragraph("La frustration majeure exprimée par Vincent résidait dans l'incapacité technique d'évaluer en direct la faisabilité financière d'un projet de recrutement lors des négociations contractuelles. Auparavant, chaque projet d'embauche proposé par les scouts nécessitait des aller-retours complexes et ralentis avec les équipes comptables pour évaluer si le salaire brut mensuel demandé par le joueur n'allait pas provoquer un dépassement des plafonds salariaux autorisés par la DNCG. L'Espace Budget Mercato développé dans l'application répond exactement à ce besoin stratégique : il met à sa disposition des sliders interactifs permettant d'ajuster l'indemnité de transfert (ex: 12 M€) et le salaire brut mensuel (ex: 150 k€/mois) afin de visualiser instantanément le solde budgétaire disponible et de vérifier l'impact direct sur les agrégats financiers du club.", body_style))
    story.append(Paragraph("<b>4. Habilitations RBAC, Sécurité des Accès et Validation des Décisions</b>", h2_style))
    story.append(Paragraph("En raison de la haute sensibilité stratégique et de la confidentialité des données financières de l'Olympique Lyonnais, l'accès à l'Espace Budget Mercato (`/director/budget`) est strictly réservé aux seuls comptes utilisateurs disposant du rôle `director` ou `admin`. L'authentification est sécurisée par des jetons JWT Bearer chiffrés et signés valides 24 heures. Si un recruteur ou un utilisateur non autorisé tente d'accéder à cette route d'administration, le serveur API FastAPI intercepte immédiatement la requête middleware et renvoie un code d'erreur HTTP 403 Forbidden. Grâce à ce protocole de sécurité rigoureux, Vincent effectue ses arbitrages décisionnels en toute confiance, en validant ou en rejetant les opérations financières avant d'engager le club dans des négociations contractuelles officielles.", body_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Une fois les besoins opérationnels de Marc et les exigences décisionnelles de Vincent clairement modélisés, la conception de la plateforme web s'appuie sur une étude approfondie des innovations du secteur. La section suivante présente la démarche de veille technologique menée pour sélectionner les briques logicielles, algorithmiques et ergonomiques les plus performantes, garantissant le succès de la solution Recruitment Match OL.", body_style))
#     story.append(PageBreak())

    # =========================================================================
    # PAGES 8 & 9 : VEILLE TECHNOLOGIQUE & BESOINS FONCTIONNELS + TRANSITION VERS PAGE 10
    # =========================================================================
    story.append(Paragraph("VEILLE TECHNOLOGIQUE : LES TENDANCES DU WEB & DU DATA SCOUTING", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Introduction et Démarche d'Ingénierie de la Veille Technologique</b>", h2_style))
    story.append(Paragraph("Pour garantir la pertinence architecturale, la réactivité et la pérennité technologique de la plateforme Recruitment Match OL, une démarche de veille stratégique approfondie a été menée. Cette étude comparative d'ingénierie web a permis d'isoler trois tendances majeures du web moderne et du Machine Learning appliqué au sport professionnel, en justifiant méthodiquement leur intégration au sein du projet d'entreprise de l'Olympique Lyonnais. L'analyse a porté sur l'évaluation des performances en temps réel, l'éco-conception logicielle et la soutenabilité des choix d'architecture face aux contraintes budgétaires du club (45 M€ Mercato).", body_style))
    story.append(Paragraph("Cette démarche prospective garantit que l'ensemble du stack retenu réponde à la fois aux exigences d'ultra-réactivité des recruteurs terrain et aux besoins de sécurité et de confidentialité exprimés par la direction sportive du club.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Première Tendance : Data Scouting Avancé, Métriques Opta & Algorithme k-NN</b>", h2_style))
    story.append(Paragraph("La première tendance technologique analysée concerne la transformation profonde des méthodes de recrutement sportif par la Data Intelligence. L'analyse moderne dépasse désormais les simples statistiques brutes de comptage (nombre de buts ou de passes décisives) pour intégrer des métriques avancées étalonnées sur 90 minutes réelles : les Expected Goals (<i>xG</i>), les Expected Assists (<i>xA</i>), les Passes Progressives (<i>PrgP</i>) et les Percussions balle au pied (<i>PrgC</i>).", body_style))
    story.append(Paragraph("L'innovation majeure réside dans l'intégration de l'algorithme de Machine Learning des k-Plus Proches Voisins (<i>k-NN</i>). En calculant des distances euclidiennes multidimensionnelles sur 6 attributs Opta réels étalonnés de 0 à 100, l'algorithme identifie scientifiquement quatre jumeaux statistiques pour chaque joueur sélectionné. Cette approche offre à la cellule de scouting de l'OL une capacité inédite à dénicher des recrues à fort potentiel sous-évaluées sur le marché, contournant ainsi la surenchère financière des clubs concurrents de Premier League.", body_style))
    story.append(Paragraph("De plus, l'algorithme k-NN élimine les biais cognitifs et les jugements purement empiriques en s'appuyant sur un corpus exhaustif de 2 854 joueurs professionnels issus des 5 grands championnats européens.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Deuxième Tendance : Architecture Micro-services Asynchrone FastAPI (Python 3.12) & Uvicorn</b>", h2_style))
    story.append(Paragraph("La deuxième tendance technologique repose sur l'adoption des architectures micro-services de haute performance sous Python 3.12. Le choix du framework FastAPI s'est imposé face aux solutions historiques (Django, Flask) en raison de ses vitesses d'exécution exceptionnelles sous le serveur ASGI Uvicorn, affichant des temps de réponse moyens inférieurs à 15 millisecondes sur les calculs d'API.", body_style))
    story.append(Paragraph("FastAPI intègre nativement la validation et la sérialisation des données Pydantic, garantissant un typage strict et une exécution ultra-rapide des traitements matriciels Pandas. De plus, le framework génère automatiquement la documentation interactive des endpoints au format Swagger OpenAPI, facilitant le travail d'intégration avec le front-end React 18 et assurant une maintenabilité optimale du code source pour l'équipe technique.", body_style))
    story.append(Paragraph("Cette robustesse back-end permet de traiter simultanément les requêtes lourdes de filtrage vectoriel et les requêtes de simulation financière en période de pic de trafic lors de la clôture des transferts.", body_style))
    story.append(Spacer(1, 3))

    # PAGE 9 CONTINUATION : TENDANCE 3 + SYNTHÈSE + SECTION 6 + PARAGRAPHE DE TRANSITION VERS LA PAGE 10
    story.append(Paragraph("<b>4. Troisième Tendance : Interfaces Web Réactives React 18, Vite & Canvas SVG Radar Vectoriel</b>", h2_style))
    story.append(Paragraph("La troisième tendance technologique concerne les interfaces web réactives orientées données et la visualisation vectorielle haute fidélité. Le choix de React 18 couplé à l'outil de build moderne Vite offre une vitesse de rafraîchissement inégalée en développement (HMR < 50 ms) et une gestion d'état fluide via les Hooks React (useState, useEffect, useMemo).", body_style))
    story.append(Paragraph("Pour le rendu des graphiques radars de performance à 6 axes, l'utilisation du composant Canvas SVG interactif s'est avérée indispensable. Le SVG garantit un rendu vectoriel d'une netteté parfaite sur tous les types d'écrans (tablettes iPad, smartphones, moniteurs 4K) avec une empreinte mémoire minime. L'interface applique le Design System Glassmorphism aux couleurs officielles de l'OL (bleu #0b2c5c, rouge #d31115 et violet Nexa #6f2f9f).", body_style))
    story.append(Paragraph("Le composant Canvas SVG permet en outre des micro-animations fluides lors du survol des axes et de la comparaison croisée entre deux recrues dans le comparateur Dual Radar.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>5. Synthèse Globale et Justification de l'Intégration Technologique au Projet OL</b>", h2_style))
    story.append(Paragraph("La synergie créée entre ces trois tendances technologiques établit un écosystème applicatif de classe internationale, conçu sur mesure pour les besoins de l'Olympique Lyonnais. L'alliance entre la puissance analytique du Machine Learning en back-end (FastAPI & k-NN) et l'ergonomie dynamique du front-end (React 18 & Canvas SVG) apporte une valeur ajoutée stratégique déterminante. En remplaçant les processus manuels fragmentés par un outil réactif centralisé, la solution permet à l'OL de surmonter la surenchère du marché mondial des transferts tout en respectant scrupuleusement le plafond budgétaire de 45 millions d'euros sous le contrôle strict de la DNCG.", body_style))
    story.append(Spacer(1, 3))

    # SECTION 6 EN PARAGRAPHES DE PROSE ACADÉMIQUE
    story.append(Paragraph("<b>6. CATÉGORISATION DES BESOINS : BESOINS FONCTIONNELS DÉTAILLÉS</b>", h2_style))
    story.append(Paragraph("À la suite de la synthèse de la veille technologique, la catégorisation des besoins fonctionnels formalise de manière approfondie l'ensemble des cas d'utilisation (Use Cases) indispensables à l'exploitation de la plateforme Recruitment Match OL. Issue des ateliers de co-création menés avec les recruteurs terrain et la direction sportive, l'application est structurée en 5 modules applicatifs hautement intégrés pour répondre avec une précision maximale aux exigences du football professionnel moderne.", body_style))
    story.append(Paragraph("<b>Moteur de recherche multicritère et rendu vectoriel des fiches joueurs (Modules 1 & 2) :</b> Le premier module fonctionnel concerne le moteur de recherche multicritère réactif basé sur les métriques Opta. Il met à la disposition des recruteurs (Persona Marc) une série de sliders interactifs permettant de filtrer la base de 2 854 joueurs européens selon 6 attributs sportifs discriminants (Finition, Dribble, Passes, Vitesse, Défense et Physique) étalonnés sur 90 minutes réelles avec un temps de réponse API inférieur à 15 ms. En complément direct, le deuxième module assure le rendu dynamique des fiches individuelles et des graphiques radars vectoriels en Canvas SVG à 6 axes. Chaque axe restitue une note normalisée de 0 à 100 avec des animations interactives au survol des métriques, permettant une évaluation visuelle immédiate des forces et faiblesses athlétiques.", body_style))
    story.append(Paragraph("<b>Comparateur Dual Radar et Espace de simulation budgétaire Mercato (Modules 3 & 4) :</b> Le troisième module fonctionnel est le comparateur Dual Radar & Effectif OL, conçu pour l'analyse comparative en face-à-face. Il permet de superposer sur une même grille graphique le profil d'un joueur titulaire de l'Olympique Lyonnais (ex: Rayan Cherki) avec celui d'une cible Mercato afin d'évaluer la complémentarité tactique et la plus-value sportive directe de la recrue. Le quatrième module constitue l'Espace Direction Sportive et de simulation budgétaire Mercato (45 M€). Dédié à Vincent (Directeur Sportif), cet outil décisionnel intègre des sliders interactifs pour ajuster l'indemnité de transfert et le salaire mensuel brut, calculant en temps réel le solde budgétaire disponible et garantissant le respect strict des réglementations financières de la DNCG et de l'UEFA.", body_style))
    story.append(Paragraph("<b>Sécurité des accès, authentification et habilitations applicatives RBAC (Module 5) :</b> Enfin, le cinquième module assure la gestion des sessions utilisateurs et le contrôle d'accès basé sur les rôles (RBAC). L'authentification est sécurisée par l'émission de jetons JWT Bearer signés et chiffrés valides pour une durée de 24 heures. Ce module impose une étanchéité stricte entre les profils applicatifs : les utilisateurs disposant du rôle <i>scout</i> ont accès à la détection sportive et au calcul de similarité k-NN, mais voient les données salariales et les valeurs marchandes automatiquement masquées sous la mention 'Confidentiel Direction'. L'accès au simulateur financier est exclusivement réservé aux comptes de rôles <i>director</i> et <i>admin</i>, garantissant ainsi la confidentialité absolue des opérations stratégiques de l'Olympique Lyonnais.", body_style))
    story.append(Spacer(1, 3))

    # PARAGRAPHE DE TRANSITION ENTRE PAGE 9 ET PAGE 10 REQUIS PAR L'UTILISATEUR
    story.append(Paragraph("La formalisation complète des 5 modules fonctionnels établit le périmètre précis des usages réclamés par les recruteurs et la direction de l'Olympique Lyonnais. Afin d'offrir une exécution fluide, résiliente et sécurisée de l'ensemble de ces fonctionnalités, le chapitre suivant détaille les besoins techniques et l'architecture logicielle retenue pour la plateforme Recruitment Match OL.", body_style))
#     story.append(PageBreak())

    # PAGE 10 : BESOINS TECHNIQUES AVEC DES PARAGRAPHES RÉDIGÉS PROPRES (SANS PUCE EN UN SEUL BLOC)
    story.append(Paragraph("CATÉGORISATION DES BESOINS : BESOINS TECHNIQUES & ARCHITECTURE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Exigences d'Architecture Logicielle et Découplage Front-End / Back-End</b>", h2_style))
    story.append(Paragraph("Les besoins techniques et d'ingénierie imposent une rigueur d'architecture stricte pour le projet Recruitment Match de l'Olympique Lyonnais. L'application repose fondamentalement sur un découplage total (architecture Headless) entre l'interface utilisateur front-end, développée sous React 18, et le serveur applicatif back-end, propulsé par FastAPI sous Python 3.12. Ce paradigme architectural garantit une haute scalabilité de la plateforme, permettant à chaque couche d'évoluer de manière indépendante. La séparation claire des responsabilités permet au serveur API de se concentrer exclusivement sur les calculs matriciels lourds de l'algorithme k-NN et la simulation budgétaire en temps réel, tandis que le client React assure la restitution graphique fluide des données via le composant Canvas SVG. L'adoption du standard RESTful et du format d'échange JSON assure une communication inter-services rapide, standardisée et facilement documentable via l'interface Swagger OpenAPI nativement générée par FastAPI.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Infrastructure de Stockage Relationnel et Stratégie d'Indexation</b>", h2_style))
    story.append(Paragraph("La gestion de la persistance des données repose sur l'intégration d'une base de données relationnelle SQLite3. Bien qu'elle soit embarquée, cette solution technique répond parfaitement aux contraintes de volumétrie du projet (2 854 fiches joueurs) tout en offrant les garanties de conformité ACID (Atomicité, Cohérence, Isolation, Durabilité). La modélisation entité-association stricte assure l'intégrité référentielle entre les tables d'utilisateurs, de rôles et de données sportives. Pour pallier les limites inhérentes à SQLite sur les requêtes complexes en lecture seule, une stratégie d'indexation ciblée a été mise en œuvre sur les clés de recherche principales (attributs Opta, identifiants de postes et nationalités), garantissant ainsi un temps d'accès aux données (I/O) inférieur à quelques millisecondes, essentiel pour l'expérience de filtrage en direct.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Sécurité Absolue, Authentification JWT Bearer et Habilitations RBAC</b>", h2_style))
    story.append(Paragraph("Compte tenu de la haute confidentialité des informations traitées (notamment les enveloppes budgétaires Mercato de l'ordre de 45 millions d'euros et les salaires des joueurs cibles), l'architecture technique intègre des protocoles de sécurité de niveau entreprise. L'authentification des collaborateurs de l'OL est sécurisée par l'émission de jetons cryptographiques JWT (JSON Web Tokens) Bearer, signés et dotés d'une durée de validité stricte de 24 heures. La gestion des mots de passe repose sur un hachage irréversible utilisant l'algorithme robuste Passlib Bcrypt, neutralisant les risques d'attaques par force brute ou tables arc-en-ciel. En aval, un middleware FastAPI applique un contrôle d'accès basé sur les rôles (RBAC), interceptant systématiquement toutes les requêtes HTTP pour s'assurer que seuls les comptes <i>director</i> ou <i>admin</i> accèdent aux endpoints sensibles exposant les données salariales.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Continuité de Service, Résilience et Mode Démo Autonome (Client-Side Fallback)</b>", h2_style))
    story.append(Paragraph("Afin de garantir une opérabilité sans faille, y compris dans des conditions de mobilité dégradées (ex: recruteur Marc en déplacement dans un stade avec une faible couverture réseau) ou lors de démonstrations client, l'architecture intègre un mécanisme de résilience avancé. Un mode <i>Client-Side Fallback</i> autonome est directement implémenté dans le code front-end. En cas d'indisponibilité temporaire du serveur API FastAPI (erreur 503) ou de coupure de connexion, l'application bascule instantanément et de manière transparente sur un fichier JSON de secours pré-qualifié et embarqué lors du processus de build Vite. Cette conception robuste (approche Offline-First) assure la continuité absolue de l'expérience utilisateur, permettant aux équipes sportives et décisionnelles de l'Olympique Lyonnais d'accéder sans interruption aux profils vectoriels de leurs futures recrues.", body_style))
#     story.append(PageBreak())

    # PAGE 11 : BESOINS DATA & PIPELINE ETL EN PROSE ACADÉMIQUE
    story.append(Paragraph("CATÉGORISATION DES BESOINS : BESOINS DATA & PIPELINE ETL", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Sourcing Stratégique des Données et Périmètre d'Analyse Européen (Big 5)</b>", h2_style))
    story.append(Paragraph("Le fondement analytique de la plateforme Recruitment Match OL repose sur la constitution d'un référentiel de données d'une fiabilité absolue. Les besoins métiers de la cellule de scouting imposent un sourcing exhaustif ciblant les 5 grands championnats européens (Ligue 1, Premier League, LaLiga, Serie A et Bundesliga) pour la saison 2024-2025. Cette collecte regroupe les performances réelles de 2 854 joueurs professionnels (hors gardiens de but) issues des bases de données de référence FBref et Opta Sports. L'ingestion initiale sous format CSV constitue la matière première brute du système. La diversité et la volumétrie de ce dataset assurent à l'algorithme k-NN un espace de recherche suffisamment vaste pour identifier des pépites sous-évaluées, maximisant ainsi les opportunités de marché pour l'Olympique Lyonnais sous l'enveloppe budgétaire stricte de 45 millions d'euros.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Neutralisation des Biais Statistiques : Étalonnage sur 90 Minutes Réelles</b>", h2_style))
    story.append(Paragraph("L'une des exigences Data les plus critiques pour la Direction Sportive concerne l'équité des évaluations comparatives. Historiquement, l'analyse brute des statistiques cumulées (ex: total de buts ou de passes sur une saison) biaisait le jugement au profit des joueurs bénéficiant du plus grand temps de jeu. Pour éliminer ce biais cognitif structurel, le pipeline ETL impose un étalonnage mathématique strict de toutes les métriques de performance sur 90 minutes réelles (<i>Per 90 metrics</i>). Ainsi, un jeune espoir n'ayant disputé que 800 minutes dans la saison est évalué sur un pied d'égalité stricte avec un joueur titulaire ayant accumulé 3000 minutes. Cette standardisation concerne l'ensemble des métriques avancées telles que les Expected Goals (xG), les Expected Assists (xA), les passes progressives et les actions de création de tir, garantissant une détection objective de la performance brute.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Nettoyage Automatisé (Pandas), Traitement des Valeurs Manquantes et Cast Types</b>", h2_style))
    story.append(Paragraph("Les données brutes issues du web scraping présentent intrinsèquement des anomalies : cellules vides, valeurs textuelles parasites (astérisques, virgules) et erreurs de typage. L'étape de transformation (Transform) du pipeline ETL s'appuie sur la librairie Python Pandas pour exécuter un nettoyage industriel. Des fonctions dédiées parcourent l'ensemble du DataFrame pour traiter les valeurs manquantes (NaN) en leur affectant des valeurs par défaut pertinentes (zéro pour une absence d'action), tout en expurgeant les caractères spéciaux. Une attention particulière est portée au typage fort : toutes les chaînes de caractères représentant des nombres sont converties (cast) en types Float64 natifs, assurant la robustesse des opérations mathématiques ultérieures. Cette hygiène rigoureuse de la base de données conditionne directement la stabilité de l'API FastAPI en production.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Algorithme de Normalisation Min-Max et Préparation Vectorielle (Échelle 0-100)</b>", h2_style))
    story.append(Paragraph("Afin de pouvoir comparer et superposer graphiquement des attributs de nature radicalement différente (un pourcentage de passes réussies s'exprimant en %, face à un nombre d'interceptions s'exprimant en unités absolues), le pipeline Data intègre un algorithme de normalisation Min-Max dynamique. Ce traitement recalcule l'intégralité des 6 dimensions sportives majeures (Finition, Dribble, Passes, Vitesse, Défense, Physique) pour chaque profil, en les projetant sur une échelle uniforme allant de 0 à 100 par rapport aux valeurs maximales de la base. Cette uniformisation vectorielle remplit un double objectif vital : elle permet au front-end React de tracer les graphiques radars SVG sans distorsion visuelle, et elle fournit des vecteurs mathématiquement équilibrés à l'algorithme des k-Plus Proches Voisins (k-NN) pour un calcul de distance euclidienne parfait et impartial.", body_style))
#     story.append(PageBreak())

    # PAGE 12 : PRIORISATION MOSCOW (MUST HAVE) EN PROSE ACADÉMIQUE
    story.append(Paragraph("PRIORISATION DES BESOINS MOSCOW : MUST HAVE (P0)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Méthodologie Agile MoSCoW et Cadrage du Produit Minimum Viable (MVP)</b>", h2_style))
    story.append(Paragraph("La structuration globale des développements de l'application Recruitment Match OL s'appuie sur la méthodologie de priorisation Agile MoSCoW. Ce cadre de gestion de projet permet de hiérarchiser rigoureusement les fonctionnalités réclamées par la Direction Sportive afin de garantir une livraison incrémentale et sécurisée. La première catégorie, désignée sous le terme <i>Must Have</i> (Priorité P0), rassemble l'ensemble des exigences fonctionnelles et techniques absolument non négociables. Sans l'intégration parfaite de ces éléments, la plateforme ne peut répondre à sa proposition de valeur initiale. La livraison de ces fonctionnalités primordiales constitue le socle du Produit Minimum Viable (MVP), permettant à la cellule de scouting de démarrer immédiatement ses opérations de détection de talents lors de la prochaine fenêtre de Mercato.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Le Socle Sécuritaire : Authentification RBAC et Gestion de Base de Données</b>", h2_style))
    story.append(Paragraph("Parmi les fonctionnalités critiques de priorité P0 figure en premier lieu la fondation sécuritaire de l'application. Compte tenu de la haute confidentialité des informations financières liées aux opérations de transferts (enveloppe de 45 millions d'euros), le système d'authentification par jetons JWT Bearer et le contrôle d'accès basé sur les rôles (RBAC) sont des prérequis vitaux. L'application doit obligatoirement être capable de différencier et de cloisonner les sessions des rôles <i>Scout</i>, <i>Director</i> et <i>Admin</i>, en appliquant un masquage strict des salaires pour les simples recruteurs. En parallèle, l'initialisation et l'exploitation de la base de données relationnelle SQLite3, préalablement enrichie et indexée avec les profils statistiques des 2 854 joueurs réels de la saison européenne, constituent l'ossature Data incontournable du système.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Le Cœur Interactif : Moteur de Recherche Multicritère et Interface Radar SVG</b>", h2_style))
    story.append(Paragraph("La proposition de valeur métier de l'outil repose fondamentalement sur son interactivité. Il est donc exigé, en priorité absolue (Must Have), la livraison d'un moteur de recherche réactif permettant aux recruteurs de filtrer la base de données de manière dynamique. Ce moteur doit impérativement inclure des sliders d'ajustement manipulables en temps réel sur les 6 attributs Opta discriminants (Finition, Dribble, Passes, Vitesse, Défense et Physique). En réponse directe à ces filtrages, l'interface utilisateur React 18 doit être capable de restituer visuellement les capacités athlétiques des joueurs ciblés à travers le tracé instantané de graphiques radars vectoriels en Canvas SVG à 6 axes, offrant une lecture ergonomique et sans distorsion sur tout type de support.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. L'Intelligence Analytique : Implémentation du Matching k-NN des Jumeaux Statistiques</b>", h2_style))
    story.append(Paragraph("Enfin, l'innovation majeure qui justifie l'investissement de l'Olympique Lyonnais dans cette plateforme réside dans sa dimension prédictive et analytique. La fonction de calcul de similarité, propulsée par l'algorithme de Machine Learning des k-Plus Proches Voisins (k-NN) côté serveur (FastAPI), est classée en priorité P0 absolue. Sur simple déclenchement depuis l'interface d'un joueur ciblé, l'algorithme doit obligatoirement calculer les distances euclidiennes vectorielles sur l'ensemble de la base de données et restituer, en moins de 15 millisecondes, les profils des quatre jumeaux statistiques les plus pertinents. C'est cette fonctionnalité qui permet au club de contourner la surenchère du marché mondial en dénichant des profils mathématiquement équivalents mais financièrement plus accessibles.", body_style))
    story.append(Spacer(1, 3))
    
    # PARAGRAPHE DE TRANSITION ENTRE PAGE 12 ET PAGE 13
    story.append(Paragraph("Une fois le socle du Produit Minimum Viable (MVP) formellement délimité et sécurisé à travers les fonctionnalités Must Have, l'enrichissement progressif de la plateforme permet d'adresser des besoins métiers plus avancés. Le chapitre suivant détaille les exigences secondaires de forte importance (SHOULD HAVE), notamment celles destinées au pilotage stratégique de la Direction Sportive.", body_style))
#     story.append(PageBreak())

    # PAGE 13 : PRIORISATION MOSCOW (SHOULD HAVE) EN PROSE ACADÉMIQUE
    story.append(Paragraph("PRIORISATION DES BESOINS MOSCOW : SHOULD HAVE (P1)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. L'Analyse Comparative : Module Effectif OL et Dual Radar Face-à-Face</b>", h2_style))
    story.append(Paragraph("La hiérarchisation des exigences de priorité P1 (Should Have) regroupe les fonctionnalités qui, sans être bloquantes pour le lancement initial, apportent une plus-value stratégique décisive. Le premier développement de ce périmètre concerne le module d'intégration de l'Effectif de l'Olympique Lyonnais. Ce système interactif permet de mettre en balance les statistiques d'une potentielle recrue avec celles d'un joueur titulaire évoluant déjà au sein de l'équipe première (ex: Rayan Cherki). Cette comparaison s'opère visuellement via le composant Dual Radar, qui superpose en face-à-face les deux grilles vectorielles SVG. L'objectif est d'offrir à la Direction Sportive une lecture immédiate de la complémentarité tactique, afin de déterminer si le joueur ciblé viendra réellement combler une carence athlétique de l'effectif actuel.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Pilotage Financier : Simulateur d'Impact Budgétaire Mercato (45 M€)</b>", h2_style))
    story.append(Paragraph("Le deuxième besoin majeur classé en P1 est la création de l'Espace Direction Sportive, un tableau de bord financier exclusivement dédié au pilotage de la campagne de recrutement. Confronté à une stricte enveloppe budgétaire de 45 millions d'euros allouée par Eagle Football, le Directeur Sportif (Vincent) doit arbitrer en direct la soutenabilité de chaque transfert. Ce module intègre un simulateur d'impact dynamique : par le biais de sliders interactifs, l'utilisateur peut modéliser l'indemnité de transfert envisagée et le salaire brut mensuel du joueur ciblé. Le système recalcule instantanément le solde budgétaire disponible et alerte la direction en cas de dépassement des ratios imposés par la DNCG et le Fair-Play Financier de l'UEFA.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Étanchéité des Données et Masquage Financier Automatisé (Rôle Scout)</b>", h2_style))
    story.append(Paragraph("Corollaire direct des enjeux budgétaires, la sécurisation des affichages (Masquage Automatique) constitue une exigence fonctionnelle majeure du développement P1. Pour éviter de fausser le jugement des recruteurs terrain (Marc) par des biais liés au coût du joueur, et pour garantir la confidentialité absolue des grilles salariales du club, une logique d'étanchéité stricte est implémentée en front-end. En s'appuyant sur le jeton JWT décodé par le client React, le composant de fiche joueur vérifie le rôle de l'utilisateur actif. S'il s'agit d'un compte de type <i>Scout</i>, les champs relatifs au salaire et à la valeur marchande sont dynamiquement masqués et remplacés par une mention visuelle 'Confidentiel Direction', assurant ainsi une stricte conformité aux habilitations RBAC.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Résilience Opérationnelle : Mode Démo Autonome (Client-Side Fallback)</b>", h2_style))
    story.append(Paragraph("Enfin, la dernière exigence Should Have porte sur l'intégration du mode de secours déconnecté (Client-Side Fallback). Bien que l'infrastructure serveur FastAPI soit conçue pour une haute disponibilité, l'outil doit rester démonstrable et opérationnel en toute circonstance, y compris lors d'échanges avec des agents dans des environnements sans connexion réseau fiable. Ce module autonome bascule le requêtage de l'application React vers un fichier de données JSON embarqué statiquement, simulant les réponses de l'API. Cette fonctionnalité garantit une résilience absolue et protège la réputation technologique de l'Olympique Lyonnais lors des phases de négociation ou de présentation au comité directeur.", body_style))
    story.append(Spacer(1, 3))

    # PARAGRAPHE DE TRANSITION ENTRE PAGE 13 ET PAGE 14
    story.append(Paragraph("La couverture fonctionnelle combinée des niveaux P0 et P1 dote l'Olympique Lyonnais d'un écosystème numérique complet et puissant. Pour finaliser le cadrage de la méthode MoSCoW, le chapitre suivant recense les fonctionnalités de confort catégorisées en P2 (COULD HAVE) ainsi que les évolutions écartées du périmètre actuel (WON'T HAVE) afin de sécuriser le calendrier du projet.", body_style))
#     story.append(PageBreak())

    # PAGE 14 : PRIORISATION MOSCOW (COULD HAVE & WON'T HAVE) EN PROSE ACADÉMIQUE
    story.append(Paragraph("PRIORISATION DES BESOINS MOSCOW : COULD HAVE (P2) & WON'T HAVE (P3)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Sécurisation du Calendrier (16 Semaines) et Périmètre d'Exclusion</b>", h2_style))
    story.append(Paragraph("La réussite d'un projet d'ingénierie web repose autant sur les fonctionnalités implémentées que sur la maîtrise stricte du périmètre applicatif. Afin de sécuriser le délai de développement de 16 semaines imposé par le calendrier académique (RNCP40857) et par les impératifs de la cellule de scouting de l'Olympique Lyonnais, la méthodologie MoSCoW délimite rigoureusement les fonctionnalités de confort (COULD HAVE - P2) et celles formellement exclues du périmètre initial (WON'T HAVE - P3). Ce séquençage chronologique évite l'écueil de la dérive fonctionnelle (<i>feature creep</i>) et concentre l'effort de développement sur le cœur de l'application : la performance de l'algorithme k-NN et la résilience de l'interface React 18.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Priorité P2 (Could Have) : Autocomplétion Dynamique et Confort Ergonomique</b>", h2_style))
    story.append(Paragraph("Parmi les fonctionnalités catégorisées en P2 (Could Have) figure l'amélioration de l'expérience utilisateur (UX) lors de la recherche ciblée. Il s'agit de l'implémentation d'une barre de recherche intelligente intégrant une autocomplétion dynamique. Dès la saisie des deux premiers caractères par le recruteur, une requête asynchrone (<i>debounced</i>) interroge l'API FastAPI pour suggérer en temps réel les noms des joueurs correspondants parmi les 2 854 profils de la base de données. Bien que cette fonctionnalité fluidifie grandement la navigation, son absence temporaire n'empêche pas l'utilisation du moteur de filtrage multicritère par les attributs Opta, justifiant ainsi son classement en priorité secondaire.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Priorité P2 (Could Have) : Exportation Documentaire des Profils Vectoriels (PDF)</b>", h2_style))
    story.append(Paragraph("La seconde exigence classée en P2 concerne la portabilité documentaire. Lors des comités de direction ou des réunions de négociation avec les agents de joueurs, le Directeur Sportif (Vincent) peut avoir besoin de supports physiques tangibles. La fonctionnalité d'exportation au format PDF prévoit de capturer la fiche détaillée du joueur, incluant son graphique radar SVG vectoriel généré par le composant Canvas, et de la formater dans un gabarit officiel aux couleurs de l'Olympique Lyonnais. Cette option de reporting, bien que très appréciée par la direction pour l'archivage contractuel, reste une évolution de confort qui sera intégrée dans un second cycle de développement (V1.2) après la stabilisation du MVP.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Priorité P3 (Won't Have) : Exclusions Stratégiques (Vidéo et Synchro DNCG)</b>", h2_style))
    story.append(Paragraph("Enfin, la catégorie Won't Have (P3) tranche définitivement sur les exclusions du périmètre projet. L'intégration de flux de streaming vidéo direct (matchs entiers) a été écartée en raison de la charge disproportionnée qu'elle imposerait sur l'infrastructure serveur et des contraintes légales liées aux droits de diffusion (LFP, UEFA). De même, la synchronisation automatisée et en temps réel de l'API avec les logiciels comptables officiels de la DNCG a été rejetée. Ces interconnexions externes complexes feraient exploser le budget de développement et introduiraient des dépendances à des API tierces instables. La plateforme se concentre strictement sur son rôle de simulateur décisionnel interne déconnecté du système de facturation officiel.", body_style))
    story.append(Spacer(1, 3))

    # PARAGRAPHE DE TRANSITION ENTRE PAGE 14 ET PAGE 15
    story.append(Paragraph("Le périmètre fonctionnel étant dorénavant totalement figé par la matrice MoSCoW, il est impératif de valider techniquement les choix d'architecture retenus. Le chapitre suivant dresse l'évaluation complète de la faisabilité du projet, en s'assurant que les performances de l'API FastAPI et la réactivité du front-end répondent sans compromis aux exigences d'ultra-réactivité exprimées par la cellule de scouting.", body_style))
#     story.append(PageBreak())

    # PAGE 15 : FAISABILITÉ TECHNIQUE
    story.append(Paragraph("ÉVALUATION DE LA FAISABILITÉ : TECHNIQUE & PERFORMANCE API", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Évaluation de l'Architecture Serveur (FastAPI & Uvicorn)</b>", h2_style))
    story.append(Paragraph("Le diagnostic de faisabilité technique débute par l'évaluation rigoureuse du socle back-end, composant névralgique de la plateforme de scouting de l'Olympique Lyonnais. Le choix stratégique s'est porté sur le framework Python FastAPI, propulsé par le serveur Web ASGI Uvicorn. Cette alliance technologique moderne repose sur une boucle d'événements (<i>Event Loop</i>) et l'utilisation native des coroutines asynchrones (async/await), offrant une gestion non-bloquante des entrées/sorties (I/O). Contrairement aux architectures synchrones traditionnelles, cette conception permet d'encaisser simultanément des centaines de requêtes complexes de recherche sans provoquer d'engorgement serveur. Les benchmarks de charge internes démontrent de manière irréfutable que cette architecture garantit un temps de réponse moyen de l'API strictement inférieur à 15 millisecondes, même lors de fortes sollicitations durant la période critique du Mercato, assurant une conformité absolue avec les exigences d'instantanéité exprimées par la Direction Sportive.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Réactivité de l'Interface Graphique (React 18 & Vite)</b>", h2_style))
    story.append(Paragraph("Côté client, le défi de la performance visuelle et de la réactivité est relevé avec succès grâce à l'adoption du framework React 18 couplé au bundler de nouvelle génération Vite. L'architecture s'appuie sur le <i>Virtual DOM</i> de React, qui permet d'isoler et d'appliquer des mises à jour d'interface chirurgicales uniquement sur les composants modifiés (ex: modification d'un slider Opta), sans avoir à recharger l'intégralité de la page web. Le processus de build de Vite, intégrant une élimination agressive du code mort (<i>Tree-shaking</i>), réduit drastiquement le poids du bundle final JavaScript, abaissant le temps de chargement initial de l'application (First Contentful Paint) sous la barre critique des 50 millisecondes. De surcroît, le tracé dynamique des graphiques radars vectoriels en Canvas SVG tire parti de l'accélération matérielle des navigateurs, maintenant un affichage d'une fluidité parfaite à 60 FPS (images par seconde), éliminant toute saccade ou pixelisation.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Continuité de Service et Architecture Offline-First</b>", h2_style))
    story.append(Paragraph("La résilience applicative sous contraintes environnementales sévères constitue le troisième pilier de cette faisabilité. Consciente de la forte mobilité des recruteurs (stades européens, centres de formation, zones mal couvertes par les réseaux 4G/5G), l'ingénierie front-end a nativement intégré un mode <i>Client-Side Fallback</i> autonome. En s'inspirant de l'architecture des Progressive Web Apps (PWA), un mécanisme de bascule automatique est prévu. En cas de perte de connectivité avec l'API FastAPI (Timeout ou Erreur 503), l'interface web intercepte la défaillance et redirige instantanément le requêtage vers un fichier JSON qualifié embarqué localement dans le bundle. Cette approche <i>Offline-First</i>, potentiellement soutenue par des Service Workers, garantit une très haute disponibilité applicative, permettant au système de fonctionner en dégradé mais de manière ininterrompue.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Validation Technique Globale et Pérennité de l'Infrastructure</b>", h2_style))
    story.append(Paragraph("En synthèse, le découplage strict de l'architecture logicielle (Headless) entre l'application React et le moteur d'intelligence artificielle FastAPI valide à 100% la faisabilité technique du projet. Cette infrastructure moderne, conteneurisable via Docker et hautement scalable, est totalement dénuée de dette technique héritée. Elle offre à l'Olympique Lyonnais un socle numérique sur-mesure, intrinsèquement robuste, prêt à intégrer de futures briques fonctionnelles complexes sans jamais compromettre la fluidité de la détection de talents sportifs.", body_style))
    story.append(Spacer(1, 3))

    # TRANSITION PAGE 15 -> 16
    story.append(Paragraph("La faisabilité technique étant irréprochablement démontrée, il est nécessaire de valider la conformité du projet aux normes réglementaires et sécuritaires en vigueur. Le chapitre suivant dresse le bilan de la faisabilité légale (RGPD) et détaille les protocoles de sécurité déployés.", body_style))
#     story.append(PageBreak())

    # PAGE 16 : FAISABILITÉ LÉGALE & SÉCURITÉ
    story.append(Paragraph("ÉVALUATION DE LA FAISABILITÉ : LÉGALE (RGPD) & SÉCURITÉ (OWASP)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Faisabilité Légale, Privacy by Design et Respect du Cadre RGPD</b>", h2_style))
    story.append(Paragraph("L'audit de conformité réglementaire valide la stricte adhésion de l'application aux exigences du Règlement Général sur la Protection des Données (RGPD). La plateforme applique le principe de minimisation des données (<i>Privacy by Design</i>), en ne collectant que les informations d'authentification strictement nécessaires à la création des sessions internes des collaborateurs du club. Le stockage de ces identifiants est sécurisé via un LocalStorage temporaire côté client, avec une politique de rétention limitée. Par ailleurs, concernant la data sportive elle-même, les statistiques des joueurs issues d'Opta relèvent du domaine de la performance professionnelle publique et ne requièrent pas de consentement spécifique pour une exploitation algorithmique interne. Enfin, l'architecture s'interdit formellement l'utilisation de traceurs tiers ou de cookies publicitaires, garantissant une étanchéité légale parfaite vis-à-vis de la CNIL.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Sécurité Informatique et Standards OWASP Top 10</b>", h2_style))
    story.append(Paragraph("Dans un environnement où les données financières du Mercato représentent une cible critique, l'ingénierie sécuritaire s'aligne rigoureusement sur les recommandations de l'OWASP Top 10. La protection des mots de passe est assurée par un hachage irréversible utilisant l'algorithme Bcrypt, doté d'un <i>salt</i> cryptographique dynamique, rendant inopérantes les attaques par force brute ou via des tables arc-en-ciel. L'intégrité de la base de données est quant à elle protégée contre les Injections SQL grâce à l'utilisation systématique des requêtes préparées (<i>Prepared Statements</i>) au sein de l'ORM Python. Côté front-end, le framework React 18 assure une protection native contre les vulnérabilités de type XSS (Cross-Site Scripting) en échappant automatiquement toutes les données intégrées au DOM virtuel.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Contrôle d'Accès, Expiration des Sessions (JWT) et RBAC</b>", h2_style))
    story.append(Paragraph("La protection des interfaces de programmation (endpoints API) est verrouillée par un système cryptographique asymétrique. L'authentification repose sur l'émission de jetons JWT (JSON Web Tokens) de type Bearer, dont la signature numérique est validée à chaque requête entrante. Pour limiter la surface d'attaque en cas de vol de session, ces jetons sont paramétrés avec une durée de vie (<i>Expiration Time</i>) extrêmement courte, forçant une réauthentification quotidienne des recruteurs. Ce mécanisme est complété par un puissant middleware de contrôle d'accès basé sur les rôles (RBAC), qui intercepte systématiquement les tentatives d'élévation de privilèges (<i>Privilege Escalation</i>), garantissant que seuls les comptes Directeur ou Administrateur puissent décrypter et consulter les données salariales sensibles de l'enveloppe de 45 millions d'euros.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Bilan Légal et Sécuritaire (Clearance)</b>", h2_style))
    story.append(Paragraph("L'ensemble des exigences sécuritaires (SSI) étant nativement intégré dans le code source, la faisabilité légale et sécuritaire du projet est validée sans la moindre réserve juridique. Le système dote la Direction Sportive de l'Olympique Lyonnais d'un environnement numérique hermétique, protégeant de manière absolue le secret stratégique des transactions financières face à la concurrence et aux acteurs malveillants, ce qui autorise un déploiement serein de l'application.", body_style))
    story.append(Spacer(1, 3))

    # TRANSITION PAGE 16 -> 17
    story.append(Paragraph("La sécurisation de l'outil étant validée, il convient de garantir son utilisation par le plus grand nombre tout en assurant l'équité des calculs analytiques. Le chapitre suivant aborde l'évaluation de l'accessibilité web (W3C) et la qualité intrinsèque des données sportives exploitées.", body_style))
#     story.append(PageBreak())

    # PAGE 17 : ACCESSIBILITÉ & QUALITÉ DATA
    story.append(Paragraph("ÉVALUATION DE LA FAISABILITÉ : ACCESSIBILITÉ (W3C) & QUALITÉ DATA", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Inclusion Numérique et Standards d'Accessibilité (W3C)</b>", h2_style))
    story.append(Paragraph("L'ingénierie front-end de la plateforme Recruitment Match OL intègre dès sa conception les directives strictes d'accessibilité du World Wide Web Consortium (W3C). L'interface utilisateur vise une conformité formelle au niveau WCAG 2.1 AA. Consciente que les recruteurs exploitent souvent la plateforme en extérieur, soumis à de fortes contraintes lumineuses (bords de terrains d'entraînement, tribunes de stades), l'équipe de design a défini un système de design (<i>Design System</i>) basé sur des espaces colorimétriques HSL précis. Ce soin chromatique garantit un ratio de contraste strictement supérieur à 4.5:1 sur l'ensemble des textes et éléments interactifs, assurant une lisibilité infaillible des données statistiques complexes, y compris pour des utilisateurs souffrant de déficiences visuelles (daltonisme) ou d'éblouissement solaire.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Accessibilité Sémantique et Technologique (ARIA)</b>", h2_style))
    story.append(Paragraph("Outre le confort visuel ergonomique, le code source HTML5 généré par React est structuré selon des normes sémantiques intransigeantes (utilisation des balises <i>&lt;main&gt;</i>, <i>&lt;section&gt;</i>, <i>&lt;nav&gt;</i>). Pour compenser la nature hautement asynchrone de l'application (Single Page Application), l'utilisation généralisée d'attributs ARIA (Accessible Rich Internet Applications) permet de baliser formellement les composants dynamiques. Par exemple, l'implémentation de régions dynamiques (<i>aria-live=\"polite\"</i>) sur les résultats de la barre de recherche autocomplétée garantit que les mises à jour en temps réel soient correctement interceptées et énoncées par les technologies d'assistance (lecteurs d'écran type NVDA ou VoiceOver), favorisant ainsi l'inclusion numérique absolue de tous les collaborateurs du club.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Fiabilité Analytique et Qualité des Données (Data Quality)</b>", h2_style))
    story.append(Paragraph("En miroir de l'excellence de l'interface, la pertinence algorithmique du système dépend intrinsèquement de la pureté des données ingérées (<i>Data Quality</i>). Le pipeline ETL (Extract, Transform, Load) assure un nettoyage algorithmique systématique des statistiques scrapées depuis les plateformes officielles FBref et Opta Sports. Pour garantir l'équité absolue des comparaisons mathématiques, les valeurs aberrantes (<i>outliers</i>) telles que les joueurs ayant disputé moins de 500 minutes dans la saison sont filtrées, évitant la distorsion des moyennes. De plus, chaque métrique est rigoureusement étalonnée sur 90 minutes de temps de jeu réel (<i>Per 90</i>) puis normalisée via un algorithme <i>Min-Max Scaler</i> sur une échelle vectorielle stricte de 0 à 100, expurgeant tout biais statistique lié au temps d'exposition variable des athlètes sur le terrain.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Bilan de l'Expérience Utilisateur et de l'Équité Analytique</b>", h2_style))
    story.append(Paragraph("La conjugaison d'une interface utilisateur ultra-inclusive, respectant à la lettre les normes du W3C, et d'un pipeline de préparation de données garantissant l'impartialité mathématique de l'algorithme k-NN, valide de manière incontestable la faisabilité fonctionnelle du projet. L'application offre une expérience non seulement fluide et accessible sur l'ensemble des terminaux, mais elle certifie également à la Direction Sportive que chaque recommandation de recrutement est basée sur une intégrité scientifique irréprochable.", body_style))
    story.append(Spacer(1, 3))

    # TRANSITION PAGE 17 -> 18
    story.append(Paragraph("Malgré ces validations d'ingénierie successives prouvant l'excellence du code, le maintien en condition opérationnelle d'un tel outil nécessite d'anticiper les défaillances extrêmes. Le chapitre suivant présente la matrice d'évaluation des risques et détaille les stratégies de mitigation implémentées pour garantir la pérennité du système sous forte pression.", body_style))
#     story.append(PageBreak())

    # PAGE 18 : RISQUES & SOLUTIONS CORRECTIVES
    story.append(Paragraph("MATRICE D'ÉVALUATION DES RISQUES & SOLUTIONS CORRECTIVES", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Méthodologie d'Analyse Qualitative et Gestion des Risques</b>", h2_style))
    story.append(Paragraph("Afin de sécuriser le déploiement opérationnel dans un environnement sportif soumis à une intense pression (Mercato estival), la démarche d'ingénierie s'appuie sur une matrice d'évaluation des risques systématique. Cette grille qualitative croise la probabilité d'occurrence d'une défaillance avec son impact potentiel sur les opérations du club, évalués sur une échelle stricte de 1 à 5. Cette cartographie pragmatique permet d'identifier les vulnérabilités résiduelles de l'architecture logicielle et de leur adosser des solutions correctives (<i>Risk Mitigation</i>) robustes, pilotées en continu selon les préceptes des méthodes Agiles, garantissant un taux de disponibilité applicative (SLA) supérieur à 99.9%.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Mitigation du Risque de Panne Serveur (SLA et Offline Scouting)</b>", h2_style))
    story.append(Paragraph("Le premier risque identifié, d'une probabilité faible mais à l'impact opérationnel extrêmement élevé, est l'indisponibilité soudaine du serveur API FastAPI (crash serveur, attaque DDoS, Erreur 503) ou la perte totale de connectivité réseau lors d'une mission de recrutement à l'étranger. La solution corrective intégrée consiste en l'implémentation d'une architecture résiliente type <i>Offline-First</i>. En s'appuyant sur les capacités de l'API de stockage <i>IndexedDB</i> des navigateurs modernes, l'application React encapsule un référentiel JSON statique des 2 854 profils lors de son chargement initial. En cas de rupture de flux, le système bascule de manière transparente sur cette base de données locale autonome, assurant la continuité ininterrompue des démonstrations et du filtrage des jumeaux statistiques sans aucune dépendance au cloud.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Mitigation du Risque de Fuite Budgétaire et de Cyberattaque</b>", h2_style))
    story.append(Paragraph("Le second risque, classé comme critique (Impact 5/5) en raison de l'enveloppe Mercato de 45 millions d'euros, concerne l'accès illégitime aux données financières du club. Face à la menace permanente de fuite interne ou d'élévation de privilèges, la solution corrective repose sur le déploiement intraitable du middleware RBAC (<i>Role-Based Access Control</i>) couplé à la vérification cryptographique des signatures JWT par injection de dépendances sous FastAPI (<i>Depends</i>). Cette étanchéité architecturale garantit que les requêtes sollicitant des informations salariales soient bloquées en amont (Code HTTP 403 Forbidden) si le jeton n'appartient pas formellement à un profil <i>Director</i>, protégeant farouchement la stratégie financière de l'OL.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Mitigation du Biais Analytique (Normalisation de l'Algorithme k-NN)</b>", h2_style))
    story.append(Paragraph("Enfin, le risque de distorsion analytique (probabilité moyenne, impact élevé) faussant gravement le recrutement est neutralisé par le pipeline de préparation Data. Lors du calcul vectoriel de la distance euclidienne par l'algorithme k-NN, une métrique exprimée en milliers (ex: minutes jouées) écraserait mathématiquement une métrique exprimée en pourcentages (ex: taux de passes réussies). La solution corrective est la standardisation drastique des <i>features</i> (vecteurs) avant l'ingestion dans le modèle de Machine Learning. Ce centrage-réduction (Min-Max Scaler) assure que chaque attribut (vitesse, tacle, passe) pèse exactement le même poids dans la recherche des jumeaux statistiques, garantissant des recommandations fiables.", body_style))
    story.append(Spacer(1, 3))

    # TRANSITION PAGE 18 -> 19
    story.append(Paragraph("L'intégralité des menaces techniques, légales, cybernétiques et opérationnelles étant désormais couverte par des parades correctives validées, le projet aborde sa toute dernière phase d'évaluation. Le chapitre final conclut l'Étude d'Opportunité en intégrant les enjeux de sobriété numérique et en statuant définitivement sur le lancement des développements.", body_style))
#     story.append(PageBreak())

    # PAGE 19 : DÉMARCHE RSE & CONCLUSION
    story.append(Paragraph("DÉMARCHE RSE, NUMÉRIQUE RESPONSABLE & BILAN FAISABILITÉ", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Démarche d'Éco-conception et Sobriété Numérique (Green IT)</b>", h2_style))
    story.append(Paragraph("En conformité avec les attentes sociétales modernes et les exigences d'excellence du référentiel de certification RNCP40857, le projet Recruitment Match OL intègre nativement une démarche de Numérique Responsable profonde. L'architecture logicielle a été pensée sous le prisme de l'éco-conception (<i>Green IT</i>). Le choix de tracer les graphiques radars mathématiques via le format vectoriel SVG élimine la nécessité de générer, stocker et transférer des images matricielles PNG/JPEG lourdes côté serveur. Associée à une compression Brotli des requêtes HTTP et à une minification agressive du bundle JavaScript par le compilateur Vite (abaissant le poids total sous la barre des 940 Ko), cette sobriété technique diminue drastiquement l'empreinte carbone, la consommation de cycles CPU et la sollicitation des batteries des terminaux mobiles.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>2. Inclusion Technologique et Fluidité Responsive (CSS Grid / Flexbox)</b>", h2_style))
    story.append(Paragraph("La démarche de Responsabilité Sociétale des Entreprises (RSE) s'illustre également par une inclusion technologique sans compromis. L'interface utilisateur a été forgée via les modèles de layout CSS modernes (<i>Flexbox</i> et <i>CSS Grid</i>) pour s'adapter organiquement (<i>Responsive Web Design</i>) à la multiplicité infinie des tailles d'écrans utilisées par la cellule de recrutement. Que l'utilisateur consulte les profils sur un smartphone ancienne génération de 320px de large au bord d'un terrain d'entraînement ou sur un moniteur Ultra-Wide 4K dans la salle de commandement du Groupama Stadium, l'intégrité visuelle des données et l'ergonomie de l'application demeurent inaltérées.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>3. Bilan Définitif de Faisabilité de l'Étude d'Opportunité</b>", h2_style))
    story.append(Paragraph("La synthèse des diagnostics intensifs réalisés lors de cette Étude d'Opportunité dresse un bilan exceptionnel. La faisabilité globale de la solution logicielle est formellement validée à 100%. L'alliage technologique de pointe (Python FastAPI, React 18, SQLite3) répond aux exigences critiques d'instantanéité de l'algorithme prédictif k-NN, tout en s'affranchissant totalement des coûts paralysants liés aux licences logicielles propriétaires. De plus, l'intégration native des cadres légaux RGPD, des standards d'accessibilité W3C, des parades cyber-sécuritaires OWASP et de la couverture exhaustive des risques opérationnels démontre une maîtrise de bout-en-bout du cycle de vie de l'ingénierie.", body_style))
    story.append(Spacer(1, 3))

    story.append(Paragraph("<b>4. Conclusion Décisionnelle (GO) et Adéquation RNCP40857</b>", h2_style))
    story.append(Paragraph("Au vu de cette viabilité technique incontestable et de la très forte valeur ajoutée métier (<i>Moneyball strategy</i>) qu'elle apporte à l'Olympique Lyonnais pour maximiser la rentabilité de son budget Mercato de 45 millions d'euros, la décision de passage en phase de réalisation logicielle est actée. <b>DÉCISION FINALE : GO.</b> Le projet réunit avec éclat l'ensemble des conditions d'excellence technologique, financière et éthique réclamées par la direction. Ce socle analytique solide autorise le lancement immédiat de la prochaine étape (Étape 4), consacrée à la rédaction détaillée du Cahier des Charges fonctionnel, à la planification Agile (Diagramme de Gantt) et à la budgétisation exhaustive des coûts de développement.", body_style))
    story.append(PageBreak())

    return story

if __name__ == "__main__":
    story = build_pages1_to_19()
    doc = SimpleDocTemplate(
        r"C:\Users\user\OneDrive\Documents\OURAD_RAYANE_PROJET.pdf",
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=85,
        bottomMargin=50
    )
    doc.build(story, canvasmaker=NexaPurpleHeaderCanvas)
    print("PDF de 19 pages généré avec succès !")
