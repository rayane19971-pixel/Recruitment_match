from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors

# Import du générateur des pages 1 à 40 + du header
from step5_pages30_40 import build_pages1_to_40
from step1_pages1_2 import NexaPurpleHeaderCanvas

def append_step6(story):
    styles = getSampleStyleSheet()

    c_purple = colors.HexColor('#6f2f9f')
    c_dark = colors.HexColor('#0f172a')
    c_text = colors.HexColor('#334155')

    h1_style = ParagraphStyle(
        'H1Style', parent=styles['Heading1'], fontSize=16, leading=20,
        textColor=c_purple, fontName='Calibri-Bold', spaceAfter=8
    )

    h2_style = ParagraphStyle(
        'H2Style', parent=styles['Heading2'], fontSize=12.5, leading=16,
        textColor=c_dark, fontName='Calibri-Bold', spaceBefore=6, spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyStyle', parent=styles['Normal'], fontSize=11, leading=16.5,
        textColor=c_text, alignment=TA_JUSTIFY, fontName='Calibri', spaceAfter=6
    )

    # ----------------------------------------------------------------------
    # PARTIE 1 : BILAN FONCTIONNEL
    # ----------------------------------------------------------------------
    story.append(Spacer(1, 10))
    story.append(Paragraph("ÉTAPE 6 — BILAN, ANALYSE FINANCIÈRE ET CONCLUSION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. L'Achèvement du Cycle de Développement</b>", h2_style))
    story.append(Paragraph("Le déploiement en production de l'application Recruitment Match OL marque l'aboutissement formel des 16 semaines de gestation du projet. La transition du concept théorique initial (l'intégration du Moneyball dans le recrutement rhodanien) vers un produit logiciel tangible, hébergé et sécurisé, a été menée avec succès. L'ensemble des exigences fixées par la Direction Sportive d'Eagle Football dans le Cahier des Charges a été implémenté sans dérive de périmètre (Scope Creep). Le produit livré dépasse le stade du simple prototype (MVP) pour s'inscrire comme un véritable actif technologique, prêt à affronter l'intensité et l'urgence de la prochaine fenêtre du Mercato estival.", body_style))

    story.append(Paragraph("<b>2. Validation Fonctionnelle et Atteinte des KPIs</b>", h2_style))
    story.append(Paragraph("D'un point de vue strictement fonctionnel, les Indicateurs Clés de Performance (KPIs) définis en début de projet ont été pulvérisés. L'objectif d'ultra-réactivité est atteint : le calcul géométrique k-NN balayant les 2 854 profils statistiques s'exécute et s'affiche sur le front-end React en moins de 100 millisecondes. La fluidité du composant RadarChart superposant les profils asseoit la supériorité ergonomique de l'outil face aux solutions propriétaires du marché. L'adoption par les utilisateurs finaux (User Adoption Rate) a été immédiate lors de la phase d'UAT, les recruteurs confirmant que l'outil décuple leur force de frappe analytique sans exiger aucune compétence préalable en Data Science.", body_style))

    story.append(Paragraph("<b>3. Bilan Architectural : Robustesse et Indépendance</b>", h2_style))
    story.append(Paragraph("L'architecture Headless retenue a tenu toutes ses promesses. La stricte séparation entre le moteur algorithmique Python (FastAPI / Pandas) et l'interface de consommation JavaScript (React / Vite) garantit une isolation parfaite des responsabilités. Le modèle est immunisé contre l'obsolescence : l'équipe d'ingénierie pourra, à l'avenir, modifier le front-end web ou développer une application mobile native sans jamais avoir à réécrire une seule ligne du code mathématique serveur. La base SQLite, encapsulée derrière l'ORM SQLAlchemy, a prouvé sa capacité à soutenir des rafales de requêtes asynchrones intenses grâce à la non-bloquance de l'Event Loop Python.", body_style))

    story.append(Paragraph("<b>4. Évaluation Technologique de l'Intelligence Artificielle</b>", h2_style))
    story.append(Paragraph("La pertinence de l'algorithme k-Nearest Neighbors (k-NN) a été validée scientifiquement. En croisant les résultats algorithmiques avec l'expertise visuelle des recruteurs (analyse vidéo a posteriori), le taux de faux positifs a été estimé à un niveau négligeable. La normalisation statistique (StandardScaler) a effectivement empêché l'écrasement des échelles, permettant de découvrir des jumeaux tactiques dans des championnats de seconde zone (Scandinavie, Europe de l'Est). Le système démontre que la similarité vectorielle des performances peut mathématiquement contourner la subjectivité du regard humain et l'inflation spéculative des prix liés au 'nom' ou à la réputation d'un joueur.", body_style))

    # ----------------------------------------------------------------------
    # PARTIE 2 : COÛTS ET ROI
    # ----------------------------------------------------------------------
    story.append(Spacer(1, 10))
    story.append(Paragraph("ANALYSE FINANCIÈRE : COÛTS TECHNIQUES ET RETOUR SUR INVESTISSEMENT (ROI)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Modélisation des Coûts du Capital Humain (TJM)</b>", h2_style))
    story.append(Paragraph("Le véritable poste de dépense de ce projet technologique ne réside pas dans l'infrastructure, mais dans l'ingénierie intellectuelle (CAPEX). Le développement sur 16 semaines a mobilisé une équipe pluridisciplinaire d'experts. En appliquant un Taux Journalier Moyen (TJM) réaliste de marché, l'allocation budgétaire inclut le travail d'un Data Scientist pour la conception du modèle k-NN (600€/j), d'un développeur Full-Stack Python/React pour l'architecture Headless (550€/j), d'un ingénieur DevOps pour le pipeline CI/CD (600€/j) et du Chef de Projet Web assurant l'orchestration Scrum (650€/j). Cet investissement en capital humain avoisine les 150 000 €, justifié par l'exigence d'excellence technique imposée par le standing de l'Olympique Lyonnais.", body_style))

    story.append(Paragraph("<b>2. Acquisition de la Data Sportive Premium (Opta API)</b>", h2_style))
    story.append(Paragraph("Le carburant exclusif du simulateur Recruitment Match réside dans la précision millimétrique de ses données. Plutôt que de recourir à des bases de données gratuites non vérifiées (Web Scraping aléatoire), la Direction a validé l'abonnement à la licence commerciale Premium du fournisseur officiel Opta (StatsPerform). Ce flux de données en temps réel, incluant la couverture de 36 métriques ultra-détaillées sur des milliers de joueurs, représente un coût d'exploitation majeur (OPEX) s'élevant à environ 50 000 € par an. Cet abonnement est toutefois un prérequis inaliénable : la fiabilité d'une Intelligence Artificielle dépend strictement de la pureté des données ingérées (principe du <i>Garbage In, Garbage Out</i>).", body_style))

    story.append(Paragraph("<b>3. Compression Radicale de l'Infrastructure Cloud (OPEX)</b>", h2_style))
    story.append(Paragraph("À l'inverse des coûts de développement et d'acquisition de données, les frais d'hébergement ont été compressés de manière spectaculaire. Grâce à l'utilisation exclusive de technologies Open Source (FastAPI, React) et à l'architecture légère (SQLite locale, absence de bases de données distribuées onéreuses), l'application peut être servie de manière optimale sur un VPS (Virtual Private Server) cloud standard coûtant moins de 30 € par mois. L'effondrement des coûts d'infrastructure rend le fonctionnement technique quotidien du logiciel quasi-gratuit pour les finances d'Eagle Football.", body_style))

    story.append(Paragraph("<b>4. Calcul du Retour sur Investissement (ROI) Sportif</b>", h2_style))
    story.append(Paragraph("Le bilan financier du projet prend tout son sens lors du calcul du ROI. Le coût global (Ingénierie de pointe + Licence Opta annuelle) gravite autour de 200 000 €. Or, dans l'économie du football moderne, l'erreur de casting sur un seul transfert d'un joueur moyen est estimée à une perte sèche minimale de 10 à 15 millions d'euros (indemnité de transfert, salaires amortis, commission d'agents). Si le simulateur Recruitment Match permet à l'Olympique Lyonnais d'éviter une seule erreur de recrutement en détectant les signaux faibles, ou s'il permet de dénicher une pépite sous-évaluée revendue avec une forte plus-value, le logiciel rembourse instantanément 75 fois son coût de création. La rationalité du projet est absolue.", body_style))

    # ----------------------------------------------------------------------
    # PARTIE 3 : RETROSPECTIVE ET LEÇONS APPRISES
    # ----------------------------------------------------------------------
    story.append(Spacer(1, 10))
    story.append(Paragraph("RÉTROSPECTIVE AGILE ET LEÇONS APPRISES (LESSONS LEARNED)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. L'Épreuve de la Complexité Front-End vs Back-End</b>", h2_style))
    story.append(Paragraph("En prenant du recul sur ces 16 semaines intenses, je réalise que les plus grands défis ne se trouvaient pas toujours là où je les attendais. Contre toute attente, l'implémentation de l'algorithme mathématique k-NN via SciPy a été relativement fluide. Le véritable goulet d'étranglement a surgi lors du couplage entre l'écosystème React et le bouclier sécuritaire JWT du back-end FastAPI. Gérer les requêtes CORS et la persistance sécurisée du Token dans le navigateur client m'a forcé à organiser plusieurs sessions de <i>Pair Programming</i> imprévues avec mon équipe technique. Cela m'a prouvé que la sécurité réseau reste le talon d'Achille des architectures Web Headless modernes.", body_style))

    story.append(Paragraph("<b>2. Le Défi de la Normalisation des Données Sportives</b>", h2_style))
    story.append(Paragraph("L'ingénierie de la donnée a constitué mon second défi majeur. Lors du Sprint 2, nos premiers tests renvoyaient des résultats aberrants : notre algorithme favorisait systématiquement des joueurs aux statistiques kilométriques élevées, écrasant les données tactiques fines. J'ai alors appris une leçon décisive : une donnée brute n'a aucune valeur algorithmique. J'ai dû introduire en urgence le calcul du Z-Score (StandardScaler) pour normaliser chaque colonne statistique. Cette crise m'a fait comprendre l'importance cruciale du rôle de Data Engineer en amont de toute démarche d'Intelligence Artificielle.", body_style))

    story.append(Paragraph("<b>3. L'Efficacité Redoutable de la Matrice MoSCoW</b>", h2_style))
    story.append(Paragraph("Sur le plan de la gestion de projet, j'ai rapidement réalisé que l'utilisation stricte de la matrice MoSCoW allait être ma meilleure arme contre la dérive du périmètre (Scope Creep). À de multiples reprises, les recruteurs de l'OL m'ont formulé des demandes d'évolutions enthousiastes (intégration de flux vidéo, export PDF des radars) qui menaçaient notre calendrier de livraison. Assumer mon rôle de chef de projet a consisté à arbitrer de manière impartiale et à repousser diplomatiquement ces demandes vers le backlog futur, protégeant ainsi le travail de mon équipe et garantissant la livraison de notre MVP en temps et en heure.", body_style))

    story.append(Paragraph("<b>4. Ma Montée en Compétence de Chef de Projet Web</b>", h2_style))
    story.append(Paragraph("Piloter ce projet d'envergure de A à Z a été une véritable révélation professionnelle. J'ai dû traduire un besoin métier subjectif de la Direction Sportive ('je veux un joueur qui ressemble à X') en spécifications mathématiques et logicielles concrètes. Naviguer entre ma casquette d'analyste fonctionnel et celle de directeur technique, maîtriser le cycle Scrum face aux imprévus, et enfin présenter un bilan financier exécutif devant le Comex d'Eagle Football ont constitué un saut qualitatif majeur dans mon parcours. Ce projet m'a véritablement transformé en Chef de Projet Web.", body_style))

    # ----------------------------------------------------------------------
    # PARTIE 4 : PERSPECTIVES ET CONCLUSION
    # ----------------------------------------------------------------------
    story.append(Spacer(1, 10))
    story.append(Paragraph("PERSPECTIVES D'ÉVOLUTION (V2) ET CONCLUSION GÉNÉRALE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Notre Roadmap Technologique : Vers l'Analyse Prédictive (V2)</b>", h2_style))
    story.append(Paragraph("La version actuelle de notre logiciel effectue une analyse de similarité statique (une photographie à un instant T). Ma feuille de route stratégique pour la Version 2 ambitionne d'intégrer la dimension temporelle. En couplant l'historique massif d'Opta à des réseaux de neurones récurrents (Deep Learning de type LSTM), je souhaite faire passer le système de l'analytique à la prédictive. Notre outil sera alors capable d'extrapoler la courbe de progression d'un joueur de 19 ans et de prédire son niveau statistique probable à 23 ans. Cela transformera le simulateur en un véritable oracle d'investissement.", body_style))

    story.append(Paragraph("<b>2. Intégration de la Biométrie et de la Computer Vision</b>", h2_style))
    story.append(Paragraph("L'autre axe de développement qui me tient à cœur concerne l'élargissement du champ de données. Au-delà des métriques d'événements de jeu, j'envisage pour la V2 l'ingestion de données de tracking biométrique spatial (Computer Vision via les caméras du Groupama Stadium). Mesurer l'intensité réelle des courses et le placement d'un joueur par rapport au bloc défensif enrichira considérablement notre calcul k-NN. Cette granularité physique absolue viendra réduire encore davantage la part de hasard inhérente au recrutement.", body_style))

    story.append(Paragraph("<b>3. La Réconciliation de l'Humain et de la Machine</b>", h2_style))
    story.append(Paragraph("S'il y a bien une chose que ce projet Recruitment Match prouve, c'est qu'il n'existe pas d'antagonisme entre le flair historique du recruteur et la rigueur de l'Intelligence Artificielle. Je n'ai jamais eu pour vocation de remplacer le jugement de la Direction Sportive, mais de lui offrir un puissant exosquelette décisionnel. L'algorithme déblaie la complexité de 2 854 profils et met en lumière les pépites, tandis que l'humain conserve le monopole de la validation finale (évaluation mentale, psychologique et adaptabilité). J'ai pu observer une osmose totale entre la Data Science et la réalité du terrain.", body_style))

    story.append(Paragraph("<b>4. Ma Conclusion Officielle</b>", h2_style))
    story.append(Paragraph("Pour conclure, concevoir et déployer l'application Recruitment Match a été une expérience fondatrice qui démontre la pertinence écrasante de l'ingénierie Web au service de la performance sportive. En m'appuyant sur une méthodologie Agile rigoureuse, une architecture moderne (FastAPI/React) et une analyse financière lucide, je suis fier d'avoir livré un outil qui se mue en un avantage compétitif stratégique pour l'Olympique Lyonnais. Ce mémoire technique vient sceller l'acquisition de mes compétences en ingénierie, en gestion d'équipe et en vision stratégique, validant ainsi avec passion mon titre de Chef de Projet Web certifié.", body_style))

    return story

def build_full_report():
    story_1_to_40 = build_pages1_to_40()
    story_final = append_step6(story_1_to_40)
    return story_final

if __name__ == "__main__":
    story = build_full_report()
    pdf_path = r"C:\Users\user\OneDrive\Documents\OURAD_RAYANE_PROJET.pdf"
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=70,
        bottomMargin=40
    )
    doc.build(story, canvasmaker=NexaPurpleHeaderCanvas)
    print("PDF FINAL de certification généré avec succès !")
