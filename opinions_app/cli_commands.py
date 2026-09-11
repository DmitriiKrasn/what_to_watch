import csv

from . import app, db
from .models import Opinion


@app.cli.command('load_opinions')
def load_opinions_command():
    """Загружает мнения о фильмах из файла opinions.csv."""
    with open('opinions.csv', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file)
        opinions = list(reader)
    added = 0
    for opinion in opinions:
        if Opinion.query.filter_by(text=opinion['text']).first():
            continue
        db.session.add(Opinion(**opinion))
        added += 1
    db.session.commit()
    print(f'Загружено мнений: {added}')
