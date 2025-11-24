import gradio as gr
import requests
import uuid
import json
import os
import io # Needed for handling file bytes

# ==============================================================================
# 1. Configuration (MUST BE REPLACED WITH YOUR SECURE KEYS)
# ==============================================================================

# --- Azure Computer Vision Config ---
# Replace with your actual Azure CV Endpoint and Key
AZURE_CV_ENDPOINT = os.environ.get("AZURE_CV_ENDPOINT", "https://lab1mohamedosama.cognitiveservices.azure.com/")
AZURE_CV_KEY = os.environ.get("AZURE_CV_KEY", "DeHwAiaMnQAbjHrBaZSkWr7l5NCzRsu06C9m1nVYvYa6X3U9fIx0JQQJ99BKACF24PCXJ3w3AAAFACOG1xt9")

# --- Gemini API Config ---
# Replace with your actual Gemini API Key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyBPucQmtN3_o1crt06oDLzgRlgkkxQEhCg")

# --- Azure Translator Config ---
# Replace with your actual Azure Translator Region and Key
AZURE_TRANS_KEY = os.environ.get("AZURE_TRANS_KEY", "BcCzXIVw5H2pYxniWIhMuV4BYqjqJaZrfYoTRMcPJSyRerEvZP4lJQQJ99BKACF24PCXJ3w3AAAbACOGsVC0")
AZURE_TRANS_REGION = os.environ.get("AZURE_TRANS_REGION", "uaenorth") # Example region

# Attempt to configure Gemini
try:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    GEMINI_MODEL = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    print(f"Warning: Gemini configuration failed. Text generation functions will not work. Error: {e}")
    GEMINI_MODEL = None

# ==============================================================================
# 2. Core AI Functions (Refactored for single script)
# ==============================================================================

def analyze_image(image_path):
    """
    Analyzes an image file path (provided by Gradio) using Azure Computer Vision.
    It reads the file locally and sends the binary data, which is more robust
    than relying on external URLs.
    """
    if not AZURE_CV_KEY or not AZURE_CV_ENDPOINT:
        return "Error: Azure CV Key or Endpoint is missing.", "", []

    analyze_url = f"{AZURE_CV_ENDPOINT}/vision/v3.2/analyze"
    
    # Read image file as binary data
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_CV_KEY,
        "Content-Type": "application/octet-stream"
    }
    params = {"visualFeatures": "Description,Tags"}
    
    try:
        response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        result = response.json()
    except requests.exceptions.RequestException as e:
        return f"Azure CV API Error: {e}", "", []
    except json.JSONDecodeError:
        return f"Azure CV returned an invalid response.", "", []

    # Extract caption
    caption = ""
    captions = result.get('description', {}).get("captions", [])
    if captions:
        caption = captions[0]['text']
    
    # Extract tags
    tags = []
    if 'tags' in result:
        tags = [tag['name'] for tag in result['tags']]
    
    vision_context = f"Image description: {caption}\nImage tags: {', '.join(tags)}"
    
    return vision_context, caption, tags

def generate_creative_content(vision_context):
    """Generates a creative paragraph using the Gemini model."""
    if not GEMINI_MODEL:
        return "Gemini model is not configured."
    
    prompt = f"""
Using this image analysis:

{vision_context}

Write a short, engaging paragraph (3–4 sentences) describing the scene in a creative and simple way.
"""
    try:
        response = GEMINI_MODEL.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Creative Generation Error: {e}"

def rewrite_in_style(original_text, target_style):
    """Rewrites a paragraph in a new writing style using the Gemini model."""
    if not GEMINI_MODEL:
        return "Gemini model is not configured."

    prompt = f"""
You are a rewriting assistant. 
Rewrite the following paragraph in the style of: {target_style}

Original paragraph:
{original_text}

Rewrite it clearly, keeping the meaning but fully changing the tone and style.
"""
    try:
        response = GEMINI_MODEL.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini Style Rewriting Error: {e}"

