from typing import TYPE_CHECKING

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from main_app.endpoints.internal.router import main_app_internal_router
from main_app.endpoints.router import main_app_router
from mysite.asgi import django_app
from mysite.config import settings
from mysite.errors.handlers import error_handler_pairs
from mysite.middleware import add_middlewares

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator


async def lifecycle(_: FastAPI) -> "AsyncGenerator[None]":
    """Add your lifecycle events here."""
    yield


# app is a wrapper, while `main_app` is the actual FastAPI instance.
# `app` should only contain `/healthz` endpoint for it to be:
#   - accessible by health checks
#   - not be accessible by users
#   - be in the true root of the path
app = FastAPI(
    lifespan=lifecycle,
)

main_app = FastAPI(
    debug=settings.debug,
    title=settings.title,
    version=settings.version,
    root_path=settings.root_path,
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
)

for handler in error_handler_pairs:
    main_app.add_exception_handler(handler[0], handler[1])

app.include_router(main_app_internal_router)
main_app.include_router(main_app_router)


main_app.mount("/django", django_app)

main_app.mount(
    "/static",
    StaticFiles(
        directory="static",
    ),
    name="static",
)
main_app.mount(
    "/media",
    StaticFiles(
        directory="media",
    ),
    name="media",
)

app.mount("", main_app)


add_middlewares(main_app)
