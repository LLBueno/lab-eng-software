from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(DATABASE_URL, convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    '''
    Todos os models devem ser importados aqui, caso contrário
    deve-se importar todos manualmente antes de chamar init_db().
    '''
    import app.core.models
    Base.metadata.create_all(bind=engine)
