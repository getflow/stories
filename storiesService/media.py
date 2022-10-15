class Media:
    def __init__(self,
                 media_type: str,
                 media_url: str):
        self.__media_id = None  # type: int or None
        self.__media_type = media_type  # type: str
        self.__media_url = media_url    # type: str

    @property
    def media_id(self) -> int or None:
        return self.__media_id

    @property
    def media_type(self) -> str:
        return self.__media_type

    @property
    def media_url(self) -> str:
        return self.__media_url
