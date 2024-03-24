"""Notion Tool."""
from typing import Optional

from llama_hub.notion.base import NotionPageReader


INTEGRATION_TOKEN_NAME = "NOTION_INTEGRATION_TOKEN"


class NotionTool:
    """Notion Tool."""

    def __init__(self, integration_token: Optional[str] = None) -> None:
        """Initialize with parameters."""
        self.reader = NotionPageReader(integration_token=integration_token)
