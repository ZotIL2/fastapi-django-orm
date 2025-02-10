from fastapi.responses import RedirectResponse

from yumgo_python_template.settings import settings

from .router import router


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
