from fastapi import APIRouter

router = APIRouter()


# Compare this snippet from app\api_router\user\views.py:

# from fastapi import APIRouter

@router.get("/user")
async def get_user():
    return {"user": "user"}


@router.post("/user/add_user")
async def add_user():
    return {"user": "add_user"}


@router.put("/user/update_user")
async def update_user():
    return {"user": "update_user"}


@router.delete("/user/delete_user")
async def delete_user():
    return {"user": "delete_user"}
