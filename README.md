# CircleCI Test Project

Минимальный тестовый проект для проверки, что CircleCI корректно запускается для GitHub-репозитория.

## Что внутри

- `demo_app/` — маленький Python-модуль без внешних зависимостей
- `tests/` — unit-тесты на `unittest`
- `.circleci/config.yml` — конфиг CircleCI

## Локальный запуск

```bash
python3 main.py
python3 -m unittest discover -s tests -v
```

## Как проверить CircleCI с GitHub

1. Запушить этот репозиторий на GitHub.
2. Подключить репозиторий в CircleCI.
3. Убедиться, что CircleCI видит файл `.circleci/config.yml`.
4. Сделать commit/push и дождаться запуска pipeline.

Ожидаемое поведение:

- job `test` стартует в контейнере `cimg/python:3.12`
- CircleCI выполняет `python -m unittest discover -s tests -v`
- pipeline завершается со статусом `success`

## Как быстро проверить падающий pipeline

Измените ожидаемое значение в `tests/test_calculator.py`, например:

```python
self.assertEqual(add(20, 22), 43)
```

После `git push` CircleCI должен показать failed build.
