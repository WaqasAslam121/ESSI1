from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

#SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Netsolpk1@localhost:5432/Blog"
'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
'''
'''
# p1008057155153-qa0qp8@gcp-sa-cloud-sql.iam.gserviceaccount.com
engine = create_engine(
    "postgresql://postgres:Netsolpk1@localhost:5432/Blog")
'''

engine = create_engine(
    "postgresql://postgresessi:978K0RHW5L2UJVpWbQmzsWezC1QMi2Dg@dpg-cg0dk45269vdqr9mpt10-a.oregon-postgres.render.com/blog_1bqo")

#postgres://postgresessi:978K0RHW5L2UJVpWbQmzsWezC1QMi2Dg@dpg-cg0dk45269vdqr9mpt10-a.oregon-postgres.render.com/blog_1bqo

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
