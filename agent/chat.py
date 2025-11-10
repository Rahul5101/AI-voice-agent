import google.generativeai as genai
from agent.memory import MemoryManager

class ConversationAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")
        self.memory = MemoryManager()

    def generate_reply(self, user_id: str, user_message: str):
        history = self.memory.get_memory(user_id)
        prompt = "You are Riverwood Assistant. Speak warmly and naturally in English.\n\n"
        for msg in history[-5:]:
            prompt += f"{msg['role']}: {msg['content']}\n"
        prompt += f"User: {user_message}\nAssistant:"

        response = self.model.generate_content(prompt)
        reply = response.text.strip()

        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": reply}) 
        self.memory.save_memory(user_id, history)
        return reply
