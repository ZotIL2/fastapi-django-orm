from typing import Literal

from main_app.schemas.base import Schema


class HealthSchema(Schema):
    status: Literal["ok"] = "ok"
