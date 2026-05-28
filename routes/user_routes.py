from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from models.model import User
from schemas.user_schema import UserCreate,UserLogin
from auth import create_access_token, employee_only, manager_only,verify_password,hash_password
from auth import verify_token
from auth import get_current_user
from auth import admin_only
from schemas.user_schema import UserUpdate
router = APIRouter()

@router.post("/signup")
def signup(user:UserCreate,db:Session=Depends(get_db)):
    # Logic to create a new user in the database
    new_user = User(
        username = user.username,
        email = user.email,
        role = user.role,
        password = hash_password(user.password)

    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{
        "message":"User Created Successfully",
        "user":{
            "id":new_user.id,
            "username":new_user.username,
            "email":new_user.email,
            "role":new_user.role
        }
    }

@router.post("/login")
def login(user:UserLogin,db:Session=Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        return {
            "message" : "User not Found"
        }
    if not verify_password(user.password,existing_user.password):
        return{
            "message":"Incorrect Password"
        }
    access_token = create_access_token(
       data =  {
           "sub":existing_user.email,
           "role":existing_user.role

        }
    )
    return {
        "message" : "Login Successful",
       
        "access_token":access_token,
        "token_type":"bearer"

    }

@router.get("/profile")
def profile(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
        "is_active": current_user.is_active,
        "is_verified": current_user.is_verified
    }


@router.get("/admin-dashboard")
def admin_dashboard(current_user:User=Depends(admin_only)):
    return {
        "message":"Welcome to the Admin Dashboard",
        "user":{
            "id":current_user.id,
            "username":current_user.username,
            "email":current_user.email,
            "role":current_user.role
        }
    }

@router.get("/manager-dashboard")
def manager_dashboard(current_user:User=Depends(manager_only)):
    return {
        "message":"Welcome to the Manager Dashboard",
        "user":{
            "id":current_user.id,
            "username":current_user.username,
            "email":current_user.email,
            "role":current_user.role
        }
    }

@router.get("/employee-dashboard")
def employee_dashboard(current_user:User=Depends(employee_only)):
    return {
        "message":"Welcome to the Employee Dashboard",
        "user":{
            "id":current_user.id,
            "username":current_user.username,
            "email":current_user.email,
            "role":current_user.role
        }
    }
@router.patch("/profile")
def update_profile(
    updated_data: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    if updated_data.username:
        current_user.username = updated_data.username

    if updated_data.email:
        current_user.email = updated_data.email

    if updated_data.password:
        current_user.password = hash_password(
            updated_data.password
        )

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Profile updated successfully",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email
        }
    }


@router.delete("/profile")
def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    db.delete(current_user)

    db.commit()

    return {
        "message": "Profile deleted successfully"
    }
