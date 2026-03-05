import argparse
import sys
from .scaffolder import create_project
from .data_loader import load_data
from .trainer import train_model


def main():
    parser = argparse.ArgumentParser(
        prog="dsdashboard",
        description="🚀 Data Science Dashboard CLI Framework"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="dsdashboard 1.0.1"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    # ---------------- CREATE ----------------
    create_parser = subparsers.add_parser(
        "create",
        help="Create new dashboard project"
    )
    create_parser.add_argument("project_name")
    create_parser.set_defaults(func=handle_create)

    # ---------------- LOAD DATA ----------------
    load_parser = subparsers.add_parser(
        "load-data",
        help="Load dataset into project"
    )
    load_parser.add_argument("project_name")
    load_parser.add_argument("file_path")
    load_parser.add_argument("--target", default=None)
    load_parser.set_defaults(func=handle_load_data)

    # ---------------- TRAIN ----------------
    train_parser = subparsers.add_parser(
        "train",
        help="Train model using external training script"
    )
    train_parser.add_argument("project_name")
    train_parser.add_argument(
        "--script",
        required=True,
        help="Path to external training script"
    )
    train_parser.set_defaults(func=handle_train)

    args = parser.parse_args()

    try:
        args.func(args)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


# ---------------- Handlers ----------------

def handle_create(args):
    create_project(args.project_name)


def handle_load_data(args):
    load_data(
        project_name=args.project_name,
        file_path=args.file_path,
        target=args.target
    )


def handle_train(args):
    train_model(
        project_name=args.project_name,
        script_path=args.script
    )


if __name__ == "__main__":
    main()