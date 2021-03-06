from .views import liveness, marker, redirect


def setup_routes(app):
    app.router.add_get("/liveness", liveness)
    app.router.add_get("/__marker.gif", marker)
    app.router.add_get("/{deeplink_id}", redirect)
