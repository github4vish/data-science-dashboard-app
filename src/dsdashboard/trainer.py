import subprocess
from pathlib import Path
import sys
import os


def train_model(project_name, script_path):
    project_path = Path(project_name).resolve()

    if not project_path.exists():
        raise Exception(f"Project '{project_name}' does not exist.")

    train_script = Path(script_path).resolve()

    if not train_script.exists():
        raise Exception("Training script not found.")

    print("🚀 Starting model training using external script...\n")

    result = subprocess.run(
        [sys.executable, str(train_script)],
        cwd=project_path,
        capture_output=True,
        text=True,
        env={**os.environ, "PROJECT_ROOT": str(project_path)}
    )

    print(result.stdout)

    if result.returncode != 0:
        print(result.stderr)
        raise Exception("Training failed.")

    print("\n✅ Training completed successfully!")