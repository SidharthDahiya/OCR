import gradio as gr
import easyocr
from PIL import Image
import numpy as np

# Initialize EasyOCR reader for both English and Hindi
reader = easyocr.Reader(['en', 'hi'])


def extract_text(image):
    """
    This function takes an image as input and uses OCR to extract text.
    It returns the extracted text as a string.
    """
    # Convert the image to a numpy array for processing
    image_np = np.array(image)

    # Use the OCR reader to detect and read text from the image
    results = reader.readtext(image_np, detail=0, paragraph=True)

    # Join the detected text into a single string
    extracted_text = '\n'.join(results)

    return extracted_text


def search_keyword(extracted_text, keyword):
    """
    This function searches for a keyword in the extracted text.
    Returns a message indicating whether the keyword was found.
    """
    if keyword.lower() in extracted_text.lower():
        return f"Keyword '{keyword}' found in the extracted text!"
    else:
        return f"Keyword '{keyword}' not found in the extracted text."


def process_image(image, keyword):
    """
    Process the uploaded image to extract text and search for a keyword.
    Returns extracted text and search results.
    """
    extracted_text = extract_text(image)
    search_result = search_keyword(extracted_text, keyword)
    return extracted_text, search_result


# Create Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Textbox(label="Enter Keyword")
    ],
    outputs=[
        gr.Textbox(label="Extracted Text"),
        gr.Textbox(label="Search Result")
    ],
    title="OCR Insight - English and Hindi",
    description="Upload an image containing text in English or Hindi. Extract the text and search for specific keywords."
)

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
