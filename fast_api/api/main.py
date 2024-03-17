from fastapi import FastAPI


def init_app():
    app = FastAPI(
        title="Fast SQLModel Study",
        description="CRUD",
        version="1"
    )

    @app.get("/")
    async def root():
        return {"message": "Hello World, I am here!"}
    
    return app


app = init_app()
