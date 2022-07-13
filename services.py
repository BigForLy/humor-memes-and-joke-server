import requests


def string_replace(string: str) -> dict:
    content = string[12:string.rfind('"')]  # получает значение из словаря в строке

    return {"content": content}


def get_humor(humor_type: int) -> str:
    url = f'http://rzhunemogu.ru/RandJSON.aspx?CType={humor_type}'
    try:
        response = requests.get(url)
        assert response.status_code == 200
        result = response.text
    except:
        result = 'Попробуйте еще раз!'
    return result
