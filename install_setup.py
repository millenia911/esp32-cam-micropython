def install_camweb_dep():
    import upip
    upip.install('picoweb')
    upip.install('micropython-ulogging')
    upip.install('ujson')
