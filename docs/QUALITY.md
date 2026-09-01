# Quality policy

The repository is useful only when readers can tell what is complete, what is personal, and what still needs checking.

## Current gates

- `python scripts/check_content.py` checks local Markdown links and image targets.
- PDF files are expected to be readable by standard PDF tooling.
- Notebook files must remain valid JSON.
- External links are not fetched in CI because many course URLs require login or change by cohort.

## Status vocabulary

- **Verified:** local path works and the page has been checked for obvious structural issues.
- **Needs review:** content exists but formulas, attribution, or rendering still need a human pass.
- **Incomplete:** a page is a placeholder or only points to an external source.
- **External:** content belongs to another author or platform.

Green CI proves link integrity only. It does not prove mathematical correctness, course equivalence, or permission to redistribute an asset.
