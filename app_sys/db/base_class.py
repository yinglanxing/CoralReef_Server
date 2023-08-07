import app_sys.configs.config

settings = app_sys.configs.config.Settings()

from tortoise import fields, models
from app_sys.utils.transform import camel_case_2_underscore
from typing import Annotated


class Base(models.Model):
    id = fields.IntField(pk=True, index=True)
    created_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    creator_id = fields.IntField(default=0, description="创建人id")
    modified_time = fields.DatetimeField(auto_now=True, description="更新时间")
    modifier_id = fields.IntField(default=0, description="修改人id")
    is_deleted = fields.IntField(default=0, description="逻辑删除:0=未删除,1=删除")

    class Meta:
        abstract = True

    @classmethod
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls._meta.table = (settings.SQL_TABLE_PREFIX or "") + camel_case_2_underscore(cls.__name__)

    @staticmethod
    def dt2ts(column: fields.DatetimeField, label: str = ""):
        return Annotated[column.to_db_value(), label] if label else column.to_db_value()

    @staticmethod
    def ts2dt(column: fields.DatetimeField, label: str = ""):
        return Annotated[column.to_python_value(), label] if label else column.to_python_value()

    @classmethod
    def listColumns(cls):
        return list(cls._meta.fields_map.values())

    def dict(self):
        return {field.attname: getattr(self, field.attname, None) for field in self._meta.fields_map.values()}

    def list(self):
        return [getattr(self, field.attname, None) for field in self._meta.fields_map.values()]
