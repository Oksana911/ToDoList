from dataclasses import dataclass
from typing import List

from marshmallow import EXCLUDE


@dataclass
class Message:
    pass


@dataclass
class Update:
    pass


@dataclass
class Chat:
    pass


@dataclass
class MessageFrom:
    pass


@dataclass
class UpdateObj:
    pass


@dataclass
class GetUpdatesResponse:
    ok: bool
    result: List[UpdateObj]  # todo

    class Meta:
        unknown = EXCLUDE


@dataclass
class SendMessageResponse:
    ok: bool
    result: Message  # todo

    class Meta:
        unknown = EXCLUDE
