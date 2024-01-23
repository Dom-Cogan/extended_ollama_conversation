"""The extended_ollama_conversation component."""
from homeassistant.helpers.discovery import async_load_platform

DOMAIN = "extended_ollama_conversation"

async def async_setup(hass, config):
    """Set up the extended_ollama_conversation component."""
    # Your setup logic goes here
    return True

async def async_setup_entry(hass, entry):
    """Set up the component from a config entry."""
    name = entry.data.get("name")
    hass.components.persistent_notification.create(
        f"Extended Ollama Conversation added with name: {name}",
        title="Extended Ollama Conversation",
        notification_id="extended_ollama_conversation_notification",
    )
    # Your additional setup logic goes here
    return True

async def async_unload_entry(hass, entry):
    """Unload the component."""
    # Your entry unload logic goes here
    return True

async def async_get_options_flow(config_entry):
    """Provide the options flow for the integration."""
    return ExtendedOllamaConversationOptionsFlowHandler(config_entry)
