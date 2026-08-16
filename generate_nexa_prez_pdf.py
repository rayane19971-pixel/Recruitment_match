import os
import sys
from reportlab.lib.pagesizes import landscape, A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def generate_presentation():
    pdf_path = r"C:\Users\user\OneDrive\Documents\OURAD_RAYANE_PREZ.pdf"
    
    # Orientation Paysage (Diaporama Presentation)
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=landscape(A4),
        rightMargin=30,
        leftMargin=30,
        topMargin=25,
        bottomMargin=25
    )

    styles = getSampleStyleSheet()

    c_purple = colors.HexColor('#5b21b6')
    c_dark = colors.HexColor('#0f172a')
    c_ol_red = colors.HexColor('#d31115')
    c_ol_blue = colors.HexColor('#0b2c5c')
    c_gold = colors.HexColor('#f59e0b')

    slide_title = ParagraphStyle(
        'SlideTitle', parent=styles['Heading1'], fontSize=20, leading=24,
        textColor=c_purple, fontName='Helvetica-Bold', spaceAfter=8
    )

    slide_subtitle = ParagraphStyle(
        'SlideSubTitle', parent=styles['Normal'], fontSize=11, leading=15,
        textColor=c_ol_blue, fontName='Helvetica-Bold', spaceAfter=12
    )

    body_style = ParagraphStyle(
        'SlideBody', parent=styles['Normal'], fontSize=9.5, leading=13.5,
        textColor=colors.HexColor('#334155'), fontName='Helvetica', spaceAfter=6
    )

    story = []

    # =========================================================================
    # SLIDE 1 : TITRE & PRESENTATION
    # =========================================================================
    story.append(Spacer(1, 20))
    story.append(Paragraph("NEXA DIGITAL SCHOOL — CERTIFICATION CHEF DE PROJET WEB (RNCP40857)", ParagraphStyle('S1Header', parent=styles['Normal'], fontSize=12, textColor=c_purple, alignment=TA_CENTER, fontName='Helvetica-Bold')))
    story.append(Spacer(1, 15))
    story.append(HRFlowable(width="100%", thickness=3, color=c_purple, spaceAfter=15))
    story.append(Paragraph("SUPPORT DE SOUTENANCE ORALE — PROJET ANNUEL", ParagraphStyle('S1Title', parent=styles['Heading1'], fontSize=26, leading=30, textColor=c_dark, alignment=TA_CENTER, fontName='Helvetica-Bold')))
    story.append(Spacer(1, 10))
    story.append(Paragraph("RECRUITMENT MATCH — OLYMPIQUE LYONNAIS 🔴🔵", ParagraphStyle('S1Sub', parent=styles['Normal'], fontSize=16, textColor=c_ol_red, alignment=TA_CENTER, fontName='Helvetica-Bold')))
    story.append(Paragraph("Plateforme Full-Stack Data Scouting, Matching Opta (k-NN) & Budget Mercato", ParagraphStyle('S1Desc', parent=styles['Normal'], fontSize=11, textColor=colors.HexColor('#64748b'), alignment=TA_CENTER)))
    story.append(HRFlowable(width="100%", thickness=3, color=c_purple, spaceBefore=15, spaceAfter=25))

    s1_table = [
        [Paragraph("<b>Candidat :</b> Rayane OURAD", body_style), Paragraph("<b>Formation :</b> Bachelor Data & Business Intelligence", body_style)],
        [Paragraph("<b>Client :</b> Olympique Lyonnais (Scouting)", body_style), Paragraph("<b>Modalité :</b> Soutenance Orale Certificative (1h30)", body_style)]
    ]
    t_s1 = Table(s1_table, colWidths=[380, 380])
    t_s1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 8)
    ]))
    story.append(t_s1)
    story.append(PageBreak())

    # =========================================================================
    # SLIDE 2 : CONTEXTE & PROBLEMATIQUE
    # =========================================================================
    story.append(Paragraph("1. CONTEXTE & PROBLÉMATIQUE MÉTIER (OLYMPIQUE LYONNAIS)", slide_title))
    story.append(Paragraph("Optimiser le recrutement sportif sous contrainte budgétaire (45 M€ Mercato)", slide_subtitle))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=12))

    s2_content = [
        [Paragraph("<b>Problématique Métier OL</b>", body_style), Paragraph("<b>Solution Apportée par Recruitment Match</b>", body_style)],
        [
            Paragraph("• Inflation constante des indemnités de transfert.<br/>• Encadrement strict par la DNCG et le Fair-Play Financier.<br/>• Risque élevé d'erreur de recrutement sur les profils à forte valeur.", body_style),
            Paragraph("• Moteur de recherche multicritère sur <b>2 854 joueurs d'Europe</b>.<br/>• Détection de jumeaux statistiques ($k$-NN) sous-évalués.<br/>• Tableau de bord et simulateur financier mercato en temps réel.", body_style)
        ]
    ]
    t_s2 = Table(s2_content, colWidths=[380, 380])
    t_s2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (0,0), colors.HexColor('#fee2e2')),
        ('BACKGROUND', (1,0), (1,0), colors.HexColor('#dcfce7')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(t_s2)
    story.append(PageBreak())

    # =========================================================================
    # SLIDE 3 : VEILLE & ARCHITECTURE
    # =========================================================================
    story.append(Paragraph("2. VEILLE TECHNOLOGIQUE & ARCHITECTURE TECHNIQUE", slide_title))
    story.append(Paragraph("Stack Full-Stack découplée FastAPI + React 18 + SQLite", slide_subtitle))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=12))

    s3_table = [
        [Paragraph("<b>Brique Technique</b>", body_style), Paragraph("<b>Choix Technologique</b>", body_style), Paragraph("<b>Bénéfice & Justification</b>", body_style)],
        [Paragraph("Data Engineering", body_style), Paragraph("Python / `soccerdata` (FBref)", body_style), Paragraph("Scraping automatisé des 2 854 joueurs réels des 5 grands championnats (2024-2025).", body_style)],
        [Paragraph("API Backend", body_style), Paragraph("FastAPI / Uvicorn (ASGI)", body_style), Paragraph("Temps de réponse ultra-rapide (< 15 ms), endpoints sécurisés JWT.", body_style)],
        [Paragraph("Base de données", body_style), Paragraph("SQLite (`recruitment_app.db`)", body_style), Paragraph("Requêtes SQL paramétrées sécurisées anti-injections SQL.", body_style)],
        [Paragraph("Frontend UI", body_style), Paragraph("React 18 / Vite / Canvas SVG", body_style), Paragraph("Interface réactive glassmorphism, radar vectoriel et mode démo client-side.", body_style)]
    ]
    t_s3 = Table(s3_table, colWidths=[150, 200, 410])
    t_s3.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_ol_blue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 6)
    ]))
    story.append(t_s3)
    story.append(PageBreak())

    # =========================================================================
    # SLIDE 4 : FONCTIONNALITÉS & DEMO
    # =========================================================================
    story.append(Paragraph("3. FONCTIONNALITÉS CLÉS & SÉCURITÉ RBAC", slide_title))
    story.append(Paragraph("Trois espaces de travail adaptés aux besoins des utilisateurs", slide_subtitle))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=12))

    s4_table = [
        [Paragraph("<b>Espace de travail</b>", body_style), Paragraph("<b>Accès & Rôle RBAC</b>", body_style), Paragraph("<b>Fonctionnalités Clés</b>", body_style)],
        [Paragraph("1. Scouting & Matching", body_style), Paragraph("Scout / Directeur / Admin", body_style), Paragraph("Filtres multicritères (Opta 0-100), radars 6 axes et jumeaux $k$-NN.", body_style)],
        [Paragraph("2. Effectif OL & Comparateur", body_style), Paragraph("Scout / Directeur / Admin", body_style), Paragraph("Fiches de l'effectif actuel lyonnais et comparateur dual radar face-à-face.", body_style)],
        [Paragraph("3. Budget Mercato", body_style), Paragraph("Directeur Sportif & Admin (Scout bloqué)", body_style), Paragraph("Enveloppe de 45 M€, suivi de masse salariale et simulateur financier.", body_style)]
    ]
    t_s4 = Table(s4_table, colWidths=[180, 180, 400])
    t_s4.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_purple),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 8)
    ]))
    story.append(t_s4)
    story.append(PageBreak())

    # =========================================================================
    # SLIDE 5 : ALGORITHME KNN & VALIDAION
    # =========================================================================
    story.append(Paragraph("4. ALGORITHME $k$-NN DES JUMEAUX STATISTIQUES", slide_title))
    story.append(Paragraph("Matching de performance et distance euclidienne pondérée", slide_subtitle))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=12))

    s5_info = [
        [Paragraph("<b>Formule Mathématique de Distance</b>", body_style), Paragraph("<b>Résultats de Matching Validés</b>", body_style)],
        [
            Paragraph("$$Distance = \\sqrt{\\frac{1}{6}\\sum_{i=1}^6 (Stat_{target,i} - Stat_{candidat,i})^2 + \\left(14 \\cdot (\\log_{10}(Val_{target}) - \\log_{10}(Val_{candidat}))\\right)^2}$$", body_style),
            Paragraph("• <b>Jumeaux de Kylian Mbappé :</b> Khvicha Kvaratskhelia (90.7%), Erling Haaland (88.9%), Bradley Barcola (88.9%), Ousmane Dembélé (88.8%).<br/>• <b>Jumeaux de Rayane Cherki :</b> Jude Bellingham, Florian Wirtz, Antoine Griezmann.", body_style)
        ]
    ]
    t_s5 = Table(s5_info, colWidths=[380, 380])
    t_s5.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(t_s5)
    story.append(PageBreak())

    # =========================================================================
    # SLIDE 6 : DEPLOIEMENT & BILAN
    # =========================================================================
    story.append(Paragraph("5. DÉPLOIEMENT, CONFORMITÉ & BILAN", slide_title))
    story.append(Paragraph("Publication en ligne sur Vercel, Responsive Mobile-First et respect RGPD/W3C", slide_subtitle))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=12))

    s6_table = [
        [Paragraph("<b>Axe de Validation</b>", body_style), Paragraph("<b>Conformité & Réalisation</b>", body_style)],
        [Paragraph("Déploiement Vercel", body_style), Paragraph("Site en ligne 24h/24 : <b>https://recruitment-match-pro.vercel.app</b> (Coût : 0 € / an).", body_style)],
        [Paragraph("Responsive Mobile-First", body_style), Paragraph("Optimisé pour smartphones (iOS/Android) avec curseurs tactiles de 20px.", body_style)],
        [Paragraph("Accessibilité & RGPD", body_style), Paragraph("Normes W3C/ARIA, contrastes élevés WCAG AA, hachage Bcrypt des mots de passe.", body_style)],
        [Paragraph("Bilan RNCP40857", body_style), Paragraph("100% des exigences des Blocs 1 et 4 validées avec succès.", body_style)]
    ]
    t_s6 = Table(s6_table, colWidths=[200, 560])
    t_s6.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), c_ol_blue),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('PADDING', (0,0), (-1,-1), 8)
    ]))
    story.append(t_s6)
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>Merci pour votre attention — Place aux questions du jury (Soutenance 1h30)</b>", ParagraphStyle('ThanksText', parent=styles['Normal'], fontSize=12, leading=16, textColor=c_purple, alignment=TA_CENTER, fontName='Helvetica-Bold')))

    doc.build(story)
    print(f"Support de présentation PDF généré avec succès dans : {pdf_path}")

if __name__ == "__main__":
    generate_presentation()
