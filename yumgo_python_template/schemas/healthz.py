from typing import Literal

from yumgo_python_template.schemas.base import Schema


class HealthSchema(Schema):
    status: Literal["ok"] = "ok"
