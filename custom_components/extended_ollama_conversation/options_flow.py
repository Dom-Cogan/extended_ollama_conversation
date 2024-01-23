"""Options flow for extended_ollama_conversation."""
from homeassistant import config_entries
from homeassistant.helpers import config_validation as vol
from homeassistant.config_entries import ConfigFlow

class ExtendedOllamaConversationOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle extended_ollama_conversation options."""

    def __init__(self, config_entry):
        """Initialize extended_ollama_conversation options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle the options form."""
        if user_input is not None:
            # Process user input if needed
            return self.async_create_entry(title="", data=user_input)

        # Display the options form
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("ollamaURL", description="Enter the updated Ollama URL", default=self.config_entry.options.get("ollamaURL", "")): str
            }),
        )
