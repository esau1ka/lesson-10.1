from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info):
    slovo = ["Maestro", "MasterCard", "Visa Classic", "Visa Platinum", "Visa Gold"]
    account = "Счет"
    for i in slovo:
        if i.lower() in info.lower():
            no_word = info.replace(i, "")
            no_space = no_word.strip()
            return f"{i} {get_mask_card_number(no_space)}"

    if account.lower() in info.lower():
        no_word = info.replace(account, "")
        no_space = no_word.strip()
        return f"{account} {get_mask_account(no_space)}"

    return "Некорректный номер или счет"



def get_date(raw_date: str) -> str:

    dt = datetime.strptime(raw_date, "%Y-%m-%dT%H:%M:%S.%f")

    formatted_date = dt.strftime("%d.%m.%Y")

    return formatted_date


# Пример использования
raw_date = "2024-03-11T02:26:18.671407"
formatted_date = get_date(raw_date)
print(formatted_date)

you_text = "Счет 73654108430135874305"
print(mask_account_card(you_text))
# проверка коммитаssssgidddffdfпшеdfdffdfdfdffgvvvvgit statusfgfggfgvbvbvb

