### Homework ###
# 실행 명령어 예시: python cli-profile_with_AI.py profile
# 본인 이름이 포함된 디렉토리에서 실행하면 됩니다.

import json
import os
from click import group, echo
from rich import print
from rich.table import Table
from pyfiglet import figlet_format
from models.developer import Developer
from utils.config import load_config
from utils.logger import logger

@group()
def cli():
    """Vibe Coding Profile AI"""

@cli.command()
def profile():
    """Display developer profile"""
    config = load_config()
    developer = Developer(**config)  # developer는 Developer 객체

    echo(figlet_format(developer.initial))
    echo(developer.bio)

    # Tech Stack 출력
    table = Table(title="Tech Stack")
    table.add_column("Name", justify="center", style="cyan")
    table.add_column("Level", justify="center", style="magenta")

    for tech in developer.tech_stack:
        table.add_row(tech["name"], tech["level"])

    print(table)

    # School 정보
    echo("🎓 School:")
    echo(f"  Name: {developer.school['name']}")
    echo(f"  Major: {developer.school['major']}")
    echo(f"  Experience: {developer.school['experience']}")

    # Projects
    echo("🛠️ Projects:")
    for project in developer.projects:
        echo(f"  - {project['name']}: {project['description']}")

    # Interests
    echo("🌱 Interests:")
    for interest in developer.interests:
        echo(f"  - {interest}")

    # Philosophy & Vibe
    echo(f"💡 Philosophy: {developer.philosophy}")
    echo(f"🔥 Vibe Coding Experience:\n{developer.vibe_coding_experience}")

if __name__ == "__main__":
    cli()
