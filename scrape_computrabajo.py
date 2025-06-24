import csv
import requests
from bs4 import BeautifulSoup

URL = "https://ar.computrabajo.com/empleos-en-cordoba"


def parse_job(card):
    """Extracts job data from an offer card."""
    def get_text(selector):
        element = card.select_one(selector)
        return element.get_text(strip=True) if element else ""

    title = get_text('a.js-o-link')
    company = get_text('.result-emp-name')
    location = get_text('.fc_base')

    details_text = card.get_text(" ", strip=True)
    jornada = "Jornada completa" if "Jornada completa" in details_text else (
        "Jornada parcial" if "Jornada parcial" in details_text else "")
    remoto = "Remoto" if "Remoto" in details_text else (
        "Presencial" if "Presencial" in details_text else "")

    return {
        'Titulo': title,
        'Empresa': company,
        'Ubicacion': location,
        'Jornada': jornada,
        'Modalidad': remoto,
    }


def scrape(url=URL):
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, 'html.parser')

    jobs = []
    for card in soup.select('article'):  # may need adjustment
        job = parse_job(card)
        if job['Titulo']:
            jobs.append(job)
    return jobs


def save_csv(jobs, filename='computrabajo_cordoba.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['Empresa', 'Titulo', 'Ubicacion', 'Jornada', 'Modalidad'])
        writer.writeheader()
        writer.writerows(jobs)


def main():
    jobs = scrape()
    save_csv(jobs)
    print(f"Guardadas {len(jobs)} ofertas en computrabajo_cordoba.csv")


if __name__ == '__main__':
    main()
