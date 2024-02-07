import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import microphone
from esphome.const import CONF_ID

from .. import (
    esp_adf_ns,
    ADFPipelineComponent,
    ADF_COMPONENT_SCHEMA,
    add_pipeline_elements,
)

CODEOWNERS = ["@gnumpi"]
DEPENDENCIES = ["my_esp_adf", "microphone"]


ADFMicrophone = esp_adf_ns.class_(
    "ADFMicrophone", ADFPipelineComponent, microphone.Microphone, cg.Component
)

CONFIG_SCHEMA = microphone.MICROPHONE_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(ADFMicrophone),
    }
).extend(ADF_COMPONENT_SCHEMA)


# @coroutine_with_priority(100.0)
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await add_pipeline_elements(var, config)
    await microphone.register_microphone(var, config)