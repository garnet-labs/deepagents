from pathlib import Path
from tempfile import TemporaryDirectory

from deepagents.backends import FilesystemBackend


def main() -> None:
    with TemporaryDirectory() as directory:
        root = Path(directory)
        (root / "sample.txt").write_text(
            "before\nexecution-diff\nafter\n",
            encoding="utf-8",
        )

        backend = FilesystemBackend(root_dir=root, virtual_mode=True)
        result = backend.grep("execution-diff", path="/")

    expected_matches = [
        {"path": "/sample.txt", "line": 2, "text": "execution-diff"},
    ]
    if result.error or result.matches != expected_matches:
        raise RuntimeError(f"Unexpected grep result: {result}")

    print(f"GREP_OK {result.matches}")


if __name__ == "__main__":
    main()
