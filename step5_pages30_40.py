from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors

# Import du générateur des 29 premières pages + du header canvas personnalisé
from step4_pages20_29 import build_pages1_to_29
from step1_pages1_2 import NexaPurpleHeaderCanvas

def append_pages30_to_40(story):
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

    # PAGE 30 : INITIALISATION ET DEVOPS
    story.append(Paragraph("ÉTAPE 5 — DÉVELOPPEMENT ACTIF ET RÉALISATION TECHNIQUE", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))
    
    story.append(Paragraph("<b>1. Transition Stratégique : De la Conception à l'Implémentation</b>", h2_style))
    story.append(Paragraph("La validation exhaustive du cahier des charges et de l'architecture UML marque la fin des phases préparatoires. L'Étape 5 initie concrètement le cycle de développement (Sprint 1). Cette phase d'exécution repose sur la traduction des spécifications théoriques en lignes de code exécutables. L'objectif premier est de construire un produit robuste, sécurisé et performant, capable de s'interfacer sans friction avec les processus métiers de la cellule de recrutement de l'Olympique Lyonnais. L'intégration continue et la rigueur algorithmique seront les maîtres mots de cette phase de réalisation.", body_style))

    story.append(Paragraph("<b>2. Configuration de l'Environnement de Développement</b>", h2_style))
    story.append(Paragraph("Le démarrage du codage exige la mise en place préalable d'un environnement de travail standardisé et déterministe. Le projet s'articule autour d'un dépôt centralisé Git, hébergé sur une forge logicielle sécurisée (GitHub/GitLab). Ce dépôt adopte la méthodologie GitFlow, séparant strictement la branche de production (main), l'environnement de recette (develop) et les branches de fonctionnalités (feature). Cette isolation garantit que chaque nouveau développement lié à l'algorithme k-NN ou à l'interface React est isolé et n'altère en aucun cas la stabilité du socle principal en cours d'audit.", body_style))

    story.append(Paragraph("<b>3. Pipeline CI/CD et Assurance Qualité Continue</b>", h2_style))
    story.append(Paragraph("Afin d'automatiser les contrôles d'intégrité, un pipeline CI/CD (Continuous Integration / Continuous Deployment) a été greffé sur le dépôt source. À chaque soumission de code (commit), des workflows automatisés se déclenchent (via GitHub Actions). Ils exécutent systématiquement les linters de code (Flake8 pour Python, ESLint pour JavaScript) pour garantir le respect des normes syntaxiques industrielles. Ensuite, la suite de tests unitaires est lancée à blanc. Tout échec bloque immédiatement la fusion du code (Merge Request), assurant que seules les briques logicielles 100 % saines sont intégrées à la branche principale.", body_style))

    story.append(Paragraph("<b>4. Conteneurisation des Services (Docker)</b>", h2_style))
    story.append(Paragraph("Pour pallier le syndrome du 'ça marche sur ma machine', la plateforme Recruitment Match OL est intégralement conteneurisée via Docker. Un fichier <i>docker-compose.yml</i> orchestre le montage simultané du back-end FastAPI, du modèle de Machine Learning et du serveur de développement React Vite. Cette virtualisation légère permet aux directeurs sportifs ou aux testeurs fonctionnels de cloner le dépôt et de lancer l'intégralité du simulateur de recrutement en une seule commande terminal, garantissant une reproductibilité totale des calculs de similarité d'un environnement à l'autre.", body_style))
