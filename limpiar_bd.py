import pandas as pd

INPUT_FILE  = "Base_de_Datos_Sucia.xlsx"
OUTPUT_FILE = "Base_de_Datos_Limpia.xlsx"

def limpiar_hoja(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    reporte = {}
    total_inicial = len(df)

    df_sin_nulos = df.dropna(how="any")
    eliminadas_por_nulos = total_inicial - len(df_sin_nulos)

    df_limpio = df_sin_nulos.drop_duplicates()
    eliminadas_por_duplicados = len(df_sin_nulos) - len(df_limpio)

    reporte.update({
        "filas_iniciales": total_inicial,
        "eliminadas_por_nulos": eliminadas_por_nulos,
        "eliminadas_por_duplicados": eliminadas_por_duplicados,
        "filas_finales": len(df_limpio),
    })
    return df_limpio, reporte

def main():
    libro = pd.read_excel(INPUT_FILE, sheet_name=None)

    limpio = {}
    print("=== LIMPIEZA DE LIBRO ===")
    for nombre_hoja, df in libro.items():
        df_limpio, rep = limpiar_hoja(df)
        limpio[nombre_hoja] = df_limpio

        print(f"\n[{nombre_hoja}]")
        print(f"  Filas iniciales:          {rep['filas_iniciales']}")
        print(f"  Eliminadas por nulos:     {rep['eliminadas_por_nulos']}")
        print(f"  Eliminadas por duplicados:{rep['eliminadas_por_duplicados']}")
        print(f"  Filas finales:            {rep['filas_finales']}")

    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        for nombre_hoja, df in limpio.items():
            df.to_excel(writer, sheet_name=nombre_hoja, index=False)

    print(f"\n✅ Limpieza completada. Archivo generado: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()