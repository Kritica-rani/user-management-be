from http.client import HTTPException
import logging
from sqlite3 import IntegrityError
from sqlalchemy.orm import Session
from app import models, schemas


from fastapi import HTTPException


def create_user(db: Session, user: schemas.UserCreate):
    try:
        logging.info("Creating user with data: %s", user.dict())

        # Check if the email already exists first
        existing_user = db.query(models.User).filter(
            models.User.email == user.email).first()

        if existing_user:
            # Use FastAPI's HTTPException
            raise HTTPException(status_code=400, detail="Email already exists")

        # Create and add user
        db_user = models.User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    except HTTPException:
        # Re-raise FastAPI HTTP exceptions
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500, detail="Oops, Something went wrong!")


def get_users(db: Session):
    try:
        return db.query(models.User).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Could not fetch users")


def delete_user(db: Session, user_id: int):
    try:
        # Find the user by ID
        db_user = db.query(models.User).filter(
            models.User.id == user_id).first()
        # If user doesn't exist, return 404
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        # Delete the user
        db.delete(db_user)
        db.commit()
        return {"message": "User deleted successfully"}

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Failed to delete user")