#     story.append(PageBreak())

    # PAGE 31 : BACK-END FASTAPI & SECURITE
    story.append(Paragraph("DÉVELOPPEMENT DU MOTEUR BACK-END (FASTAPI)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Instanciation du Serveur ASGI FastAPI</b>", h2_style))
    story.append(Paragraph("Le développement logiciel débute logiquement par l'ossature back-end, pilier central de l'application. Le choix s'est porté sur FastAPI, un framework Python moderne, rapide (haute performance) et basé sur les annotations de type (Type Hints). L'instanciation de l'objet <i>FastAPI()</i> s'accompagne d'une configuration stricte des middlewares. L'application est servie par Uvicorn, un serveur ASGI ultra-léger capable de traiter des requêtes asynchrones en parallèle. Cette conception garantit que le serveur ne s'engorge jamais, même si plusieurs recruteurs lancent simultanément des calculs algorithmiques lourds de recherche de jumeaux.", body_style))

    story.append(Paragraph("<b>2. Gestion Sécurisée des Cross-Origin (CORS)</b>", h2_style))
    story.append(Paragraph("Étant donné la nature Headless de l'architecture, où le front-end React et le back-end FastAPI sont hébergés sur des domaines ou des ports distincts, la barrière de sécurité CORS (Cross-Origin Resource Sharing) des navigateurs bloque nativement les communications. Un middleware <i>CORSMiddleware</i> est donc injecté dès l'amorçage de l'API. Il est configuré pour n'autoriser les requêtes entrantes que depuis l'origine spécifique du serveur React de l'OL. Cette restriction drastique prévient toute attaque de type CSRF (Cross-Site Request Forgery) provenant de scripts malveillants tiers tentant d'exploiter la base de données des joueurs.", body_style))

    story.append(Paragraph("<b>3. Implémentation du Bouclier Sécuritaire (Authentification JWT)</b>", h2_style))
    story.append(Paragraph("Les données statistiques Opta traitées par l'application étant hautement confidentielles et stratégiques, la route d'authentification a été développée avec une rigueur militaire. L'implémentation repose sur le standard OAuth2 avec émission de jetons JWT (JSON Web Tokens). Lorsqu'un recruteur valide ses identifiants hachés cryptographiquement via <i>bcrypt</i>, le serveur génère un jeton signé numériquement par une clé secrète (HS256). Ce jeton a une durée de vie limitée (expiration au bout de quelques heures) et doit être attaché à l'en-tête (Header Authorization) de chaque requête API ultérieure.", body_style))

    story.append(Paragraph("<b>4. Mécanisme de Validation et Dépendances Injectées</b>", h2_style))
    story.append(Paragraph("La force de FastAPI réside dans son système d'injection de dépendances. Une fonction <i>get_current_user</i> a été développée et attachée à toutes les routes API critiques en tant que dépendance obligatoire. À chaque appel (ex: recherche d'un joueur), cette fonction intercepte la requête, décode le jeton JWT, vérifie sa signature et valide les privilèges de l'utilisateur. Si le jeton est invalide ou expiré, une exception HTTP 401 (Unauthorized) est immédiatement levée et le calcul algorithmique est avorté avant même de solliciter les ressources du processeur serveur.", body_style))
