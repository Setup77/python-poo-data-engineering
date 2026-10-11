class Product:
    # 1. Le Constructeur : Initialisation des attributs
    def __init__(self, id_produit: int, name: str, price: float, stock_quantity: int):
        self.id_produit = id_produit
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    # 2. Méthode de calcul : Retourne la valeur financière en stock
    def calculer_valeur_stock(self) -> float:
        return self.price * self.stock_quantity

    # 3. Méthode d'action : Modifie le stock suite à une vente
    def vendre(self, quantite: int):
        if quantite <= self.stock_quantity:
            self.stock_quantity -= quantite
            print(f"[VENTE] {quantite} unités de '{self.name}' vendues.")
        else:
            print(
                f"[ERREUR] Stock insuffisant pour vendre {quantite} unités de '{self.name}'."
            )


# --- ZONE DE TEST ---
if __name__ == "__main__":
    # Instanciation de votre montre connectée (Produit 26)
    ma_montre = Product(
        id_produit=26, name="Montre Connectée", price=2000.0, stock_quantity=26
    )

    # Test 1 : Calcul de la valeur du stock
    valeur_initiale = ma_montre.calculer_valeur_stock()
    print(f"Valeur totale du stock initiale : {valeur_initiale} €")
    # Affiche : Valeur totale du stock initiale : 52000.0 €

    # Test 2 : Simulation d'une vente
    ma_montre.vendre(6)
    print(f"Nouveau stock de sécurité : {ma_montre.stock_quantity} unités.")
    # Affiche : Nouveau stock de sécurité : 20 unités.
