from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Raíz del código (src)
SRC_DIR = Path(__file__).resolve().parent
DATA_DIR = SRC_DIR / "data" / "clean"

## GUARDAR DF
def guardar_pickle(df, archivo="df.pkl"):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ruta = DATA_DIR / archivo
    df.to_pickle(ruta)
    print(f"DataFrame guardado en: {ruta}")

# -----------------------------------------------------------
## CARGAR DF
def cargar_pickle(nombre_archivo):
    ruta = DATA_DIR / nombre_archivo
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo: {ruta}")
    return pd.read_pickle(ruta)

# -----------------------------------------------------------

## ASIGNACIÓN DE RANGO EDAD
def rango_edad(edad, start=24, step=5, end=73):
    if edad < start:
        return f"<{start}"
    if edad > end:
        return f">{end}"
    
    rango_inicio = start + ((edad - start) // step) * step
    rango_fin = rango_inicio + step - 1 
    return f"{int(rango_inicio)}-{int(rango_fin)}"

# -----------------------------------------------------------

## ASIGNACIÓN PERFIL MARCA
def perfil_marca(marca):
    if marca in ('Shiseido','Dior'):
        return 'Lujo'
    elif marca in ('Weleda', 'Lush'):
        return 'Natural'
    elif marca in ('Avene','Cerave'):
        return 'Dermo'
    else:
        return 'Trendy'

# -----------------------------------------------------------

## GUARDAR GRÁFICOS 
def guardar_grafico(fig, nombre_base, formato="jpg", dpi=300):
    actual = Path.cwd()
    ROOT = None

    for parent in [actual] + list(actual.parents):
        if parent.name == "src":
            ROOT = parent.parent
            break

    if ROOT is None:
        raise FileNotFoundError(
            "No se pudo detectar la raíz del proyecto"
        )

    ruta_figures = ROOT / "figures"
    ruta_figures.mkdir(parents=True, exist_ok=True)

    ruta_archivo = ruta_figures / f"{nombre_base}.{formato}"

    fig.savefig(ruta_archivo, bbox_inches="tight", dpi=dpi)
    plt.close(fig)

    print(f"Gráfico guardado en: {ruta_archivo}")

