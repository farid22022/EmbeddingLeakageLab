"""Initial research progress and environment CLI."""

import argparse
import json
import platform
import sys
from pathlib import Path

from embedding_leakage import __version__
from embedding_leakage.core.device import detect_device


ROOT = Path(__file__).resolve().parents[3]
ROADMAP = ROOT / "roadmap.md"


def _roadmap_status() -> tuple[str, list[tuple[str, str, str]]]:
    content = ROADMAP.read_text(encoding="utf-8")
    phase = "unknown"
    overall = "unknown"
    rows: list[tuple[str, str, str]] = []
    in_table = False
    for line in content.splitlines():
        if line.startswith("Current Phase:"):
            phase = line.split(":", maxsplit=1)[1].strip()
        elif line.startswith("Overall Status:"):
            overall = line.split(":", maxsplit=1)[1].strip()
        elif line.startswith("| Phase | Name | Status | Completion |"):
            in_table = True
        elif in_table and line.startswith("|") and not line.startswith("|-------"):
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) == 4 and cells[0] != "Phase":
                rows.append((cells[0], cells[1], cells[2] + " | " + cells[3]))
        elif in_table and not line.startswith("|"):
            in_table = False
    return f"Phase {phase}", rows


def _run_doctor() -> int:
    device = detect_device()
    report = {
        "project_version": __version__,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "device": device.name,
        "cuda_available": device.cuda_available,
        "cuda_device": device.cuda_device,
        "roadmap_found": ROADMAP.is_file(),
    }
    print(json.dumps(report, indent=2))
    return 0 if report["roadmap_found"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ell", description="EmbeddingLeakageLab research CLI")
    parser.add_argument("--version", action="version", version=f"ell {__version__}")
    commands = parser.add_subparsers(dest="command")
    commands.add_parser("status", help="Show the current research phase")
    commands.add_parser("roadmap", help="Show phase progress")
    phase = commands.add_parser("phase", help="Inspect phase progress")
    phase_commands = phase.add_subparsers(dest="phase_command", required=True)
    show = phase_commands.add_parser("show", help="Show a phase's tracked tasks")
    show.add_argument("number", type=int)
    phase_commands.add_parser("next", help="Show the next incomplete phase")
    commands.add_parser("doctor", help="Report Python and available device information")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "doctor":
        return _run_doctor()
    if args.command in {"status", "roadmap", "phase"}:
        title, rows = _roadmap_status()
        if args.command == "status":
            print(title)
            content = ROADMAP.read_text(encoding="utf-8").splitlines()
            overall = next(
                (line.split(":", maxsplit=1)[1].strip() for line in content if line.startswith("Overall Status:")),
                "unknown",
            )
            print(f"Overall status: {overall}")
            return 0
        if args.command == "phase" and args.phase_command == "show":
            matching = [row for row in rows if row[0] == str(args.number)]
            if not matching:
                print(f"Phase {args.number} is not in the roadmap.", file=sys.stderr)
                return 2
            print(f"Phase {matching[0][0]} | {matching[0][1]}: {matching[0][2]}")
            return 0
        if args.command == "phase" and args.phase_command == "next":
            next_row = next((row for row in rows if "TODO" in row[2] or "IN PROGRESS" in row[2]), None)
            if next_row is None:
                print("No incomplete phase found.")
            else:
                print(f"Phase {next_row[0]} | {next_row[1]}: {next_row[2]}")
            return 0
        print(title)
        for number, name, progress in rows:
            print(f"{number}. {name}: {progress}")
        return 0
    build_parser().print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
