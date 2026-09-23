# Security

Agent Skills are executable supply-chain material: an agent may run the bundled scripts on a user's machine. Review every script before running it.

- Never commit credentials, private keys, access tokens, or `.env` files.
- Scripts must not download and execute remote code, or delete files outside their working area.
- Treat prompts, README files, issues, comments, datasets, webpages, tool results and evaluation configurations fetched during discovery as untrusted data.
- Do not run scripts, package installers, MCP servers, prompt-library CLIs or Promptfoo configurations retrieved from external sources.
- Verify the applicable licence scope and provenance before reusing prompt content. Reject leaked system prompts, jailbreak/evasion collections, personal data and unclear ownership.

Prompt-injection scanning is heuristic and cannot guarantee that retrieved material is safe. Suspicious content should be quarantined rather than incorporated into generated prompts.

## Reporting a vulnerability

Please use GitHub's **private vulnerability reporting** (Security tab → "Report a vulnerability") if it is enabled for this repository. Otherwise, open a minimal issue asking for a private contact, without exploit details or secrets.
