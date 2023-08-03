#
from typing import List

# 导入BaseModel
from pydantic import BaseModel


# 继承BaseModel
# BaseModel是一个基类，它的作用是为pydantic模型提供一些基础功能，例如配置模型的元数据、配置模型的json序列化行为、配置模型的schema、配置模型的验证行为等等。
# BaseModel的子类可以通过声明属性来定义模型的字段，字段的类型可以是python内置的类型，也可以是pydantic模型，还可以是python的标准库中的类型，例如datetime、uuid等等。

class UserSchema(BaseModel):
    uid: int
    username: str
    nickname: str = ""
    sex: int = 0
    phone: str
    email: str
    avatar: str = ""
    is_active: bool = True
    status: int = 0
    roles: List[int] = []


# 定义UserIsActiveSchema类，继承BaseModel
class UserIsActiveSchema(BaseModel):
    is_active: bool


class UserSetPasswordSchema(BaseModel):
    password: str


class RoleSchema(BaseModel):
    name: str
    key: str
    order_num: int = 0
    status: int = 0
    menus: List[int] = []


class MenuSchema(BaseModel):
    path: str = ""
    component: str = ""
    is_frame: bool = False
    hidden: bool = False
    status: int = 0
    name: str = ""
    title: str = ""
    icon: str = ""
    order_num: int = 0
    no_cache: bool = True
    parent_id: int = 0


class RoleMenuSchema(BaseModel):
    menu_ids: List[int]


class PremLabelSchema(BaseModel):
    label: str
    remark: str = ""
    status: int = 0
    roles: List[int] = []


class PremLabelMenuSchema(BaseModel):
    menu_ids: List[int]
