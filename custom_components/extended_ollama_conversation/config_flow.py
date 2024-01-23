"""Config flow for extended_ollama_conversation."""
from homeassistant import config_entries

DOMAIN = "extended_ollama_conversation"

class ExtendedOllamaConversationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        """Handle the initial step when the user adds a new integration."""
        if user_input is not None:
            # Validate and process user input
            # For example, you can check if 'name' is provided
            if 'name' in user_input:
                # Process user input and create the entry
                return self.async_create_entry(title="Extended Ollama Conversation", data=user_input)
            else:
                return self.async_show_form(
                    step_id="user",
                    data_schema=vol.Schema({"name": str}),
                    errors={"base": "Please provide a name."},
                )

        # Show form to the user to collect input
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({"name": str}),
        )
