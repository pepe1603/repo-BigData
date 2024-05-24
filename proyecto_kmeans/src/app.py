import pandas as pd
import plotly.express as px
from sklearn.cluster import KMeans
from shiny import App, ui, render, reactive
import tempfile
import os

# Cargar los datos limpios
df = pd.read_csv('data/WallCityTap_Consumer_clustered.csv')

# Definir la interfaz de usuario
app_ui = ui.page_fluid(
    ui.h2("Dashboard de Clustering K-means"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_slider("k_slider", "Número de clusters (K)", 3, 5, 3),
            ui.input_action_button("run_analysis", "Ejecutar Análisis")
        ),
        ui.panel_main(
            ui.div( ui.h2("Datos generales"),
                   
                   ui.output_table("data_table"),
            ui.output_image("cluster_plot"),
                   
                               ),

            ui.br(),
            ui.h2("Graficos relacionados a las preguntas de los directivos"),
            
            ui.output_image("age_plot"),
            ui.output_image("payment_plot"),
            ui.output_image("potential_customers_plot")
        )
    )
)

# Definir la lógica del servidor
def server(input, output, session):
    @reactive.Calc
    def clustered_data():
        k = input.k_slider()
        kmeans = KMeans(n_clusters=k, random_state=42)
        df['Cluster'] = kmeans.fit_predict(df[['Age', 'Annual_Income', 'Spending Score (1-100)']])
        return df

    @output
    @render.table
    def data_table():
        return clustered_data()

    @output
    @render.image
    async def cluster_plot():
        clustered_df = clustered_data()
        fig = px.scatter(
            clustered_df, x='Annual_Income', y='Spending Score (1-100)', color='Cluster',
            hover_data=['Age'], title=f"Clustering K-means (K={input.k_slider()})"
        )
        fig.update_layout(legend_title="Clusters", legend=dict(orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            fig.write_image(tmpfile.name)
            tmpfile.seek(0)
            return {"src": tmpfile.name, "alt": "Cluster Plot - Gráfico de Clústeres"}

    @output
    @render.image
    async def age_plot():
        age_data = df[df['Age'] > 50]
        fig = px.histogram(age_data, x='Spending Score (1-100)', nbins=20, title="Puntaje de Gasto de Clientes Mayores de 50 Años")
        fig.update_layout(legend_title="Edad", legend=dict(orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            fig.write_image(tmpfile.name)
            tmpfile.seek(0)
            return {"src": tmpfile.name, "alt": "Age Plot - Gráfico de Edad"}

    @output
    @render.image
    async def payment_plot():
        payment_counts = df['Payment_Methods'].value_counts().reset_index()
        payment_counts.columns = ['Medio de Pago', 'Cantidad']
        fig = px.pie(payment_counts, names='Medio de Pago', values='Cantidad', title="Métodos de Pago Preferidos")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            fig.write_image(tmpfile.name)
            tmpfile.seek(0)
            return {"src": tmpfile.name, "alt": "Payment Methods Plot - Gráfico de Métodos de Pago"}

    @output
    @render.image
    async def potential_customers_plot():
        clustered_df = clustered_data()
        potential_customers = clustered_df[clustered_df['Cluster'] == clustered_df['Cluster'].mode()[0]]
        fig = px.scatter(
            potential_customers, x='Annual_Income', y='Spending Score (1-100)', color='Age',
            title="Clientes Potenciales para Altas Ventas"
        )
        fig.update_layout(legend_title="Edad", legend=dict(orientation="h", yanchor="top", y=-0.1, xanchor="center", x=0.5))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
            fig.write_image(tmpfile.name)
            tmpfile.seek(0)
            return {"src": tmpfile.name, "alt": "Potential Customers Plot - Gráfico de Clientes Potenciales"}

# Crear la aplicación Shiny
app = App(app_ui, server)

if __name__ == "__main__":
    app.run()
