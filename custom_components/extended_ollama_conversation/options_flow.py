# options_flow.py
from homeassistant.config_entries import ConfigFlow
import voluptuous as vol

class OptionsFlowHandler(ConfigFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            # Process user input if needed
            return self.async_create_entry(title="", data=user_input)

        # Display the options form
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ollama_url", description="Enter the updated Ollama URL", default=self.config_entry.options.get("ollama_url", "")): str,
                vol.Required("model_name", description="Enter the updated model name", default=self.config_entry.options.get("model_name", "")): str
            }),
        )
