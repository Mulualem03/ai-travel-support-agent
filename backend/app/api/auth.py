from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login():
    return {
        "access_token": "demo-token",
        "token_type": "bearer",
        "note": "MVP placeholder. Replace with real JWT authentication.",
    }


@router.post("/register")
def register():
    return {
        "message": "MVP placeholder. Replace with real user registration and password hashing."
    }


@router.get("/me")
def me():
    return {
        "id": 1,
        "email": "customer@example.com",
        "role": "customer",
        "note": "MVP placeholder user."
    }
