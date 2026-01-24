from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int = 5432

    @property
    def get_sql_url(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()
print("DB_NAME:", settings.DB_NAME)
print("DB_USER:", settings.DB_USER)
print("DB_HOST:", settings.DB_HOST)
