class Config :
    SQLALCHEMY_POOL_RECYCLE = 3600
    WTF_CSRF_ENABLED = True
    DEBUG = True 
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://addtoit:vinsan14248@datalocker.cvbtcsncwnmo.us-east-2.rds.amazonaws.com/storebox'
    