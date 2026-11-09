# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project uses
[semantic versioning](https://semver.org/).

## [0.1.2] - 2026-11-08

### Fixed

- Words already delivered in an earlier final are no longer repeated when a `Finalize` lands
  mid-word (for example "coffee shops" followed by "shop" and "shops near me"), in finals and
  interims.
- When the pipeline has a local VAD, results that arrive while nobody is speaking (faint
  background sound, or words replayed from the previous segment) are dropped, so they no longer
  start a user turn or interrupt the bot. Finals get a 1.5 s grace after the VAD stops.

### Changed

- The package now has its own repository,
  [SaidwireLLC/pipecat-saidwire](https://github.com/SaidwireLLC/pipecat-saidwire).
  Source, issue and changelog links point there.
- License changed from MIT to BSD 2-Clause, the same license as Pipecat.
- Tested again with Pipecat v1.15.0: unit tests, and `examples/transcribe_file.py` run
  end to end against the local fake server. No code changes.

## [0.1.1] - 2026-11-06

### Changed

- Repository, issue and changelog links now point to
  [SaidwireLLC/saidwire-integrations](https://github.com/SaidwireLLC/saidwire-integrations).
- Cleaned up the README and package text. No code changes.

## [0.1.0] - 2026-10-31

### Added

- `SaidwireSTTService`: streaming speech-to-text over WebSocket, built on Pipecat's
  `WebsocketSTTService`. Interim and final transcripts, `Finalize` on
  `VADUserStoppedSpeakingFrame` (finals pushed with `finalized=True`), `KeepAlive` while
  idle, `CloseStream` on `EndFrame`, runtime settings via `STTUpdateSettingsFrame`.
- `on_early_word`, `on_speech_started` and `on_utterance_end` event handlers.
- Waits and retries while the service is starting up (HTTP 503 / 429 with `Retry-After`).
- Tested with Pipecat v1.15.0.
