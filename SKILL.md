# API Rate Guardrails

## Description
Tracks API token usage dynamically for AI Agents (like OpenClaw and Claude Code) without requiring external databases. Uses local JSON file storage for lightweight persistence and alerts via Telegram when usage hits 90% capacity.

## Installation
No extra dependencies required. Runs on standard Python 3.

## Usage
- Run `python3 scripts/check_limits.py` to check current token usage.
- Run `python3 scripts/check_limits.py --log <tokens>` to log usage.

## Implementation Details
This skill tracks usage via a local `~/.openclaw/api_usage_tracking.json` file. The file resets daily. When the 90% threshold of the defined limit is reached, a Telegram alert is mocked.

## Automation
Can be integrated directly into shell wrappers or agent exit hooks to automatically log estimated tokens per session.
