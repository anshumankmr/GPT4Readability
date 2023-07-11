import os
import click
from getpass import getpass
from GPT4Readability.readme_gen import generate_readme
from GPT4Readability.suggestions_gen import generate_suggestions

@click.command()
@click.argument('path')
@click.option('--function', '-f', multiple=True, type=click.Choice(['readme', 'suggestions', 'both'], case_sensitive=False), default=['both'], help="Function to use: 'readme', 'suggestions' or 'both'")
@click.option('--output_readme', '-or', type=str, default='README.md', help='Output filename for readme')
@click.option('--output_suggestions', '-os', type=str, default='suggestions.md', help='Output filename for suggestions')
@click.option('--model', '-m', type=click.Choice(['gpt-3.5-turbo', 'gpt-4'], case_sensitive=False), default='gpt-3.5-turbo', help='Model to use: "gpt-3.5-turbo" or "gpt-4"')
def main(path, function, output_readme, output_suggestions, model):
    """CLI tool for GPT4Readability."""
    
    # Check for OPENAI_API_KEY environment variable
    if not os.getenv('OPENAI_API_KEY'):
        print("OPENAI_API_KEY environment variable not found. Please input it:")
        os.environ['OPENAI_API_KEY'] = getpass()
    
    # Append '.md' if it's not there
    if not output_readme.endswith('.md'):
        output_readme += '.md'
    
    if not output_suggestions.endswith('.md'):
        output_suggestions += '.md'
    
    if 'readme' in function or 'both' in function:
        generate_readme(path, output_readme, model)
        
    if 'suggestions' in function or 'both' in function:
        generate_suggestions(path, output_suggestions, model)

if __name__ == '__main__':
    main()