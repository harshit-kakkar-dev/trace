"""SQLAlchemy model registry for T.R.A.C.E."""

from app.models.college import College
from app.models.user import User

__all__ = ["College", "User"]
