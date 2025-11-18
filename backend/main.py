from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import router
from backend.auth.routes import router as auth_router
from backend.api.batch_routes import router as batch_router
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.responses import RedirectResponse
import os

app = FastAPI(title="CreditPathAI", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api", tags=["predictions"])
app.include_router(auth_router, prefix="/api/auth", tags=["authentication"])
app.include_router(batch_router, prefix="/api/batch", tags=["batch"])

frontend_path = os.path.join(os.path.dirname(__file__), '..', 'frontend')
@app.get('/old_form.html', include_in_schema=False)
async def redirect_old_form():
    return RedirectResponse(url='/index.html')

if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

@app.on_event("startup")
async def startup_event():
    print("=" * 50)
    print("CreditPathAI API running...")
    print("=" * 50)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Return a concise, human-readable message summarizing validation errors
    errors = exc.errors()
    messages = []
    for e in errors:
        loc = "->".join(str(x) for x in e.get('loc', []))
        msg = e.get('msg', '')
        messages.append(f"{loc}: {msg}")
    return JSONResponse(status_code=422, content={"detail": "; ".join(messages)})
