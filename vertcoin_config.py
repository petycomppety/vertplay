from configparser import ConfigParser
 
 
def read_vertcoin_config(filename='config.ini', section='vertcoin'):

    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)
 
    # get vertcoin section
    if parser.has_section(section):
        vertuser = parser['vertcoin']['user']
        vertpass = parser['vertcoin']['password']         
    else:
        raise Exception('Vertcoin settings not found in the config.ini file'.format(section, filename))
 
    return vertuser, vertpass