class DataBatch:
    def __init__(self, source_name: str, records: list):
        self.source = source_name
        self.records = records  # Liste de dictionnaires contenant les données

    # 1. Représentation textuelle propre (User-friendly)
    def __str__(self) -> str:
        return f"Lot de données issu de '{self.source}' contenant {len(self.records)} lignes."

    # 2. Représentation technique de débogage (Dev-friendly)
    def __repr__(self) -> str:
        return f"DataBatch(source='{self.source}', records_count={len(self.records)})"

    # 3. Permet d'utiliser len() directement sur l'objet
    def __len__(self) -> int:
        return len(self.records)


# --- UTILISATION PRATIQUE ---
if __name__ == "__main__":
    # Simulation de données propres issues de votre pipeline
    faux_produits = [
        {"id": 26, "name": "Montre Connectée", "price": 2000.0},
        {"id": 13, "name": "Chaussures Homme", "price": 140.0},
    ]

    # Instanciation de notre lot
    batch_produits = DataBatch(source_name="MySQL_Products", records=faux_produits)

    # Test de __str__ via le print natif
    print(batch_produits)
    # Sortie : Lot de données issu de 'MySQL_Products' contenant 2 lignes.

    # Test de __len__ via la fonction native
    print(f"Volume détecté par Python : {len(batch_produits)} lignes.")
    # Sortie : Volume détecté par Python : 2 lignes.

    # Test de __repr__ (par exemple en inspectant une liste de lots)
    liste_de_plusieurs_lots = [batch_produits]
    print(f"Log de débogage : {liste_de_plusieurs_lots}")
    # Sortie : Log de débogage : [DataBatch(source='MySQL_Products', records_count=2)]
