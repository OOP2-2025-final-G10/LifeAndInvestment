from models import db
from models.job import Job

class User:
    def __init__(self, user_id: str, name: str, money: int, spot_id: int):
        self.user_id = user_id
        self.name = name
        self.money = money
        self.spot_id = spot_id
        self.job = None

    @classmethod
    def from_row(cls, row):
        user = cls(
            user_id=row["id"],
            name=row["name"],
            money=row["money"],
            spot_id=row["spot_id"]
        )
        user.job = Job.from_name(row["job"])
        return user
    
    def save(self, db):
        db.execute(
            """
            UPDATE users
            SET
                money = ?,
                job = ?,
                spot_id = ?
            WHERE id = ?
            """,
            (
                self.money,
                self.job.name if self.job else None,
                self.spot_id,
                self.user_id
            )
        )



    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "money": self.money,
            "spot_id": self.spot_id,
            "job": self.job.to_dict() if self.job else None
        }