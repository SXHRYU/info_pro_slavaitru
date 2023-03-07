from django.core.validators import EmailValidator
from abc import ABC, abstractmethod
from datetime import datetime
import re
from typing import Sequence


class DataTemplate(ABC):
    @classmethod
    @abstractmethod
    def is_valid_format(cls, data):
        raise NotImplementedError

    @property
    @abstractmethod
    def verbose_name(cls):
        raise NotImplementedError("Override 'verbose_name' attribute.")


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
    verbose_name: str = "Дата"

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
    regex: re.Pattern = re.compile(r"^\+?1?\d{9,15}")
    verbose_name: str = "Телефонный номер"

    def is_valid_format(self, data: str) -> bool:
        # fmt: off
        normalised_number = data.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
        # fmt: on
        return bool(re.fullmatch(self.regex, normalised_number))


class EmailTemplate(DataTemplate):
    regex: re.Pattern = re.compile(r"^\S+@\S+\.\S+$", re.IGNORECASE)
    verbose_name: str = "Email"

    def is_valid_format(self, data: str) -> bool:
        return bool(re.fullmatch(self.regex, data))


class AddressTemplate(DataTemplate):
    regex: re.Pattern = re.compile(
        r"^\w*[,.\-/ ]*[,.\-/ ]*\w*[,.\-/ ]*[,.\-/ ]*\w*[,.\-/ ]*[,.\-/ ]*\w*[,.\-/ ]*[,.\-/ ]\d*[,.\-/ ]\d*[,.\-/ ]*\w*[,.\-/ ]*\d*\w*[,.\-/ ]*\w.*$"
    )
    verbose_name: str = "Адрес"

    def is_valid_format(self, data: str) -> bool:
        return bool(re.fullmatch(self.regex, data))


class IPV4Template(DataTemplate):
    regex: re.Pattern = re.compile(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
    verbose_name: str = "IPv4"

    def is_valid_format(self, data: str) -> bool:
        return bool(re.fullmatch(self.regex, data))

class IPV6Template(DataTemplate):
    regex: re.Pattern = re.compile(r"((([0-9a-fA-F]){1,4})\\:){7}([0-9a-fA-F]){1,4}")
    verbose_name: str = "IPv6"

    def is_valid_format(self, data: str) -> bool:
        return bool(re.fullmatch(self.regex, data))


class INNTemplate(DataTemplate):
    regex: re.Pattern = re.compile(r"^\d{10,12}$")
    verbose_name: str = "ИНН"

    def is_valid_format(self, data: str) -> bool:
        return bool(re.fullmatch(self.regex, data))


class UnknownTemplate(DataTemplate):
    verbose_name: str = "Новый тип"

    def is_valid_format(self, data: str) -> bool:
        ...

class TypeAssigner:
    def __init__(self, templates: Sequence[DataTemplate]) -> None:
        self.templates = templates
        self.assigned_type: DataTemplate = None
    
    def assign_data_type(self, data: str) -> DataTemplate:
        for template in self.templates:
            if template.is_valid_format(data):
                self.assigned_type = template
                return self.assigned_type
        return UnknownTemplate()

def assign_file_data_types(path: str):
    t = TypeAssigner(
        (
            DateTemplate(),
            PhoneTemplate(),
            EmailTemplate(),
            AddressTemplate(),
            IPV4Template(),
            IPV6Template(),
            INNTemplate(),
        )
    )
    with open(path, "r", encoding="utf-8") as file:
        types = []
        for data in file.readline().split("\t"):
            types.append(t.assign_data_type(data))
        return types

print(assign_file_data_types("test.txt"))
