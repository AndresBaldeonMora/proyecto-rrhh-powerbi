# Proyecto RR.HH – Limpieza de Datos y Power BI

Este repositorio documenta un flujo de trabajo completo de análisis de datos en **Power BI**, partiendo de un dataset con errores simulados (“sucio”) y aplicando un proceso de limpieza inicial con **Python (Pandas)**, seguido de transformaciones adicionales en **Power Query (Power BI)**.

---

## 📂 Archivos principales
- `Base_De_Datos_Sucia.xlsx` → Dataset con **nulos y duplicados** añadidos artificialmente para simular un caso real de datos desordenados.
- `limpiar_bd.py` → Script en **Python** que elimina **nulos** y **duplicados** de cada hoja del Excel.
- `Base_de_Datos_Limpia.xlsx` → Dataset limpio generado automáticamente por el script (equivalente al dataset original).
- Carpeta `Power BI/` → Proyecto de visualización en Power BI, donde se aplicaron pasos de **Power Query**.

---

## 🔄 Flujo del proyecto
1. **Dataset inicial:**  
   Se parte de `Base_De_Datos_Sucia.xlsx`, donde se introdujeron nulos y duplicados en distintas hojas.

2. **Limpieza en Python:**  
   Se ejecuta el script de limpieza:
   ```bash
   python limpiar_bd.py
