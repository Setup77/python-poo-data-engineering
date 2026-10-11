import os


# --- 1. LA CLASSE PARENTE (Générique) ---
class BaseConnector:
    def __init__(self, name: str, host: str):
        self.name = name
        self.host = host
        self.is_connected = False

    def disconnect(self):
        """Méthode commune à tous les connecteurs."""
        if self.is_connected:
            self.is_connected = False
            print(f"[CONNECTOR] Déconnexion réussie de la source : {self.name}\n")


# --- 2. LES CLASSES ENFANTS (Spécifiques) ---


class MySQLConnector(BaseConnector):
    def __init__(self, host: str, database: str):
        # On appelle le constructeur parent en lui passant un nom fixe et le host
        super().__init__(name="MySQL_Relationnel", host=host)
        self.database = database  # Attribut spécifique à MySQL

    def connect(self):
        """Surcharge / Implémentation spécifique pour MySQL."""
        print(f"[MYSQL] Connexion à la base '{self.database}' sur {self.host}...")
        self.is_connected = True

    def fetch_data(self, table: str) -> list:
        """Méthode spécifique d'extraction SQL."""
        if self.is_connected:
            print(f"[MYSQL] Exécution : SELECT * FROM {table};")
            # Simulation de retour de données propres (vos produits par exemple)
            return [{"id": 1, "name": "Simulation Produit"}]
        return []


class MongoConnector(BaseConnector):
    def __init__(self, host: str, collection_name: str):
        super().__init__(name="MongoDB_NoSQL", host=host)
        self.collection_name = collection_name

    def connect(self):
        """Surcharge / Implémentation spécifique pour MongoDB."""
        print(f"[MONGO] Connexion au cluster {self.host}...")
        print(f"[MONGO] Sélection de la collection : {self.collection_name}")
        self.is_connected = True

    def extract_json(self) -> list:
        """Méthode spécifique d'extraction NoSQL BSON/JSON."""
        if self.is_connected:
            print(f"[MONGO] Exécution du pipeline d'agrégation...")
            return [{"_id": {"$oid": "12345"}, "title": "Simulation Projet"}]
        return []
