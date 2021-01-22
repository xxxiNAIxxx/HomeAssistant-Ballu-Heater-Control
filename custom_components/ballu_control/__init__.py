from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Tapo: Cameras Control component from YAML."""
    return True
