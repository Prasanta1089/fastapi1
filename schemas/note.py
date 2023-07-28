def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "number": int(item["number"]),
        "important": item["important"]
    }

def notesEntity(items) -> list:
    return [noteEntity(item) for item in items]