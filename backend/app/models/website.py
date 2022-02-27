from sqlalchemy import Column, Float, Integer, String

from app.db.session import Base


class Website(Base):
    __tablename__ = "website"

    url = Column(String, primary_key=True, index=True, unique=True)
    avg_bias = Column(Float, server_default=0.5, nullable=False)
    num_data_points = Column(Integer, server_default=0, nullable=False)
