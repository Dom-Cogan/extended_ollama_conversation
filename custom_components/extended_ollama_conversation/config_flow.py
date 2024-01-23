"""Config flow for extended_ollama_conversation."""
from homeassistant import config_entries

DOMAIN = "extended_ollama_conversation"

class ExtendedOllamaConversationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        # Your implementation for collecting user input
        return self.async_create_entry(title="Extended Ollama Conversation", data=user_input)
