

def buscarelemento_por_nombre(driver,name_elemento,timeout):
    import time
    from selenium import webdriver
    intentos = 0
    elemento = None
    try:
        while( elemento is None and intentos < timeout):
                elemento = driver.find_elements_by_name(name_elemento)
                if(elemento is None):
                    time.sleep(1)
                    intentos=intentos+1
    except Exception as E:
        return str(E)
    
    return elemento

def buscarelemento_por_css(driver,name_elemento,timeout):
    import time
    from selenium import webdriver
    intentos = 0
    elemento = None
    try:
        while( elemento is None and intentos < timeout):
                elemento = driver.find_elements_by_css_selector(name_elemento)
                if(elemento is None):
                    time.sleep(1)
                    intentos=intentos+1
    except Exception as E:
        return str(E)
    
    return elemento

def buscarelemento_por_path(driver,name_elemento,timeout):
    import time
    from selenium import webdriver
    intentos = 0
    elemento = None
    try:
        while( elemento is None and intentos < timeout):
                elemento = driver.find_elements_by_xpath(name_elemento)
                if(elemento is None):
                    time.sleep(1)
                    intentos=intentos+1
    except Exception as E:
        return str(E)
    
    return elemento