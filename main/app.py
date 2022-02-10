import logging
from fnmatch import fnmatch
from typing import Optional

from fastapi import Header, Request, status
from fastapi.responses import JSONResponse, RedirectResponse

from main import app, config
from main.routes import email_router

log = logging.getLogger(__name__)

log.info('Adding routers..')
app.include_router(router=email_router)


@app.middleware('http')
async def restrict_ip_middleware(request: Request, call_next):
    ip = str(request.client.host)
    for host in config.server['allowed_hosts']:
        if fnmatch(name=ip, pat=host):
            return await call_next(request)
    data = {
        "details": f"IP {ip} is not allowed to access this server."
    }
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content=data)


@app.get('/{path:path}')
async def wildcard_route(path: str, request: Request, host: Optional[list[str]] = Header(None)):
    return RedirectResponse("/docs")
