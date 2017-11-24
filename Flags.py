"""Module containing flags"""
from enum import Flag, auto, unique


@unique
class ResponseFlag(Flag):
    """Flags for bot responses"""
    OKAY = auto()
    NOT_FOUND = auto()
    WRONG_REQUEST = auto()
    KYS = auto()


@unique
class MessageEventFlag(Flag):
    NONE = auto()
    ANGERY = auto()
