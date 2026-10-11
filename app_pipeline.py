import json
import os
import re


# --- 1. GESTION DES EXCEPTIONS PERSONNALISÉES ---
class DataPipelineException(Exception):
    """Classe de base pour les exceptions du pipeline."""

    pass


class MissingFileException(DataPipelineException):
    """Levée lorsqu'un fichier source JSON obligatoire est absent."""

    def __init__(self, nom_fichier: str):
        super().__init__(
            f"[DATA QUALITY] Fichier source critique manquant : '{nom_fichier}'"
        )


# --- 2. ARCHITECTURE DES CONNECTEURS (HERITAGE & ENCAPSULATION) ---
class BaseFileConnector:
    """Classe parente pour la gestion des fichiers sources."""

    def __init__(self, filepath: str):
        self._filepath = filepath  # Attribut protégé
        self._raw_data = []

    def load_file(self) -> list:
        """Valide et charge le fichier JSON brut."""
        if not os.path.exists(self._filepath):
            raise MissingFileException(self._filepath)

        with open(self._filepath, "r", encoding="utf-8") as f:
            self._raw_data = json.load(f)
        return self._raw_data


class MongoProjectConnector(BaseFileConnector):
    """Connecteur spécifique pour l'export MongoDB des projets."""

    def __init__(self):
        super().__init__("projecttracker.projects.json")

    def extract_clean_projects(self) -> list:
        """Extrait et nettoie les données spécifiques à MongoDB."""
        raw_list = self.load_file()
        cleaned_list = []

        for p in raw_list:
            # Nettoyage des balises HTML (ex: <p>) et normalisation de l'ID
            desc_brute = p.get("description", "")
            desc_clean = re.sub(r"<[^>]*>", "", desc_brute).strip()

            oid = (
                p.get("_id", {}).get("$oid", "")
                if isinstance(p.get("_id"), dict)
                else ""
            )

            cleaned_list.append(
                {
                    "id_projet": oid,
                    "titre": p.get("title", "").strip(),
                    "description": desc_clean,
                    "statut": p.get("status", "active"),
                }
            )
        return cleaned_list


class MySqlProductConnector(BaseFileConnector):
    """Connecteur spécifique pour l'export MySQL converti en JSON."""

    def __init__(self):
        super().__init__("produits_mysql_propres.json")

    def extract_clean_products(self) -> list:
        """Extrait et renvoie les produits issus de MySQL."""
        # Les données de ce fichier ont déjà été prélavées par votre script mysql_extract.py
        return self.load_file()


# --- 3. CONTEUR ANALYTIQUE (DUNDER METHODS) ---
class DataBatch:
    """Conteneur standardisé pour transporter les lots de données nettoyés."""

    def __init__(self, data_type: str, records: list):
        self.data_type = data_type
        self.records = records

    def __str__(self) -> str:
        return f"Batch [{self.data_type}] : {len(self.records)} enregistrements prêts."

    def __len__(self) -> int:
        return len(self.records)


# --- 4. ORCHESTRATEUR GLOBAL (ETL PIPELINE ENGINE) ---
class ETLPipelineEngine:
    def __init__(self):
        self.mongo_conn = MongoProjectConnector()
        self.mysql_conn = MySqlProductConnector()

    def run(self):
        print("=== 🏁 DEMARRAGE DU PIPELINE ETL EN POO ===\n")

        try:
            # --- 1. EXTRACT & TRANSFORM ---
            projets_propres = self.mongo_conn.extract_clean_projects()
            produits_propres = self.mysql_conn.extract_clean_products()

            # Encapsulation dans nos objets de lot standardisés
            batch_projets = DataBatch("MongoDB_Projects", projets_propres)
            batch_produits = DataBatch(
                "MySQL_Products", produits_produits_clean := produits_propres
            )

            # --- Affichage via les Dunder Methods ---
            print(batch_projets)
            print(batch_produits)

            # --- 2. LOAD (Sauvegarde de la synthèse finale) ---
            synthese = {
                "total_projets": len(batch_projets),  # Utilise __len__
                "total_produits": len(batch_produits),  # Utilise __len__
                "projets": batch_projets.records,
                "produits": batch_produits.records,
            }

            fichier_sortie = "synthese_poo_complete.json"
            with open(fichier_sortie, "w", encoding="utf-8") as f:
                json.dump(synthese, f, indent=4, ensure_ascii=False)

            print(
                f"\n✨ Synthèse globale enregistrée proprement dans : '{fichier_sortie}'"
            )

        except MissingFileException as e:
            print(f"❌ [ERREUR PIPELINE COUPEE] : {e}")
            print(
                "Action requise : Assurez-vous que les fichiers JSON bruts sont présents dans le dossier."
            )

        except Exception as e:
            print(f"❌ [CRITICAL ERROR] Erreur imprévue : {e}")

        finally:
            print("\n=== 🛑 FERMETURE DES COMPOSANTS ET LIBERATION MEMOIRE ===")


if __name__ == "__main__":
    # Instanciation et exécution du moteur de pipeline
    engine = ETLPipelineEngine()
    engine.run()
