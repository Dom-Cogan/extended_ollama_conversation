"""Config flow for extended_ollama_conversation."""
from homeassistant import config_entries
from homeassistant.helpers import config_validation as vol

DOMAIN = "extended_ollama_conversation"

class ExtendedOllamaConversationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        """Handle the initial step when the user adds a new integration."""
        if user_input is not None:
            # Validate and process user input
            if 'ollamaURL' in user_input:
                # Process user input and create the entry
                return self.async_create_entry(title="Extended Ollama Conversation", data=user_input)
            else:
                return self.async_show_form(
                    step_id="user",
                    data_schema=vol.Schema({
                        vol.Required("ollamaURL", description="Enter the Ollama URL", default=""): str
                    }),
                    errors={"base": "Please provide the Ollama URL."},
                )

        # Show form to the user to collect input
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ollamaURL", description="Enter the Ollama URL", default=""): str
            }),
        )
