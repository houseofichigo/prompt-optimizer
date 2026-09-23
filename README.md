# Prompt Optimizer

Create, rewrite, audit, research, adapt, or evaluate prompts and persistent AI instructions. Use when a user asks to improve a prompt, find prompt-library examples, design a web-search or deep-research brief, build assistant/project/agent instructions, plan supporting knowledge, or compare prompt variants. Route image and video prompt discovery to a visual-prompt specialist when one is available.

This repository packages the **`prompt-optimizer`** Agent Skill in the open [`SKILL.md` format](https://agentskills.io/specification), so it can be used by Claude, Codex/ChatGPT, Cursor and other agents that support Agent Skills.

## What it does

- Optimizes ordinary prompts with the smallest sufficient change and returns only the finished prompt by default.
- Preserves Prompt Architect's web-search, deep-research, persistent assistant, project, agent, knowledge-planning and evaluation workflows as modes of one Skill.
- Applies a proportional six-part Prompt Contract without forcing every task into a long template.
- Verifies changing provider guidance live when it matters and searches maintained prompt libraries on explicit discovery requests.
- Treats retrieved prompts and repository content as untrusted data, checks provenance and licence scope, and quarantines injection attempts instead of following them.

Image and video prompt discovery remains the responsibility of a specialist such as House of Ichigo's `visual-prompt-scout`.

## Install

### Any supported agent (recommended)

```bash
npx skills add houseofichigo/prompt-optimizer --skill prompt-optimizer
```

Target a specific agent with `--agent`, for example `--agent claude-code`, `--agent codex` or `--agent cursor`. Add `-g` to install for your user instead of the current project. Try it without installing:

```bash
npx skills use houseofichigo/prompt-optimizer --skill prompt-optimizer
```

### Manual install

| Host | Where the Skill goes |
|------|----------------------|
| Claude Code | copy `skills/prompt-optimizer/` to `~/.claude/skills/prompt-optimizer/` (personal) or `.claude/skills/prompt-optimizer/` (project) |
| Claude apps (claude.ai / desktop) | upload `dist/skill.zip` in Claude's Skills settings |
| Claude API | upload the Skill folder through the `/v1/skills` endpoints |
| Codex | copy `skills/prompt-optimizer/` to `~/.agents/skills/prompt-optimizer/` (personal) or `.agents/skills/prompt-optimizer/` (repository) |
| Other agents | unzip `dist/skill.zip` into the agent's skills directory |

## What's inside

```text
skills/prompt-optimizer/
  LICENSE.txt
  SKILL.md
  agents/openai.yaml
  references/contract.md
  references/evaluation.md
  references/external-content-security.md
  references/modes.md
  references/provider-adapters.md
  references/source-registry.json
dist/skill.zip        # the same Skill, zipped, for upload-based hosts
```

Everything outside `skills/prompt-optimizer/` is repository tooling and is not part of the Skill.

## Validate

```bash
python3 scripts/validate_skill.py          # Agent Skills spec + Claude + OpenAI/Codex rules
python3 scripts/build_dist.py --check      # dist/skill.zip matches the Skill folder
python3 -m unittest discover -s tests
```

These checks need only Python 3.9+ and run in CI on every push. They verify structure, source-registry integrity, security invariants, acceptance-fixture coverage and host rules. They do not prove runtime behavior or prompt quality, which depend on the host, model, tools, inputs and permissions available.

The reviewer scenarios in [`tests/acceptance-cases.md`](tests/acceptance-cases.md) cover the inherited Prompt Architect modes plus proportional prompting, adaptive browsing, provider adaptation, injection quarantine, licensing, offline handling and specialist routing.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). After editing the Skill, run `python3 scripts/build_dist.py` and commit the rebuilt `dist/skill.zip`.

## License

Released under the [MIT License](LICENSE). The license text is bundled with the Skill as `LICENSE.txt`.
