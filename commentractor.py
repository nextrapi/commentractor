import click
import requests
from bs4 import BeautifulSoup as BS
from bs4 import Comment
import os,sys


@click.command()
@click.option('--url', '-u', help='Url to scan for comments.', prompt=True, prompt_required=False)
@click.option('--file', '-f', help='File containing URLs to scan for comments.', prompt=True, prompt_required=False)
@click.option('--output', '-o',
              help='Output location.', prompt=True, prompt_required=False)
def main(output, url='', file=''):
    if ((not url) and (not file)):
        click.echo(click.style(
            'A URL to scan for comments or a file containing multiple urls is required.', fg='red'))
        ctx = click.get_current_context()
        click.echo(ctx.get_help())
        return
    if file:
        file = open(file, 'r').readlines()
        with click.progressbar(file) as file:
            for url in file:
                click.echo('\n\n')
                try:
                    saveComments(getComments(url.strip()), output)
                except KeyboardInterrupt:
                    sys.exit()  
                except:
                    click.echo(click.style('Failed to fetch ' + url, fg='red'))
                click.echo('\n\n')

    else:
        saveComments(getComments(url.strip()), output)
    return


def getComments(url):
    return {
        url:BS(requests.get(url).text, 'html.parser').find_all(string=lambda text: isinstance(text, Comment))
    }


def saveComments(urls, output):
    file = open((output or os.getcwd())+'/comments.txt', "a+")
    for url in urls:
        click.echo(click.style(url, fg='green'))
        file.write('\n'+url + '\n\n')
        for comment in urls[url]:
            click.echo(comment.extract())
            file.write(comment.extract().strip() + '\n')
    return

if __name__ == '__main__':
    main()
