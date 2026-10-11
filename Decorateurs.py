class PipelineConfiguration:
    def __init__(self, batch_size: int):
        self.__batch_size = batch_size  # Privé

    # Le Getter
    @property
    def batch_size(self) -> int:
        return self.__batch_size

    # Le Setter (permet de contrôler et valider la donnée reçue)
    @batch_size.setter
    def batch_size(self, nouvelle_valeur: int):
        if nouvelle_valeur > 0:
            self.__batch_size = nouvelle_valeur
        else:
            print("[WARN] Le volume d'un batch doit être supérieur à 0 !")


# --- Utilisation ---
config = PipelineConfiguration(100)
config.batch_size = (
    500  # Utilise le setter de manière transparente (comme une variable !)
)
config.batch_size = -10  # Affiche le message d'avertissement et bloque la modification
print(config.batch_size)  # Utilise le getter -> 500
