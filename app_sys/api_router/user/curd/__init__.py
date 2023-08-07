class CURDUser():
    def getByUsername(self, db: Session, *, username: str):
        """
        通过用户名获取用户
        """
        return db.query(Users).filter(Users.username == username).first()
