from pathlib import Path

from pydantic import BaseModel


class Paper(BaseModel):
    title: str | None = None
    authors: list[str] | None = None
    abstract: str | None = None
    arxiv_id: str | None = None
    content_md: str | None = None
    pdf_url: str
    path: Path
