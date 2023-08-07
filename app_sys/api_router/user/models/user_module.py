from pydantic import BaseModel, EmailStr, Field
from enum import Enum
from typing import Optional


# 登录用户信息数据模型类
class LoginUserInfoSchema(BaseModel):
    user: str
    password: str
    code: Optional[str] = None
    key: Optional[str] = None


# 性别枚举类
class GenderEnum(str, Enum):
    MALE = "male"
    FEMALE = "female"
    UNKNOWN = "unknown"


class RegisterUserInfoSchema(BaseModel):
    username: str
    email: EmailStr
    phone: str
    password: str
    sex: Optional[GenderEnum] = GenderEnum.UNKNOWN
    nickname: str = ""
    avatar: str = ""
    code: Optional[str] = None
    key: Optional[str] = None


# 忘记密码提交数据模型类
class ForgetPasswordSubmitSchema(BaseModel):
    email: EmailStr
    code: str
    key: str


# 忘记密码设置密码数据模型类
class ForgetPasswordSetPasswordSchema(BaseModel):
    password: str
    code: str
    key: str


# 修改用户信息数据模型类
class ChangeUserInfoSchema(BaseModel):
    nickname: str
    email: EmailStr
    phone: str
    sex: GenderEnum


# 修改密码数据模型类
class ChangePasswordSchema(BaseModel):
    old_password: str
    new_password: str


# 用户可用性数据模型类
class UserAvailabilitySchema(BaseModel):
    data: str
    exclude_user_id: Optional[int] = None



