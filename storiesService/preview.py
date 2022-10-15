from media import Media


class Preview:
    def __init__(self,
                 media: Media,
                 text: str or None = None):
        self.__media = media
        self.__text = text

    @property
    def media(self) -> Media:
        return self.__media

    @property
    def text(self) -> str or None:
        return self.__text
