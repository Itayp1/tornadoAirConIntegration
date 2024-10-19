from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_HEAT,
    HVAC_MODE_COOL,
    HVAC_MODE_AUTO,
    HVAC_MODE_OFF,
    SUPPORT_FAN_MODE,
    SUPPORT_TARGET_TEMPERATURE,
    SUPPORT_PRESET_MODE , 
    ClimateEntityFeature ,
    HVACMode

)

# from homeassistant.components.climate.const import (
#     SUPPORT_TARGET_TEMPERATURE, SUPPORT_FAN_MODE, SUPPORT_SWING_MODE,
#     SUPPORT_PRESET_MODE, PRESET_NONE, PRESET_ECO, PRESET_BOOST)

# SUPPORT_FLAGS = SUPPORT_TARGET_TEMPERATURE | SUPPORT_FAN_MODE | SUPPORT_SWING_MODE | SUPPORT_PRESET_MODE
from .const import DOMAIN

from homeassistant.const import TEMP_CELSIUS, ATTR_TEMPERATURE
from .entity import TornadoEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([TornadoClimat(coordinator, entry)])



class TornadoClimat(TornadoEntity ,ClimateEntity):
    """Representation of a custom climate entity."""

    def __init__(self , cord ,entry):
        """Initialize the climate device."""
        super().__init__(cord,entry)        
        self._attr_name = "My Climate Device"
        self._attr_hvac_mode = HVAC_MODE_OFF
        self._attr_current_temperature = 26.0
        self._attr_target_temperature = 25.0
        self._attr_temperature_unit = TEMP_CELSIUS
        self._attr_fan_mode = "auto"
        self._attr_preset_mode = None
        self._attr_hvac_modes = [HVACMode.OFF, HVACMode.HEAT, HVACMode.COOL, HVACMode.AUTO]
        self._attr_fan_modes = ["auto", "silent", "low", "medium", "high"]
        self._attr_coordinator = cord
        self._attr_entry = entry
        self._attr_preset_modes = ['ECO' ,'NORMAL']
        # Using the ClimateEntityFeature IntFlag enum
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE |
            ClimateEntityFeature.FAN_MODE |
            ClimateEntityFeature.TURN_OFF   |
            ClimateEntityFeature.TURN_ON  |
            ClimateEntityFeature.PRESET_MODE
        )



    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is not None:
            self._attr_target_temperature = temperature
            self.async_write_ha_state()

    async def async_set_hvac_mode(self, hvac_mode):
        """Set the HVAC mode."""
        if hvac_mode in self._attr_hvac_mode:
            self._hvac_mode = hvac_mode
            self.async_write_ha_state()

    async def async_set_fan_mode(self, fan_mode):
        """Set the fan mode."""
        if fan_mode in self._attr_fan_modes:
            self._fan_mode = fan_mode
            self.async_write_ha_state()


    def update(self):
        """Fetch the latest state from the device."""
        # You should implement logic here to update the device state
        pass
