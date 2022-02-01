from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
import os.path 
from os.path import join
from datetime import date
import pandas as pd

def get_pagos(fecha_desde, fecha_hasta, destino):
    codigos = ['1115 - a0601115 - Naranja10', '1128 - a0601128 - Naranja23',  '179 - a0600179 - neabajo1instancia179',  '243 - a0600243 - rosario1instancia243',  '549 - a0600549 - Cordoba1instancia549',  '866 - a0600866 - neuquen1instancia866',  '997 - a0600997 - riogrande1instancia997',  '149 - a0600149 - patagonia2instancia149',  '170 - a0600170 - ushuaia2instancia170',  '173 - a0600173 - litoral2instancia173',  '875 - a0600875 - ushuaia3instancia875',  '879 - a0600879 - lapampa3instancia879',  '939 - a0600939 - patagonia3instancia939',  '998 - a0600998 - patagonia3instancia998',  '368 - a0600368 - neuquen1instancia368',  '388 - a0600388 - santarosa1instancia388',  '886 - a0600886 - Naranja10']
    fecha_desde = str(fecha_desde)
    fecha_hasta = str(fecha_hasta)
    #Opciones de navegación
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-infobars")
    #options.add_argument('--start maximized')
    #options.add_argument('--disable extensions')
    download_dir = destino.replace('/','\\') 
    print( download_dir)
    profile = {"download.default_directory": download_dir,
                "savefile.default_directory": "C:\\"}
    options.add_experimental_option("prefs", profile)

    driver_path = '\\\\DC2.internal.gesinco.com.ar\\sistemas\\Procesadores - Vicky\\Descargador TN\\chromedriver.exe'

    driver = webdriver.Chrome(driver_path, options=options)

    #Iniciarla en la pantalla 2
    driver.set_window_position(2000, 0)
    driver.maximize_window()
    time.sleep(1)

    #Inicializamos el navegador
    driver.get('https://abogados.naranja.com/login_abogados.asp')

    for codigo in codigos:
        codigo = codigo.split(' - ')
        usuario = str(codigo[1])
        print(usuario)
        password = str(codigo[2])
        print(password)
        codigo = str(codigo[0])
        nombrearchivo = "Detalle_Cobranzas_Externas.csv"

        #Seleccionar inputs, botón y hacer click
        driver.find_element_by_css_selector("input.input_texto[name='Codigo']").send_keys(usuario)
        #codigo = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.CSS_SELECTOR, "input.input_texto[name='Codigo']")).send_keys('a0601115') NO FUNCA MÁS

        #AyudaBuscarElewmento
        # elemento = "[name='Codigo']"
        # rst= buscar_elementos.buscarelemento_por_nombre(driver_path, elemento, 5)
        # print(rst)

        driver.find_element_by_css_selector("input.input_texto[name='Contrasenia']").send_keys(password)
        #contrasenia = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(By.NAME, "Contrasenia")) NO FUNCA MÁS

        driver.find_element_by_css_selector("input.mybutton[name='Submit']").click()
        time.sleep(2)
        #ingresar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(By.CSS_SELECTOR,"input.mybutton[name='Submit']")).click() NO FUNCA MÁS

        #codigo.send_keys('a0601115')
        #contrasenia.send_keys('Naranja10')
        #ingresar.click()

        #SegundaPantalla
        driver.find_element_by_partial_link_text('Informes').click()
        driver.find_element_by_partial_link_text('Externas').click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        #driver.switch_to.active_element

        # empresa2 = driver.find_element_by_css_selector("select.input_texto[name='Empresa']")
        # print("WEBELEMENT_2")
        # print(empresa2)
        empresa = Select(driver.find_element_by_css_selector("select.input_texto[name='Empresa']"))
        empresa.select_by_visible_text("Indistinto")
        if codigo == '886' or codigo == '368' or codigo == '388':
            driver.find_element_by_css_selector("option[value='NEV']").click()
        else:
            driver.find_element_by_css_selector("option[value='NAR']").click()

        driver.find_element_by_css_selector("input[name='PadronDesde']").send_keys(fecha_desde)
        driver.find_element_by_css_selector("input[name='PadronHasta']").send_keys(fecha_hasta)

        driver.find_element_by_css_selector("input[name='Submit']").click()
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[0])

        driver.find_element_by_partial_link_text('Salir').click()

        unir_archivos(nombrearchivo, download_dir, codigo)


    return "Proceso Terminado"


# def cambiar_nombre_archivo(download_dir, codigo):
#     old_name = "Detalle_Cobranzas_Externas.csv"
#     new_name = str(codigo)+".csv"
#     file_oldname = os.path.join(download_dir, old_name)
#     file_newname_newfile = os.path.join(download_dir, new_name)
#     os.rename(file_oldname, file_newname_newfile)
#     unir_archivos(file_newname_newfile, download_dir, codigo)


def unir_archivos(nombre_archivo, download_dir, codigo):
    fecha = date.today().strftime("%d/%m/%Y")
    fecha = str(fecha).replace("/", ".")
    archivo_pagos = download_dir + "\\Pagos_TN_"+fecha+".csv"
    archivo_remove = download_dir + nombre_archivo
    archivo = os.path.join(download_dir, nombre_archivo)
    with open(archivo_pagos, 'a') as pagos:
        pagos.write("ESTADO;TIPODOC;NRODOC;APELLIDO;NOMBRE;PRODUCTO;NROPRODUCTO;INICIOMORA;FINMORA;EMPRESA;NROARQUEO;LUGAR_PAGO;NRORECIBO;FECHAPAGO;ULTIMO_PAGO;PAGO_TOTAL;CAPITAL;FINANCIEROS;PUNITORIOS;IVAINTERESES;HONORARIOS;IVAHONORARIOS;ISOM;CODIGO\n")
    with open(archivo, 'r+') as nombre_archivo:
        nombre_archivo.readline()
        for line in nombre_archivo:
            salida = open(archivo_pagos, 'a+')
            line = line.replace('\n', '')
            linea = (line+";"+str(codigo)+"\n")
            salida.write(linea)
        nombre_archivo.close()
        os.remove(archivo_remove)











