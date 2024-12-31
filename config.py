class Config:
    API_KEY = os.getenv("API_KEY")  # Sin valor por defecto
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"