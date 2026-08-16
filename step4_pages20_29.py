import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_JUSTIFY

# Importer les éléments de l'étape 3
sys.path.append(r"C:\Users\user\OneDrive\Documents\web-rayane-ourad-main")
from step3_pages5_19 import build_pages1_to_19, NexaPurpleHeaderCanvas

def append_pages20_to_29(story):
    # Redéfinition locale des styles nécessaires pour la suite
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
    # PAGE 20 : INTRODUCTION ÉTAPE 4 (CAHIER DES CHARGES)
    # ----------------------------------------------------------------------
    story.append(Paragraph("ÉTAPE 4 — CAHIER DES CHARGES & PLANIFICATION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Transition Stratégique : De l'Opportunité à la Conception Rigoureuse</b>", h2_style))
    story.append(Paragraph("La validation exécutive (GO) obtenue au terme de l'Étude d'Opportunité marque un tournant décisif dans le cycle de vie du projet Recruitment Match OL. La phase d'idéation et de faisabilité s'efface désormais au profit d'une ingénierie de conception stricte. Cette quatrième grande étape du rapport vise à traduire les besoins métiers validés en spécifications logicielles opposables. L'élaboration d'un Cahier des Charges Technique et Fonctionnel (CCTF) détaillé devient impérative pour encadrer le travail des développeurs, prévenir toute dérive de périmètre (<i>Feature Creep</i>) et garantir contractuellement la livraison du produit attendu par la Direction Sportive.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Objectifs du Cahier des Charges (CCTF)</b>", h2_style))
    story.append(Paragraph("Le Cahier des Charges constitue la pierre angulaire du projet. Son objectif premier est de modéliser exhaustivement les cas d'utilisation (<i>Use Cases</i>) et les parcours utilisateurs (<i>User Journeys</i>). Il détermine avec une précision algorithmique ce que le système doit faire (Spécifications Fonctionnelles) et la manière exacte dont l'architecture logicielle doit être structurée pour y parvenir (Spécifications Techniques). Ce document opposable sert de référentiel unique pour l'équipe technique, les auditeurs de sécurité et les parties prenantes du club, garantissant que la solution finale réponde au millimètre près à la stratégie <i>Moneyball</i> visée par Eagle Football.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Modélisation UML et Architecture Logicielle</b>", h2_style))
    story.append(Paragraph("Afin d'offrir une vision claire et universelle des mécanismes sous-jacents de l'application, cette phase de conception s'appuie massivement sur le langage de modélisation unifié (UML). La transcription des processus de recrutement en diagrammes de séquence et en diagrammes de classes permet d'anticiper les goulots d'étranglement (<i>bottlenecks</i>) au niveau des requêtes asynchrones entre le client React et l'API FastAPI. Cette abstraction architecturale préalable au codage est une exigence forte de la norme de certification RNCP40857, prouvant la capacité du Chef de Projet à conceptualiser des systèmes d'information complexes.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Planification Financière et Temporelle (Gantt & Budget)</b>", h2_style))
    story.append(Paragraph("Enfin, la conception technique est indissociable de la maîtrise des contraintes de temps et d'argent. Ce chapitre déploiera une planification Agile (Sprints) matérialisée par un Diagramme de Gantt strictement verrouillé sur 16 semaines. Parallèlement, une budgétisation exhaustive modélisera les dépenses d'investissement (CAPEX) liées aux coûts de développement cognitif, ainsi que les dépenses de fonctionnement (OPEX) inhérentes à l'hébergement de la plateforme. Cet exercice financier garantira que le coût de possession du logiciel (TCO) demeure parfaitement indolore face à l'enveloppe Mercato colossale de 45 millions d'euros qu'il a pour vocation d'optimiser.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("Le socle conceptuel étant posé, le chapitre suivant aborde directement les spécifications fonctionnelles détaillées, décrivant les habilitations et les parcours des acteurs au sein de l'application.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 21 : SPÉCIFICATIONS FONCTIONNELLES (USE CASES)
    # ----------------------------------------------------------------------
    story.append(Paragraph("SPÉCIFICATIONS FONCTIONNELLES (ACTEURS ET CAS D'UTILISATION)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Cartographie des Acteurs et Gestion des Rôles (RBAC)</b>", h2_style))
    story.append(Paragraph("La spécification fonctionnelle démarre par la définition stricte des acteurs interagissant avec le système. L'application Recruitment Match OL identifie deux typologies d'utilisateurs distinctes, gérées par un système de contrôle d'accès basé sur les rôles (RBAC). Le premier acteur est le 'Scout' (Recruteur Terrain), dont la mission se cantonne à l'identification sportive pure ; il ne possède des droits de lecture que sur les profils et les statistiques vectorisées k-NN. Le second acteur est le 'Director' (Directeur Sportif / Cellule Financière), qui cumule les droits analytiques du Scout et bénéficie d'une élévation de privilèges lui octroyant l'accès au simulateur d'offres, aux grilles salariales confidentielles et aux métriques budgétaires.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Cas d'Utilisation Principal : Recherche de Jumeaux Statistiques</b>", h2_style))
    story.append(Paragraph("Le cœur fonctionnel du produit (<i>Core Feature</i>) est la recherche de profils similaires. Le parcours utilisateur (<i>User Flow</i>) exige que l'acteur (Scout ou Director) puisse saisir le nom d'un joueur ciblé via une barre de recherche à autocomplétion dynamique. Le système doit alors exécuter instantanément l'algorithme k-NN (k-Nearest Neighbors) et afficher sous forme de cartes d'identité les 4 joueurs européens possédant les spectres de performances les plus ressemblants. Cette interface doit permettre de comparer simultanément les graphiques radars interactifs superposés des jumeaux statistiques afin de valider visuellement la pertinence du résultat analytique.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Cas d'Utilisation Secondaire : Filtrage Multicritère Opta</b>", h2_style))
    story.append(Paragraph("La détection ne se limite pas à la simple similarité. La spécification exige l'implémentation d'un module de filtrage granulaire avancé. L'utilisateur doit pouvoir affiner le pool de joueurs analysés par l'algorithme en ajustant des curseurs interactifs (sliders) sur les 6 axes de performance brute (Défense, Physique, Tirs, Passes, Dribbles, Vitesse) étalonnés de 0 à 100. Ce filtre dynamique doit interagir en temps réel avec le moteur vectoriel pour recalculer les jumeaux statistiques en excluant les profils qui ne satisfont pas aux exigences athlétiques minimales requises par l'entraîneur principal.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Cas d'Utilisation Restreint : Simulation Financière du Mercato</b>", h2_style))
    story.append(Paragraph("Exclusivement réservée au rôle 'Director', cette fonctionnalité est le nerf de la guerre budgétaire. Lorsqu'un jumeau statistique sportif est identifié et validé, le système doit autoriser le Directeur à ouvrir un panneau de simulation (<i>Split-Screen</i>). Il y renseignera le montant de l'indemnité de transfert estimée et le salaire brut mensuel projeté sur 3 à 5 ans. L'application calculera alors instantanément le coût d'amortissement total de l'opération, le déduira de l'enveloppe Mercato globale de 45 millions d'euros, et alertera l'utilisateur si la projection financière enfreint les règles strictes imposées par la DNCG.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("Le périmètre des interactions humaines étant formellement cadré, il est indispensable de structurer l'architecture des données capable de soutenir ces fonctionnalités. Le chapitre suivant détaille les spécifications techniques du back-end.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 22 : SPÉCIFICATIONS TECHNIQUES (MODÈLE DE DONNÉES)
    # ----------------------------------------------------------------------
    story.append(Paragraph("SPÉCIFICATIONS TECHNIQUES (ARCHITECTURE ET DATA)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Architecture Headless Orientée Microservices</b>", h2_style))
    story.append(Paragraph("La traduction technique des besoins fonctionnels repose sur une architecture <i>Headless</i> stricte, scindant impérativement l'interface graphique (Front-end) de la logique métier (Back-end). Cette conception moderne garantit une séparation des préoccupations (<i>Separation of Concerns</i>). Le socle de données est propulsé par une API RESTful robuste codée en Python avec FastAPI. Ce back-end agit comme un moteur de calcul pur, exposant des routes (endpoints) asynchrones. Il communique de manière totalement agnostique, via l'échange de payloads au format JSON, avec le front-end React 18, assurant une évolutivité maximale et la capacité future de greffer une application mobile native sans modifier le code serveur.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Modèle Conceptuel des Données (MCD) et Base SQLite</b>", h2_style))
    story.append(Paragraph("Le stockage de l'information est confié à une base de données relationnelle SQLite3, choisie pour sa légèreté, sa vélocité de lecture (essentielle pour le calcul k-NN) et son encapsulation directe sous forme de fichier statique (`database.db`), simplifiant drastiquement les déploiements (CI/CD). Le Modèle Conceptuel des Données (MCD) s'articule autour de trois tables maîtresses : `Players` (clés primaires, métadonnées biométriques et URL des portraits), `Stats` (table relationnelle contenant les vecteurs de performance normés 0-100 pour le calcul algorithmique) et `Users` (stockage sécurisé des rôles RBAC et des hachages Bcrypt des mots de passe pour l'authentification).", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Pipeline ETL (Extract, Transform, Load) des Métriques Opta</b>", h2_style))
    story.append(Paragraph("La fiabilité de la plateforme repose sur l'ingénierie du pipeline ETL. L'extraction (<i>Extract</i>) s'effectue via un script Python qui scrape les données officielles des 5 grands championnats européens sur la plateforme FBref. La transformation (<i>Transform</i>) constitue la phase critique : les statistiques brutes sont d'abord agrégées, puis converties en ratio 'Per 90 minutes' pour annuler le biais du temps de jeu. Elles subissent ensuite une passe de nettoyage via la librairie Pandas (suppression des valeurs nulles et des joueurs ayant moins de 500 minutes de temps de jeu). Enfin, une normalisation Min-Max Scaler ramène chaque axe de performance sur un vecteur strict allant de 0 à 1. La phase de chargement (<i>Load</i>) insère finalement ces vecteurs purifiés dans la table SQLite, prêts pour l'algorithme.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Scalabilité de l'Intelligence Artificielle (k-NN)</b>", h2_style))
    story.append(Paragraph("Le moteur d'intelligence artificielle est encapsulé dans un service FastAPI dédié. Le calcul de similarité (algorithme des k-Plus Proches Voisins) utilise la distance euclidienne sur un espace vectoriel à 6 dimensions (correspondant aux 6 attributs sportifs). Pour garantir un temps de réponse foudroyant (< 15 millisecondes) sur une base de données contenant des milliers d'entrées, le back-end met en cache (<i>In-Memory Caching</i>) la matrice des vecteurs normalisés lors du démarrage du serveur Uvicorn, évitant ainsi de coûteuses requêtes SQL répétitives à chaque sollicitation de la barre de recherche par un recruteur.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("Afin de visualiser dynamiquement l'orchestration complexe entre le front-end React et le moteur vectoriel FastAPI, le chapitre suivant expose la modélisation UML via le diagramme de séquence de la recherche.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 23 : CONCEPTION UML (DIAGRAMME DE SÉQUENCE)
    # ----------------------------------------------------------------------
    story.append(Paragraph("CONCEPTION LOGICIELLE UML (DIAGRAMME DE SÉQUENCE)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    try:
        seq_img = Image('uml_sequence.png', width=500, height=350)
        story.append(seq_img)
    except Exception as e:
        print("Erreur chargement image UML Sequence:", e)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<b>1. Rôle et Portée du Diagramme de Séquence</b>", h2_style))
    story.append(Paragraph("La modélisation comportementale via le diagramme de séquence UML est une étape incontournable pour sécuriser la phase de développement. Elle offre une cartographie temporelle et synchrone des interactions entre les différents acteurs et composants du système. Pour la plateforme Recruitment Match OL, l'enjeu critique se situe au niveau du flux de données lors d'une requête de recherche (<i>Query</i>). Ce diagramme détaille précisément la chaîne d'appels HTTP, la validation sécuritaire des jetons JWT et le retour asynchrone des résultats depuis la base de données SQLite, prévenant ainsi les failles d'architecture (Race conditions, Timeouts) avant même la rédaction de la première ligne de code.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Phase d'Interception et Contrôle de Sécurité (Middleware)</b>", h2_style))
    story.append(Paragraph("L'orchestration débute lorsqu'un Recruteur (Scout) saisit le nom d'un joueur dans le champ de recherche React. Une fonction <i>Debounce</i> (temporisation de 300ms) s'assure de ne pas surcharger le serveur à chaque frappe de touche. L'application front-end émet alors une requête asynchrone <i>GET /api/knn/{player_id}</i> vers FastAPI. Le système n'interroge pas immédiatement la base de données. La requête est d'abord interceptée par le middleware de sécurité de FastAPI qui extrait le jeton Bearer JWT des en-têtes (<i>Headers</i>) HTTP. Le serveur décode cryptographiquement le jeton, valide sa signature et vérifie sa date d'expiration. En cas de fraude ou d'expiration, une exception HTTP 401 Unauthorized est instantanément renvoyée au client, bloquant radicalement l'accès à la logique métier.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Exécution Algorithmique et Traitement Vectoriel (k-NN)</b>", h2_style))
    story.append(Paragraph("Une fois le passeport de sécurité validé (Clearance 200 OK), le routeur FastAPI délègue la tâche au contrôleur de l'intelligence artificielle. Le contrôleur extrait les statistiques vectorielles (valeurs normées de 0 à 1) du joueur ciblé depuis la mémoire cache. Il exécute ensuite la fonction mathématique de la distance euclidienne, comparant le vecteur du joueur cible avec la matrice complète des 2 854 autres profils. Le système trie les résultats par ordre croissant de distance géométrique, isole les 4 profils présentant la plus faible distance (les <i>Nearest Neighbors</i>), puis enrichit ces données statistiques avec les métadonnées biométriques (Nom, Club, Âge, URL de l'image) extraites dynamiquement via une requête SQL `SELECT` ciblée sur la table SQLite.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Résolution Asynchrone et Rendu Graphique (Virtual DOM)</b>", h2_style))
    story.append(Paragraph("La boucle temporelle s'achève par la phase de restitution. L'API FastAPI compile les 4 profils jumeaux dans un payload JSON hautement structuré et le renvoie au client. Dès réception de cette promesse (<i>Promise Resolved</i>), le composant parent React met à jour son état interne (<i>State</i>). Ce déclencheur force le Virtual DOM à s'actualiser de manière chirurgicale : les composants enfants (<i>PlayerCards</i>) re-rendent leurs graphiques radars Canvas SVG en injectant les nouveaux axes de performance. L'intégralité de ce cycle de requête/réponse ultra-complexe s'exécute en moins de 30 millisecondes, offrant une expérience de fluidité absolue à l'utilisateur.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("Cette mécanique d'exécution asynchrone garantissant la robustesse des requêtes, le chapitre suivant s'attarde sur la cartographie structurelle de l'application via le diagramme de classes et de composants.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 24 : CONCEPTION UML (DIAGRAMME DE CLASSES / COMPOSANTS)
    # ----------------------------------------------------------------------
    story.append(Paragraph("CONCEPTION LOGICIELLE UML (DIAGRAMME DE COMPOSANTS)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    try:
        comp_img = Image('uml_component.png', width=500, height=380)
        story.append(comp_img)
    except Exception as e:
        print("Erreur chargement image UML Component:", e)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<b>1. Abstraction Structurelle du Système (Component Diagram)</b>", h2_style))
    story.append(Paragraph("Le Diagramme de Composants UML constitue l'ossature statique du projet d'ingénierie. Contrairement au diagramme de séquence qui modélise le temps, cette représentation cartographie l'architecture physique et logique de l'application. Elle explicite l'emboîtement des modules logiciels, les dépendances externes (bibliothèques) et les interfaces de communication (API). Cette vision d'ensemble est cruciale pour l'équipe de développement, car elle permet de diviser le travail en micro-tâches (composants React isolés, routes API dédiées) et garantit que l'architecture Headless respecte le principe de faible couplage et de forte cohésion, condition sine qua non d'une maintenance pérenne.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Écosystème Front-End (React, TailwindCSS et Recharts)</b>", h2_style))
    story.append(Paragraph("La couche de présentation (Interface Utilisateur) est modélisée comme un nœud applicatif autonome. Au sommet de l'arborescence front-end trône l'instance <i>App.jsx</i> (le routeur principal). Elle gère les états globaux (<i>Context API</i>) liés à la session utilisateur et au thème graphique. Elle distribue les données vers des composants enfants isolés tels que la <i>SearchBar</i> (gestion des inputs debounced), la <i>PlayerGrid</i> (matrice d'affichage des résultats) et le <i>BudgetSimulator</i> (module financier). Pour le rendu graphique, le composant <i>RadarChart</i> importe la puissante librairie externe <i>Recharts</i> (basée sur D3.js et SVG), tandis que l'habillage visuel (UI) dépend étroitement de la librairie utilitaire <i>TailwindCSS</i>, garantissant une intégration responsive chirurgicale.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Noyau Back-End et Services Algorithmiques (FastAPI)</b>", h2_style))
    story.append(Paragraph("Isolé derrière la barrière du protocole HTTP, le nœud back-end est modélisé autour de l'instance ASGI FastAPI. L'architecture interne respecte le pattern MVC (Modèle-Vue-Contrôleur) revisité. Les requêtes entrantes frappent d'abord le module <i>Routers</i>, qui dispatche l'action vers les <i>Controllers</i> appropriés (Auth, Players, ML). L'intelligence algorithmique est confinée dans un module indépendant (<i>ML_Engine.py</i>) s'appuyant massivement sur les librairies scientifiques <i>Pandas</i> (manipulation matricielle) et <i>SciPy</i> (fonctions spatiales k-NN). Cette ségrégation permet de mettre à jour ou de remplacer le modèle d'intelligence artificielle sans altérer le reste du code serveur.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Couche de Persistance et Base de Données (SQLite)</b>", h2_style))
    story.append(Paragraph("La fondation de l'architecture est la couche de persistance des données. Elle est modélisée par le composant de base de données SQLite, interfacé avec le back-end via l'ORM (Object-Relational Mapping) ou le query builder de FastAPI. Ce composant est responsable du stockage statique des tables <i>Users</i>, <i>Players</i> et <i>Stats</i>. Son encapsulation locale protège le système des dépendances réseaux externes, assurant que la lecture des 2 854 profils européens s'exécute à la vitesse du disque dur local de l'instance serveur, maximisant ainsi le débit analytique global de la plateforme.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("Les spécifications techniques et l'architecture logicielle UML étant définitivement figées, le projet entre dans la phase cruciale de l'organisation temporelle. Le chapitre suivant justifie l'approche méthodologique Agile et la planification par Sprints.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 25 : PLANIFICATION PROJET (MÉTHODOLOGIE AGILE)
    # ----------------------------------------------------------------------
    story.append(Paragraph("PLANIFICATION PROJET & MÉTHODOLOGIE AGILE (SCRUM)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Adoption du Framework Agile Scrum</b>", h2_style))
    story.append(Paragraph("La réussite du projet Recruitment Match OL ne repose pas uniquement sur l'excellence du code, mais sur la maîtrise absolue de sa cadence de livraison. Afin de respecter le calendrier critique de 16 semaines imposé par le cahier des charges et la fenêtre du Mercato estival, la gestion de projet traditionnelle (Cycle en V) a été proscrite au profit de la méthodologie Agile, et plus spécifiquement du framework Scrum. Cette approche empirique et itérative permet d'absorber les retours utilisateurs en continu et de réaligner la trajectoire du logiciel face aux ajustements stratégiques (pivots) exigés par la Direction Sportive d'Eagle Football.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Découpage Temporel : Structuration en Sprints (16 Semaines)</b>", h2_style))
    story.append(Paragraph("Le Macro-Planning du projet est rigoristement saucissonné en 4 itérations principales (Sprints), d'une durée uniforme de 4 semaines chacune. Le <i>Sprint 1</i> est consacré à l'ingénierie de la donnée (ETL) et à l'architecture Back-end FastAPI. Le <i>Sprint 2</i> aborde le développement du moteur front-end React et la liaison API. Le <i>Sprint 3</i> se concentre sur l'intelligence algorithmique (modèle k-NN) et la couche de sécurité (RBAC / JWT). Enfin, le <i>Sprint 4</i> est dédié aux tests d'assurance qualité (QA), au débogage intensif et au déploiement en production. Ce découpage cadencé (<i>Timeboxing</i>) garantit la livraison d'un incrément logiciel fonctionnel à la fin de chaque mois.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Cérémonies Scrum et Suivi de la Performance</b>", h2_style))
    story.append(Paragraph("Afin de maintenir une vélocité de développement optimale, la gestion du projet intègre les rituels Scrum fondamentaux. Le <i>Sprint Planning</i> mensuel fige les fonctionnalités (<i>User Stories</i>) à développer depuis le Product Backlog. Des <i>Daily Stand-ups</i> virtuels de 15 minutes assurent la synchronisation quotidienne de l'équipe d'ingénierie pour lever les points de blocage (bloqueurs techniques). À l'issue de chaque itération, la <i>Sprint Review</i> permet de démontrer le fonctionnement de l'application directement au Directeur Sportif (Vincent), garantissant ainsi un niveau d'alignement métier parfait avant d'amorcer le cycle de développement suivant.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Maîtrise de la Dérive et Sécurisation du Périmètre (Scope Creep)</b>", h2_style))
    story.append(Paragraph("L'intérêt majeur de cette planification Agile est la protection contre l'inflation du périmètre fonctionnel (<i>Scope Creep</i>). Les idées d'évolutions non urgentes soumises par les recruteurs (ex: export PDF, flux vidéo) sont systématiquement repoussées dans le backlog selon la matrice MoSCoW, sans jamais perturber l'itération en cours d'exécution. Cette rigueur méthodologique assure contractuellement que le MVP (Minimum Viable Product), centré sur l'algorithme k-NN de détection des jumeaux statistiques, sera livré, audité et déployé exactement au terme de la seizième semaine du calendrier projet.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("Ce cadre de travail Agile étant fermement établi, le chapitre suivant matérialise visuellement cette organisation temporelle au travers du Diagramme de Gantt détaillé des 4 Sprints.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 26 : DIAGRAMME DE GANTT DÉTAILLÉ
    # ----------------------------------------------------------------------
    story.append(Paragraph("DIAGRAMME DE GANTT (MACRO-PLANNING OPÉRATIONNEL)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    try:
        gantt_img = Image('gantt_chart.png', width=500, height=250)
        story.append(gantt_img)
    except Exception as e:
        print("Erreur chargement image Gantt:", e)
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("<b>1. Structuration Temporelle de la Phase de Données (Sprint 1 : Semaines 1 à 4)</b>", h2_style))
    story.append(Paragraph("Le démarrage opérationnel du projet est exclusivement focalisé sur la consolidation de la fondation des données. Durant les 4 premières semaines, l'effort d'ingénierie (Data Engineering) cible le scraping des plateformes FBref et Opta Sports. L'équipe technique développe et calibre le pipeline ETL (Extract, Transform, Load) chargé de nettoyer et normaliser les données brutes des 2 854 joueurs européens (formatage 'Per 90' et traitement Min-Max Scaler). En parallèle, l'architecture SQLite est initialisée et les premières routes (endpoints) de l'API FastAPI sont déployées, constituant la colonne vertébrale du back-end.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Ingénierie Front-end et Rendu Graphique (Sprint 2 : Semaines 5 à 8)</b>", h2_style))
    story.append(Paragraph("Dès que l'API est capable de renvoyer des flux JSON fiables, le Sprint 2 inaugure la construction de l'interface utilisateur. Le framework React 18 est instancié avec le bundler Vite. Cette phase intègre le développement chirurgical du système de composants (Component Design) : implémentation de la barre de recherche intelligente (Debounce), de la grille des profils, et du module financier (Split-Screen). L'accent est mis sur la performance visuelle avec l'intégration de la librairie Recharts, qui génère les graphiques radars interactifs SVG en 60 FPS, garantissant une ergonomie irréprochable et un design responsive parfait via TailwindCSS.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Intégration de l'IA k-NN et Sécurisation (Sprint 3 : Semaines 9 à 12)</b>", h2_style))
    story.append(Paragraph("Le troisième itérium est le point d'orgue analytique du projet. L'algorithme d'intelligence artificielle (k-Nearest Neighbors) est infusé dans le moteur FastAPI, exploitant la distance euclidienne pour faire émerger les jumeaux statistiques. Simultanément, la sécurisation hermétique de l'application est activée. Le middleware de contrôle d'accès (RBAC) est déployé pour segmenter les droits entre les 'Scouts' et les 'Directors', le chiffrement Bcrypt des mots de passe est verrouillé en base de données, et la délivrance des tokens JWT (Json Web Tokens) est paramétrée avec une expiration stricte, bouclant ainsi le périmètre de cybersécurité.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Qualité, Débogage et Mise en Production (Sprint 4 : Semaines 13 à 16)</b>", h2_style))
    story.append(Paragraph("Le dernier mois du macro-planning est entièrement sanctuarisé pour l'assurance qualité (Quality Assurance - QA) et le déploiement opérationnel. L'équipe mène des campagnes de tests automatisés (Unit Testing) et des stress tests sur l'architecture asynchrone pour garantir une tenue de charge sans faille (< 15 ms). Les audits d'accessibilité W3C et les tests de pénétration OWASP sont exécutés. Une fois la clearance technique (Zéro bug critique) validée, l'application est conteneurisée via Docker et déployée sur l'infrastructure cloud de production. Le projet s'achève par la formation de la Direction Sportive à l'outil, clôturant triomphalement le cycle des 16 semaines.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("La ligne du temps étant solidement cadencée et figée, le projet aborde sa dernière contrainte : la viabilité économique. Le chapitre suivant décortique la budgétisation exhaustive (CAPEX / OPEX) du logiciel.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 27 : BUDGÉTISATION DU PROJET (CAPEX)
    # ----------------------------------------------------------------------
    story.append(Paragraph("BUDGÉTISATION DU PROJET : COÛTS DE CRÉATION (CAPEX)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Philosophie Budgétaire et Ingénierie Open-Source</b>", h2_style))
    story.append(Paragraph("La faisabilité financière du projet Recruitment Match OL repose sur une stratégie de budgétisation frugale et chirurgicale. Afin de maximiser le Retour sur Investissement (ROI) de l'Olympique Lyonnais, le modèle économique écarte totalement l'achat de licences logicielles propriétaires onéreuses (modèle SaaS B2B). L'ingénierie s'appuie à 100% sur des technologies Open-Source matures, performantes et gratuites (Python, FastAPI, React, SQLite, TailwindCSS). Cette décision stratégique annule <i>de facto</i> les coûts d'acquisition technologiques. Les dépenses d'investissement initiales, ou <i>Capital Expenditures</i> (CAPEX), se résument donc exclusivement à la valorisation du temps de développement cognitif.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Évaluation des Coûts de Développement (Taux Journalier Moyen - TJM)</b>", h2_style))
    story.append(Paragraph("Le cœur de l'investissement budgétaire est la masse salariale (ou honoraires) de l'équipe de développement. La charge de travail totale est estimée à 16 semaines, soit environ 80 jours ouvrés (<i>Man-Days</i>). En projetant un Taux Journalier Moyen (TJM) d'ingénierie Full-Stack et Data estimé à 500 € HT sur le marché du numérique (ou son équivalent en salaire chargé pour une équipe interne), le coût global de création de la plateforme est budgétisé aux alentours de 40 000 € HT. Cette enveloppe englobe la modélisation des données, le développement algorithmique k-NN, la conception du front-end React, ainsi que les phases d'assurance qualité (QA) et de déploiement en production.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Amortissement Stratégique de l'Investissement Initial</b>", h2_style))
    story.append(Paragraph("Si l'investissement cognitif (40 000 € HT) représente l'écrasante majorité du CAPEX, son amortissement comptable est immédiat à l'échelle d'un club professionnel de l'envergure de l'Olympique Lyonnais. L'outil est spécifiquement conçu pour sécuriser une enveloppe de recrutement (Mercato) s'élevant à 45 millions d'euros. Il suffit que l'algorithme k-NN détecte un seul profil sous-évalué (pépite sportive) permettant d'éviter une erreur de casting coûteuse, ou de réaliser une plus-value à la revente, pour que le logiciel rembourse instantanément son propre coût de création par un facteur multiplicateur de cent.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Bilan des Dépenses en Capital (CAPEX)</b>", h2_style))
    story.append(Paragraph("Le bilan financier de création est exceptionnellement maîtrisé. Le projet numérique affiche une efficience budgétaire absolue : la valeur ajoutée (<i>Business Value</i>) produite est colossale pour un coût de développement (CAPEX) plafonné et parfaitement prévisible. Il n'y a aucun risque de dérive financière liée à l'achat de serveurs physiques (<i>on-premise</i>) grâce à la légèreté de la base SQLite, ni à des frais de licences surprises.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("L'investissement initial étant clarifié, l'analyse budgétaire doit également couvrir la durée de vie du produit. Le chapitre suivant détaille les dépenses de fonctionnement (OPEX) et la rentabilité globale.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 28 : OPEX ET RENTABILITÉ GLOBALE (ROI)
    # ----------------------------------------------------------------------
    story.append(Paragraph("BUDGÉTISATION DU PROJET : COÛTS D'EXPLOITATION (OPEX) & ROI", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Modélisation des Coûts d'Hébergement Cloud (Hosting)</b>", h2_style))
    story.append(Paragraph("Une fois l'application déployée en production, le modèle financier bascule sur les Dépenses Opérationnelles (<i>Operational Expenditures</i> ou OPEX). Grâce à l'architecture applicative découpée (<i>Headless</i>) extrêmement frugale, l'hébergement du système ne nécessite aucune infrastructure serveur lourde. Le déploiement de l'API FastAPI et de l'interface React peut être assuré par des instances cloud légères (ex: Google Cloud Run, AWS EC2 ou un Virtual Private Server type DigitalOcean). Associé au stockage local SQLite ne nécessitant pas de base de données managée coûteuse, le coût d'hébergement cloud global est estimé à moins de 30 € HT par mois, garantissant une empreinte budgétaire récurrente quasi-nulle pour la trésorerie du club.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Frais de Maintenance et de Maintien en Condition Opérationnelle (MCO)</b>", h2_style))
    story.append(Paragraph("Le maintien en condition opérationnelle (MCO) constitue la seconde charge de l'OPEX. Il couvre les mises à jour de sécurité des dépendances (NPM, Pip), la sauvegarde (Backups) régulière de la base SQLite, et l'actualisation périodique des datasets Opta pour intégrer de nouvelles statistiques de fin de saison. Étant donné la simplicité du code source et l'absence de dette technique héritée, ces opérations d'infogérance sont légères. Une estimation prévisionnelle alloue environ un jour-homme (<i>Man-Day</i>) de prestation externe par trimestre, soit une charge de maintenance annuelle lissée aux alentours de 2 000 € HT, assurant la pérennité et la sécurité de l'outil sur le très long terme.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Rentabilité Massive et Stratégie Moneyball (ROI)</b>", h2_style))
    story.append(Paragraph("L'analyse combinée du CAPEX (Création : ~40 000 €) et de l'OPEX (Fonctionnement annuel : ~2 500 €) démontre le potentiel financier dévastateur du logiciel. Le <i>Total Cost of Ownership</i> (TCO - Coût Total de Possession) de la solution sur 3 ans est d'environ 47 500 €. En regard, cet outil dote l'Olympique Lyonnais d'un avantage comparatif majeur sur le marché des transferts en fiabilisant l'allocation d'un budget de 45 millions d'euros. Le Retour sur Investissement (ROI) de la plateforme n'est pas simplement positif, il est exponentiel : l'application est un bouclier technologique garantissant la protection et la maximisation de l'actif le plus précieux du club : ses joueurs professionnels.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Conclusion de l'Évaluation Budgétaire</b>", h2_style))
    story.append(Paragraph("Le verdict budgétaire est sans appel. Le développement de la plateforme Recruitment Match OL est une opération d'ingénierie remarquablement économique, affichant un profil de risque financier proche de zéro. La combinaison de technologies gratuites, d'une hébergement cloud frugal et d'une conception ciblée sur l'essentiel métier (MVP) démontre une gestion de projet chirurgicale, parfaitement en phase avec les exigences d'excellence du diplôme RNCP40857.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("L'ensemble des paramètres techniques, temporels et financiers du projet étant désormais gravés dans le marbre par ce cahier des charges, le chapitre final dresse la conclusion de la conception avant le passage à l'étape du développement actif.", body_style))
#     story.append(PageBreak())

    # ----------------------------------------------------------------------
    # PAGE 29 : CONCLUSION DE L'ÉTAPE 4
    # ----------------------------------------------------------------------
    story.append(Paragraph("CONCLUSION DE LA PHASE DE CONCEPTION & DÉMARRAGE DU DÉVELOPPEMENT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Validation Systémique du Cahier des Charges</b>", h2_style))
    story.append(Paragraph("Cette quatrième grande étape du rapport marque l'accomplissement magistral de la phase d'ingénierie conceptuelle. L'intégralité du Cahier des Charges (CCTF) a été scrupuleusement rédigée. Les spécifications fonctionnelles ont délimité avec précision les parcours de recherche des recruteurs et les accès privilégiés du Directeur Sportif. Les spécifications techniques ont validé l'architecture asynchrone FastAPI couplée à la réactivité foudroyante de React 18, tout en structurant un pipeline ETL (Opta) garantissant la pureté vectorielle vitale pour l'algorithme k-NN. La fondation logicielle est désormais formellement théorisée et documentée.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>2. Sécurisation par l'UML et la Gestion des Risques Temporels</b>", h2_style))
    story.append(Paragraph("L'utilisation avancée de la modélisation UML (Diagrammes de Séquence et de Composants) a permis de mettre en exergue l'étanchéité absolue des flux d'authentification (JWT/RBAC) et d'isoler les dépendances de chaque micro-service applicatif. Parallèlement, l'implémentation du framework Agile Scrum et la cartographie détaillée du Diagramme de Gantt sur 16 semaines assurent une maîtrise absolue de la trajectoire du projet. L'équipe d'ingénierie dispose désormais d'une véritable feuille de route tactique, prévenant toute dérive périmétrique (<i>Feature Creep</i>) et garantissant des livraisons d'incréments testés à l'issue de chaque Sprint.", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>3. Cohérence Budgétaire et Vision Stratégique</b>", h2_style))
    story.append(Paragraph("Le verrouillage budgétaire (CAPEX et OPEX) confirme l'efficience économique exceptionnelle de l'architecture retenue. En annihilant les coûts d'infrastructures lourdes et de licences logicielles propriétaires, l'outil s'avère hautement rentable. Il incarne parfaitement la stratégie algorithmique (<i>Moneyball</i>) voulue par Eagle Football : utiliser les mathématiques et le code pour maximiser la rentabilité sportive du capital Mercato de l'Olympique Lyonnais (45 M€).", body_style))
    story.append(Spacer(1, 3))
    
    story.append(Paragraph("<b>4. Passage à l'Action : Le Démarrage du Codage (Étape 5)</b>", h2_style))
    story.append(Paragraph("Tous les voyants d'ingénierie, d'architecture, de planification et de financement étant formellement au vert, la phase de conception théorique est définitivement clôturée. Le cahier des charges opposable est validé. Le projet bascule à présent vers sa cinquième et dernière phase : l'exécution technique. L'Étape 5 abordera l'implémentation algorithmique réelle, la structuration de la base de données, la création des interfaces graphiques React, et la démonstration des cas d'usage de la plateforme Recruitment Match OL en conditions opérationnelles réelles.", body_style))
#     story.append(PageBreak())

    return story

def build_pages1_to_29():
    story_1_to_19 = build_pages1_to_19()
    story_1_to_29 = append_pages20_to_29(story_1_to_19)
    return story_1_to_29

if __name__ == "__main__":
    story = build_pages1_to_29()
    
    pdf_path = r"C:\Users\user\OneDrive\Documents\OURAD_RAYANE_PROJET.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        rightMargin=36,
        leftMargin=36,
        topMargin=70,
        bottomMargin=40
    )
    doc.build(story_complete, canvasmaker=NexaPurpleHeaderCanvas)
    print("PDF de 29 pages généré avec succès (Étape 1 à Étape 4 complètes) !")