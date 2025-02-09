from main_app.schemas.healthz import HealthSchema

from .router import main_app_internal_router


@main_app_internal_router.get("/healthz")
def health_check() -> HealthSchema:
    return HealthSchema()
