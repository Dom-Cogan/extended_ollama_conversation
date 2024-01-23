"""Options flow for extended_ollama_conversation."""
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as vol
import voluptuous as vol

class ExtendedOllamaConversationOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for extended_ollama_conversation."""

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        return await self.async_step_advanced_options()

    async def async_step_advanced_options(self, user_input=None):
        """Handle advanced options."""
        if user_input is not None:
            # Process advanced options
            return self.async_create_entry(title="", data=user_input)

        # Show form for advanced options
        return self.async_show_form(
            step_id="advanced_options",
            data_schema=vol.Schema({
                vol.Required("additional_setting", default=self.entry.options.get("additional_setting", "")): str,
            }),
        )
