# AI_Vision_pipline_with_AZURE
<img width="1912" height="907" alt="Screenshot 2025-11-24 194810" src="https://github.com/user-attachments/assets/c91a7d93-b33b-4262-809c-4c38fac8db50" />
Image-to-Multilingual-Story AI Pipeline (Azure + Gemini + Gradio)

🌟 Project Title

Image-to-Multilingual-Story AI Pipeline (Azure + Gemini + Gradio)

💡 Overview

This project presents a robust, full-stack AI pipeline designed to transform a single image input into a creative, style-transferred, and translated textual output, delivered via an interactive web interface.

Built as a single, efficient Gradio application, the pipeline successfully chains services from different providers: Azure Cognitive Services handles the raw computer vision analysis and final translation, while Google Gemini performs the advanced creative writing and style transformation.

This demonstrates end-to-end orchestration, secure API management via environment variables, and the ability to combine best-in-class models into a unified user experience. The development environment was primarily based on Azure Machine Learning Studio (Notebooks).

⚙️ Tech Stack

Cloud Vision: Azure Computer Vision

Translation: Azure Translator

Generative AI: Google Gemini (gemini-2.5-flash)

Web Framework: Gradio

Orchestration & Tools: Python, Prompt Engineering

Development Environment: Azure Machine Learning Studio (Notebooks)

🌐 Pipeline Diagram

The pipeline executes a five-step transformation on every user submission:

graph TD
    A[Image Input (Gradio)] --> B(Vision API - Azure CV);
    B --> C(Creative Text Generation - Gemini);
    C --> D(Style Transformation - Gemini);
    D --> E(Translation - Azure Translator);
    E --> F[Multilingual Output (Gradio)];

    style A fill:#4CAF50,stroke:#333,stroke-width:2px
    style B fill:#2196F3,stroke:#333,stroke-width:2px
    style C fill:#FFC107,stroke:#333,stroke-width:2px
    style D fill:#FFC107,stroke:#333,stroke-width:2px
    style E fill:#2196F3,stroke:#333,stroke-width:2px
    style F fill:#4CAF50,stroke:#333,stroke-width:2px


✨ Key Features

Image Understanding: Utilizes Azure Computer Vision for accurate and detailed object recognition, tagging, and caption generation.

Creative Text Generation: Leverages the Gemini API for high-quality, contextual storytelling based on visual inputs.

Style Transformation (Fine-Tuning Lite): Implements dynamic prompt engineering to rewrite the base story into a selected style (e.g., academic, poetic, or marketing).

Multilingual Output: Integrates Azure Translator to deliver the final styled story in various languages, proving multilingual support.

Web Interface Demo: A user-friendly, single-page web interface (Gradio) for real-time demonstration and interaction.

📦 Setup and Installation

Prerequisites

Python 3.9+

API Keys for Azure Computer Vision, Azure Translator, and Google Gemini.

Steps

Clone the Repository:

git clone [your-repo-link]
cd AI_Vision_Pipeline_with_AZURE


Install Dependencies (from requirements.txt):

pip install -r requirements.txt


Configure Environment Variables (Securely): Set the following secrets in your shell or deployment platform's secret manager:

# Example values shown. Use your actual keys.
export AZURE_CV_ENDPOINT="[https://lab1mohamedosama.cognitiveservices.azure.com/](https://lab1mohamedosama.cognitiveservices.azure.com/)"
export AZURE_CV_KEY="[YOUR-AZURE-CV-KEY]"
export GEMINI_API_KEY="[YOUR-GEMINI-KEY]"
export AZURE_TRANS_KEY="[YOUR-TRANSLATOR-KEY]"
export AZURE_TRANS_REGION="uaenorth"
