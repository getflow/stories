from datetime import datetime

from slide import Slide
from preview import Preview


class Story:
    """
    This is a story.
    """
    def __init__(self,
                 slides: list[Slide],
                 preview: Preview,
                 author_id: str,
                 created_at: datetime,
                 updated_at: datetime or None = None):
        self.__story_id = None  # type: int or None
        self.__slides = slides  # type: list[Slide]
        self.__preview = preview    # type: Preview
        self.__author_id = author_id  # type: str
        self.__created_at = created_at  # type: datetime
        self.__updated_at = updated_at  # type: datetime or None

    @property
    def story_id(self) -> int or None:
        return self.__story_id

    @property
    def slides(self) -> list[Slide]:
        return self.__slides

    @property
    def preview(self) -> Preview:
        return self.__preview

    @property
    def author_id(self) -> str:
        return self.__author_id

    @property
    def created_at(self) -> datetime:
        return self.__created_at

    @property
    def updated_at(self) -> datetime or None:
        return self.__updated_at
