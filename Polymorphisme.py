# 1. Importation des classes spécifiques depuis le fichier Heritage.py
from Heritage import MongoConnector, MySQLConnector

# --- 3. L'ORCHESTRATEUR DE PIPELINE ---
if __name__ == "__main__":
    # Instanciation de nos connecteurs spécifiques
    sql_source = MySQLConnector(host="127.0.0.1", database="stock_api")
    nosql_source = MongoConnector(
        host="mongodb+srv://cluster0", collection_name="projects"
    )

    # Liste de nos sources de données (Polymorphisme)
    sources_pipeline = [sql_source, nosql_source]

    print("=== DÉMARRAGE DU PIPELINE GLOBAL ===\n")

    for source in sources_pipeline:
        # 1. On appelle .connect() (Polymorphisme)
        source.connect()

        # 2. On effectue l'extraction selon la nature du connecteur
        if isinstance(source, MySQLConnector):
            donnees = source.fetch_data("product")
        elif isinstance(source, MongoConnector):
            donnees = source.extract_json()

        # 3. On appelle la méthode commune héritée du parent
        source.disconnect()

    print("=== PIPELINE TERMINÉ AVEC SUCCÈS ===")
