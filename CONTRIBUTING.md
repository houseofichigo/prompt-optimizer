# Contributing

The canonical Skill lives in `skills/prompt-optimizer/`. Everything outside that folder is repository tooling and is never shipped in `dist/skill.zip`.

## Workflow

1. Edit files under `skills/prompt-optimizer/`.
2. Rebuild the distributable archive:

   ```bash
   python3 scripts/build_dist.py
   ```

3. Validate and test:

   ```bash
   python3 scripts/validate_skill.py
   python3 -m unittest discover -s tests
   ```

4. Commit the Skill changes **and** the rebuilt `dist/skill.zip` together. CI fails if they drift apart.

## Rules

- Keep `SKILL.md` frontmatter portable: `name`, `description`, and optionally `license` and `metadata`. Avoid `compatibility` (OpenAI's validator rejects it); state environment needs in the body. Quote any value containing `: ` or ` #`.
- Keep `SKILL.md` under 500 lines; move detail into `references/`.
- No credentials, `.env` files, private keys, caches, or machine-specific paths.
- Scripts must run with the tools they document and fail with clear messages.
- Do not add copied prompt libraries or the source research PDF. Add concise original guidance and canonical links instead.
- Source-registry changes require a canonical URL, source type, authority tier, current licence scope, permitted use and caution note.
- New modes or safety decisions need a reviewer scenario in `tests/acceptance-cases.md`.
