from sqlmodel import Session, select
from api.config import engine

from api.models.students.StudentModel import Student
from api.schemas.students.StudentSchema import StudentCreate


class StudentRepository:

    # CREATE
    def create(create_data_form: StudentCreate):
        with Session(engine) as session:
            data_upper = create_data_form.nome.upper()
            new_row = Student(nome=data_upper)
            session.add(new_row)
            session.commit()
            session.refresh(new_row)
            return new_row
        
    
    # READ
    def get_all():
        with Session(engine) as session:
            return session.exec(select(Student)).all()
        

    # GET BY ID
    def get_by_id(student_id: int):
        with Session(engine) as session:
            return session.get(Student, student_id)


    # UPDATE
    def update(student_id: int, update_form: StudentCreate):
        with Session(engine) as session:
            data_db = session.get(Student, student_id)
            if not data_db:
                return None
            data_to_update = update_form.model_dump(exclude_unset=True)
            for key,value in data_to_update.items():
                setattr(data_db, key, value)
            session.add(data_db)
            session.commit()
            session.refresh(data_db)
            return data_db
        

    # DELETE
    def delete(student_id: int):
        with Session(engine) as session:
            data_db = session.get(Student, student_id)
            if not data_db:
                return None
            session.delete(data_db)
            session.commit()
            return {"detail": "Successfully Deleted"}
        