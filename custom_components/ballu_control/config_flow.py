from homeassistant import config_entries
from homeassistant.const import CONF_IP_ADDRESS, CONF_USERNAME, CONF_PASSWORD
import voluptuous as vol
from .const import DOMAIN, ENABLE_MOTION_SENSOR, LOGGER, CLOUD_PASSWORD


@config_entries.HANDLERS.register(DOMAIN)
class FlowHandler(config_entries.ConfigFlow):
    """Handle a config flow."""

    VERSION = 3

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        return await self.async_step_auth()

    async def async_step_auth(self, user_input=None):
        host = ""
        password = ""
        if user_input is not None:
            host="123.123.123.123"
        return self.async_show_form(
            step_id="auth",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_IP_ADDRESS, description={"suggested_value": host}
                    ): str,
                    vol.Required(
                        CONF_PASSWORD, description={"suggested_value": password}
                    ): str,
                }
            )

        )