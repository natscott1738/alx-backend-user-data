#!/usr/bin/env python3
"""

Authentication class for API
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class for managing authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Returns False for now, to be used for checking authentication for certain paths.
        """

        return False

    def authorization_header(self, request=None) -> str:
        """ Returns None for now, to be used for getting the Authorization header"""

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns None for now, to be used for retrieving the current user"""

        return None
~

