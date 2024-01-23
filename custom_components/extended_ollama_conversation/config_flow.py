# config_flow.py
import requests
from homeassistant import config_entries
import voluptuous as vol
from functools import partial
from .options_flow import OptionsFlowHandler

DOMAIN = "extended_ollama_conversation"

class ExtendedOllamaConversationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    async def async_step_user(self, user_input=None):
        """Handle the initial step when the user adds a new integration."""
        if user_input is not None:
            # Validate and process user input
            if 'ollamaURL' in user_input:
                ollama_url = user_input['ollamaURL']
                ollama_model = user_input.get('model', 'ollama/llama')  # Assuming a default value if not provided
                # Process user input and create the entry
                return self.async_create_entry(title="Extended Ollama Conversation", data={'ollamaURL': ollama_url, 'model': ollama_model})
            else:
                return self.async_show_form(
                    step_id="user",
                    data_schema=vol.Schema({
                        vol.Required("ollamaURL", description="Ollama URL"): str,
                        vol.Required("model", description="Model name", default="default_model"): str,
                    }),
                    errors={"base": "Please provide the Ollama URL."},
                )

        # Show form to the user to collect input
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ollamaURL", description="Enter the Ollama URL"): str,
                vol.Required("model", description="Enter the model", default="default_model"): str,
            }),
        )

    async def ollama_installed(self, ollama_url, ollama_model):
        """Check if Ollama is installed."""
        try:
            # Use a partial function to pass arguments to async_add_executor_job
            response = await self.hass.async_add_executor_job(
                partial(requests.post, f"{ollama_url}/api/chat", json={"model": f"{ollama_model}"})
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            self.hass.log(f"Error checking Ollama installation: {e}")
            return False

    @staticmethod
    def async_get_options_flow(
        config_entry: config_entries.ConfigEntry,
    ) -> config_entries.OptionsFlow:
        """Create the options flow."""
        return OptionsFlowHandler(config_entry)

    async def async_step_options(self, user_input=None):
        if user_input is not None:
            # Process user input if needed
            return self.async_create_entry(title="", data=user_input)

        # Display the options form
        options_flow = await self.async_get_options_flow(self.config_entry)
        return await self.async_show_form(
            step_id="options",
            data_schema=options_flow,
        )
