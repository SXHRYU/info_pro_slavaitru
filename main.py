from django.core.validators import EmailValidator
from abc import ABC, abstractmethod
from datetime import datetime
import csv


class DataTemplate(ABC):
    @classmethod
    @abstractmethod
    def is_valid_format(cls, data):
        raise NotImplementedError
    
    @property
    @abstractmethod
    def formats(cls):
        raise NotImplementedError("Override 'formats' instance attribute.")


class DateTemplate(DataTemplate):
    formats: list[str] = [
        "%Y-%m-%d",  # -> "2022-08-11"
        "%Y/%m/%d",  # -> "2022/08/11"
        "%Y-%m-%dT%H:%M:%S.%fZ",  # -> "2022-08-11T21:09:01.123456Z"
        "%Y-%m-%dT%H:%M:%SZ",  # -> "2018-03-12T10:12:45Z"
        "%b %d %Y at %I:%M%p",  # -> "Jun 28 2018 at 7:40AM"
        "%B %d, %Y, %H:%M:%S",  # -> "September 18, 2017, 22:19:55"
        "%a,%d/%m/%y,%I:%M%p",  # -> "Sun,05/12/99,12:30PM"
        "%a, %d %B, %Y",  # -> "Mon, 21 March, 2015"
    ]

    @classmethod
    def is_valid_format(cls, data: str) -> bool:
        datetime_obj: datetime = None
        for format_ in cls.formats:
            try:
                datetime_obj = datetime.strptime(data, format_)
            except ValueError:
                continue
            else:
                break
        return bool(datetime_obj)


class PhoneTemplate(DataTemplate):
    def is_valid_format(self) -> bool:
        return True


class EmailTemplate(DataTemplate):
    def is_valid_format(self) -> bool:
        return True


class AddressTemplate(DataTemplate):
    def is_valid_format(self) -> bool:
        return True


class IPV4Template(DataTemplate):
    def is_valid_format(self) -> bool:
        return True


class ITNTemplate(DataTemplate):
    def is_valid_format(self) -> bool:
        return True


def read_txt(path: str):
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            print(line)
