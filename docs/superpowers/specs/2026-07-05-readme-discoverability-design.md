# README and Discoverability Design

## Goal

Make `lazy-paper-reader` understandable and installable for an international audience while retaining a concise Chinese introduction at the end of the README. Improve GitHub-native discovery without changing the skill's behavior.

## Scope

1. Rewrite the root README with English as the primary language.
2. Replace the legacy installation location with the current official user-level Agent Skills location: `$HOME/.agents/skills`.
3. Update the GitHub repository description and add focused repository topics.

The skill instructions, runtime behavior, source layout, release process, social preview, and external promotion are out of scope.

## README Structure

The English section will contain:

1. A short value proposition that distinguishes interactive reading from one-shot summarization.
2. A compact feature list covering staged reading, confirmation-gated note updates, evidence discipline, resumable Markdown notes, and the autonomous-driving world-model profile.
3. The five-stage reading workflow.
4. Supported paper inputs.
5. User-level installation commands targeting `$HOME/.agents/skills/lazy-paper-reader`.
6. An explicit invocation example and a brief note that Codex can also invoke the skill implicitly.
7. Repository structure and license.

The final `中文说明` section will summarize the purpose, workflow, supported inputs, and installation location without duplicating every English detail.

## Repository Metadata

Description:

> An interactive Codex skill for reading research papers stage by stage and maintaining evidence-aware Markdown notes.

Topics:

- `codex`
- `agent-skills`
- `research-papers`
- `paper-reading`
- `academic-research`
- `markdown`
- `computer-vision`
- `world-model`

The topic list stays focused enough to describe the repository accurately and avoids unrelated popularity keywords.

## Verification

- Run the existing contract tests.
- Run the official skill validator.
- Check README links and shell commands for path consistency.
- Confirm the GitHub API reports the intended description and topics.
- Confirm the remote `main` commit matches the local commit and the worktree is clean.
