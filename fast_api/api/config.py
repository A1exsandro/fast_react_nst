from sqlmodel import SQLModel, create_engine


DB_URI = "postgresql://postgres:admin@localhost:5432/fast_sqlmodel"


engine = create_engine(DB_URI, echo=True)

def create_db_tables():
    SQLModel.metadata.create_all(engine)
