"""The exceptions used by Extended Ollama Conversation."""
from homeassistant.exceptions import HomeAssistantError


class EntityNotFound(HomeAssistantError):
    """When the referenced entity is not found."""

    def __init__(self, entity_id: str) -> None:
        """Initialize error."""
        super().__init__(f"Entity {entity_id} not found")
        self.entity_id = entity_id

    def __str__(self) -> str:
        """Return string representation."""
        return f"Unable to find entity {self.entity_id}"


class EntityNotExposed(HomeAssistantError):
    """When the referenced entity is not exposed."""

    def __init__(self, entity_id: str) -> None:
        """Initialize error."""
        super().__init__(f"Entity {entity_id} not exposed")
        self.entity_id = entity_id

    def __str__(self) -> str:
        """Return string representation."""
        return f"Entity {self.entity_id} is not exposed"


class CallServiceError(HomeAssistantError):
    """Error during service calling"""

    def __init__(self, domain: str, service: str, data: object) -> None:
        """Initialize error."""
        super().__init__(
            f"Unable to call service {domain}.{service} with data {data}. One of 'entity_id', 'area_id', or 'device_id' is required"
        )
        self.domain = domain
        self.service = service
        self.data = data

    def __str__(self) -> str:
        """Return string representation."""
        return f"Unable to call service {self.domain}.{self.service} with data {self.data}. One of 'entity_id', 'area_id', or 'device_id' is required"


class FunctionNotFound(HomeAssistantError):
    """When the referenced function is not found."""

    def __init__(self, function: str) -> None:
        """Initialize error."""
        super().__init__(f"Function '{function}' does not exist")
        self.function = function

    def __str__(self) -> str:
        """Return string representation."""
        return f"Function '{self.function}' does not exist"


class NativeNotFound(HomeAssistantError):
    """When the native function is not found."""

    def __init__(self, name: str) -> None:
        """Initialize error."""
        super().__init__(f"Native function '{name}' does not exist")
        self.name = name

    def __str__(self) -> str:
        """Return string representation."""
        return f"Native function '{self.name}' does not exist"


class FunctionLoadFailed(HomeAssistantError):
    """When function loading fails."""

    def __init__(self) -> None:
        """Initialize error."""
        super().__init__(
            "Failed to load functions. Verify functions are valid in a YAML format"
        )

    def __str__(self) -> str:
        """Return string representation."""
        return "Failed to load functions. Verify functions are valid in a YAML format"


class ParseArgumentsFailed(HomeAssistantError):
    """When parsing arguments fails."""

    def __init__(self, arguments: str) -> None:
        """Initialize error."""
        super().__init__(
            f"Failed to parse arguments `{arguments}`. Increase maximum tokens to avoid the issue."
        )
        self.arguments = arguments

    def __str__(self) -> str:
        """Return string representation."""
        return f"Failed to parse arguments `{self.arguments}`. Increase maximum tokens to avoid the issue."


class InvalidFunction(HomeAssistantError):
    """When function validation fails."""

    def __init__(self, function_name: str) -> None:
        """Initialize error."""
        super().__init__(f"Failed to validate function `{function_name}`")
        self.function_name = function_name

    def __str__(self) -> str:
        """Return string representation."""
        return f"Failed to validate function `{self.function_name}` ({self.__cause__})"
