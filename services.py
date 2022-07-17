import requests


def string_replace(string: str) -> dict:
    # получает значение из словаря в строке
    content = string[12:string.rfind('"')]

    return {"content": content}


def get_humor(humor_type: int) -> str:
    try:
        url = f'http://rzhunemogu.ru/RandJSON.aspx?CType={humor_type}'
        response = requests.get(url)
        assert response.status_code == 200
        result = response.text
    except:
        result = 'Попробуйте еще раз!'
    return result
