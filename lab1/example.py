import json
import shlex

records = []

while True:
    try:
        parts = shlex.split(input("search> "))
        if not parts:
            continue
        if parts[0] == "load" and len(parts) == 2:
            with open(parts[1], encoding="utf-8") as file:
                records = json.load(file)
            print("Загружено:", len(records))
        elif parts == ["show"]:
            for record in records:
                print(record["id"], record["title"])
        elif parts[0] == "search" and len(parts) == 2:
            query = parts[1]
            matches = []
            for record in records:
                if query in record["title"]:
                    score = record["title"].count(query) if query else 0
                    matches.append((score, record))
            print("Найдено:", len(matches), "Показано:", min(1, len(matches)))
            if matches:
                score, record = max(matches, key=lambda match: match[0])
                print(record["id"], record["title"])
                print("Релевантность:", score)
        else:
            print('Команды: load <файл>, show, search "<запрос>"')
    except EOFError:
        break
    except (OSError, ValueError) as error:
        print("Ошибка:", error)
