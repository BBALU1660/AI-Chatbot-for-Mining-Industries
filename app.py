import streamlit as st
import pdfplumber
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.callbacks import get_openai_callback
from deep_translator import GoogleTranslator
import speech_recognition as sr
from langdetect import detect
from gtts import gTTS
import os
import time

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Sidebar
with st.sidebar:
    st.title('🔨Coal Miner Chat App👷')
    st.markdown('''
    ## About
    Coal Boy is a self-learning chat-bot, 
    where it will give outputs to queries pertaining to various Acts, Rules, and Regulations applicable to Mining industries.
    ''')
    st.write('''
    Made by
    - Swaroop
    - Nikhil
    - Abhinav
    - Rohit
    - Shanmukh
    - Sahithi
    ''')

# Initialize session state
if 'query' not in st.session_state:
    st.session_state.query = None

if 'input_language' not in st.session_state:
    st.session_state.input_language = 'en'

# Retry logic for handling rate limits and other retriable errors
def retry_with_backoff(func, max_retries=5, backoff_factor=2):
    retries = 0
    while retries < max_retries:
        try:
            return func()
        except Exception as e:
            if "rate limit" in str(e).lower():
                retries += 1
                wait_time = backoff_factor ** retries
                time.sleep(wait_time)
            else:
                raise e
    raise Exception("Max retries reached. Unable to execute the function.")

