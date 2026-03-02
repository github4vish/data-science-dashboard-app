import shutil
from pathlib import Path
import pandas as pd
import json


def load_data(project_name, file_path, target=None):
    project_path = Path(project_name)
    data_folder = project_path / "data"

    if not project_path.exists():
        raise Exception(f"Project '{project_name}' does not exist.")

    if not Path(file_path).exists():
        raise Exception("Data file not found.")

    # Copy dataset
    destination = data_folder / Path(file_path).name
    shutil.copy(file_path, destination)

    print(f"✅ Dataset copied to {destination}")

    # Load dataset
    try:
        df = pd.read_csv(destination)

        print("\n📊 Dataset Preview:")
        print(df.head())
        print("\n🧾 Columns:", list(df.columns))
        print(f"📈 Shape: {df.shape}")

        # If target provided → save metadata
        if target:
            if target not in df.columns:
                raise Exception(f"Target column '{target}' not found in dataset.")

            metadata = {
                "dataset": destination.name,
                "target_column": target,
                "columns": list(df.columns),
                "shape": df.shape
            }

            metadata_path = project_path / "data" / "metadata.json"
            with open(metadata_path, "w") as f:
                json.dump(metadata, f, indent=4)

            print(f"\n🎯 Target column set to: {target}")
            print("📝 Metadata saved to data/metadata.json")

    except Exception as e:
        raise Exception(f"Dataset copied but failed to process: {e}")