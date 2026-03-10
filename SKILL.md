---
name: api-rate-guardrails
description: Tracks API token usage dynamically for AI Agents without external DBs, alerts at 90% capacity.
emoji: 🚦
---

# 🚦 API Rate Guardrails

## Core Value
Provides a lightweight, zero-dependency token tracking system for AI agents (like OpenClaw and Claude Code). Prevents unexpected API overages by alerting users via Telegram when usage reaches 90% of the daily limit.

## Use This Skill For
- Tracking API token usage automatically during agent sessions.
- Preventing catastrophic billing overages from recursive loops.
- Emulating external DB tracking with a simple, persistent local JSON state.

## Quick Prompt Patterns
- "Check API usage limits"
- "Log 50000 tokens to the guardrail tracker"
- "Audit my token consumption for today"

## Workflow
1. **Initialize/Load State:** The script checks `~/.openclaw/api_usage_tracking.json` for current daily usage. If the date has rolled over, usage is reset to 0.
2. **Log Usage:** When called with `--log <amount>`, the script adds the token count to the daily total and saves the state.
3. **Threshold Check:** The script calculates the percentage of the 1,000,000 token limit used.
4. **Alerting:** If the usage exceeds 90%, a mock Telegram notification is triggered to alert the operator.
5. **Report:** Output the current usage and percentage to the console.

## Reference Files

| File | Type | Description |
|------|------|-------------|
| `scripts/check_limits.py` | Python Script | Core logic for tracking tokens and triggering alerts. |
