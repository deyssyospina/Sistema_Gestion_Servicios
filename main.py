# Geraldine Muñoz Jaramillo
# Deyssy Mariana Ospina
# Freddy Samir Bustos
# Codigo: 213023_102
# Ingenieria en Sistemas
# Autoria propia

# MODIFICACIONES REALIZADAS:
# 1. Separacion de errores controlados e inesperados.
# 2. Registro del tipo de excepcion.
# 3. Aviso de operaciones omitidas.
# 4. Seguimiento de operaciones dependientes.
# 5. Mejora en la presentacion del resumen.
# 6. Se agregaron siete simulaciones invalidas.
# 7. Se organizo la operacion 13.
# 8. Se centralizo el calculo de costos en Servicio.


# Importacion de las clases necesarias.
from cliente import Cliente
from servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)
from reserva import Reserva
from excepciones import ErrorSistema
from logs import registrar_evento, registrar_error


# Listas para almacenar clientes y servicios.
clientes = []
servicios = []


# Funcion para ejecutar y controlar cada operacion.
def ejecutar_operacion(numero, descripcion, accion):

    print(f"\nOPERACION {numero}: {descripcion}")

    try:
        # Ejecuta la accion correspondiente.
        resultado = accion()

        print("Resultado:", resultado)

        # Registra la operacion exitosa.
        registrar_evento(f"Operacion {numero}: {descripcion}")

        return resultado

    # MODIFICACION 1:
    # Se separan los errores controlados del sistema de los errores
    # inesperados, para facilitar su identificacion y manejo.
    except ErrorSistema as error:

        print("Error controlado:", error)

        registrar_error(
            f"Operacion {numero} (ErrorSistema): {error}"
        )

        return None

    # MODIFICACION 2:
    # Se identifica el tipo de excepcion y se registra en el log
    # para facilitar la revision de los errores inesperados.
    except Exception as error:

        print(f"Error inesperado ({type(error).__name__}):", error)

        registrar_error(
            f"Operacion {numero} (inesperado, {type(error).__name__}): {error}"
        )

        return None


# MODIFICACION 3:
# Se crea una funcion para informar cuando una operacion no puede
# ejecutarse por falta de datos o por el fallo de una operacion anterior.

# Funcion para informar cuando una operacion no se puede realizar.
def omitir_operacion(numero, descripcion, motivo):

    print(f"\nOPERACION {numero}: {descripcion}")
    print("Omitida:", motivo)

    registrar_error(
        f"Operacion {numero} omitida: {motivo}"
    )