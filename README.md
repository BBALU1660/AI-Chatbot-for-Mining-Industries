Coal Miner AI Chatbot
The Coal Miner AI Chatbot is an AI-powered, multilingual assistant designed to streamline queries related to the mining industry. Developed for the Smart India Hackathon 2023, this project earned an Honorable Mention for its effectiveness in assisting mining professionals with laws, regulations, and other information through PDF documents. The chatbot uses voice and text input for queries, making it accessible and user-friendly.

Features
Voice Search: Speak your queries for a more hands-free interaction.
Text Search: Input queries manually to search for information.
Multilingual Support: The chatbot supports input and output in multiple languages.
PDF Integration: It extracts and processes text from mining-related PDFs for relevant responses.
AI-Powered Responses: Utilizes FAISS, Langchain, and OpenAI GPT for intelligent answers.
Translation & Text-to-Speech: Responses are translated to the user's language and read aloud using Google TTS.
Technologies Used
Streamlit: Web app framework
FAISS: Vector search for document content
Langchain: Language models and question-answering functionality
OpenAI GPT: NLP and embeddings
GoogleTranslator: Translates responses
gTTS: Converts text into speech
pdfplumber, PyPDF2: Extracts content from PDFs
SpeechRecognition: Converts voice input to text
Screenshots

![Screenshot 2023-12-21 233657](https://github.com/user-attachments/assets/fe56784b-988c-4730-8869-eb6aea9c5acc)
![Screenshot 2023-12-21 233628](https://github.com/user-attachments/assets/ffa796b3-7155-49df-8b08-3b5f02272359)
![Screenshot 2023-12-21 233615](https://github.com/user-attachments/assets/ed76d4cd-d6f9-48d8-8df9-b7c4a8261251)
![Screenshot (108)](https://github.com/user-attachments/assets/465e2da5-8819-460c-9006-be15a1ce04eb)



Installation Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/username/repo.git
cd repo
2. Install Dependencies
Set up a virtual environment and install the required Python libraries:

bash
Copy code
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
3. Set up Environment Variables
Create a .env file in the root directory with your API keys:

makefile
Copy code
OPENAI_API_KEY=your_openai_api_key
4. Run the Application
Launch the Streamlit application:

bash
Copy code
streamlit run app.py
5. Add PDF Files
Make sure to upload the mining-related PDF you want to search through. Place it in the root directory or provide its path when prompted.

Usage
Select between Voice Search or Text Search.
Choose the input language.
Enter or speak your query.
The chatbot processes the query and returns relevant information from the mining-related PDF.
You can also translate the output into your preferred language and listen to it using text-to-speech.
Team Members
Swaroop
Nikhil
Abhinav
Rohit
Shanmukh
Sahithi
License
This project is licensed under the MIT License.

