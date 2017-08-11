import os

from flask import *
from werkzeug.utils import secure_filename
from flask_sqlalchemy import *

from sqlalchemy import *
from flask import Flask, render_template
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("postgresql://postgres:123@localhost/teste")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
