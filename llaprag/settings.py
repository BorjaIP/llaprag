from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class Redis(BaseModel):
    host: str
    port: int
    password: str
    namespace: str


class Chroma(BaseModel):
    host: str
    port: str
    collection_name: str
    embedding_model: str
    # dim: int


class LLM(BaseModel):
    api_key: str
    model: str
    timeout: int


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_nested_delimiter="__", validate_default=False, extra="ignore"
    )
    port: int
    llm: LLM
    chroma: Chroma
    redis: Redis


settings = Settings()
