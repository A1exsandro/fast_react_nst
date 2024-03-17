from fastapi import APIRouter, HTTPException
from typing import List


from api.repositories.students.StudentRepository import StudentRepository
from api.schemas.students.StudentSchema import ResponseSchema, StudentCreate


router = APIRouter(
    prefix="/student",
    tags=['Student']
)


# CREATE
@router.post("", response_model=ResponseSchema)
def create_student(
    create_data_form: StudentCreate
):
    return StudentRepository.create(create_data_form)


# READ
@router.get("", response_model=List[ResponseSchema])
def get_all_student():
    return StudentRepository.get_all()


# GET BY ID
@router.get("/{student_id}", response_model=ResponseSchema)
def get_student_by_id(student_id: int):
    data = StudentRepository.get_by_id(student_id)
    if not data:
        raise HTTPException(status_code=404, detail="Item not Found!")
    return data


# UPADATE 
@router.patch("/{student_id}", response_model=ResponseSchema)
def update_student(student_id: int, update_form: StudentCreate):
    data = StudentRepository.update(student_id, update_form)
    if not data:
        raise HTTPException(status_code=404, detail="Item not Found!")
    return data


# DELETE
@router.delete("/{student_id}")
def delete_student(student_id: int):
    data = StudentRepository.delete(student_id)
    if not data:
        raise HTTPException(status_code=404, detail="Item not Found!")
    return data
