from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_HEAT,
    HVAC_MODE_COOL,
    HVAC_MODE_AUTO,
    HVAC_MODE_OFF,
    SUPPORT_FAN_MODE,
    SUPPORT_TARGET_TEMPERATURE,
    SUPPORT_PRESET_MODE,
    SUPPORT_TURN_ON,
    SUPPORT_TURN_OFF

)
from .const import DOMAIN

from homeassistant.const import TEMP_CELSIUS, ATTR_TEMPERATURE
from .entity import TornadoEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([TornadoClimat(coordinator, entry)])



class TornadoClimat(TornadoEntity ,ClimateEntity):
    """Representation of a custom climate entity."""

    def __init__(self):
        """Initialize the climate device."""
        self._name = "My Climate Device"
        self._hvac_mode = HVAC_MODE_OFF
        self._current_temperature = 26.0
        self._target_temperature = 25.0
        self._temperature_unit = TEMP_CELSIUS
        self._fan_mode = "auto"
        self._preset_mode = None

        self._hvac_modes = [HVAC_MODE_OFF, HVAC_MODE_HEAT, HVAC_MODE_COOL, HVAC_MODE_AUTO]
        self._fan_modes = ["auto", "silent", "low", "medium", "high"]
 
    @property
    def name(self):
        """Return the name of the climate device."""
        return self._name

    @property
    def temperature_unit(self):
        """Return the unit of measurement."""
        return self._temperature_unit

    @property
    def current_temperature(self):
        """Return the current temperature."""
        return self._current_temperature

    @property
    def target_temperature(self):
        """Return the temperature we try to reach."""
        return self._target_temperature

    @property
    def hvac_mode(self):
        """Return the current operation mode (HVAC mode)."""
        return self._hvac_mode

    @property
    def hvac_modes(self):
        """Return the list of available HVAC operation modes."""
        return self._hvac_modes

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_TARGET_TEMPERATURE | SUPPORT_FAN_MODE | SUPPORT_PRESET_MODE | SUPPORT_TURN_ON | SUPPORT_TURN_OFF
    

    @property
    def fan_mode(self):
        """Return the current fan mode."""
        return self._fan_mode

    @property
    def fan_modes(self):
        """Return the list of available fan modes."""
        return self._fan_modes


    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is not None:
            self._target_temperature = temperature
            self.async_write_ha_state()

    async def async_set_hvac_mode(self, hvac_mode):
        """Set the HVAC mode."""
        if hvac_mode in self._hvac_modes:
            self._hvac_mode = hvac_mode
            self.async_write_ha_state()

    async def async_set_fan_mode(self, fan_mode):
        """Set the fan mode."""
        if fan_mode in self._fan_modes:
            self._fan_mode = fan_mode
            self.async_write_ha_state()


    def update(self):
        """Fetch the latest state from the device."""
        # You should implement logic here to update the device state
        pass
