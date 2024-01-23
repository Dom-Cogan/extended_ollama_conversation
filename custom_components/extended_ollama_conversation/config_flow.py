"""Config flow for extended_ollama_conversation."""
import requests
from homeassistant import config_entries
import voluptuous as vol

DOMAIN = "extended_ollama_conversation"

class ExtendedOllamaConversationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        """Handle the initial step when the user adds a new integration."""
        if user_input is not None:
            # Validate and process user input
            # For example, you can check if 'ollama_url' is provided
            if 'ollama_url' in user_input:
                ollama_url = user_input['ollama_url']
                if await self.ollama_installed(ollama_url):
                    # Ollama is installed, save the configuration
                    return self.async_create_entry(title="Extended Ollama Conversation", data=user_input)
                else:
                    return self.async_show_form(
                        step_id="user",
                        data_schema=vol.Schema({vol.Required("ollama_url", default=""): str}),
                        errors={"base": "Ollama is not installed or the provided URL is incorrect."},
                    )

        # Show form to the user to collect input
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({vol.Required("ollama_url", default=""): str}),
        )

    async def ollama_installed(self, ollama_url):
        """Check if Ollama is installed."""
        try:
            # Make a test request to the Ollama API
            response = requests.post(f"{ollama_url}/api/chat", json={"model": "llama2"})
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException:
            return False