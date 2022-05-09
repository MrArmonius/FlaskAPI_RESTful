

class Config(object):
    TESTING = False

    #Def CuraEngine Path
    CURAENGINE= '/home/mrarmonius/Documents/Site_Impression3D/CuraEngineInstallation/CuraEngine/build/CuraEngine'
    

class ProductionConfig(Config):
    DATABASE_URI= ''

class DevelopmentConfig(Config):
    DATABASE_URI= 'otherthings'


    #Def of path for def.json config files
    PATH_JSON_CURAENGINE= ''
    FDMPRINTER_DEF= PATH_JSON_CURAENGINE + ''
    DEFAULT_PRINTERDEF= PATH_JSON_CURAENGINE + ''

class TestingConfig(Config):
    DATABASE_URI= 'againotherthings'
    TESTING= True