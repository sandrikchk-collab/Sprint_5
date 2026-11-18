# Sprint_5 — автотесты для Stellar Burgers

UI-автотесты на Selenium + pytest для сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/).

## Что проверяется
| Файл | Проверки |
|---|---|
| `tests/test_registration.py` | успешная регистрация; ошибка «Некорректный пароль» (пароль < 6 символов) |
| `tests/test_login.py` | вход через «Войти в аккаунт», «Личный кабинет», форму регистрации, форму восстановления пароля |
| `tests/test_personal_account.py` | переход в личный кабинет |
| `tests/test_account_to_constructor.py` | переход из ЛК в конструктор по «Конструктор» и по логотипу |
| `tests/test_logout.py` | выход по кнопке «Выход» в ЛК |
| `tests/test_constructor.py` | переходы к разделам «Булки», «Соусы», «Начинки» |

## Структура
- `data.py` — URL и данные пользователя
- `helpers.py` — генераторы логина (email) и пароля
- `locators.py` — локаторы с комментариями
- `tests/conftest.py` — все фикстуры (драйвер, регистрация, авторизация)

## Запуск
```bash
pip install -r requirements.txt
pytest -v
```
Тесты запускаются в Google Chrome. Каждый тест открывает браузер и закрывает его через `driver.quit()` в фикстуре `driver`.
