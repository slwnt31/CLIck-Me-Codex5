### 실습6 ###
# 실행 명령어: python [본인_이름]/01_cli6.py

# ==========|코드 실습|========= #
import click
import pyfiglet

@click.command()
def main():
    click.echo(pyfiglet.figlet_format("Sujin", font="banner3-D"))

if __name__ == "__main__":
    main()
