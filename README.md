# API Rate Guardrails Skill

A lightweight, local-first token tracking and rate limit protection skill for AI agents (OpenClaw, Claude Code).

## Overview
Prevents AI agents from burning through provider quotas or hitting unexpected 429 errors during long-running background tasks. It monitors local usage and sends Telegram alerts at 90% capacity, gracefully pausing execution without crashing.

## Installation
```bash
npx skills add emrekent/api-rate-guardrails
```

## Structure
- `SKILL.md` - Core agent instructions and logic flows
- `scripts/` - Python utilities for token counting and alert generation
- `references/` - Architectural documentation for local state tracking
