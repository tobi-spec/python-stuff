from sqlalchemy import create_engine

# postgres
# dialect+driver://username:password@host:port/dbname
# SQLAchlemy uses psycopg2 database driver communicates with postgresSQL
engine = create_engine('postgresql+psycopg2://admin:admin@localhost:5432/exampledb', echo=True)