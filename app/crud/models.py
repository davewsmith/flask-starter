from datetime import datetime, timezone

import sqlalchemy as sa
import sqlalchemy.orm as so

from app import db


class Crud(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    created_at: so.Mapped[datetime] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc))
    name: so.Mapped[str] = so.mapped_column(sa.String(128))

    def __repr__(self):
        return f"<Crud {self.id}>"
