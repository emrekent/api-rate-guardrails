# API Rate Guardrails

**Production-grade API token tracking and threshold protection for autonomous agents.**

A lightweight, local-first rate limit protection skill for OpenClaw and Claude Code. Prevents agents from burning through quotas or crashing during long-running batch jobs.

---

## Install

From GitHub:
```bash
npx skills add https://github.com/emrekent/api-rate-guardrails --skill api-rate-guardrails
```

---

## What It Does

When your agents are executing large loops or running overnight, this skill provides:

```
1. TRACKING → Monitors token/request usage locally without external databases.
2. ALERTING → Pushes Telegram notifications when 90% capacity is reached.
3. THROTTLING → Gracefully pauses execution queues to prevent HTTP 429 crashes.
4. RECOVERY → Auto-resumes when rate limits reset.
```

## What Makes This Worth Installing
- **Zero Database Requirement**: Uses native file-system tracking (`api_usage_tracking.json`), perfect for sandboxed AI agents.
- **Provider Agnostic**: Works across Gemini, Claude, and OpenAI APIs.
- **Save Money & Sleep**: Stops your autonomous agents from running up massive bills due to runaway loops.

## Quick Proof

When an agent hits the 90% threshold, instead of crashing the process, the guardrail triggers:

```text
[Telegram Alert: emrekentbot]
⚠️ API Rate Limit Warning
Provider: Anthropic Claude 3.5 Sonnet
Usage: 91% (910,000 / 1,000,000 TPM)
Action Taken: Zero-Idle Queue Paused. Sleeping for 60 seconds.
```

---

## Best Prompts To Try

```text
"Implement API guardrails on my next script execution."
"Check my current token usage."
"Configure a Telegram alert for 90% token capacity."
```

---

## What's Inside

```
api-rate-guardrails/
├── SKILL.md                 Core skill guide (imperative agent instructions)
├── scripts/
│   ├── check_limits.py      Token counter and webhook/alert trigger
└── references/
    ├── architecture.md      Documentation on local state tracking
```

---

## About the Creator

Built by **[Emre Kent](https://www.linkedin.com/in/emrekent)** — Systems architect & builder. Former math teacher turned automation designer.

I design growth engines, AI workflows, and automation systems. I build CRM architectures, AI agents, n8n automation systems, and personal operating systems that compound.

For discussions on AI agents, skills architecture, and automation systems — [connect on LinkedIn](https://www.linkedin.com/in/emrekent).

---

## License

Open source. Free to use, adapt, and build on.
