from main import Pars_rest
import click


@click.command()
@click.option('--json-schema', required=True, type=click.Path(exists=True), help='Path to the JSON schema file.')
@click.option('--out-dir', required=True, type=click.Path(file_okay=False, writable=True),
              help='Output directory for the generated models.')

def gen_rest(json_schema, out_dir):
    """
    A CLI tool to generate models from a JSON schema.
    """
    # Ваша логика для генерации моделей.
    out_dir += 'models.py'

    pars_obj = Pars_rest(json_schema, out_dir)
    pars_obj.open_js_file()
    pars_obj.create_controller_file()



if __name__ == '__main__':
    gen_rest()