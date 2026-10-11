# En PHP: class DataExtractor { ... }
# En Python:
class DataExtractor:
    # Le Constructeur (équivalent de __construct en PHP ou constructor en JS)
    def __init__(self, source_name: str):
        self.source = source_name  # Attribut d'instance (équivalent de $this->source)
        self.total_processed = 0  # Compteur initialisé par défaut

    # Une Méthode de la classe
    def log_status(self):
        # /!\ 'self' est obligatoire en argument de chaque méthode pour accéder aux attributs
        print(
            f"[STATUS] Source : {self.source} | Lignes traitées : {self.total_processed}"
        )

    def extraire(self, faux_volume: int):
        print(f"Extraction de {faux_volume} lignes depuis {self.source}...")
        self.total_processed += faux_volume


# --- UTILISATION (Instanciation) ---
# Pas de mot-clé 'new' en Python ! On appelle directement la classe comme une fonction.
extracteur_mysql = DataExtractor("MySQL_Stock")

# Accès aux attributs et méthodes
extracteur_mysql.extraire(14)
extracteur_mysql.log_status()
# Sortie : [STATUS] Source : MySQL_Stock | Lignes traitées : 14