#     story.append(PageBreak())

    # PAGE 32 : ENDPOINTS & GESTION DES DONNÉES
    story.append(Paragraph("INGÉNIERIE DES ENDPOINTS ET DU MODÈLE DE DONNÉES", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Modélisation de la Base de Données (SQLite & SQLAlchemy)</b>", h2_style))
    story.append(Paragraph("Le stockage persistant des 2 854 profils de joueurs issus des championnats européens majeurs requiert une fondation solide. La base de données SQLite a été choisie pour sa légèreté, sa vélocité de lecture et son caractère <i>Serverless</i> (pas de processus d'arrière-plan). L'interaction avec cette base n'est pas codée en requêtes SQL brutes (sujettes aux failles d'injection), mais abstraite via l'ORM SQLAlchemy. Les tables <i>Users</i> et <i>Players</i> sont modélisées sous forme de classes Python. L'ORM se charge de convertir de manière transparente et sécurisée les objets Python en requêtes SQL optimisées pour la lecture matricielle.", body_style))

    story.append(Paragraph("<b>2. Développement de l'Endpoint de Recherche Textuelle</b>", h2_style))
    story.append(Paragraph("La première interaction métier du recruteur consiste à retrouver un joueur cible (ex: 'Rayan Cherki') pour initier la simulation. Un endpoint REST `GET /players/search` a été conçu spécifiquement à cet effet. Il expose un paramètre de requête (<i>Query Parameter</i>) permettant de filtrer dynamiquement le catalogue. Cet endpoint utilise une requête SQL `ILIKE` via SQLAlchemy pour trouver les correspondances partielles et insensibles à la casse. Il retourne une liste limitée (pagination) d'objets JSON contenant les ID, noms et équipes des joueurs trouvés, optimisant ainsi la consommation de bande passante réseau.", body_style))

    story.append(Paragraph("<b>3. Schémas de Validation avec Pydantic</b>", h2_style))
    story.append(Paragraph("La transmission des données entre le client React et le serveur FastAPI est strictement typée et contrôlée. Cette prouesse est accomplie grâce à la librairie Pydantic intégrée nativement dans FastAPI. Les modèles de données (ex: <i>PlayerOut</i>, <i>Token</i>) héritent de <i>BaseModel</i>. Ils forcent la conversion et la validation des types (chaînes de caractères, nombres flottants, entiers). Si un champ manquant ou un type erroné est détecté dans la requête entrante ou la réponse sortante, Pydantic bloque l'opération et génère instantanément un message d'erreur détaillé au format JSON (HTTP 422 Unprocessable Entity).", body_style))

    story.append(Paragraph("<b>4. Construction du Contrôleur Principal de Simulation</b>", h2_style))
    story.append(Paragraph("Le cœur du réacteur est l'endpoint `POST /simulate/twins`. Contrairement à une simple lecture en base, cette route agit comme un <i>Controller</i> qui orchestre un pipeline d'opérations lourdes. À la réception de l'ID du joueur ciblé et des poids d'importance (pondération des statistiques défensives, offensives, de distribution), le contrôleur interroge d'abord la base SQLite pour extraire la ligne statistique exacte du joueur de référence. Une fois cette extraction validée, les données et les filtres sont instanciés en objets Pydantic et injectés directement dans le moteur de Machine Learning (k-NN) pour lancer l'algorithme prédictif de similarité mathématique.", body_style))
#     story.append(PageBreak())

    # PAGE 33 : DATA SCIENCE ET MACHINE LEARNING
    story.append(Paragraph("DATA SCIENCE : INGÉNIERIE DES DONNÉES ET PIPELINE K-NN", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Isolement du Moteur d'Intelligence Artificielle</b>", h2_style))
    story.append(Paragraph("La puissance du simulateur Recruitment Match réside dans son intelligence algorithmique. Conformément aux principes de l'architecture logicielle propre (<i>Clean Architecture</i>), le module de Data Science est totalement encapsulé dans une classe dédiée (<i>ML_Engine</i>). Ce module n'a aucune connaissance du réseau HTTP (FastAPI) ou de la base de données SQL. Il n'accepte que des DataFrames Pandas (tableaux de données) purs en entrée. Cet isolement chirurgical permet aux Data Scientists de l'OL de faire évoluer, ré-entraîner ou modifier l'algorithme sans jamais risquer de casser l'infrastructure web globale du projet.", body_style))

    story.append(Paragraph("<b>2. Chargement et Préparation Matricielle (Pandas)</b>", h2_style))
    story.append(Paragraph("À l'initialisation du moteur ML, la base de données complète des 2 854 joueurs est chargée intégralement dans la mémoire vive (RAM) du serveur sous forme de DataFrame Pandas. Cette approche <i>In-Memory</i> est indispensable pour garantir des calculs mathématiques quasi-instantanés. Pandas excelle dans la manipulation vectorisée. Les colonnes inutiles (noms, équipes, ligues) sont temporairement détachées pour ne conserver qu'une matrice purement numérique (buts, passes, tacles, dribbles). C'est cet espace dimensionnel brut qui servira de terrain de calcul géométrique pour l'algorithme de détection des profils jumeaux.", body_style))

    story.append(Paragraph("<b>3. Normalisation Statistique (Z-Score & Min-Max Scaler)</b>", h2_style))
    story.append(Paragraph("Un défi mathématique majeur se pose lors de l'analyse des statistiques footballistiques : l'écrasement des échelles. Un joueur effectue en moyenne 50 passes par match, mais ne marque que 0.3 but. Si l'on calcule une distance brute, l'écart sur le nombre de passes va masquer totalement l'importance capitale du nombre de buts. Le moteur d'intelligence pallie ce défaut via une normalisation des données (<i>StandardScaler</i> de scikit-learn). Chaque variable statistique est centrée autour d'une moyenne de zéro et réduite à un écart-type unitaire, garantissant que chaque attribut (du tacle à la passe décisive) possède exactement le même poids mathématique brut.", body_style))

    story.append(Paragraph("<b>4. Application Dynamique de la Pondération Métier</b>", h2_style))
    story.append(Paragraph("L'expertise humaine du recruteur est réinjectée dans le modèle sous forme de pondération mathématique. Avant de lancer le calcul géométrique final, la matrice de données normalisées subit une multiplication scalaire par les poids fournis par le client React (ex: x3 pour la finition, x0.5 pour le jeu aérien). Cette opération déforme l'espace dimensionnel algorithmique. Elle allonge virtuellement les axes des statistiques jugées primordiales par la Direction Sportive, forçant ainsi l'algorithme à chercher des joueurs qui se ressemblent de manière hyper-spécifique sur ces critères précis, plutôt que des clones statistiquement parfaits mais déconnectés de la consigne tactique ciblée.", body_style))
#     story.append(PageBreak())

    # PAGE 34 : CALCUL DES DISTANCES EUCLIDIENNES
    story.append(Paragraph("ALGORITHMIQUE : CALCUL DES DISTANCES SPATIALES", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Fondements Géométriques de l'Algorithme k-NN</b>", h2_style))
    story.append(Paragraph("L'algorithme de recommandation retenu est le k-Nearest Neighbors (k-NN, ou algorithme des k plus proches voisins). Dans le contexte de la Data Science sportive, chaque joueur de la base de données est modélisé comme un point unique perdu dans un hyper-espace mathématique à 36 dimensions (correspondant aux 36 statistiques Opta analysées). L'objectif absolu de l'algorithme est de localiser le point représentant le joueur cible (ex: 'Maxence Caqueret'), puis de scanner tout l'hyper-espace pour identifier mathématiquement les 'k' points (joueurs) qui gravitent le plus près de cette coordonnée de référence centrale.", body_style))

    story.append(Paragraph("<b>2. Calcul Vectorisé de la Distance Euclidienne (SciPy)</b>", h2_style))
    story.append(Paragraph("Pour mesurer la 'proximité' entre deux joueurs, le moteur ML utilise le théorème mathématique de la distance euclidienne (calculée grâce à la librairie scientifique de pointe <i>SciPy</i>). La distance (D) entre le point de référence (A) et un joueur candidat (B) correspond à la racine carrée de la somme des écarts au carré sur chaque dimension statistique. Plus cette distance globale D est proche de 0, plus la similarité entre les deux profils footballistiques est parfaite. L'utilisation des fonctions spatiales optimisées en langage C (via <i>scipy.spatial.distance.cdist</i>) permet de croiser le joueur ciblé avec les 2 854 candidats en une fraction de milliseconde.", body_style))

    story.append(Paragraph("<b>3. Tri, Sélection et Reconstruction du Résultat</b>", h2_style))
    story.append(Paragraph("Une fois le vecteur des 2 854 distances mathématiques généré par SciPy, le moteur ML procède à un tri croissant (via <i>numpy.argsort</i>). Le profil de référence lui-même (distance = 0) est écarté, puis l'algorithme capture chirurgicalement les 5 ou 10 index possédant les distances les plus faibles. Ces index sont ensuite utilisés pour ré-interroger le DataFrame initial non-normalisé. Cette étape de rétro-ingénierie permet de récupérer les vrais noms, les équipes, et les statistiques brutes (buts réels, passes réelles) des jumeaux identifiés, rendant le résultat final directement interprétable par un humain.", body_style))

    story.append(Paragraph("<b>4. Renvoi du Payload JSON à l'API FastAPI</b>", h2_style))
    story.append(Paragraph("La classe ML_Engine finalise son exécution en encapsulant les résultats des joueurs jumeaux dans un tableau de dictionnaires Python. Ce tableau est renvoyé au contrôleur FastAPI qui l'attendait de manière asynchrone. L'ORM et Pydantic prennent alors le relais pour parser ces dictionnaires de données brutes, s'assurer que les pourcentages de similarité calculés (convertis sur une échelle de 0 à 100%) sont valides, et expédier un Payload JSON formellement structuré à travers le réseau Internet en direction du navigateur du recruteur. L'intelligence serveur a terminé son travail.", body_style))
#     story.append(PageBreak())

    # PAGE 35 : FRONT-END REACT & ARCHITECTURE
    story.append(Paragraph("DÉVELOPPEMENT DE L'INTERFACE UTILISATEUR (REACT)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Initialisation du Projet Client avec Vite.js</b>", h2_style))
    story.append(Paragraph("Le développement de la couche visuelle (Front-end) démarre par la structuration de l'application cliente. Le traditionnel <i>Create React App</i>, jugé trop lourd et obsolète en matière de performance de build, a été écarté au profit exclusif de <i>Vite.js</i>. Cet outil de construction moderne (Bundler), développé en langage Go, s'appuie sur le support natif des modules ES du navigateur (ESM). Il offre une expérience de développement fulgurante avec un <i>Hot Module Replacement</i> (HMR) quasi-instantané, permettant aux intégrateurs UI d'observer en temps réel les ajustements de design sur les composants sans aucun rechargement complet de la page.", body_style))

    story.append(Paragraph("<b>2. Architecture Atomique des Composants (Component-Driven)</b>", h2_style))
    story.append(Paragraph("Le code source React est organisé selon les préceptes de l'<i>Atomic Design</i>, promouvant une granularité extrêmement fine et une réutilisabilité maximale du code. L'interface globale de la plateforme de scouting n'est pas codée d'un seul bloc monolithique, mais segmentée en micro-composants encapsulés. Des atomes basiques (boutons, inputs de texte, badges) sont assemblés pour former des molécules (barres de recherche, curseurs de pondération), qui elles-mêmes constituent des organismes complexes autonomes (la grille de résultats, le panneau d'authentification). Cette architecture permet une maintenance aisée et réduit drastiquement les collisions de code entre développeurs.", body_style))

    story.append(Paragraph("<b>3. Routage Dynamique Côté Client (React Router)</b>", h2_style))
    story.append(Paragraph("Bien que l'application soit conçue comme une SPA (Single Page Application) ultra-rapide, une navigation logique demeure indispensable pour structurer l'expérience utilisateur. La librairie <i>React Router DOM</i> orchestre virtuellement les changements d'URLs dans le navigateur du recruteur sans jamais interroger le serveur Web pour de nouvelles pages HTML. Le routage défini isole la page de Login <i>/login</i> du Dashboard privé <i>/dashboard</i>. Des gardiens de routes (<i>Private Routes</i>) interceptent instantanément la navigation : si le JWT de session est absent de la mémoire, l'utilisateur est violemment redirigé vers l'écran de connexion, sécurisant ainsi la logique applicative cliente.", body_style))

    story.append(Paragraph("<b>4. Communication Asynchrone avec l'API (Fetch & Axios)</b>", h2_style))
    story.append(Paragraph("La passerelle de communication entre les composants React et le cerveau FastAPI est assurée par un service réseau dédié, exploitant l'API <i>Fetch</i> ou la surcouche <i>Axios</i>. Toutes les requêtes HTTP (recherche, simulation) sont exécutées de manière asynchrone (Promises). L'architecture réseau côté client est centralisée (<i>apiService.js</i>) afin d'intercepter globalement les requêtes pour y injecter automatiquement le token JWT d'authentification dans les Headers. De même, ce service central capture les codes d'erreurs (401, 500) pour déclencher l'affichage instantané de notifications (Toasts) à destination de l'utilisateur en cas de défaillance réseau.", body_style))
#     story.append(PageBreak())

    # PAGE 36 : STATE MANAGEMENT ET PERFORMANCE
    story.append(Paragraph("GESTION DES ÉTATS ET OPTIMISATION DE PERFORMANCE REACT", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Cadrage du State Management (React Context API)</b>", h2_style))
    story.append(Paragraph("L'une des complexités majeures d'une SPA réactive est la circulation de la donnée entre des composants profondément imbriqués. Plutôt que de subir l'enfer du <i>Props Drilling</i> (passage manuel des variables d'un composant parent à ses petits-enfants) ou de déployer l'artillerie lourde d'un store Redux, l'équipe d'ingénierie a judicieusement exploité l'API native <i>React Context</i>. Deux contextes globaux ont été instanciés : l'un gère le statut d'authentification sécurisé et l'identité du recruteur connecté, l'autre centralise l'état global de la simulation algorithmique (joueur de référence, pondérations activées, liste des profils jumeaux trouvés).", body_style))

    story.append(Paragraph("<b>2. Programmation Réactive via les Hooks Fonctionnels</b>", h2_style))
    story.append(Paragraph("Le cycle de vie et la réactivité des composants s'appuient exclusivement sur les Hooks fonctionnels introduits dans les versions modernes de React. Le <i>useState</i> capture la donnée volatile (ce que tape le recruteur dans la barre de recherche). Le <i>useEffect</i> orchestre les effets de bord asynchrones : il déclenche le ping réseau vers l'API FastAPI uniquement lorsque des paramètres précis (les <i>dependencies array</i>) sont altérés. Cette approche mathématique de la réactivité garantit que l'interface graphique reste parfaitement synchronisée avec le moteur d'intelligence serveur, sans provoquer de re-rendus inutiles (<i>renders</i>) fatals pour le processeur local.", body_style))

    story.append(Paragraph("<b>3. Maîtrise de l'API Search (Debouncing Technic)</b>", h2_style))
    story.append(Paragraph("Un problème d'optimisation majeur se produit lors de l'utilisation de la barre de recherche textuelle dynamique : si un recruteur tape 'Lacazette', 9 frappes clavier successives risqueraient de lancer 9 requêtes HTTP immédiates, inondant inutilement le serveur API. Une fonction utilitaire de <i>Debouncing</i> (temporisation) a été intégrée au hook de saisie. Elle impose un délai de rétention de 300 millisecondes après la dernière frappe avant de déclencher l'appel réseau vers SQLite. Cette micro-optimisation invisible pour l'œil humain divise par dix la charge de la base de données et préserve le temps de réponse magistral du système.", body_style))

    story.append(Paragraph("<b>4. Gestion Visuelle de l'Attente (Skeletons & Spinners)</b>", h2_style))
    story.append(Paragraph("L'expérience utilisateur (UX) ne se résume pas à la vitesse, mais à la perception de la vitesse. Lors du déclenchement du lourd algorithme de similarité k-NN, un délai inévitable de traitement (calcul des distances sur 2854 profils) s'applique. Plutôt que de figer l'interface dans un mutisme anxiogène, le composant parent déclenche immédiatement un état booléen <i>isLoading = true</i>. React détruit temporairement la grille de résultats pour afficher des <i>Skeleton Loaders</i> (formes grises animées pulsant au rythme du calcul). Dès réception du JSON final, l'état bascule, déclenchant l'apparition gracieuse des cartes des profils jumeaux.", body_style))
#     story.append(PageBreak())

    # PAGE 37 : TAILWINDCSS & STYLING
    story.append(Paragraph("STYLISATION AVANCÉE ET DESIGN SYSTEM (TAILWINDCSS)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. Rupture de Paradigme : L'Utilitaire CSS (Tailwind)</b>", h2_style))
    story.append(Paragraph("L'habillage graphique de la plateforme Recruitment Match OL abandonne radicalement l'approche sémantique classique (fichiers BEM .css) au profit du framework utilitaire <i>TailwindCSS</i>. Ce changement de paradigme architectural permet aux intégrateurs front-end de styliser l'application en injectant directement des classes atomiques ultra-spécifiques (ex: <i>flex, justify-center, text-ol-blue</i>) directement dans le code JSX (React). Cette fusion étroite entre le HTML et le CSS accélère massivement la vitesse de développement des composants visuels tout en éradiquant le problème du code CSS mort et des conflits de nommage au sein des gros projets.", body_style))

    story.append(Paragraph("<b>2. Intégration Rigoureuse de la Charte Graphique OL</b>", h2_style))
    story.append(Paragraph("L'excellence esthétique d'un logiciel interne forge la confiance de l'utilisateur final. Le fichier de configuration racine <i>tailwind.config.js</i> a été étendu pour absorber l'intégralité du Design System officiel de l'Olympique Lyonnais. Le rouge institutionnel (Hex: #D31115) et le bleu profond (Hex: #0B2C5C) ont été enregistrés comme variables natives. De même, les polices de caractères officielles sans-serif ont été forcées par défaut. Cette surcouche garantit une homogénéité absolue de la plateforme avec l'écosystème numérique corporate d'Eagle Football, offrant une interface premium et rassurante aux yeux du Directeur Sportif.", body_style))

    story.append(Paragraph("<b>3. Responsive Design au Cœur de l'Interface</b>", h2_style))
    story.append(Paragraph("Bien que le simulateur algorithmique soit principalement destiné à être manipulé sur les grands écrans de la salle d'analyse vidéo du centre d'entraînement, le développement intègre nativement la fluidité adaptative (Responsive Design). Tailwind permet l'utilisation de préfixes d'écrans (<i>md:, lg:, xl:</i>) pour moduler l'affichage en cascade. Ainsi, la matrice de présentation affichant 3 profils jumeaux côte-à-côte sur un ordinateur de bureau basculera intelligemment sur une pile verticale élégante si l'application est consultée en urgence depuis la tablette ou le smartphone d'un recruteur en plein déplacement lors d'un match de ligue.", body_style))

    story.append(Paragraph("<b>4. Interactions et Micro-Animations Numériques</b>", h2_style))
    story.append(Paragraph("La fluidité perçue du logiciel s'appuie grandement sur l'intégration chirurgicale de micro-animations. Les classes utilitaires de transition (<i>transition-all, duration-300, ease-in-out</i>) ont été greffées sur tous les boutons interactifs, les cartes de profils de joueurs et les barres de pondération tactique. Au survol d'une souris (Hover), l'élément ciblé s'élève légèrement avec l'ajout dynamique d'une ombre portée douce (<i>shadow-lg, -translate-y-1</i>). Ces détails subtils, qui ne sollicitent que l'accélération matérielle du navigateur, enrichissent considérablement le feeling premium de l'outil et encouragent l'interaction de l'utilisateur.", body_style))
#     story.append(PageBreak())

    # PAGE 38 : DATA VISUALIZATION
    story.append(Paragraph("DATA VISUALIZATION ET GÉNÉRATION DE GRAPHIQUES (RECHARTS)", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. L'Enjeu de la Représentation Visuelle des Statistiques</b>", h2_style))
    story.append(Paragraph("L'analyse visuelle prime sur la lecture de longs tableaux mathématiques pour des décisionnaires pressés. Une fois que l'algorithme k-NN a localisé mathématiquement les profils jumeaux, le rôle du Front-end n'est pas de vomir un fichier Excel brut, mais de traduire ces données brutes en une représentation visuelle percutante. Le choix technologique s'est arrêté sur <i>Recharts</i>, une puissante librairie React basée sur D3.js. Elle excelle dans la génération d'éléments graphiques SVG scalaires de haute fidélité, parfaitement interpolables et directement paramétrables via les <i>Props</i> des composants React.", body_style))

    story.append(Paragraph("<b>2. Conception du Graphique Radar Multidimensionnel</b>", h2_style))
    story.append(Paragraph("Le graphique en toile d'araignée (Radar Chart) s'impose comme l'étalon-or dans l'écosystème du football moderne (football manager, outils d'analytics) pour représenter l'empreinte globale d'un joueur. Un composant React <i>StatsRadar</i> a été développé sur-mesure. Il projette les scores normalisés du joueur (défense, attaque, distribution, possession) sur des axes polygonaux équidistants. Les aires générées sont remplies avec des variations opalescentes du rouge et du bleu OL (<i>fillOpacity=0.5</i>). La surface visuelle globale indique en un instant l'empreinte technique et la polyvalence absolue du profil analysé.", body_style))

    story.append(Paragraph("<b>3. Superposition Graphique pour Comparaison Relative</b>", h2_style))
    story.append(Paragraph("La force du composant <i>StatsRadar</i> réside dans sa capacité de superposition multimodale. Lorsque le recruteur analyse un profil jumeau, le graphique trace le polygone du joueur découvert en rouge OL. Mais de manière simultanée, il dessine, en arrière-plan transparent (gris léger), le polygone géométrique du joueur de référence initialement ciblé par le simulateur. Cette superposition visuelle magistrale permet à l'œil humain de déceler instantanément les légers déficits ou excédents statistiques (ex: volume défensif supérieur) entre la demande théorique et la trouvaille algorithmique, accélérant massivement la prise de décision analytique.", body_style))

    story.append(Paragraph("<b>4. Interactivité et Infobulles Dynamiques (Tooltips)</b>", h2_style))
    story.append(Paragraph("La conception de la Data Visualization ne s'arrête pas au simple dessin vectoriel statique. Les graphiques Recharts intègrent une couche d'interactivité riche. Au survol du curseur sur un sommet spécifique du Radar (ex: le sommet 'Passes Réussies'), une infobulle (Tooltip) stylisée via TailwindCSS apparaît instantanément pour révéler la valeur numérique exacte de la statistique calculée, échappant ainsi à l'imprécision visuelle inhérente aux toiles d'araignée. Cette dualité – vision globale via la surface du polygone et précision absolue via le survol interactif – garantit une analyse chirurgicale, complète et sans ambiguïté.", body_style))
#     story.append(PageBreak())

    # PAGE 39 : TESTS & QA
    story.append(Paragraph("ASSURANCE QUALITÉ (QA) ET INGÉNIERIE DE TESTS", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. La Philosophie du Test-Driven Development (TDD)</b>", h2_style))
    story.append(Paragraph("Le développement d'un outil décisionnel engageant des dizaines de millions d'euros sur le marché des transferts ne tolère absolument aucune faille algorithmique ou comportementale. Afin de verrouiller la fiabilité du code, une stratégie d'Assurance Qualité (QA) stricte a été déployée dès les premières lignes de code, s'inspirant des principes du Test-Driven Development (Développement piloté par les tests). L'infrastructure logicielle complète (Front-end, API, Modèle ML) est couverte par une matrice de tests unitaires et d'intégration, garantissant qu'aucune mise à jour ultérieure (régression) ne viendra corrompre silencieusement les calculs ou la sécurité de la plateforme.", body_style))

    story.append(Paragraph("<b>2. Validation Back-end et Mathématique avec Pytest</b>", h2_style))
    story.append(Paragraph("Le socle Python (FastAPI et Intelligence Artificielle) est audité en permanence par le framework de test <i>Pytest</i>. Des bancs d'essais simulent de fausses requêtes d'authentification pour vérifier que le middleware JWT bloque impitoyablement les requêtes sans signature valide (code 401). Plus crucial encore, le moteur de Machine Learning (k-NN) subit des <i>Asserts</i> mathématiques automatisés : des données factices pré-calculées manuellement sont injectées dans la fonction de calcul euclidien (SciPy) pour vérifier au centième de décimale près que le moteur de production retourne invariablement les mêmes index géométriques. L'intelligence est ainsi sanctuarisée.", body_style))

    story.append(Paragraph("<b>3. Tests d'Interface et Composants React avec Jest & RTL</b>", h2_style))
    story.append(Paragraph("Le pendant visuel du projet, l'application React, est soumis aux tortures du framework d'exécution JavaScript <i>Jest</i> couplé à la librairie <i>React Testing Library</i> (RTL). L'approche RTL favorise le test comportemental, simulant les actions réelles du recruteur. Les tests s'assurent que la barre de recherche déclenche bien son appel réseau (<i>fetch mocké</i>) après le délai de debounce imparti. Ils vérifient que les Skeleton Loaders s'affichent correctement lors de l'attente du Payload API, et que la tentative d'accès à la route sécurisée du Dashboard sans token JWT dans le Context déclenche une redirection forcée et silencieuse.", body_style))

    story.append(Paragraph("<b>4. Profilage de la Performance Mémoire (Stress Test)</b>", h2_style))
    story.append(Paragraph("Une fois la justesse fonctionnelle verrouillée, le logiciel affronte la validation matérielle (Stress Testing). Des scripts de simulation (Locust ou Artillery) inondent massivement le serveur Uvicorn de centaines de requêtes algorithmiques lourdes par seconde pour auditer la consommation de la RAM du DataFrame Pandas. L'objectif est de vérifier l'absence totale de fuites de mémoire (<i>Memory Leaks</i>) lors de la vectorisation de la base de données. Les conclusions de ces crash-tests confirment l'élasticité et la résilience totale du serveur, capable de supporter sans sourciller la charge effrénée des recruteurs lors du dernier jour (Deadline Day) du Mercato.", body_style))
#     story.append(PageBreak())

    # PAGE 40 : RECETTE FINALE & DEPLOIEMENT
    story.append(Paragraph("RECETTE MÉTIER FINALE, MISE EN PRODUCTION ET CONCLUSION", h1_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=c_purple, spaceAfter=8))

    story.append(Paragraph("<b>1. La Démonstration du Sprint Final (Sprint Review)</b>", h2_style))
    story.append(Paragraph("L'aboutissement des quatre semaines du dernier Sprint de développement est marqué par l'ultime cérémonie Scrum : la Sprint Review finale. Dans la salle du conseil du Groupama Stadium, le logiciel fonctionnel Recruitment Match est dévoilé en conditions réelles d'utilisation devant la Direction Sportive (Vincent et ses recruteurs en chef). L'application est soumise à des scénarios de simulation à haute complexité, exigeant de trouver la doublure technique parfaite d'un milieu de terrain sous la contrainte d'un budget étriqué. La plateforme exécute la fouille des 2 854 profils, calcule l'hyper-espace k-NN et affiche instantanément les Radars graphiques des jumeaux trouvés, validant magistralement le concept.", body_style))

    story.append(Paragraph("<b>2. Recette Fonctionnelle et Feedback Utilisateur Avancé</b>", h2_style))
    story.append(Paragraph("Cette démonstration déclenche l'ouverture de la phase de recette fonctionnelle (UAT - User Acceptance Testing). Durant cette fenêtre décisive, les recruteurs de l'Olympique Lyonnais prennent personnellement les commandes du simulateur sur leurs ordinateurs portables. L'ergonomie intuitive de l'interface React, couplée à la vitesse d'exécution époustouflante du serveur Python, suscite l'adhésion immédiate des utilisateurs finaux. Les retours confirment que la granularité des sliders de pondération tactique offre une finesse d'analyse inédite, bouleversant fondamentalement leur approche traditionnelle du sourcing vidéo en introduisant la rationalité mathématique absolue.", body_style))

    story.append(Paragraph("<b>3. Signature du Procès-Verbal de Recette et Déploiement</b>", h2_style))
    story.append(Paragraph("L'absence totale de bugs majeurs (Critères d'Acceptation atteints) autorise la signature officielle du PV de recette par la Direction. Le projet bascule du statut de développement à la Mise En Production (MEP). Les images Docker contenant le front-end optimisé (fichiers JavaScript minifiés) et l'API Python sont déployées sur le serveur d'hébergement sécurisé (Cloud privé ou VPS). Le routage DNS est configuré et les certificats SSL de cryptage sont activés. La plateforme Recruitment Match OL est désormais officiellement en ligne, hautement sécurisée, et accessible en continu pour préparer le Mercato estival d'Eagle Football.", body_style))

    story.append(Paragraph("<b>4. Conclusion de l'Étape 5 et Transition Vers le Bilan</b>", h2_style))
    story.append(Paragraph("L'Étape 5 s'achève sur un succès technologique et méthodologique total. De l'initialisation asynchrone du backend FastAPI à la sublimation visuelle du frontend React via Tailwind et Recharts, l'architecture globale a prouvé son éclatante supériorité algorithmique. Le modèle k-NN, encapsulé dans un écosystème robuste, est prêt à dicter l'orientation du recrutement sportif avec une objectivité mathématique glaciale. Le chapitre final (Étape 6) sera désormais consacré à la rétrospective du projet : il en dressera le bilan critique formel, mesurera la rentabilité économique effective, et proposera des axes d'améliorations futurs pour pérenniser l'outil.", body_style))
#     story.append(PageBreak())

    return story

def build_pages1_to_40():
    story_1_to_29 = build_pages1_to_29()
    story_1_to_40 = append_pages30_to_40(story_1_to_29)
    return story_1_to_40

if __name__ == "__main__":
    story = build_pages1_to_40()
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
    print("PDF généré avec succès (Étape 1 à Étape 5 complètes) !")