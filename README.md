<p align="center">   
<img src="./sources/logo.png" height="130">
</p>

---

![GitHub release (latest by date)](https://img.shields.io/github/v/release/FeelinVoids/outbreak-resourcepack)
![Minecraft version](https://img.shields.io/badge/minecraft--version-1.14%20--%201.16-blue)

Данный ресурспак разрабатывается для моего сервера <здесь будет IP после открытия>.  
Протестирован и нормально работает на версиях Minecraft 1.14 - 1.16.  

В ресурспаке используются карты нормалей/отражений/свечения, использующиеся шейдерами,
так что для наилучшего игрового опыта рекомендуется использовать [шейдеры BSL](https://bitslablab.com/) или другие.

Также в ресурспаке использованы такие фичи, как соединения блоков (ctm) и кастомные текстуры/модели предметов
по именам/описаниям (cit), так что для их работы
### необходим [OptiFine](http://optifine.net/)!
## Последние версии качать [здесь](https://github.com/FeelinVoids/outbreak-resourcepack/releases)

###### [Как собрать нестабильную версию?](#building)

# Список изменений

- [Изменения в обычной игре](#forvanilla)
    - [3D люки](#trapdoors)
    - [Морские огурцы на суше заменены на свечи](#candles)
    - [Полированный андезит, гранит, диорит](#polished)
    - [Блеск и отражения](#specular)
    - [Объёмные лестницы](#ladders)
    - [Объёмные рельсы](#rails)
    - [Рычаги со светящимися индикаторами on/off](#levers)
    - [3D нажимные плиты](#pressure)
    - [Нить светится в темноте](#string)
    - [Более низкий щит](#shield)
    - [Схема зельеварения вместо одной из картин](#scheme)
    - [Более прозрачная тыква на голове](#pumpkin_head)
    - [3D доски](#planks)
    - [Повторители и компараторы](#comparators)
    - [Интерфейс](#interface)
    - [Часы](#clock)
    - [Зачаровальные книги со значками зачарований](#books)
    - [Зелья со значками эффектов](#potions)
    - [Соединяющиеся текстуры](#connections)
    - [Растительность](#plants)
    - [Торт](#cake)
    - [Лёд](#ice)
    - [Пышная листва](#leaves)
    - [Голова дракона](#dragon_head)

- [Для сервера](#forserver)
    - [3D оружие для плагина CrackShot](#crackshot)
    
- [Распознавание предметов с изменёнными моделями](#selectors)
    - [Оружие CrackShot](#crackshot-selectors)
    - [Ключи для ящиков](#keys-selectors)

## Изменения в обычной игре

### <a name="trapdoors"></a> 3D люки
![Люки](./sources/screenshots/trapdoors.png)

### <a name="candles"></a> Морские огурцы на суше заменены на свечи
![Свечи](./sources/screenshots/candles.png)

### <a name="polished"></a> Полированный андезит, гранит, диорит
Текстуры более бесшовные
![Полированные камни](./sources/screenshots/seamless.png)

### <a name="specular"></a> Блеск и отражения
Добавлены specular карты для ламп, полированных камней, железных, золотых и алмазных блоков.
![Блеск 2](./sources/screenshots/shine.png)
![Блеск 1](./sources/screenshots/shine2.png)

### <a name="ladders"></a> Объёмные лестницы
![Лестницы](./sources/screenshots/ladders.png)

### <a name="rails"></a> Объёмные рельсы
![Рельсы днём](./sources/screenshots/rails_day.png)
![Рельсы ночью](./sources/screenshots/rails_night.png)

### <a name="levers"></a> Рычаги со светящимися индикаторами on/off
![Рычаги](./sources/screenshots/levers.png)

### <a name="pressure"></a> 3D нажимные плиты
![Нажимные плиты](./sources/screenshots/pressure_plates.png)

### <a name="string"></a> Нить светится в темноте
![Нить](./sources/screenshots/string.png)

### <a name="shield"></a> Более низкий щит
Не закрывает обзор
![Щит](./sources/screenshots/shield.png)

### <a name="scheme"></a> Схема зельеварения вместо одной из картин
![Схема](./sources/screenshots/scheme.png)

### <a name="pumpkin_head"></a> Более прозрачная тыква на голове
![Тыква на голове](./sources/screenshots/pumpkin_head.png)

### <a name="planks"></a> 3D доски
![Доски](./sources/screenshots/planks.png)

### <a name="comparators"></a> Повторители и компараторы
Позаимствованы из God Of Redstone, который давно не обновляется.
Компаратору добавлено свечение, изменяющееся в зависимости от режима.
![Повторители и компараторы](./sources/screenshots/comparators.png)

### <a name="interface"></a> Интерфейс
Интерфейс инвентаря креатива и хотбар также взяты из God Of Redstone и переработаны
для нормального отображения в новых версиях. На хотбар добавлены номера для
более удобного выбора кнопками.
![Интерфейс](./sources/screenshots/interface.png)

### <a name="clock"></a> Часы
Кривое отображение поверх сетки инвентаря - норма.
![Часы](./sources/screenshots/clock.png)

### <a name="books"></a> Зачаровальные книги со значками зачарований
Также отличается рамка в зависимости от уровня зачарования
![Книжки](./sources/screenshots/books.png)

### <a name="potions"></a> Зелья со значками эффектов
В ресурспаке есть все значки, однако, некоторые не работают. Видимо, не поддерживаются OptiFine.
![Зелья](./sources/screenshots/potions.png)

### <a name="connections"></a> Соединяющиеся текстуры
Соединяющиеся текстуры имеют песок, красный песок, все виды листвы и гравий.
Соединение песков с разными каменными кирпичами особенное.
![Соединяющиеся текстуры](./sources/screenshots/connections.png)

### <a name="plants"></a> Растительность
Тростник, картофель, морковь, свёкла и ягоды переработаны в 3D.
Для картофеля и моркови проработаны все 7 стадий (вместо стандартных 4-х)
![Растительность](./sources/screenshots/foodstuff/plants.png)
![Адский нарост](./sources/screenshots/foodstuff/nether_wart.png)
Картофель | Морковь | Свёкла
--------- | ------- | ------
![Картофель](./sources/screenshots/foodstuff/potato_grows.gif) | ![Морковь](./sources/screenshots/foodstuff/carrot_grows.gif) | ![Свёкла](./sources/screenshots/foodstuff/beetroot_grows.gif)

### <a name="cake"></a> Торт
![Торт днём](./sources/screenshots/foodstuff/cake_day.png)
![Торт ночью](./sources/screenshots/foodstuff/cake_night.png)
![Поедание торта](./sources/screenshots/foodstuff/cake.gif)

### <a name="ice"></a> Лёд
Для льда и плотного льда добавлены карты отражений и карты нормалей
![Лёд](./sources/screenshots/ice.png)

### <a name="dragon_head"></a> Голова дракона
Глаза и рот теперь светятся
![Голова дракона](./sources/screenshots/dragon_head_emission.png)

### <a name="leaves"></a> Пышная листва
![Берёзовый лес](./sources/screenshots/bushy/birch.png)
![Лес](./sources/screenshots/bushy/forest.png)
![Меза](./sources/screenshots/bushy/mesa.png)
![Болото](./sources/screenshots/bushy/swamp.png)
![Джунгли](./sources/screenshots/bushy/jungle.png)
![Саванна](./sources/screenshots/bushy/savanna.png)
![Тайга](./sources/screenshots/bushy/spruce.png)






## <a name="forserver"></a> Изменения для сервера
### <a name="crackshot"></a> 3D оружие для плагина CrackShot

![Оружие](./sources/screenshots/guns.png)

Третье лицо | Первое лицо
----------- | -----------
![ak471.png](./sources/screenshots/guns/ak471.png) | ![ak472.png](./sources/screenshots/guns/ak472.png)
![c41.png](./sources/screenshots/guns/c41.png) | ![c42.png](./sources/screenshots/guns/c42.png)
![grenade1.png](./sources/screenshots/guns/grenade1.png) | ![grenade2.png](./sources/screenshots/guns/grenade2.png)
![olympa1.png](./sources/screenshots/guns/olympa1.png) | ![olympia2.png](./sources/screenshots/guns/olympia2.png)
![potato1.png](./sources/screenshots/guns/potato1.png) | ![potato2.png](./sources/screenshots/guns/potato2.png)
![putty1.png](./sources/screenshots/guns/putty1.png) | ![putty2.png](./sources/screenshots/guns/putty2.png)
![riotshield1.png](./sources/screenshots/guns/riotshield1.png) | ![riotshield2.png](./sources/screenshots/guns/riotshield2.png)
![sniper1.png](./sources/screenshots/guns/sniper1.png) | ![sniper2.png](./sources/screenshots/guns/sniper2.png)
![type951.png](./sources/screenshots/guns/type951.png) | ![type952.png](./sources/screenshots/guns/type952.png)
![type951.png](./sources/screenshots/guns/energy_sniper1.png) | ![type952.png](./sources/screenshots/guns/energy_sniper2.png)

# <a name="selectors"></a> Распознавание предметов с изменёнными моделями

Изменённая модель будет отображаться с OptiFine, если в описании (Lore)
предмета присутствуют следующие id:

## <a name="crackshot-selectors"></a> Оружие
ID | Название
-- | --------
id100 | Снайперская винтовка
id101 | Щит
id102 | Граната
id103 | C4
id104 | Putty
id105 | Olympia
id106 | Картофельная пушка
id107 | ПП Поток
id108 | Энергетическая снайперская винтовка
id109 | АК-47
id110 | Type-95

## <a name="keys-selectors"></a> Ключи
ID | Название
-- | --------
id1 | Ежедневный ящик
id2 | Оружие
id3 | Оружие+
id4 | Броня
id5 | Броня+
id6 | Паркур


## <a name="rails"></a> Сборка версии в разработке

• Необходим установленный [Python 3](https://www.python.org/downloads/windows/)  
• Скачайте репозиторий и распакуйте архив.  
• Запустите файл make.bat или make-non-shaders.bat (если нужна non-shader версия).
Эти файлы находятся в папке sources.  
• Скрипт сгенерирует архивы в папку sources./.build

#### Альтернативный способ:
Откройте терминал в папке `sources` и выполните команду:

    python make.py ВЫХОДНОЙ_ПУТЬ NON_SHADER ВЕРСИЯ ЗАПАКОВАТЬ
Где:

    • ВЫХОДНОЙ_ПУТЬ - место, в которое будет сохранён результат.

    • NON_SHADER - 1 или 0 - собрать non-shader-версию без карт
      нормалей/отражений и прочих не нужных без шейдеров файлов.
    
    • ЗАПАКОВАТЬ - 1 или 0 - сразу запаковать результат в zip
