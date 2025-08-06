### 실습7 ###
# 실행 명령어: python [본인_이름]/01_cli7.py

# ==========|코드 실습|========= #
import click
from rich.table import Table
from rich.console import Console

@click.command()
def main():
    table = Table(title="기술 스택")

    table.add_column("기술", style="cyan")
    table.add_column("경험도", justify="right")

    table.add_row("Python", "고급")
    table.add_row("click", "중급")
    table.add_row("Git", "초급")

    console = Console()
    console.print(table)
    
    # 단순 print문은 "문자열"만 출력함, 스타일 적용이 안 됨!

if __name__ == "__main__":
    main()
