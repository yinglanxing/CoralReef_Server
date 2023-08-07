from fastapi import APIRouter

router = APIRouter()


# Compare this snippet from app\api_router\user\views.py:

# from fastapi import APIRouter


@router.get("/")
async def user():
    return {"user": "main"}


@router.get("/current")
async def get_user():
    return {"user": "user"}


@router.post("/reg_user")
async def add_user():
    return {"user": "add_user"}


@router.post("/login_user")
async def update_user():
    return {"user": "update_user"}


@router.delete("/delete_user")
async def delete_user():
    return {"user": "delete_user"}


@router.post("/update_user")
async def update_user():
    return {"user": "update_user"}


@router.get("/get_user")
async def get_user():
    return {"user": "get_user"}
