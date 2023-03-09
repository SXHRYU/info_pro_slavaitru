from typing import Sequence
from .templates import (
    DataTemplate,
    DateTemplate,
    PhoneTemplate,
    EmailTemplate,
    AddressTemplate,
    IPV4Template,
    IPV6Template,
    INNTemplate,
    TimeTemplate,
    UnknownTemplate,
)


class TypeAssigner:
    def __init__(
        self,
        templates: Sequence[DataTemplate] = (
            DateTemplate(),
            PhoneTemplate(),
            EmailTemplate(),
            AddressTemplate(),
            IPV4Template(),
            IPV6Template(),
            INNTemplate(),
            TimeTemplate(),
        ),
    ) -> None:
        self.templates = templates
        self.assigned_type: DataTemplate = None

    def assign_data_type(self, data: str) -> DataTemplate:
        for template in self.templates:
            if template.is_valid_format(data):
                self.assigned_type = template
                return self.assigned_type
        return UnknownTemplate()
