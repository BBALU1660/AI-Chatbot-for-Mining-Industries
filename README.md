To help you prepare the GitHub description and the README file with the provided code and images, here's how you can organize it.

### 1. **Project Description** (for GitHub repository)

---

# **Coal Miner AI Chatbot**
An AI-powered multilingual chatbot tailored for the mining sector. This project was developed as part of the Smart India Hackathon 2023 and awarded an Honorable Mention. It provides seamless interaction with PDFs related to mining industry laws, regulations, and safety guidelines. It offers voice and text search, multiple language support, and translates outputs to various languages, increasing operational efficiency in the mining industry.

### Key Features:
- **Multilingual support**: Offers translation and speech recognition in over 100 languages.
- **Voice & Text Search**: Allows querying the PDF using both voice and text inputs.
- **PDF Integration**: Extracts and displays text from PDF documents.
- **AI-Powered Responses**: Leverages Langchain, FAISS, and OpenAI embeddings for intelligent responses.
- **Translation & Text-to-Speech**: Translates responses to the chosen language and converts them to speech.

### Technologies Used:
- Streamlit for frontend
- FAISS for vector search
- OpenAI for LLMs and embeddings
- Google Translator for translation
- gTTS for text-to-speech conversion
- Langchain for language model integration
- PyPDF2 and pdfplumber for PDF extraction
- SpeechRecognition for voice search

### Demo Screenshots:
1. **Main Chat Interface**  
   ![Chat Interface](https://github.com/username/repo/blob/main/screenshots/Screenshot1.png)

2. **Voice Search Feature**  
   ![Voice Search](https://github.com/username/repo/blob/main/screenshots/Screenshot2.png)

3. **Language Selection Interface**  
   ![Language Selection](https://github.com/username/repo/blob/main/screenshots/Screenshot3.png)

---

### 2. **README.md** (for repository)
```markdown
# Coal Miner AI Chatbot

This repository contains the code for a multilingual AI chatbot built for the mining industry. The project was developed for the **Smart India Hackathon 2023** and received an **Honorable Mention**. The chatbot assists with queries related to mining regulations and acts, using both **voice and text inputs** to interact with PDF documents.

## Features
- **Voice Search**: Use speech input to query mining-related documents.
- **Text Search**: Directly input your queries through text.
- **Multilingual**: Supports multiple languages for input and output, including translation of responses.
- **PDF Interaction**: Parses mining-related PDFs to provide relevant responses.
- **AI-Powered Responses**: Leverages Langchain and FAISS for optimized and accurate responses.
- **Text-to-Speech**: Converts chatbot responses into audio using Google TTS.

## Technologies Used
- **Streamlit**: Web framework
- **FAISS**: Vector search for document chunks
- **Langchain**: Language models and question answering
- **OpenAI GPT**: Natural Language Processing and embeddings
- **GoogleTranslator**: Translation of responses
- **gTTS**: Text-to-speech conversion
- **SpeechRecognition**: Converts voice input into text
- **pdfplumber** and **PyPDF2**: PDF parsing and text extraction

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/username/repo.git
cd repo
```

### 2. Install dependencies
Create a virtual environment and install the required Python packages:
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the root directory and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
```

### 4. Running the application
Run the Streamlit app:
```bash
streamlit run app.py
```

### 5. Upload the mining-related PDF
Ensure you have your mining-related PDF file in the root directory or provide the path to the file.

## Screenshots

### Main Chat Interface:
![Main Interface](./screenshots/Screenshot1.png)

### Voice Search:
![Voice Search](./screenshots/Screenshot2.png)

### Language Selection:
![Language Selection](./screenshots/Screenshot3.png)

## Team Members
- Swaroop
- Nikhil
- Abhinav
- Rohit
- Shanmukh
- Sahithi

## License
This project is licensed under the MIT License.
```

### **Steps to Upload Screenshots:**
1. Place the screenshots in a folder named `screenshots`.
2. Upload the screenshots in GitHub with names matching the markdown image paths.
   - For example, `Screenshot1.png`, `Screenshot2.png`, `Screenshot3.png`.

Ensure that the word limits and descriptions are aligned with GitHub's guidelines, typically not exceeding 250 characters for descriptions, but allowing more detail in README files. Let me know if you need further adjustments or assistance!
