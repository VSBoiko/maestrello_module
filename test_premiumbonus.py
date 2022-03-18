from crm.premiumbonus import PremiumBonusSDK
import json

def log(data):

    print()
    print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4))
    print()

order_guid="729dc81b-456c-482b-9cfc-7979fd665c44"
phone_number = "79062457811"
fullName = "Sergey Safonov"
items = [
    dict(product_id="10", product_price=100, value=2),
]

pb = PremiumBonusSDK(token="test:459a9e9d73d0ccca376df9b07f230d17")

# SUCCESS
log(
    pb.buyer_info(phone_number=phone_number)
)
# SUCCESS
log(
    pb.buyer_info_detail(phone_number=phone_number)
)
# SUCCESS
log(
    pb.buyer_register(phone_number=phone_number, name=fullName)
)
# SUCCESS
log(
    pb.buyer_edit(phone_number=phone_number, name="Тест Тест")
)
# SUCCESS
# Получение максимального количества бонусов доступного для списания
log(
    pb.write_off_request(phone_number=phone_number, items=items)
)
# SUCCESS
# Эмуляция проведения покупки
log(
    pb.purchase_dry_run(
        phone_number=phone_number,
        items=items,
        order_guid=order_guid,
        write_off_bonus=15
    )
)
# SUCCESS
log(
    pb.purchase(
        phone_number=phone_number,
        items=items,
        order_guid=order_guid,
        write_off_bonus=0,
    )
)
# SUCCESS
log(
    pb.edit_purchase(
        order_guid=order_guid,
        purchase_status="approved",
        items=items,
    )
)
# SUCCESS
log(
    pb.cancel_purchase(order_guid=order_guid)
)

# SUCCESS
log(
    pb.card_get_info(phone_number=phone_number)
)

# SUCCESS
log(
    pb.confirm_order(order_guid=order_guid)
)

