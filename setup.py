import configparser

print("you only need to run this once")
bottoken = str(input("enter discord account token: "))
pekosecurity = str(input("enter pekosecurity token: "))


def create_config():
    config = configparser.ConfigParser()

    config['General'] = {'bottoken': bottoken, 'pekosecurity': pekosecurity}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)


if __name__ == "__main__":
    create_config()