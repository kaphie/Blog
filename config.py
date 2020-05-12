import os

from dotenv import load_dotenv as ld

ld()


class Config:
    debug = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SENDGRID_API_KEY=os.environ.get('SENDGRID_API_KEY')
    DEFAULT_SENDGRID_SENDER =  os.environ.get('DEFAULT_SENDGRID_SENDER')
    SQLALCHEMY_DATABASE_URI = 'postgres://sxhyfsrgirzqtx:02673b1019b23b437ab2ef728e47d819e23a21ec990c95fba7d97bb6ed460f37@ec2-34-230-149-169.compute-1.amazonaws.com:5432/dapepg93sbnl39'

    #  email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
