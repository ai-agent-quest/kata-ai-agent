# Base image identique à ton devcontainer
FROM mcr.microsoft.com/devcontainers/python:3.13

# Installer Git et curl
RUN apt-get update && apt-get install -y git curl && rm -rf /var/lib/apt/lists/*

# Installer JupyterLab
RUN pip install --no-cache-dir jupyterlab

ENV PATH="/root/.local/bin:$PATH"

# Créer le répertoire de travail pour les notebooks
WORKDIR /workspace

# Cloner ton repo (optionnel si tu veux qu'il soit copié lors du build)
RUN git clone -b binder https://github.com/ai-agent-quest/kata-ai-agent.git .

# Installer Astral UV et synchroniser
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && uv sync

# Exposer le port Jupyter
EXPOSE 8888

# Variables d'environnement pour le token (passées via Render API)
ENV NOTEBOOK_TOKEN="changeme"

# Lancer JupyterLab avec token
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=${NOTEBOOK_TOKEN}", "--NotebookApp.notebook_dir=/workspace"]
