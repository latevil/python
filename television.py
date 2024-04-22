class Television:
    """
    A class representing a television.
    """

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize the Television object with default values.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Turn the television on/off by changing the status variable.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute/unmute the television when it's on by changing the muted variable.
        """
        self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Increase the television channel value when the TV is on.
        If the TV is on the maximum channel, set the channel to the minimum channel.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the television channel value when the TV is on.
        If the TV is on the minimum channel, set the channel to the maximum channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increase the television volume when the TV is on.
        If the TV is on the maximum volume, volume remains at the maximum.
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        lower the television volume when the TV is on.
        If the TV is on the lowest volume, volume remains at the minimum.
        """
        if self.__status:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        prints the values of the TV object in the order:
        Power =  Channel = Volume =
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}*'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

