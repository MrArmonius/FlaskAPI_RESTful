

class Config(object):
    TESTING = False

    #Def CuraEngine Path
    CURAENGINE= 'CuraEngine'
    
    #Def Path Input STL and Output GCODE
    PATH_STL='./stl/'
    PATH_GCODE='./gcode/'

class ProductionConfig(Config):
    DATABASE_URI= ''

class DevelopmentConfig(Config):
    DATABASE_URI= 'otherthings'


    #Def of path for def.json config files
    PATH_JSON_CURAENGINE= '/home/armonius/Documents/flask/FlaskAPI_RESTful/config_curaengine/'
    FDMPRINTER_DEF= PATH_JSON_CURAENGINE + 'fdmprinter.def.json'
    DEFAULT_PRINTERDEF= PATH_JSON_CURAENGINE + 'prusa_i3.def.json'

class TestingConfig(Config):
    DATABASE_URI= 'againotherthings'
    TESTING= True