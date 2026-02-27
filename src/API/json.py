import json

def read_json_file(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл не найден")
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
    except Exception as e:
        print("Ошибка:", e)

# пример использования
if __name__ == "__main__":
    data = read_json_file("config.json")
    if data:
        print("JSON успешно прочитан:")
        print(data)
