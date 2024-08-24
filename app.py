
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from presentation.ping import api as ping_api
from presentation.product import api as product_api
from presentation.like import api as like_api
from presentation.cart import api as cart_api
from exception import BaseException

from exception import handle_exception


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*",],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(BaseException, handle_exception)

    app.include_router(like_api)
    app.include_router(ping_api, prefix="/ping")
    app.include_router(product_api, prefix="/product")
    app.include_router(cart_api, prefix="/cart")

    return app
