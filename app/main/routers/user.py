def user_routers():
    import app.main.factories.user as facto
    from fastapi import APIRouter

    router = APIRouter()

    router.add_api_route(path="/users/login", methods=["POST"], endpoint=facto.login_router())
    router.add_api_route(path="/users/create", methods=["POST"], endpoint=facto.add_user_router())
    router.add_api_route(path="/users/refresh_token", methods=["POST"], endpoint=facto.generate_refresh_token_router())
    router.add_api_route(path="/users/me", methods=["GET"], endpoint=facto.load_self_user_router())

    return router
