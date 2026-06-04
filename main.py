from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth
from app.core.database import Base, engine
from app.api.v1 import auth, projects
from app.api.v1 import pipelines
from app.api.v1 import deployments
from app.api.v1 import analytics, monitoring, builds


Base.metadata.create_all(bind=engine)

app = FastAPI(title="DevOps Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth.router, prefix="/api/v1")
app.include_router(projects.router, prefix="/api/v1")
app.include_router(pipelines.router, prefix="/api/v1")
app.include_router(deployments.router, prefix="/api/v1")
app.include_router(analytics.router, prefix="/api/v1")
app.include_router(monitoring.router, prefix="/api/v1")
app.include_router(builds.router, prefix="/api/v1")