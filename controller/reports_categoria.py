from config.app import *
import pandas as pd

def GenerateReportVentas(app: App):
    conn = app.bd.getConection()
    query = """
        SELECT 
            c.category_name,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            PRODUCTS p ON v.product_id = p.product_id
        JOIN 
            CATEGORIES c ON p.category_id = c.category_id
        GROUP BY 
            c.category_name
        ORDER BY 
            total_vendido DESC;
    """
    df = pd.read_sql_query(query, conn)
    
    # Guardar el reporte en un archivo CSV
    path = "/workspaces/proyecto_final/files/reporte_ventas_categorias.csv"
    df.to_csv(path, index=False)
    
    # Enviar el reporte por correo
    sendMail(app, path)

def sendMail(app: App, data):
    app.mail.send_email('from@example.com', 'Reporte de Ventas por Categoría', 'Adjunto el reporte de ventas por categoría.', data)
