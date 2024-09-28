import streamlit as st
import easyocr
from PIL import Image
import numpy as np

# Create an EasyOCR reader that can handle both English and Hindi text
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


def main():
    st.title("OCR Web Application - English & Hindi")

    # Allow users to upload an image file
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image on the app
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Extract text from the uploaded image
        with st.spinner('Extracting text...'):
            extracted_text = extract_text(image)

        # Show the extracted text in a subheader section
        st.subheader("Extracted Text")
        st.text(extracted_text)

        # Provide a text input for keyword search within the extracted text
        keyword = st.text_input("Enter a keyword to search:")

        if keyword:
            # Check if the keyword is present in the extracted text and display appropriate message
            if keyword.lower() in extracted_text.lower():
                st.success(f"Keyword '{keyword}' found in the extracted text!")
            else:
                st.warning(f"Keyword '{keyword}' not found in the extracted text.")


if __name__ == "__main__":
    main()
