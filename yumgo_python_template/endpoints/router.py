"""
The router for `main_app` endpoints.
Add all routers for the `main_app` here.
"""

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from yumgo_python_template.errors.responses import responses
from yumgo_python_template.settings import settings

router = APIRouter(
    responses=responses,
)


@router.get(
    "/",
    include_in_schema=False,
)
def index() -> RedirectResponse:
    if settings.debug:
        return RedirectResponse(
            url=settings.root_path + "/docs",
        )
    return None


internal_router = APIRouter()
