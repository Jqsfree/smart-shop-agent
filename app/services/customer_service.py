fake_customers = {
    "li": {
        "phone": "00000000000",
        "level": "SVIP",
        "last_order": "现代简约墙纸",
    },
    "lingpeng": {
        "phone": "00000000000",
        "level": "vip",
        "last_order": "森系壁纸",
    },
    "muse": {
        "phone": "00000000000",
        "level": "ssvip",
        "last_order": "king",
    },
}

def get_customer(customer_name: str):

    customer = fake_customers.get(customer_name.lower())

    if not customer:
        return {"success": False, "message": "客户不存在"}

    return {"success": True, "data": customer}

