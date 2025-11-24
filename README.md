# AI_Vision_pipline_with_AZURE
<img width="1912" height="907" alt="Screenshot 2025-11-24 194810" src="https://github.com/user-attachments/assets/c91a7d93-b33b-4262-809c-4c38fac8db50" />
Image-to-Multilingual-Story AI Pipeline (Azure + Gemini + Gradio)

Image-to-Multilingual-Story AI Pipeline (Azure + Gemini + Gradio)

This project demonstrates a complete AI pipeline that transforms a single uploaded image into a creative story, rewritten in a selected style, and translated into any language — all in one seamless Gradio web app.

The workflow integrates:

Azure Computer Vision → Image understanding

Google Gemini (gemini-2.5-flash) → Creative story generation & style transformation

Azure Translator → Multilingual translation

Gradio → Interactive front-end

The entire pipeline is implemented as a single-file Python application for clarity and portability.

🚀 Overview

This project shows how to orchestrate multiple AI providers inside one workflow by:

Combining vision, generation, style modification, and translation into a single user request.

Managing API keys securely with environment variables.

Maintaining a clean, production-friendly architecture that is easy to deploy anywhere (local, Azure, Docker, etc.).

Providing a user-friendly Gradio interface to experiment with the pipeline in real time.

🧠 Pipeline Architecture
graph TD
    A[Image Input (Gradio)] --> B(Vision API - Azure CV)
    B --> C(Creative Text Generation - Gemini)
    C --> D(Style Transformation - Gemini)
    D --> E(Translation - Azure Translator)
    E --> F[Multilingual Output (Gradio)]

    style A fill:#4CAF50,stroke:#333,stroke-width:2px
    style B fill:#2196F3,stroke:#333,stroke-width:2px
    style C fill:#FFC107,stroke:#333,stroke-width:2px
    style D fill:#FFC107,stroke:#333,stroke-width:2px
    style E fill:#2196F3,stroke:#333,stroke-width:2px
    style F fill:#4CAF50,stroke:#333,stroke-width:2px

✨ Features
🔍 Image Understanding (Azure CV)

Extracts captions, tags, and object metadata.

✍️ Creative Story Generation (Gemini)

Creates context-aware stories based on vision output.

🎨 Style Transformation (Gemini)

Rewrites the base story into:

Poetic

Academic

Marketing

Fairy-tale

Or any custom style

🌍 Multilingual Translation (Azure Translator)

Produces final styled story in dozens of supported languages.

🖥️ Web Interface Demo (Gradio)

Clean, single-page UI for interactive testing.

🧰 Tech Stack
Component	Technology
Computer Vision	Azure Cognitive Services
Translation	Azure Translator
Generative AI	Google Gemini (gemini-2.5-flash)
Front-end	Gradio
Language	Python
Dev Environment	Azure Machine Learning Studio Notebooks
📦 Installation
1. Clone the Repository
git clone https://github.com/<your-username>/AI_Vision_Pipeline_with_AZURE.git
cd AI_Vision_Pipeline_with_AZURE

2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables

You must set:

export AZURE_CV_ENDPOINT="https://<your-cv-resource>.cognitiveservices.azure.com/"
export AZURE_CV_KEY="<YOUR_AZURE_CV_KEY>"
export GEMINI_API_KEY="<YOUR_GEMINI_KEY>"
export AZURE_TRANS_KEY="<YOUR_TRANSLATOR_KEY>"
export AZURE_TRANS_REGION="uaenorth"


Or create a .env file:

AZURE_CV_ENDPOINT=https://<your-cv-resource>.cognitiveservices.azure.com/
AZURE_CV_KEY=YOUR_AZURE_CV_KEY
GEMINI_API_KEY=YOUR_GEMINI_KEY
AZURE_TRANS_KEY=YOUR_TRANSLATOR_KEY
AZURE_TRANS_REGION=uaenorth
