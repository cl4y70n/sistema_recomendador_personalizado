from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sistema de Recomendação Personalizado"
    version: str = "1.0.0"

settings = Settings()