from datetime import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    today_year: int = datetime.now().year
    return {
        'year': today_year,
    }
