# Token Tracking Architecture

## Design Decisions
The guardrails system avoids external dependencies by leveraging the local filesystem. This ensures AI agents can run self-contained limits without requiring API keys for Redis, PostgreSQL, or MongoDB.

## Storage Format
The state is stored in a simple JSON structure at `~/.openclaw/api_usage_tracking.json`:
```json
{
  "tokens_used": 145000,
  "last_reset": "2026-03-10"
}
```

## Threshold Calculations
The agent monitors the ratio `tokens_used / limit`. If it exceeds 0.90 (90%), a critical alert is generated via a mocked Telegram push. The threshold mechanism prevents runaway recursion loops typical in autonomous sub-agents.
