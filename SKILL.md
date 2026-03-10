---
name: api-rate-guardrails
description: "Tracks API token usage dynamically for AI Agents via local JSON, alerts at 90% capacity. Use when agents run autonomously and risk hitting API limits. Triggers: Check limits, log tokens. NOT for enterprise distributed tracking."
---

# API Rate Guardrails

Provides a lightweight, zero-dependency token tracking system to prevent unexpected API overages.

## Core Workflow

1. **Load State**: Read `~/.openclaw/api_usage_tracking.json`. If `last_reset` != today, reset `tokens_used` to 0.
2. **Log Tokens**: When an API call is made, append the estimated or exact token count to the daily total.
3. **Threshold Check**: Calculate the usage percentage against the predefined daily limit (e.g., 1,000,000 tokens).
4. **Alert Operator**: If usage >= 90%, immediately trigger a Telegram notification and log a critical warning.

## Key Rules

- **Zero External Dependencies**: Do not introduce Redis, SQLite, or external DB calls. Rely solely on local JSON files.
- **Fail-Safe Operation**: If the tracking file is unreadable, default to 0 tokens and recreate it. Never crash the main execution loop due to a tracking failure.
- **Stateless Verification**: Always verify the `last_reset` date upon every invocation to handle midnight rollovers automatically.

## Anti-Patterns

- **Polling the API**: Do not make external API requests (e.g., to OpenAI/Anthropic dashboards) to check limits. Track locally.
- **Blocking Execution**: Do not block the primary agent task while logging tokens. Guardrails must execute asynchronously or sub-10ms.
- **Over-Alerting**: Do not send duplicate alerts once the 90% threshold is crossed, unless usage resets.

## References

- [check_limits.py](scripts/check_limits.py) - Core logic for tracking tokens and triggering alerts.
- [Architecture Deep Dive](references/token_tracking_architecture.md) - Rationale and JSON structure.
