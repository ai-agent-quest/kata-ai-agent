import dspy
from dotenv import dotenv_values

# 1. Configurer le modèle de langage
# Ici avec OpenAI (tu peux adapter à d'autres backends)
config = dotenv_values("../.env")

llm_model = config.get('ONLINE_LLM_MODEL')
api_key = config.get('ONLINE_LLM_API_KEY')
lm = dspy.LM(llm_model, api_key=api_key)
dspy.settings.configure(lm=lm)

# 2. Définir la "signature" du chatbot
class ChatbotSignature(dspy.Signature):
    """Un chatbot simple qui répond à l'utilisateur."""
    question = dspy.InputField(desc="Message de l'utilisateur")
    answer = dspy.OutputField(desc="Réponse du chatbot")

# 3. Créer un module DSPy
class SimpleChatbot(dspy.Module):
    def __init__(self):
        super().__init__()
        self.respond = dspy.Predict(ChatbotSignature)

    def forward(self, question):
        return self.respond(question=question)

# 4. Utilisation
bot = SimpleChatbot()

while True:
    user_input = input("👤 Vous : ")
    if user_input.lower() in ["quit", "exit"]:
        break

    response = bot(question=user_input)
    print("🤖 Bot :", response.answer)
