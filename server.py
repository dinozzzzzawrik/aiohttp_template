from aiohttp import web


def setup_routes(application: web.Application) -> None:
    from app.project.routes import setup_routes as setup_forum_routes
    setup_forum_routes(application)


def setup_app(application: web.Application) -> None:
    setup_routes(application)


if __name__ == "__main__":
    app = web.Application()
    setup_app(app)
    web.run_app(app)
