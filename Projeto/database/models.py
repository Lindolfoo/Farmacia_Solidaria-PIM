from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Medicamento(Base):
    __tablename__ = "medicamentos"

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    quantidade = Column(Integer, nullable=False)
    validade = Column(Date, nullable=False)
    lote = Column(String(50), nullable=False)
    ativo = Column(Boolean, default=True)
