#-*- coding: utf-8 -*-
#se importa re(regular expressions) para obtener los predicados del texto
import re
    
def traduccion(tex):
    """la funcion traduccion utiliza la funcion de python "lambda"
    para obtener los predicados principales, ver su estructura y transformarlos en 
    formulas sencillas de leer 
    """
    tex = tex.replace(",","")
    #lista de palabras de cada categoria.

    vi = ["camina","bebe","durará","corre","rige","duerme","nada","sonrie", "vive", "baila", "come","canta","estornuda","fracasa","grita","llora","patina","pelea","respira","trabaja"]
    vt = ["desempeñar","emitir","figurará","cumplirá","somete","pagar","proporcionará","modificar","avisar","asume","aceptó","ama","presiona","responsabiliza","invita","firma","ingresó","alterar","lee","paga", "compromete", "estudia", "escribe","quiere","alimenta","asusta","dice","engaña", "evita", "llama","mira","olvida","necesita","molesta","perdona","visita", "viaja"]
    np = ["labores","boleta","títulos","ventas","montos","jornada","obligación","campo","insumos","actor","clausulas","Contrato","instrucciones","cocacola", "carulla","pedro","trabajador","empleador","maria", "juan", "javier","abel", "mario","valerie", "jose", "angela", "natalia", "rupaul", "carlos", "fernando", "alejandro", "miguel","esteban", "gabriela","oscar","samuel","victor","edgar", "carlos","eduardo", "sergio", "nicolas", "nathalia","camilo","sebastian","isabella","luisa","sara","rodrigo","angel", "daniel", "manuel","andres","felipe","david", "kevin","cristhian","edwin", "julian", "maría", "josé", "juana", "bart", "lisa"]
    viind = ["caminar","beber","durar","correr","regir","dormir","nadar","sonreir", "vivir", "bailar", "comer","cantar","estornudar","fracasar","gritar","llorar","patinar","pelear","respirar","trabajar"]
    vtind = ["desempeñar","emitir","figurar","cumplir","someter","pagar","proporcionar","modificar","avisar","asumir","aceptar","amar","presionar","responzabilizar","invitar","firmar","ingresar","alterar","leer","pagar", "comprometer", "estudiar", "escribir","querer","alimentar","asustar","decir","engañar", "evitar", "llamar","mirar","olvidar","necesitar","molestar","perdonar","visitar", "viajar"]
    
    words = tex.split(' ')
    
    categorias = []
    words2 = []
    #evalua cada palabra del predicado y si esta en alguna categoria la añade a la lista para las formulas 
    for w in words:
        if w in np:
            categorias.append('np')
            words2.append(w)
        #si la palabra es un verbo la reemplaza por su infinitivo 
        if w in vi:
            categorias.append('vi')
            wii = vi.index(w) 
            words2.append(viind[wii])
        elif w in vt:
            categorias.append('vt')
            wti = vt.index(w) 
            words2.append(vtind[wti])
    #si la longitud de el predicado despues de lo anteerior quedo en uno quiere decir que no es un predicado principal entonces no se evalua en las formulas 
    if len(words2) == 1:
        return 0   
    # asigna su debida expresión lógica a cada una de las palabras del predicado .
    traducciones = []
    
    for i in range(len(words2)):
        if categorias[i] == 'np':
            ini = words2[i]
            traducciones.append(lambda X, ini = ini: X(ini))
        elif categorias[i] == 'np':
            inicial = words2[i].lower()
            traducciones.append(lambda X, inicial=inicial: X(inicial))
        elif categorias[i] == 'vi':
            infini = words2[i]
            traducciones.append(lambda x, infini=infini: str(infini) + "(" + str(x) + ")")
        elif categorias[i] == 'vt':
            infini = words2[i]
            traducciones.append(\
            lambda XX:(lambda x:(XX(lambda y, infini=infini: (str(infini) + "(" + str(x) + "," + str(y) + ")")))))
            
    # Operar con las palabras de derecha a izquierda, aplicando la función lambda para integrar una expresión en otra
    n = len(traducciones)
    formula = traducciones[n-1]
    for i in range(0, n-1):
        j = (n - 2) - i
        formula = traducciones[j](formula)
            
    #retorna la formula sencilla final del predicado       
    return(formula)
 
