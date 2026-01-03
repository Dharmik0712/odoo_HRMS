from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import logger
from app.db.init_db import init_db
from app.api.v1 import auth, users, attendance, leave, payroll

app = FastAPI(title=settings.app_name)

@app.on_event("startup")
def startup():
    logger.info("application_startup")
    init_db()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    try:
        response = await call_next(request)
        logger.info(
            f"request_completed | method={request.method} "
            f"path={request.url.path} status={response.status_code}"
        )
        return response
    except Exception:
        logger.exception(
            f"request_failed | method={request.method} path={request.url.path}"
        )
        return JSONResponse(
            status_code=500,
            content={"message": "Internal server error"},
        )

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(attendance.router, prefix="/api/v1/attendance", tags=["Attendance"])
app.include_router(leave.router, prefix="/api/v1/leave", tags=["Leave"])
app.include_router(payroll.router, prefix="/api/v1/payroll", tags=["Payroll"])
