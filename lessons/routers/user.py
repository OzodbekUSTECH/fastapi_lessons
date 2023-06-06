from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import user as UserService
from dto import user as UserDto  
from fastapi.encoders import jsonable_encoder

router = APIRouter(
    prefix='/users',
    tags=['Users']
)
@router.get('/', name='Get All Users')
async def get_all_users(db: Session = Depends(get_db)):
    return UserService.get_users(db)

@router.post('/', name='Create User')
async def create_user(data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(data, db)

@router.get('/{id}', name='Get User by ID')
async def get_user_by_id(id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)

@router.put('/{id}', name='Update User')
async def update_user(id: int = None, data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.update_user(id, data, db)

@router.patch('/{id}', name='Patch User')
async def patch_user(id: int = None, data: UserDto.User = None, db: Session = Depends(get_db)):
    return UserService.patch_user(db, id, data)
    
@router.delete('/{id}', name='Delete User')
async def delete_user(id: int = None,  db: Session = Depends(get_db)): 
    return UserService.remove(db, id)