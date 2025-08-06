### Homework ###
# 실행 명령어: python [본인_이름]/cli-proflie.py

# ==========|코드 실습|========= #
import click
from rich.markdown import Markdown
from rich.console import Console
from rich.progress import track
from rich.table import Table
from rich.syntax import Syntax
import time, pyfiglet

console = Console()

@click.command()
def main():
    for step in track(range(5), description="Wait..."):
        time.sleep(0.3)
                
    md = Markdown("""# ⭐ BAEK'S CLI PROFILE⭐
안녕하세요, **백수진**입니다. 현재 컴퓨터공학과에서의 2-1을 마쳤으며, 이제 막 따끈따끈해진 **레몬 파이**입니다 ;) \n
저는 `ESTP`이고, 짧은 순간일지라도 강한 인상을 남기는 걸 좋아합니다. \n
헬로 파이 활동으로 파이썬에 한 발자국 더 가까워지길 희망합니다. 많이 배워가겠습니다 🫡
""")
    
    table = Table(title="그리고 저는..")
    
    table.add_column("장점", style="cyan")
    table.add_column("ex", justify="left")
    
    table.add_row("앉아 있기", "어릴 때부터 잘 앉아 있는다고 칭찬 받음\n(사실은 앉아서 공부만 하는 게 아님)\n")
    table.add_row("초긍정", "기억력이 그닥 좋지 않아서 나쁜 건 웬만하면 쉽게 잊음\n대신 좋은 기억은 오래 가지고 감!!! 굉장히 모순적인 사람\n")
    table.add_row("이성적임", "선공감(10%) 후해결(90%)을 좋아함")
    
    code = "\ndef BaekSujin():\n    print('모두들 만나 뵙게 되어 영광입니다!!!!')\n"
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
    
    print("\n")
    click.echo(pyfiglet.figlet_format("Welcome", font="slant"))
    
    console.print(md)
    print("\n")

    console.print(table)
    print("                                    이런 사람입니다....")
    print("\n")
    
    console.print(syntax)

    
if __name__ == "__main__":
    main()