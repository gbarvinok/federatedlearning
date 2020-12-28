from ... import BaseModel, db


class User(BaseModel):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String())
    hashed_password = db.Column(db.String())
    salt = db.Column(db.String())
    private_key = db.Column(db.String())
    role = db.Column(db.Integer, db.ForeignKey("role.id"))

    def __str__(self):
        return f"<User id: {self.id}, email: {self.email}, " f"role: {self.role}>"


def create_user(email, hashed_password, salt, private_key, role):
    new_user = User(
        email=email,
        hashed_password=hashed_password,
        salt=salt,
        private_key=private_key,
        role=role,
    )
    return new_user
