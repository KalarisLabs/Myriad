#!/usr/bin/env python3
"""Validate Kalaris-style SKILL.md files without network access."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "skill-frontmatter.schema.json"
REQUIRED_SECTIONS = [
    "# Mission",
    "# Activation conditions",
    "# Preconditions and fail-closed checks",
    "# Deterministic procedure",
    "# Output contract",
    "# Error handling",
    "# Validation tests",
    "# Safety and scope",
    "# Scientific basis",
]


def extract_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("file does not start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("frontmatter closing delimiter not found")
    data = yaml.safe_load(text[4:end])
    if not isinstance(data, dict):
        raise ValueError("frontmatter must parse to an object")
    return data, text[end + 5 :]


def validate_frontmatter(data: dict) -> list[str]:
    errors: list[str] = []
    for key in ("name", "version", "description", "parameters"):
        if key not in data:
            errors.append(f"missing frontmatter key: {key}")
    name = data.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(name)):
        errors.append("name is not strict kebab-case")
    version = data.get("version", "")
    if not re.fullmatch(r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)", str(version)):
        errors.append("version is not semantic x.y.z")
    if len(str(data.get("description", ""))) < 80:
        errors.append("description is too short for reliable routing")
    params = data.get("parameters")
    if isinstance(params, dict):
        if params.get("type") != "object":
            errors.append("parameters.type must be object")
        if params.get("additionalProperties") is not False:
            errors.append("parameters.additionalProperties must be false")
        if not isinstance(params.get("required"), list):
            errors.append("parameters.required must be an array")
        if not isinstance(params.get("properties"), dict):
            errors.append("parameters.properties must be an object")
    else:
        errors.append("parameters must be an object")
    return errors


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    try:
        data, body = extract_frontmatter(text)
    except Exception as exc:
        return [str(exc)]
    errors.extend(validate_frontmatter(data))
    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"missing required section: {section}")
    if "fail closed" not in body.lower() and "fail-closed" not in body.lower():
        errors.append("body must declare fail-closed behavior")
    if "provenance" not in body.lower():
        errors.append("body must define provenance handling")
    if path.parent.name != data.get("name"):
        errors.append("directory name must equal frontmatter name")
    return errors


def main() -> int:
    json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        print("No SKILL.md files found", file=sys.stderr)
        return 1
    failed = False
    for skill in skills:
        errors = validate_skill(skill)
        if errors:
            failed = True
            print(f"FAIL {skill.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"PASS {skill.relative_to(ROOT)}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
