import json
from pathlib import Path

class MemoryManager:
    def __init__(self,path="memory.json"):
        self.path = Path(path)
        if not self.path.exists():
            self.path.write_text(json.dumps({}))
            
    def get_memory(self,user_id:str):
        data = json.loads(self.path.read_text())
        return data.get(user_id,[])
    
    def save_memory(self,user_id:str,history:list):
        data = json.loads(self.path.read_text())
        data[user_id] = history
        self.path.write_text(json.dumps(data,indent=2))
        

