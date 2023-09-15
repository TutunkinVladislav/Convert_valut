import requests
from bs4 import BeautifulSoup as bs
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .constants import VALUT


def get_valut(data_from, data_to, data_value):
    """Получаем данные с другого сервиса"""
    content = requests.get(f"https://www.x-rates.com/table/?from={data_from}&amount={data_value}").content
    soup = bs(content, "html.parser")
    exchange_tables = soup.find_all("table")
    exchange_rates = {}
    for exchange_table in exchange_tables:
        for tr in exchange_table.find_all("tr"):
            tds = tr.find_all("td")
            if tds:
                currency = tds[0].text
                if currency == VALUT[data_to]:
                    exchange_rate = "{0:.2f}".format(float(tds[1].text))
                    exchange_rates[data_to] = exchange_rate
    return float(exchange_rate)


@api_view(['GET'])
def convert_valut_usd_to_rub(request):
    """Получаем конвертер валют"""
    data_from = request.GET['from']
    data_to = request.GET['to']
    data_value = request.GET['value']

    if get_valut(data_from, data_to, data_value):
        return Response({'result': get_valut(data_from, data_to, data_value)}, status=status.HTTP_200_OK)
    return Response('Ошибка: Неверный запрос', status=status.HTTP_400_BAD_REQUEST)
