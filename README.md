# Скрипты для курса по докингу

Как пользоваться?
1. Скачиваем functions.py
2. Импортируем новые функции в pymol (запускаем через pymol) (путь указываем без кавычек):

      ``` run путь/к/functions.py ```

3. Объединяем mol2 файлы в один через функцию merge_mols (путь указываем без кавычек)

      ``` merge_mols путь/к/папке/с/mol2/файлами```
      
      
Как строить AUROC?
1. Устанавливаем необходимые библиотеки:

      ``` pip install -r requirements.txt ```
      
2. Строим AUROC (путь указываем без кавычек):

      ``` python AUROC путь/к/данным/скрининга.csv ```
      


