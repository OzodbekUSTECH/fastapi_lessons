from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import user as UserService
from dto import user as UserDto  

router = APIRouter(
    prefix='/users',
    tags=['Users']
)

@router.post('/')
async def create(data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{id}')
async def get(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)

@router.put('/{id}')
async def update(id: int = None, data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.update_user(id, data, db)

@router.delete('/{id}')
async def delete(id: int = None, db: Session = Depends(get_db)): 
    return UserService.remove(id, db)