def main():
    st.header("Chat with Coal PDF 💬")

    pdf_path = "Mines.pdf"

    # Read and display PDF contents
    def read_pdf(pdf_path):
        with pdfplumber.open(pdf_path) as pdf:
            st.header("PDF Contents:")
            for page in pdf.pages:
                st.write(page.extract_text())

    search_mode = st.radio("Search Mode", ["Voice Search", "Text Search"])

    if search_mode == "Voice Search":
        # Language options for voice search
        languages = {
            'Auto-Detect': 'auto', 'Afrikaans': 'af', 'Albanian': 'sq', 'Amharic': 'am', 'Arabic': 'ar', 'Armenian': 'hy', 
            'Azerbaijani': 'az', 'Basque': 'eu', 'Belarusian': 'be', 'Bengali': 'bn', 'Bosnian': 'bs', 'Bulgarian': 'bg', 
            'Catalan': 'ca', 'Cebuano': 'ceb', 'Chichewa': 'ny', 'Chinese (Simplified)': 'zh-cn', 'Chinese (Traditional)': 'zh-tw', 
            'Corsican': 'co', 'Croatian': 'hr', 'Czech': 'cs', 'Danish': 'da', 'Dutch': 'nl', 'English': 'en', 
            'Esperanto': 'eo', 'Estonian': 'et', 'Filipino': 'tl', 'Finnish': 'fi', 'French': 'fr', 'Frisian': 'fy', 
            'Galician': 'gl', 'Georgian': 'ka', 'German': 'de', 'Greek': 'el', 'Gujarati': 'gu', 'Haitian Creole': 'ht', 
            'Hausa': 'ha', 'Hawaiian': 'haw', 'Hebrew': 'iw', 'Hindi': 'hi', 'Hmong': 'hmn', 'Hungarian': 'hu', 
            'Icelandic': 'is', 'Igbo': 'ig', 'Indonesian': 'id', 'Irish': 'ga', 'Italian': 'it', 'Japanese': 'ja', 
            'Javanese': 'jw', 'Kannada': 'kn', 'Kazakh': 'kk', 'Khmer': 'km', 'Korean': 'ko', 'Kurdish (Kurmanji)': 'ku', 
            'Kyrgyz': 'ky', 'Lao': 'lo', 'Latin': 'la', 'Latvian': 'lv', 'Lithuanian': 'lt', 'Luxembourgish': 'lb', 
            'Macedonian': 'mk', 'Malagasy': 'mg', 'Malay': 'ms', 'Malayalam': 'ml', 'Maltese': 'mt', 'Maori': 'mi', 
            'Marathi': 'mr', 'Mongolian': 'mn', 'Myanmar (Burmese)': 'my', 'Nepali': 'ne', 'Norwegian': 'no', 'Odia': 'or', 
            'Pashto': 'ps', 'Persian': 'fa', 'Polish': 'pl', 'Portuguese': 'pt', 'Punjabi': 'pa', 'Romanian': 'ro', 
            'Russian': 'ru', 'Samoan': 'sm', 'Scots Gaelic': 'gd', 'Serbian': 'sr', 'Sesotho': 'st', 'Shona': 'sn', 
            'Sindhi': 'sd', 'Sinhala': 'si', 'Slovak': 'sk', 'Slovenian': 'sl', 'Somali': 'so', 'Spanish': 'es', 
            'Sundanese': 'su', 'Swahili': 'sw', 'Swedish': 'sv', 'Tajik': 'tg', 'Tamil': 'ta', 'Telugu': 'te', 'Thai': 'th', 
            'Turkish': 'tr', 'Turkmen': 'tk', 'Ukrainian': 'uk', 'Urdu': 'ur', 'Uyghur': 'ug', 'Uzbek': 'uz', 'Vietnamese': 'vi', 
            'Welsh': 'cy', 'Xhosa': 'xh', 'Yiddish': 'yi', 'Yoruba': 'yo', 'Zulu': 'zu'
        }

        # Input language selection for voice search
        input_language = st.selectbox('Select Input Language', list(languages.keys()))
        input_language_code = languages[input_language]

        if st.button("Ask"):
            st.subheader("Voice Search")
            with st.spinner("Listening..."):
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                try:
                    recognized_text = r.recognize_google(audio, language=input_language_code)
                    
                    # Auto-detect the language of recognized text
                    detected_language = detect(recognized_text)
                    
                    if detected_language != 'en':
                        # Translate recognized text to English
                        translator = GoogleTranslator(source=detected_language, target='en')
                        recognized_text = translator.translate(recognized_text)
                    st.session_state.query = recognized_text
                    st.write(f"Recognized Text in English: {st.session_state.query}")

                except sr.UnknownValueError:
                    st.error("Could not understand audio")
                except sr.RequestError:
                    st.error("Could not request results")
    else:  # Text Search
        st.session_state.query = st.text_input("Ask questions about Coal mines", st.session_state.query)

    query = st.session_state.query
    if query:
        if pdf_path is not None:
            pdf_reader = PdfReader(pdf_path)

            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=5000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text=text)

            store_name = pdf_path[:-4]

    def embed_and_query():
        # Embedding text and querying the VectorStore
        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        
        # Querying with the language model
        llm = OpenAI(model_name='gpt-3.5-turbo')
        chain = load_qa_chain(llm, chain_type="stuff")

        # Perform similarity search
        docs = VectorStore.similarity_search(query=query, k=5)

        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=query)
            st.write(response)
     

        # Language mapping for translation
        Languages = {
            'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 
            'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 
            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 
            'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 
            'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 
            'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 
            'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 
            'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 
            'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 
            'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 
            'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 
            'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 
            'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 
            'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 
            'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 
            'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 
            'turkish': 'tr', 'turkmen': 'tk', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 
            'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'
        }

        # Output language selection
        target_language = st.selectbox('Output Language', Languages.keys())
        target_language_code = Languages[target_language]
        translator = GoogleTranslator(source='auto', target=target_language_code)
        translated_text = translator.translate(response)
        st.write(f"Translated Text in {target_language}: {translated_text}")

        # Text-to-Speech conversion
        tts = gTTS(text=translated_text, lang=target_language_code, slow=False)
        audio_file_path = "text.mp3"
        tts.save(audio_file_path)
        st.audio(audio_file_path)

    # Perform the embedding and querying with retry logic
    retry_with_backoff(embed_and_query)

if __name__ == '__main__':
    main()
