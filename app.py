import streamlit as st
from spellchecker import SpellChecker

def text_corrector(text):
    spell = SpellChecker()
    misspelled = spell.unknown(text.split())
    for word in misspelled:
        text = text.replace(word, spell.correction(word))
    return text

def main():
    st.header("Text Corrector")
    text = st.text_area("Enter your text here", "Type Here")
    if text is not None:
        if st.button("Submit"):
            corrected_text = text_corrector(text)
            st.write("Corrected Text:")
            st.write(corrected_text)


if __name__ == "__main__":
    main()