from media import Media


class Slide:
    def __init__(self,
                 background: Media,
                 caption: str,
                 button: dict or None = None,
                 text: str or None = None):
        self.__background = background
        self.__caption = caption
        self.__button = button
        self.__text = text

    @property
    def background(self) -> Media:
        return self.__background

    @property
    def caption(self) -> str:
        return self.__caption

    @property
    def button(self) -> dict or None:
        return self.__button
