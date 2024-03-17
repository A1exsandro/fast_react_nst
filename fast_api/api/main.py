from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.config import create_db_tables

origins = ["http://localhost:5173"]



def init_app():
    app = FastAPI(
        title="Fast SQLModel Study",
        description="CRUD",
        version="1"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.on_event("startup")
    async def startup():
        create_db_tables()

    from api.routers.students import student_router

    app.include_router(student_router.router)


    @app.get("/")
    async def root():
        return {"message": "Hello World, I am here!"}
    
    return app


app = init_app()
