from util.nebula import nebulaClient
from util.astro import astroClient

if __name__ == '__main__':
    nebula = nebulaClient()
    astro = astroClient()

    for variable in nebula.get_variables():
        astro.create_variable(key=variable['key'], value=variable['value'])
