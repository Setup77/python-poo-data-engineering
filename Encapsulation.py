class DatabaseConfig:
    def __init__(self, host: str, token: str):
        self.host = host  # Public
        self.__secret_token = token  # Privé (Deux underscores !)


# --- Utilisation ---
config = DatabaseConfig("127.0.0.1", "XyZ123Secret")

print(config.host)  # Fonctionne : "127.0.0.1"
# print(config.__secret_token) # CRASHE ! Lance une erreur AttributeError
