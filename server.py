from aiohttp import web
from core.router import routes, app


if __name__ == '__main__':
    web.run_app(app)