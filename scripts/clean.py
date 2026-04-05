import subprocess
import shutil
from pathlib import Path


class BuildPaths:
    _root: Path = Path(__file__).parent

    PUBLIC: Path = _root / "public"
    RESOURCE: Path = _root / "resource"
    BUILD_LOCK: Path = _root / ".hugo_build.lock"


def get_paths() -> list[Path]:
    return [v for k, v in vars(BuildPaths).items() if not k.startswith("_")]


def main():
    paths = get_paths()

    for p in paths:
        if not p.exists():
            continue
        if p.is_dir():
            shutil.rmtree(p)
        else:
            p.unlink()


if __name__ == "__main__":
    main()
