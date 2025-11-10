# AI-voice-agent
This is a voice agent which respond contextually using llm of any user query and also take voice input and speak back at human like voice and give output in a voice format.



# flowchart LR
A[User] -->|Voice/Text Input| B[FastAPI / HTML Form]
B -->|Send Query| C[LLM (GPT-4o-mini)]
C -->|Generate Reply| D[Text-to-Speech Engine]
D -->|Audio File| E[Browser Audio Player]
E -->|Plays Response| A

# clone the repo

git clone https://github.com/yourusername/riverwood-voice-agent.git
cd riverwood-voice-agent


# create and activate virtual environment

python -m venv myenv
myenv\Scripts\activate     # Windows

pip install -r requirements.txt

# Start the server

uvicorn app:app --reload


