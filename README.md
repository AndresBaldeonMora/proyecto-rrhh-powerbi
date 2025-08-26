# Proyecto RR.HH – Limpieza de Datos y Power BI

Este repositorio documenta un flujo de trabajo completo de análisis de datos en **Power BI**, partiendo de un dataset con errores simulados (“sucio”) y aplicando un proceso en **dos etapas**:

1. **Limpieza automática con Python (Pandas).**  
2. **Transformaciones adicionales en Power BI (Power Query).**

---

## 📂 Archivos principales
- `Base_De_Datos_Sucia.xlsx` → Dataset con **nulos y duplicados** añadidos artificialmente para simular un caso real de datos desordenados.
- `limpiar_bd.py` → Script en **Python** que elimina **nulos** y **duplicados** de cada hoja del Excel.
- `Base_de_Datos_Limpia.xlsx` → Dataset limpio generado automáticamente por el script (equivalente al dataset original sin nulos/duplicados).
- Carpeta `Power BI/` → Proyecto de visualización en Power BI, donde se aplicaron pasos de **Power Query**.

---

## 🔄 Flujo del proyecto
1. **Etapa 1 – Limpieza con Python:**  
   Se ejecuta el script:
   ```bash
   python limpiar_bd.py
