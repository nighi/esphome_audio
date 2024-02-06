import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import speaker
from esphome.core import coroutine_with_priority

from esphome.const import CONF_ID, CONF_MODE

from ...matrixio import my_esp_adf as matrix_io_adf

CODEOWNERS = ["@gnumpi"]
DEPENDENCIES = ["my_esp_adf", "speaker"]

from .. import (
    esp_adf_ns,
    ADFPipelineComponent,
    CONF_ADF_COMP_ID,
    ADF_COMPONENT_SCHEMA,
    add_pipeline_elements
)

ADFSpeaker = esp_adf_ns.class_(
    "ADFSpeaker", ADFPipelineComponent, speaker.Speaker, cg.Component
)

CONFIG_SCHEMA = speaker.SPEAKER_SCHEMA.extend(
    {
      cv.GenerateID(): cv.declare_id(ADFSpeaker),  
    }
).extend(ADF_COMPONENT_SCHEMA)

#@coroutine_with_priority(100.0)
async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await add_pipeline_elements(var, config)
    await speaker.register_speaker(var, config)
