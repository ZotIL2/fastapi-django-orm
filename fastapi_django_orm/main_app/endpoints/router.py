"""
The router for `main_app` endpoints.
Add all routers for the `main_app` here.
"""

from fastapi import APIRouter
from main_app.endpoints.demo.router import demo_router
from mysite.errors.responses import responses

main_app_router = APIRouter(
    responses=responses,
)

main_app_router.include_router(
    demo_router,
)
