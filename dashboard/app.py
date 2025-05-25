from datetime import datetime
from flask import Flask, render_template, jsonify, send_file, make_response
import pandas as pd
import os
import sys
import io
from fpdf import FPDF

# ✅ Assure l'accès aux modules du dossier parent
sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from data_analysis.analyzer import detect_overconsumption
from comparison import compare_methods

app = Flask(__name__)

# 🔹 Route principale
@app.route('/')
def index():
    data_file = os.path.join('data_simulation', 'data.csv')
    data = None
    comparison_results = {}

    if os.path.exists(data_file):
        df = pd.read_csv(data_file)
        data = df.tail(20).to_dict(orient='records')

        stats = {
            "total_production": round(df['production'].sum(), 2),
            "total_consumption": round(df['consumption'].sum(), 2),
            "avg_production": round(df['production'].mean(), 2),
            "avg_consumption": round(df['consumption'].mean(), 2),
            "max_consumption": round(df['consumption'].max(), 2)
        }

        anomalies = detect_overconsumption(data_file)
        recent_anomalies = not anomalies.empty

        comparison_results = compare_methods(data_file)

        if comparison_results:
            linear_df = comparison_results["linear"]["data"].tail(20)
            meta_df = comparison_results["metaheuristic"]["data"].tail(20)
            comparison_results["linear"]["graph_data"] = linear_df.to_dict(orient="records")
            comparison_results["metaheuristic"]["graph_data"] = meta_df.to_dict(orient="records")
    else:
        stats = {}
        recent_anomalies = False

    return render_template(
        'index.html',
        data=data,
        stats=stats,
        has_anomalies=recent_anomalies,
        comparison=comparison_results
    )

# 🔹 Filtre Jinja pour formater les dates
@app.template_filter('datetimeformat')
def datetimeformat(value, format='%d/%m/%Y %H:%M:%S'):
    try:
        dt = datetime.fromisoformat(value)
        return dt.strftime(format)
    except Exception:
        return value

# 🔹 Route API AJAX
@app.route('/api/data')
def get_data():
    data_file = os.path.join('data_simulation', 'data.csv')
    if os.path.exists(data_file):
        df = pd.read_csv(data_file)
        data = df.tail(20).to_dict(orient='records')
        return jsonify(data)
    return jsonify([])

# 🔹 Export CSV
@app.route('/export/csv')
def export_csv():
    data_file = os.path.join('data_simulation', 'data.csv')
    comparison = compare_methods(data_file)

    if comparison:
        linear_df = comparison["linear"]["data"].copy()
        linear_df["method"] = "linear"
        meta_df = comparison["metaheuristic"]["data"].copy()
        meta_df["method"] = "metaheuristic"

        final_df = pd.concat([linear_df, meta_df], ignore_index=True)
        output = io.StringIO()
        final_df.to_csv(output, index=False)
        output.seek(0)

        return send_file(
            io.BytesIO(output.getvalue().encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='optimisation_resultats.csv'
        )
    return "Aucune donnée à exporter", 404

# 🔹 Export PDF
@app.route('/export/pdf')
def export_pdf():
    data_file = os.path.join('data_simulation', 'data.csv')
    comparison = compare_methods(data_file)

    if comparison:
        pdf = FPDF()
        pdf.add_page()

        # Titre principal
        pdf.set_font("Arial", 'B', 16)
        pdf.set_text_color(0, 102, 204)
        pdf.cell(0, 10, "Rapport d'Optimisation Énergétique", ln=True, align='C')
        pdf.ln(5)

        # Résumé de la meilleure méthode
        pdf.set_font("Arial", '', 12)
        best = comparison["best_method"].capitalize()
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(0, 10, f"La méthode '{best}' a été jugée optimale selon les critères de coût et d'autoconsommation.\n")

        pdf.ln(5)

        for method in ['linear', 'metaheuristic']:
            df = comparison[method]["data"].tail(10)

            # Titre de section
            pdf.set_font("Arial", 'B', 13)
            pdf.set_text_color(50, 50, 50)
            pdf.cell(0, 10, f"[{method.capitalize()}] Dernières 10 valeurs optimisées :", ln=True)
            pdf.ln(1)

            # En-tête tableau
            pdf.set_font("Arial", 'B', 11)
            pdf.set_fill_color(220, 220, 220)
            pdf.cell(60, 8, "Horodatage", 1, 0, 'C', True)
            pdf.cell(40, 8, "Production", 1, 0, 'C', True)
            pdf.cell(60, 8, "Conso Optimisée", 1, 1, 'C', True)

            # Contenu tableau
            pdf.set_font("Arial", '', 10)
            for _, row in df.iterrows():
                timestamp = row['timestamp'][:19].replace('T', ' ')
                prod = round(row['production'], 2)
                opti = round(row['optimized_consumption'], 2)
                pdf.cell(60, 8, timestamp, 1)
                pdf.cell(40, 8, f"{prod} kWh", 1)
                pdf.cell(60, 8, f"{opti} kWh", 1, ln=True)

            pdf.ln(5)

        # Génération du fichier PDF
        response = make_response(pdf.output(dest='S').encode('latin-1'))
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=rapport_optimisation.pdf'
        return response

    return "Aucune donnée à exporter", 404



# ✅ Lancement serveur Flask
if __name__ == '__main__':
    os.makedirs('data_simulation', exist_ok=True)
    app.run(debug=True)
