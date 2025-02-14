from pysat.solvers import Glucose3

p = 1   # Suite de Richard
q = 2   # Sala de Máquinas
r = 3   # Cocina

      # Armas
s = 4   # Llave inglesa
t = 5   # Cuchillo de cocina
k = 6   # Cable eléctrico

      # Sospechosos
E = 7   # Eleanor Graves
L = 8   # Lila Hart
D = 9   # Dr. Samuel Reeves
M = 10  # Maggie Sullivan
V = 11  # Victor Kane
clauses = []
def startGame():
          
    
    logicalPropositions = []
    SatSolver = [(" \n (¬t or ¬p)"), ("\n(L or V)"), ("\n(¬q or s)"), ("\n(¬M or ¬V)"), ("\n¬t"), ("\n(¬M)"), ("\n(¬r)"),("\n¬D"), ("\n¬E"), ("\n(k or q)"), ("\n(D or V)")  ]
    
    print("Comienza el juego \n")
    print("""
           -------------------------------------------------------------------------
          \n
          En esta historia, un crimen ha ocurrido a bordo del SS Elysium.
          Usaremos lógica proposicional y un SAT-Solver para encontrar al culpable.
          \n
           -------------------------------------------------------------------------""")
  
    input(" \n Presiona enter para continuar...") 

    print("""
          -------------------------------------------------------------------------
          -------------------------------------------------------------------------
          El narrador dice: \n
          El barco de lujo SS Elysium navega por aguas oscuras y tormentosas en medio del océano.\n
          A bordo, cinco pasajeros se encuentran atrapados después de que una violenta tormenta\n
          cortara las comunicaciones y dejará la embarcación a la deriva. \n
          Entre ellos, se esconde un asesino.\n
          El magnate Richard Blackwood ha sido encontrado asesinado en su suite. \n
          La única forma de descubrir la verdad es a través de la lógica. \n
          Cada sospechoso ha hecho una declaración, y las traduciremos en proposiciones \n 
          lógicas para alimentar el SAT-Solver. \n

          -------------------------------------------------------------------------
          -------------------------------------------------------------------------
          """)
    input(" \n Presiona enter para continuar...") 
    print("""
          -------------------------------------------------------------------------
          -------------------------------------------------------------------------
          El narrador dice: \n
          La víctima, Richard Blackwood, un magnate arrogante y despiadado,\n
          es encontrado muerto en su suite. \n
          Todos tienen motivos para odiarlo: chantajes, traiciones y secretos oscuros salen a la luz.\n
          Pero solo uno de ellos lo mató. \n
          Las armas que pudieron haber asesinado a Richard: \n
          🗡️ Posibles armas \n
            🔪 Cuchillo de cocina – Afilado, letal y vinculado a la chef del barco.\n
            🔧 Llave inglesa – Pesada, contundente y útil en la sala de máquinas.\n
            ⚡ Cable eléctrico – Un método silencioso y calculado.\n
          Tu eres el detective Trevor Knott y ahora escuchas las declaraciones de cada sospechoso. \n
          Empecemos con definir las proposiciones que usaremos en este juego.\n
          -------------------------------------------------------------------------
          -------------------------------------------------------------------------
          """)
    input(" \n Presiona enter para continuar... \n") 
    print(""" \n
        p = El lugar del crimen fue la Suite de Richard. \n
        q = El lugar del crimen fue la sala de Máquinas. \n
        r = El lugar del crimen fue la cocina. \n
        s = El arma fue la llave inglesa. \n
        t = El arma fue el cuchillo de cocina. \n
        k = El arma fue el cable eléctrico.\n
        E = El culpable es Eleanor Graves. \n
        L = El culpable es Lila Hart. \n
        D = El culpable es Dr. Samuel Reeves. \n
        M = El culpable es Maggie Sullivan.\n
        V = El culpable es Victor Kane.\n
        """) 

    print(" \n Ahora estamos en condiciones de escuchar nuestra primera sospechosa.... \n")
    input(" \n Presiona enter para continuar... \n") 
          
    print(""" \n
          Eleonor Granves dice: \n
          💬 "Si el arma no fue un cuchillo de cocina, entonces el crimen no ocurrió \n
              en la Suite de Richard." \n
          📜 Proposición lógica: (¬t ∧ ¬p) \n
          Además agregá:\n
          💬 "Si el culpable no es Lila Hart, entonces el culpable es Victor Kane" \n
          📜 Proposición lógica:  ( ¬ L → V) \n
          🔍 Contexto: Eleanor Graves, una mujer fría y calculadora, ex socia de Richard, \n 
            ha sido traicionada en un turbio negocio.\n
           Su afirmación sugiere una relación entre el arma y el lugar del crimen.\n
           ¿Es una pista clave o una distracción? ¿Conoce más de lo que dice? \n
          
          \n
          Veamos que información obtenemos de la siguiente declaración: \n
          """) 
    logicalPropositions.append("(¬t ∧ ¬p)")
    logicalPropositions.append("( ¬ L → V)")
    clauses.append([t, -p])
    clauses.append([L, V])
    input(" \n Presiona enter para continuar... \n")

    print(""" \n
          Lila Hart. \n
          🔍 Contexto: \n
          Tras interrogar a Lila Hart, una extraña sensación me invade. \n
          Su mirada esquiva y la manera en que juega nerviosamente con un mechón \n
          de su cabello me indican que esconde algo. Habla en susurros, eligiendo \n
          cuidadosamente cada palabra, como si temiera revelar demasiado.\n
          Cuando le pregunto sobre el crimen, su respuesta es clara pero fría: \n 
          💬 ‘Si el crimen ocurrió en la Sala de Máquinas, entonces el arma fue una llave inglesa’.\n
          📜 Proposición lógica: (q -> s) \n
          Además agregó:\n
          💬 'Si el culpable es Maggie Sullivan, entonces el culpable no es Victor Kane. \n
          Proposición lógica: (M → ¬V).\n
          No titubea, no duda. Pero en su tono hay algo más… ¿conocimiento o simple coincidencia? \n
          Algo me dice que esta mujer sabe más de lo que admite. \n
          
          \n
          Veamos que información obtenemos del Dr. Samuel Reeves: \n
          """) 
    logicalPropositions.append("(q -> s)")
    logicalPropositions.append("(M → ¬V)")
    clauses.append([-q, s])
    clauses.append([-M, -V])
    
    input(" \n Presiona enter para continuar... \n")
    print(""" \n
          Dr. Samuel Reeves. \n
          🔍 Contexto: \n
          El Dr. Reeves se muestra sereno, demasiado sereno. Su bata impecable y su postura \n
          recta contrastan con la tensión que flota en el aire. Mientras habla, sus manos \n
          juegan con su reloj de bolsillo, un gesto casi involuntario, pero revelador. \n
          Cuando le pregunto sobre el crimen, su respuesta es directa, sin adornos: \n 
          💬 ‘El crimen no ocurrió en la Cocina’. \n
          📜 Proposición lógica: ¬r \n
          💬 ‘El culpable no soy yo, ni es Eleanor Graves.’. \n
          📜 Proposición lógica: (¬D and ¬E) \n
          Su tono es seguro, pero su mirada se desvía apenas un instante. ¿Un intento de \n
          ocultar algo o simple costumbre? Algo en él no encaja del todo. \n
          
          \n
          Veamos qué información obtenemos de la declaración de Maggie Sullivan \n
          """) 
    logicalPropositions.append("¬r")
    logicalPropositions.append("(¬D and ¬E)")
    clauses.append([-r])
    clauses.append([-D])
    clauses.append([-E])

    input(" \n Presiona enter para continuar... \n")

    print(""" \n
          Maggie Sullivan. \n
          🔍 Contexto: \n
          Maggie Sullivan cruza los brazos, su expresión es severa. Sus manos, \n
          marcadas por años de trabajo en la cocina, sostienen un cuchillo con \n
          demasiada familiaridad. Su mirada es intensa, escrutadora, como si \n
          estuviera analizando cada una de mis palabras antes de responder. \n
          Finalmente, con un suspiro pesado, suelta su declaración: \n
          💬 ‘Si el arma no fue un cable eléctrico, entonces el crimen ocurrió en la Sala de Máquinas’. \n
          📜 Proposición lógica: (¬k → q) \n
          💬 ‘Si el culpable no es Samuel Reeves, entonces el culpable es Victor Kane'. \n
          📜 Proposición lógica: ( ¬ D → V) \n
          Su voz es firme, pero hay una ligera vacilación en su tono. ¿Es miedo, \n
          duda o simplemente cautela? Algo en su actitud me dice que sabe más \n
          de lo que está dispuesta a confesar. \n
          
          \n
          Veamos qué información obtenemos de la siguiente declaración: \n
          """)
    logicalPropositions.append("(¬k → q)")
    logicalPropositions.append("( ¬ D → V)")
    clauses.append([k, q])
    clauses.append([D, V])
    input(" \n Presiona enter para continuar... \n")
    print(""" \n
          Victor Kane. \n
          🔍 Contexto: \n
          Tras interrogar a Victor Kane, me siento en una encrucijada. \n
          Su postura rígida y su mirada fija evitan cualquier contacto visual directo. \n
          Sus respuestas son precisas, casi mecánicas, como si estuviera \n
          evitando el mínimo error. Al preguntarle sobre el crimen, su respuesta \n
          es tajante: 
          💬 ‘El arma no fue un cuchillo de cocina’.\n
          📜 Proposición lógica: (¬t) \n
          💬 ‘El culpable no es Maggie Sullivan.’.\n
          📜 Proposición lógica: ( ¬M) \n
          La convicción con la que lo dice no deja lugar a dudas, pero hay algo \n
          en su actitud que me hace pensar que aún está ocultando más. \n
          
          \n
          Veamos que información recolectamos hasta el momento: \n
          """)
    logicalPropositions.append("(¬t)")
    logicalPropositions.append("( ¬M)")
    clauses.append([-M])
    clauses.append([-t])
    clauses.append([-p, -q])
    clauses.append([-p, -r])
    clauses.append([-q, -r])
    clauses.append([-s, -t])
    clauses.append([-s, -k])
    clauses.append([-t, -k])
    clauses.append([-E, -L])
    clauses.append([-E, -D])
    clauses.append([-E, -M])
    clauses.append([-E, -V])
    clauses.append([-L, -D])
    clauses.append([-L, -M])
    clauses.append([-L, -V])
    clauses.append([-D, -M])
    clauses.append([-D, -V])
    clauses.append([-M, -V])



    print("Proposiciones logicas obtenidas hasta el momento: \n" + "\n".join(logicalPropositions))
    input(" \n Presiona enter para continuar... \n")

    print(""" \n
      Soy el mejor detective! con estas declaraciones puedo encontrar el arma homicida \n
          y el culpable!, si traducimos estas proposiciones logicas obtenemos las siguentes CNF \n
      """)

    input(" \n Presiona enter para continuar... \n")
    
    print(""" 
          -------------------------------------------------------------------------
          -------------------------------------------------------------------------
          Debemos pasar las proposiciones logicas a CNF para poder usar el SAT-Solver \n
          Proposiciones lógicas obtenidas: \n
          """ + "\n".join(SatSolver) + "\n")

    input(" \n Presiona enter para continuar... \n")

    print(""" 
          -------------------------------------------------------------------------
          -------------------------------------------------------------------------
         Cada proposición debe transformarse en cláusulas disyuntivas para que el SAT-Solver pueda interpretarlas. \n
            En este caso: \n

            (¬t or ¬p)   \n


            Esto se convierte en: Si t, entonces p = [2, -1] \n

            (¬q or ¬s) \n

            Esto se convierte en: No q o s =[-3, 4]  \n

            No r = [-5]  \n

            (k or q)  \n

            Esto se convierte en: k o q = [6, 3]  \n

            (¬t)= [-2]  \n

            (L or V)  \n

            Esto se convierte en: L o V = [7, 10] \n

            (¬M or ¬V) \n

            Esto se convierte en: No M o no V = [-9, -10] \n

            No D y no E = [-8] y [-7] \n

            (D or V)\n

            Esto se convierte en: [8, 10] \n

            No M = [-9] \n

            Te desafio a que hagas tu acusación en usando los numeros proporcionados, \n
            y descubra quien es el culpable y quien es el arma homicida \n
            además, donde fue el crimen \n

            El formato para la acusación es el siguiente: \n
            
            lugar + arma + culpable \n

          -------------------------------------------------------------------------""")

    input(" \n Presiona enter para continuar... \n")

    print(""" \n
          ------------------------------------------------------------------------- \n
            Una pequeña ayuda a memoria \n
            # Lugares del crimen\n
            p = 1   # Suite de Richard\n
            q = 2   # Sala de Máquinas\n
            r = 3   # Cocina\n

            # Armas\n
            s = 4   # Llave inglesa\n
            t = 5   # Cuchillo de cocina\n
            k = 6   # Cable eléctrico\n

            # Sospechosos\n
            E = 7   # Eleanor Graves\n
            L = 8   # Lila Hart\n
            D = 9   # Dr. Samuel Reeves\n
            M = 10  # Maggie Sullivan\n
            V = 11  # Victor Kane\n

            """)

    input(" \n Presiona enter para continuar... \n")

    solver = Glucose3()
    for clause in clauses:
        solver.add_clause(clause)

    while True:
        user_input = input("Ingresa los valores separados por espacios (o escribe 'salir'): \n")

        if user_input.lower() == "salir":
            print("Saliendo del juego... ¡Hasta la próxima!\n")
            break

        arr = list(map(int, user_input.split()))

        if len(arr) != 3:
            print("Debes ingresar exactamente 3 valores.\n")
            continue

        if solver.solve():
            model = solver.get_model()

        if model is None:
            print("⚠️ No hay una solución válida en este momento.")
            continue

        # Tomar solo los valores positivos
        model_filtrado = [abs(x) for x in model if x > 0]

        # Validar si los números ingresados están en la solución
        if set(arr) <= set(model_filtrado):
            print("""\n🔍 ¡Solución encontrada! El culpable y los detalles del crimen son correctos. \n
            El culpable es : Victor Kane \n
            El arma usada fue: LLave inglesa \n
            El lugar en el que ocurrió fue: La sala de máquinas \n
            
            """)
            break
        else:
            print("\n🔍 No has encontrado la solución aún")

         # Identificar el lugar
        lugares = {p: "Suite de Richard", q: "Sala de Máquinas", r: "Cocina"}
        lugar_crimen = next((lugar for lugar in lugares if lugar in model), None)
        if (lugar_crimen == arr[0]):
            print(f"📍 \n Has identificado el lugar del crimen: \n El crimen ocurrió en: {lugares[lugar_crimen]}")
        else:
            print(f"📍 \n El lugar del crimen sigue siendo un misterio....")
        
         # Identificar el arma
        armas = {s: "Llave inglesa", t: "Cuchillo de cocina", k: "Cable eléctrico"}
        arma_usada = next((arma for arma in armas if arma in model), None)
        if (arma_usada == arr[1]):
            print(f" \n 🗡️ Has identificado el arma!: El arma usada fue: {armas[arma_usada]}")
        else:
            print(f" \n 🗡️ La arma usada sigue siendo un misterio....")

        # Identificar el culpable
        culpables = [var for var in [E, L, D, M, V] if var in model]
        if culpables:
            culpable = culpables[0]
            if(culpable == arr[2]):
                nombres = {E: "Eleanor Graves", L: "Lila Hart", D: "Dr. Samuel Reeves", M: "Maggie Sullivan", V: "Victor Kane"}
                print(f"\n 🕵️‍♂️ Has enconntrado a el culpable es: {nombres[culpable]}")
            else:
                print(f"\n 🕵️‍♂️ El culpable aún no ha sido descubierto! \n")
        


   
def logicGame():
    print(""" \n
          Hola, bienvenido al proyecto capstone de la asignatura Lógica. ¿Qué desea hacer? \n
          1. Jugar\n
          2. Conocé a los integrantes del equipo\n
          3. Salir \n
          \n
          """)
   

    option = int(input("Elige una opción: "))
    if option == 1:
        startGame()
    elif option == 2:
        print(""" \n
         Los integrantes del equipo son: \n
         2. Arroyo Matías Ariel \n
         1. Megna Juan Ignacio \n
         2. Peano Melisa Raquel \n
         2. SalomónMartin Ignacio \n
         """)
    elif option == 3:
        exit()

logicGame()