#
# Copyright (c) 2026, Saidwire
#
# SPDX-License-Identifier: BSD-2-Clause
#

"""Saidwire real-time speech-to-text for Pipecat."""

from .stt import DEFAULT_MODEL, DEFAULT_URL, SaidwireSTTService, SaidwireSTTSettings
from .version import __version__

__all__ = [
    "DEFAULT_MODEL",
    "DEFAULT_URL",
    "SaidwireSTTService",
    "SaidwireSTTSettings",
    "__version__",
]
