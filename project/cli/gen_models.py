from main import Parsing
import click


@click.command()
@click.option('--json-schema', required=True, type=click.Path(exists=True), help='Path to the JSON schema file.')
@click.option('--out-dir', required=True, type=click.Path(file_okay=False, writable=True),
              help='Output directory for the generated models.')

def gen_models(json_schema, out_dir):
    # логика для генерации моделей.
    out_dir += 'models.py'

    pars_obj = Parsing(json_schema, out_dir)
    pars_obj.open_js_file()
    pars_obj.parse_json_schema()



if __name__ == '__main__':
    gen_models()