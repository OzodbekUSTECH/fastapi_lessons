from models.user import User
from sqlalchemy.orm import Session
from dto import user

from fastapi import HTTPException
from fastapi import status

def create_user(data: user.User, db: Session):
    user = User(name=data.name)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)

    except Exception as e:
        print(e)

    return user

def get_user(id: int, db):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    return user

def get_users(db):
    return db.query(User).all()

def update_user(data: user.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    user.name = data.name
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def patch_user(db: Session, id: int, data: user.User):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    update_data = data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)

    return user

def remove(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found'
        )
    db.delete(user)
    db.commit()

    return {
        "message": 'This user was removed',
        "Data": user
    }

