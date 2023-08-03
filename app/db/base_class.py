import app.core.config

settings = app.core.config.Settings()


class Base():
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    create_time = Column(DateTime, default=datetime.datetime.now, comment="创建时间")
    creator_id = Column(Integer, default=0, comment="创建人id")
    modified_time = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment="更新时间")
    modifier_id = Column(Integer, default=0, comment="修改人id")
    is_deleted = Column(Integer, default=0, comment="逻辑删除:0=未删除,1=删除")
