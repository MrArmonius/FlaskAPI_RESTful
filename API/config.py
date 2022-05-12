

class Config(object):
    TESTING = False

    #Def CuraEngine Path
    CURAENGINE= '/home/mrarmonius/Documents/Site_Impression3D/CuraEngineInstallation/CuraEngine/build/CuraEngine'
    
    #Def Path Input STL and Output GCODE
    PATH_STL='/home/mrarmonius/Documents/Site_Impression3D/FlaskAPI_RESTful/stl/'
    PATH_GCODE='/home/mrarmonius/Documents/Site_Impression3D/FlaskAPI_RESTful/gcode/'

class ProductionConfig(Config):
    DATABASE_URI= ''

class DevelopmentConfig(Config):
    DATABASE_URI= 'otherthings'


    #Def of path for def.json config files
    PATH_JSON_CURAENGINE= '/home/mrarmonius/Documents/Site_Impression3D/CuraEngineInstallation/config/'
    FDMPRINTER_DEF= PATH_JSON_CURAENGINE + 'fdmprinter.def.json'
    DEFAULT_PRINTERDEF= PATH_JSON_CURAENGINE + 'prusa_i3.def.json'

class TestingConfig(Config):
    DATABASE_URI= 'againotherthings'
    TESTING= True