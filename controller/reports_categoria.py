from config.app import *
import pandas as pd
import os

def GenerateReportVentasCategoria(app: App):
    """Genera un reporte de ventas por categoría y lo guarda en un archivo CSV."""
    conn = app.bd.getConection()
    
    query = """
        SELECT 
            c.name AS category_name,  -- Usamos 'name' porque 'category_name' no existe
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            PRODUCTOS p ON v.product_id = p.product_id
        JOIN 
            CATEGORIAS c ON p.category_id = c.id  -- Se usa 'c.id' como clave de categoría
        GROUP BY 
            c.name
        ORDER BY 
            total_vendido DESC;
    """
    
    # Ejecutar la consulta y convertir los resultados en un DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Definir la ruta donde se guardará el archivo CSV
    path = "/workspaces/proyecto_final/files/reporte_ventas_categorias.csv"
    
    # Asegurar que la carpeta 'files/' existe antes de guardar
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    # Guardar el reporte en un archivo CSV
    df.to_csv(path, index=False)
    
    print(f"✅ Reporte generado correctamente: {path}")

    # Enviar el reporte por correo (opcional)
    sendMail(app, path)

def sendMail(app: App, data):
    """Función para enviar el reporte por correo."""
    app.mail.send_email(
        'from@example.com', 
        '📊 Reporte de Ventas por Categoría', 
        'Adjunto el reporte de ventas por categoría.', 
        data
    )