import os
import subprocess
import sys

# Répertoire pour le rapport HTML
report_dir = "flake8-report"

# Commande pour exécuter flake8 et générer le rapport HTML
flake8_command = ["flake8", "--format=html", f"--htmldir={report_dir}"]

# Exécution de la commande flake8
result = subprocess.run(flake8_command, capture_output=True, text=True)

# Vérification du résultat de flake8
if result.returncode == 0:
    print("Aucune erreur de linting détectée.")
    # Génération d'un fichier HTML vide
    os.makedirs(report_dir, exist_ok=True)
    with open(os.path.join(report_dir, "index.html"), "w") as f:
        f.write("<html><body><h1>Aucune erreur de linting détectée</h1></body></html>")
else:
    print(
        f"Des erreurs de linting ont été détectées. Consultez le rapport dans le répertoire {report_dir}."
    )
    print(result.stdout)

# Affichage de l'emplacement du rapport
print(f"Rapport Flake8 généré à : {os.path.abspath(report_dir)}")
