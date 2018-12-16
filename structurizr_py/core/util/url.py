from urllib.parse import urlparse


class Url:
    """
    Utilities for dealing with URLs.
    """

    @staticmethod
    def is_url(url: str) -> bool:
        """
        Determines whether the supplied string is a valid URL.

        :param url: str
        :return: True if the URL is valid, False otherwise
        """
        parsed = urlparse(url)
        return True if len(parsed.scheme) > 0 and len(parsed.netloc) > 0\
            else False