def regex():
    """la funcion regex obtiene los predicados 
    principales del texto 
    """
    
    #lee los textos y los convierte en listas por lineas del archivo que se le ha dado
    texto1 = open("contrato.txt", "r")
    texto = ""
    for line in texto1:
        texto += line
    
    #busca en el texto el predicado que contenga el sujeto (patron_sujeto)que se le da y obtiene ese fragmento de texto hasta el primer punto 
    patron_sujeto = re.compile(r"[Ee]mpleador")
    patron_puntos = re.compile(r"[\.|\,]")
    
    matches_sujeto = patron_sujeto.finditer(texto)
    
    indices_puntos = re.finditer("\.",texto)
    
    lista_indices_puntos = []
    for punto in indices_puntos:
        lista_indices_puntos.append(punto.start(0))
    
    indices_sujeto = []
    for match in re.finditer(r"([Ee]mpleador|Contrato|actor)(\s)",texto):
        indices_sujeto.append(match.span())
    
    indice_inicial_sujeto = []
    for i in indices_sujeto:
        indice_inicial_sujeto.append(i[0])
    #guarda todo los predicados obtenidos anteriormente en una lista            
    lista_g = []
    
    for i in indice_inicial_sujeto:
        for a in lista_indices_puntos:
            if i < a:
                lista_g.append((i,a))
                break
    
    #busca en el texto el predicado que contenga el sujeto (patron_sujeto)que se le da y obtiene ese fragmento de texto hasta el primer punto 
    patron_sujeto = re.compile(r"[Tt]rabajador")
    patron_puntos = re.compile(r"[\.|\,]")
    
    matches_sujeto = patron_sujeto.finditer(texto)
    
    indices_puntos = re.finditer("\.",texto)
    
    lista_indices_puntos = []
    for punto in indices_puntos:
        lista_indices_puntos.append(punto.start(0))
    
    indices_sujeto = []
    for match in re.finditer(r"[Tt]rabajador(\s)",texto):
        indices_sujeto.append(match.span())
    
    indice_inicial_sujeto = []
    for i in indices_sujeto:
        indice_inicial_sujeto.append(i[0])
    
    #guarda todo los predicados obtenidos anteriormente en una lista             
    lista_f = []
    
    for i in indice_inicial_sujeto:
        for a in lista_indices_puntos:
            if i < a:
                lista_f.append((i,a))
                break
    #guardar todos los predicados en una lista y la retorna 
    frases = []
    for i in lista_g:
        m = texto[i[0]:i[1]]
        frases.append(m)  
             
    for i in lista_f:
        m = texto[i[0]:i[1]]
        frases.append(m) 
    return frases


def fragmentos(frases):
    """la funcion fragmentos es la que se encarga 
    de la ejecucion (el equivalente a la funcion main),
    esta da a conocer las formulas al usuario y da la 
    posibilidad para que acceda a su fragmento correspondiente 
    """
    
    #toma la lista retornada en regex() y obtiene las formulas de cada uno de sus elemetos por medio de traduccion() y las imprime
    frases2 = []
    count = 1
    for i in frases:
        m = traduccion(i)
        if m != 0:
            frases2.append(i)
            print("{0} : {1} ".format(count,m))
            count += 1             
    #se explica al usuario como va a hacer el proceso 
    print("Escoge el número del fragmento que quieres ver y si ya no quieres ver mas coloca 0 :) ")
    indice = 1
    count2 = 1 
    #pide al usuario el indice del fragmento y va y lo busca en la lista de regex() e imprime este.
    while indice != 0:
        indice = int(input("¿Que fragmento quieres ver? : "))
        #revisa que el indice que quiere ver el usuario esta dentro del rango de formulas y accede al indice menos uno de la lista de regex()(-1 ya que empieza desde cero)
        if indice > 0 and indice <= len(frases):
            print("{0} : {1}".format(indice,frases2[indice-1]))
        #para terminar el ciclo el usuario debe ingresar cero cuando ya no quiere acceder a mas fragmentos 
        elif indice == 0:
            print("Proceso terminado :3")
            break
        #si el inidice ingresado no esta en el rango le avisa al usuario y sigue el ciclo
        else:
            print("No tengo más fragmentos :( , escoge uno de los que estan o termina el proceso con cero")

#BEGINNING-OF-EXECUTION

m = regex()
fragmentos(m) 

#END-OF-EXECUTION



