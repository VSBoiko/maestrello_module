from Maestrello import MaestrelloSDK
import json


def log(data):
    print()
    print(json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4))
    print()


mt = MaestrelloSDK()

# login = "vladboiko1996@yandex.ru"
login = "vlad2010-1996@mail.ru"
password = "-7b8Ouisb!j"

# auth = mt.user_auth(
#     login=login,
#     password=password
# )
# print(auth)
# token = auth["token"]

token = "5804caabf95788036893dfda42cbb676678"

# Авторизация и восстановление пароля

# # SUCCESS - пришло письмо на почту с паролем
# log(
#     mt.user_registration(
#         firstname="Влад",
#         lastname="Бойко",
#         email=login,
#         phone="89876543210"
#     )
# )

# # SUCCESS
# log(
#     mt.user_auth(
#         login=login,
#         password=password
#     )
# )

# # SUCCESS
# log(
#     mt.pass_recovery_link_request(
#         login=login,
#     )
# )

# # SUCCESS
# log(
#     mt.pass_recovery_new_pass(
#         login=login,
#         key=token
#     )
# )

# *** *** ***

# Профиль

# # SUCCESS
# log(
#     mt.get_user_profile(
#         token=token
#     )
# )

# # SUCCESS
# log(
#     mt.upd_user_name(
#         token=token,
#         firstname="Влад",
#         lastname="Бойко"
#     )
# )

# # SUCCESS
# log(
#     mt.upd_user_email(
#         token=token,
#         email="vlad2010-1996@mail.ru"
#     )
# )

# # SUCCESS
# log(
#     mt.upd_user_phone(
#         token=token,
#         phone="81234567890"
#     )
# )

# # SUCCESS
# log(
#     mt.add_user_address(
#         token=token,
#         city="Краснодар",
#         street="Красная",
#         house_number="176/1",
#     )
# )

# # SUCCESS
# log(
#     mt.upd_user_address(
#         token=token,
#         address_id=1,
#         city="Москва",
#         street="Арбат",
#         house_number="15",
#         flat="143",
#         entrance="2",
#         region="Московская обл.",
#         country="russia",
#     )
# )

# # SUCCESS
# log(
#     mt.del_user_address(
#         token=token,
#         address_id=0,
#     )
# )

# *** *** ***

# Категории

# # SUCCESS
# log(
#     mt.get_categories(
#         parent_id=2
#     )
# )

# *** *** ***

# Статусы заказов

# # SUCCESS
# log(
#     mt.get_statuses()
# )

# *** *** ***

# Заказы

# log(
#     mt.get_order(
#
#     )
# )

# log(
#     mt.get_orders(
#
#     )
# )

# log(
#     mt.get_order_status(
#
#     )
# )

# *** *** ***

# Создание заказа

# # SUCCESS
# log(
#     mt.get_order_settings()
# )

# log(
#     mt.create_order()
# )

# log(
#     mt.create_order_payment()
# )

# *** *** ***

# Расчет стоимости доставки
# log(
#     mt.calc_shipping()
# )




