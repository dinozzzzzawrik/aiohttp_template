from app.project import views
from aiohttp import web


def setup_routes(app: web.Application) -> None:
    app.router.add_get('', views.index)