def translate_text(text, to_language):
    """Translates text to a target language using Azure Translator."""
    if not AZURE_TRANS_KEY or not AZURE_TRANS_REGION:
        return "Error: Azure Translator Key or Region is missing."

    path = '/translate'
    endpoint = "https://api.cognitive.microsofttranslator.com"
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [to_language]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': AZURE_TRANS_KEY,
        'Ocp-Apim-Subscription-Region': AZURE_TRANS_REGION,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': text}]

    try:
        request = requests.post(constructed_url, params=params, headers=headers, json=body)
        request.raise_for_status()
        response = request.json()
    except requests.exceptions.RequestException as e:
        return f"Azure Translator API Error: {e}"
    except json.JSONDecodeError:
        return f"Azure Translator returned an invalid response."

    # Extract the translated text
    translations = response[0].get('translations', [])
    if translations:
        return translations[0]['text']
    
    return "Translation failed."


# ==============================================================================
# 3. Unified Gradio Pipeline
# ==============================================================================

def full_pipeline(image_path, rewrite_style, translate_lang):
    """
    The main, efficient pipeline function for Gradio.
    It chains the CV analysis, creative generation, style rewrite, and translation.
    """
    if not image_path:
        return (
            "No image provided.",
            "No image provided.",
            "No image provided.",
            "No image provided.",
            "No image provided."
        )

    # 1. Azure Computer Vision Analysis
    vision_context, caption, tags = analyze_image(image_path)
    tag_string = ", ".join(tags)
    
    if "Error:" in vision_context: # Check for CV errors
         return vision_context, caption, tag_string, "Analysis failed.", "Analysis failed."

    # 2. Gemini Creative Text Generation (This text is the base for other operations)
    creative_text = generate_creative_content(vision_context)
    
    # 3. Gemini Style Rewriting (Uses the base Creative Text)
    # Note: Using 'creative_text' instead of 'vision_context' for better results
    rewritten_text = rewrite_in_style(creative_text, rewrite_style)
    
    # 4. Azure Translation (Uses the Style-Rewritten Text for demonstration)
    translation = translate_text(rewritten_text, translate_lang)

    return (
        tag_string,
        caption,
        creative_text,
        rewritten_text,
        translation
    )

# ==============================================================================
# 4. Gradio Interface Definition
# ==============================================================================

# Custom list of styles for the user to pick
STYLE_OPTIONS = [
    "Professional academic style",
    "Child-friendly storytelling style",
    "Marketing advertising style",
    "Vintage noir detective style",
    "Shakespearean poetic style"
]

# Simple list of languages for the user to pick
LANGUAGE_OPTIONS = {
    "Arabic": "ar",
    "Zulu": "zu",
    "French": "fr",
    "German": "de",
    "Hindi": "hi"
}
demo = gr.Interface(
    fn=full_pipeline,
    inputs=[
        gr.Image(
            type="filepath",
            label="1. Upload Image (or provide URL)",
            sources=["upload"],
    
            width=500
        ),
        gr.Dropdown(
            label="2. Select Target Rewrite Style (Gemini)",
            choices=STYLE_OPTIONS,
            value="Professional academic style"
        ),
        gr.Dropdown(
            label="3. Select Target Translation Language (Azure Translator)",
            choices=list(LANGUAGE_OPTIONS.values()),
            value="ar",
            type="value",
            interactive=True
        )
    ],
    outputs=[
        gr.Textbox(label="Output A: Azure CV Tags", lines=2),
        gr.Textbox(label="Output B: Azure CV Caption", lines=1),
        gr.Textbox(label="Output C: Gemini Creative Text (Base)", lines=4),
        gr.Textbox(label="Output D: Gemini Style Rewrite", lines=4),
        gr.Textbox(label="Output E: Azure Translation (of Rewrite)", lines=4),
    ],
    title="AI Multi-Service Pipeline: Vision, Creative Writing, Style Transfer, & Translation",
    description="Upload an image to trigger a four-step AI process: Azure Computer Vision analysis, Gemini creative writing, Gemini style rewriting, and Azure translation. All in one efficient click!",
    allow_flagging="auto",
    theme=gr.themes.Soft()
)

if __name__ == "__main__":
    # Note: Gradio runs on a specific port. For deployment, make sure to use the
    # required host ('0.0.0.0') and port (often 7860 or specified by environment)
    demo.launch()