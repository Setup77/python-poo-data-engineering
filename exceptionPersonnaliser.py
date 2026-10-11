# Déclaration de notre exception métier
class EmptyDataSourceException(Exception):
    """Levée lorsque la source de données ne renvoie aucune ligne."""

    def __init__(
        self, source_name: str, message: str = "La source de données est vide."
    ):
        self.source_name = source_name
        self.message = f"[DATA QUALITY] Alerte sur '{source_name}' : {message}"
        super().__init__(self.message)


def verifier_donnees(lots_de_donnees: list, nom_source: str):
    if len(lots_de_donnees) == 0:
        # On déclenche l'erreur
        raise EmptyDataSourceException(source_name=nom_source)
    print(f"Validation réussie : {len(lots_de_donnees)} lignes prêtes.")


donnees_recues = []  # Simulation d'un fichier vide extrait

try:
    print("[ETL] Étape de vérification de la qualité des données...")
    verifier_donnees(donnees_recues, nom_source="Extraction_MongoDB")

except EmptyDataSourceException as e:
    # On intercepte notre erreur personnalisée
    print(f"[ALERTE MONITORING] {e}")
    # En production, on enverrait ici une notification Slack ou un email à l'équipe Data

except Exception as e:
    # Intercepte toutes les autres erreurs imprévues
    print(f"[CRITICAL] Erreur inconnue : {e}")

else:
    # S'exécute uniquement si tout est OK
    print("[ETL] Étape suivante : Lancement de la transformation des données...")

finally:
    # S'exécute TOUJOURS
    print("[ETL] Nettoyage de la mémoire et fermeture des descripteurs de fichiers.")
