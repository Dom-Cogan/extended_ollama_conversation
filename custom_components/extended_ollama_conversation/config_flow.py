import requests
from custom_components.extended_ollama_conversation.options_flow import ExtendedOllamaConversationOptionsFlowHandler
from homeassistant import config_entries
import voluptuous as vol
from functools import partial

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

    async def ollama_installed(self, ollama_url):
        """Check if Ollama is installed."""
        try:
            # Use a partial function to pass arguments to async_add_executor_job
            response = await self.hass.async_add_executor_job(
                partial(requests.post, f"{ollama_url}/api/chat", json={"model": "llama2"})
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            self.hass.log(f"Error checking Ollama installation: {e}")
            return False
        
    async def async_get_options_flow(config_entry):
        return ExtendedOllamaConversationOptionsFlowHandler(config_entry)

