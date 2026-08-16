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
        ol_logo_path = r"C:\Users\user\OneDrive\Documents\web-rayane-ourad-main\ol_logo.png"
        
        # Logo OL
        if os.path.exists(ol_logo_path):
            self.drawImage(ol_logo_path, 395, 786, width=45, height=45, mask='auto')
            
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

def build_pages1_2():
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
    c_dark = colors.HexColor('#0f172a') # NOIR ÉLÉGANT DENSE
    c_ol_blue = colors.HexColor('#0b2c5c')
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
        'SecH1', parent=styles['Heading1'], fontSize=14, leading=17,
        textColor=c_dark, fontName='Helvetica-Bold', spaceBefore=6, spaceAfter=8
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
    # PAGE 1 : PAGE DE GARDE AVEC TOUS LES TITRES EN NOIR DENSE (#0F172A)
    # =========================================================================
    story.append(Spacer(1, 10))
    story.append(Paragraph("DOSSIER DE PROJET ANNUEL CERTIFICATIF", title_cover))
    
    # TITRE EN NOIR DENSE (#0F172A)
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
        [Paragraph("URL du projet déployé :", meta_label), Paragraph("https://recruitment-match.vercel.app", meta_val)],
        [Paragraph("Dépôt Git Officiel :", meta_label), Paragraph("https://github.com/rayane19971-pixel/Recruitment_match", meta_val)],
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

    # =========================================================================
    # PAGE 2 : SOMMAIRE GÉNÉRAL DESIGN & AGRANDI
    # =========================================================================
    story.append(Paragraph("SOMMAIRE DÉTAILLÉ DU DOSSIER DE PROJET ANNUEL", h1_style))
    story.append(HRFlowable(width="100%", thickness=2, color=c_purple, spaceAfter=10))

    toc_items = [
        ("PAGE 1", "Page de garde officielle & informations administratives du projet", "Garde"),
        ("PAGE 2", "Sommaire général paginé du dossier de projet annuel (RNCP40857)", "Sommaire"),
        ("PAGES 3 - 4", "PARTIE 1.b — Contexte & Objectifs Stratégiques OL (Analyse SWOT)", "Partie 1"),
        ("PAGES 5 - 19", "PARTIE 1.c — Analyse des Besoins, Veille, MoSCoW, Risques & RSE (15 pages)", "Partie 1"),
        ("PAGES 20 - 29", "PARTIE 1.d — Cahier des Charges, Fonctionnalités, Gantt & Budget (10 pages)", "Partie 1"),
        ("PAGES 30 - 31", "PARTIE 2.a — Architecture Technique Modulaire & Data ETL (Bloc 4 - 2 pages)", "Partie 2"),
        ("PAGES 32 - 33", "PARTIE 2.b — Maquettes & Prototypes UX/UI Glassmorphism OL (Bloc 4)", "Partie 2"),
        ("PAGES 34 - 35", "PARTIE 2.c — Développement Front-End React 18, Canvas SVG & Mobile (Bloc 4 - 2 pages)", "Partie 2"),
        ("PAGES 36 - 38", "PARTIE 2.d — Développement Back-End FastAPI, SQLite & Algorithme k-NN (Bloc 4 - 3 pages)", "Partie 2"),
        ("PAGES 39 - 40", "PARTIE 2.e, f, g — Tests, RGPD, Accessibilité W3C, Maintenance & Bilan (Bloc 4 - 6 pages)", "Partie 2")
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

    doc.build(story, canvasmaker=NexaPurpleHeaderCanvas)
    print("Titre RECRUITMENT MATCH — OLYMPIQUE LYONNAIS affiché en NOIR DENSE (#0F172A) !")

if __name__ == "__main__":
    build_pages1_2()
