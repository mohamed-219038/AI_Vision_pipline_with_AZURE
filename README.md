# **AI Multi-Service Pipeline: Vision, Creative Writing, Style Transfer, & Translation**
![Uploading Screenshot 2025-11-24 194810.png…]()


This project demonstrates a powerful, multi-stage AI pipeline that integrates three distinct services: **Azure Computer Vision**, **Gemini (Google's Generative AI)**, and **Azure Translator** within a unified Gradio web interface. The application takes an image input and performs a chain of analyses and transformations, showcasing seamless interaction between vision, text generation, and translation models.

The entire workflow, from image upload to final translated text, is executed in a single, efficient process.

## **🚀 Key Features & Workflow**

The application executes the following four steps in sequence:

1.  **Image Analysis (Azure Computer Vision):** The uploaded image is sent to Azure CV to generate descriptive **tags** and a short **caption**.
2.  **Creative Content Generation (Gemini):** Using the tags and caption from Step 1, the Gemini model writes a short, engaging, **creative paragraph** (The Base Text).
3.  **Style Transfer/Rewriting (Gemini):** The Base Text from Step 2 is rewritten by the Gemini model into a **user-selected style** (e.g., professional, Shakespearean, marketing).
4.  **Language Translation (Azure Translator):** The style-rewritten text from Step 3 is translated into a **target language** (e.g., Arabic, French) using Azure Translator.

## **🛠️ Technologies Used**

* **Front-end & Interface:** [Gradio](https://www.gradio.app/)
* **Vision AI:** [Azure Computer Vision](https://azure.microsoft.com/en-us/products/cognitive-services/computer-vision)
* **Generative AI & Rewriting:** [Gemini API (using `google-generativeai`)](https://ai.google.dev/gemini-api/docs)
* **Translation:** [Azure Translator](https://azure.microsoft.com/en-us/products/cognitive-services/translator)
* **Core Language:** Python (`requests`, `os`, `uuid`, `json`, `io`)

## **🖼️ Screenshot of the Application**
![Uploading Screenshot 2025-11-24 194810.png…]()



## **⚙️ Setup and Configuration**

### **1. Prerequisites**

* Python 3.8+
* The required API keys and endpoints for the services below.

### **2. Environment Variables**

The application relies on environment variables for secure key management. You **must** replace the placeholder values in your `app.py` or set these variables in your environment.

| Variable Name | Service | Description |
| :--- | :--- | :--- |
| `AZURE_CV_ENDPOINT` | Azure Computer Vision | Your Azure CV endpoint URL. |
| `AZURE_CV_KEY` | Azure Computer Vision | Your API key for the Azure CV service. |
| `GEMINI_API_KEY` | Gemini API | Your API key for the Gemini model. |
| `AZURE_TRANS_KEY` | Azure Translator | Your API key for the Azure Translator service. |
| `AZURE_TRANS_REGION` | Azure Translator | The region associated with your Translator resource (e.g., 'uaenorth'). |

### **3. Installation**

1.  **Clone the repository (or save `app.py`):**
    ```bash
    # If using git
    git clone [your-repo-link]
    cd [your-repo-name]
    # Otherwise, ensure app.py is saved locally
    ```

2.  **Install dependencies:**
    ```bash
    pip install gradio google-generativeai requests
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

The Gradio interface will launch, typically accessible at `http://127.0.0.1:7860` in your web browser.

## **📝 Customization**

* **Styles:** The list of available rewrite styles (`STYLE_OPTIONS`) can be easily updated in the `app.py` file to include other tones (e.g., "Pirate vernacular," "Film critic review").
* **Languages:** The target languages for translation (`LANGUAGE_OPTIONS`) can be expanded using the two-letter language codes supported by Azure Translator.

## **🤝 Contributing**

Feel free to fork this project and submit pull requests to enhance the pipeline, add more AI services, or improve the Gradio interface!
