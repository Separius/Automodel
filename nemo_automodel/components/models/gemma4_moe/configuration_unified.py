"""Compatibility config names used by pre-release unified Gemma4 checkpoints.

The unified checkpoints use the same serialized config fields and state-dict
layout as the released Gemma4 implementation, but were authored with
Transformers 5.10.dev model-type names. AutoModel intentionally pins 5.8.1, so
register the newer names without changing the underlying model implementation.
"""

from transformers.models.gemma4.configuration_gemma4 import Gemma4Config, Gemma4TextConfig


class Gemma4UnifiedTextConfig(Gemma4TextConfig):
    model_type = "gemma4_unified_text"


class Gemma4UnifiedConfig(Gemma4Config):
    model_type = "gemma4_unified"

