from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user_schema import UserRegister, UserLogin, UserOut
from app.services.auth_service import get_password_hash, verify_password, create_access_token
from app.database import db

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

# Registration
@auth_router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):
    user_exist = await db.users.find_one({"email": user.email})
    if user_exist:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_pw = get_password_hash(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "hashed_password": hashed_pw,
    }
    res = await db.users.insert_one(new_user)
    return UserOut(id=str(res.inserted_id), username=user.username, email=user.email)

# Login
@auth_router.post("/login")
async def login(user: UserLogin):
    db_user = await db.users.find_one({"email": user.email})
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"user_id": str(db_user["_id"]), "username": db_user["username"]})
    return {"access_token": token, "token_type": "bearer"}
