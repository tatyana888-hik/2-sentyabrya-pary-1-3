# Домашняя библиотека — документация по 5 ролям

**Автор:** Хикматуллина Татьяна Руслановна]
**Проект:** Мобильное приложение «Домашняя библиотека»
**Платформа:** Android (Kotlin, MVVM, Room/SQLite)

---

## Часть 1. Общие разделы

### 1.1. Бизнес-логика проекта

**Задача:** приложение для учёта домашней библиотеки — каталог книг, полки, справочники жанров и форматов.

**User stories:**
- Как пользователь, я хочу добавить книгу, чтобы вести учёт.
- Как пользователь, я хочу создать полку, чтобы группировать книги.
- Как пользователь, я хочу искать книгу по названию.
- Как пользователь, я хочу настроить жанры и форматы.
- Как пользователь, я хочу работать офлайн.

**Ключевые сущности:**
- `User` — пользователь (email, password).
- `Book` — книга (id, title, genre, format, price).
- `Shelf` — полка (id, name, createdAt).
- `ShelfBook` — связь книга-полка (shelfId, bookId, quantity).
- `Genre` — жанр (id, name).
- `Format` — формат (id, name).

**Бизнес-правила:**
- Название книги не может быть пустым.
- Жанр/формат нельзя удалить, если он используется в книгах.
- При удалении полки книги остаются в каталоге.
- При удалении книги она удаляется со всех полок.

### 1.2. Архитектура

**Тип:** монолит (мобильное приложение).

**Обоснование:** учебный проект, один разработчик, микросервисы избыточны.

**Слои (MVVM):**

```
View (Activity/Fragment, XML)
    ↓
ViewModel (LiveData/StateFlow)
    ↓
Repository (Room DAO)
    ↓
SQLite (Room)
```

**Плюсы монолита:** простота, один язык, легко тестировать.
**Минусы:** сложно масштабировать.

---

### 1.3. Хранение данных

**СУБД:** SQLite через Room (локально, офлайн).

**Сущности и атрибуты:**

| Сущность | Поля |
|---|---|
| User | email (PK), password |
| Book | id (PK), title, genre, format, price |
| Shelf | id (PK), name, createdAt |
| ShelfBook | id (PK), shelfId (FK), bookId (FK), quantity |
| Genre | id (PK), name |
| Format | id (PK), name |

**Связи:**
- **1:N** — User → Book (один пользователь — много книг).
- **1:N** — User → Shelf.
- **M:N** — Book ↔ Shelf через ShelfBook.
- **1:N** — Genre → Book (денормализовано по названию).

**ER-диаграмма:** (см. файл diagrams/er_diagram.png)

---

### 1.4. Безопасность

| Угроза | Мера защиты |
|---|---|
| Слабая аутентификация | Проверка email/пароля |
| Утечка данных | Локальная БД, нет передачи по сети |
| Невалидные данные | Валидация в ViewModel |
| SQL-инъекции | Room использует параметризованные запросы |

**Инкапсуляция:** приватные поля в data-классах, доступ через геттеры/сеттеры.

---

### 1.5. Законы и нормативные акты

- **152-ФЗ «О персональных данных»** — храним email → нужно согласие.
- **149-ФЗ «Об информации»** — общие правила.
- **GDPR** — если пользователи из ЕС.
- **Политика конфиденциальности** — обязательна при регистрации.

Что учесть:
- Согласие пользователя при регистрации.
- Возможность удалить свои данные.
- Данные хранятся локально, не передаются третьим лицам.

---

### 1.6. Документы по этапам разработки

| Этап | Документ |
|---|---|
| Анализ требований | ТЗ, user stories |
| Проектирование | UML классов, ER-диаграмма, схема архитектуры |
| Разработка | README, описание модулей |
| Тестирование | Тест-план, чек-листы |
| Внедрение | Инструкция по установке APK |
| Сопровождение | Бэкапы БД (экспорт/импорт) |

---

## Часть 2. Роль 1. Архитектор ядра

### 2.1. Иерархия классов

```kotlin
// Базовый класс
abstract class LibraryItem(
    open val id: Int,
    open val title: String
) {
    abstract fun getInfo(): String
}

// Книга
data class Book(
    override val id: Int,
    override val title: String,
    val genre: String,
    val format: String,
    val price: Double
) : LibraryItem(id, title) {
    override fun getInfo(): String =
        "Книга: $title, жанр: $genre, формат: $format, цена: $price"
}

// Полка
data class Shelf(
    val id: Int,
    val name: String,
    val createdAt: String
) {
    fun getInfo(): String = "Полка: $name, создана: $createdAt"
}
```

### 2.2. UML классов

См. файл `diagrams/class_uml.png`.

### 2.3. Принцип DRY

Общие поля `id`, `title` вынесены в `LibraryItem`. Метод `getInfo()` переопределяется в наследниках.

---

## Часть 3. Роль 2. Frontend / UI

### 3.1. Экраны приложения

- Вход / Регистрация
- Книги (каталог, поиск, карточки)
- Полки (список, фильтры, содержимое)
- Справочники (жанры, форматы)
- Боковое меню

### 3.2. Инкапсуляция

UI не лезет в БД напрямую — только через ViewModel:

```kotlin
class BookViewModel(private val repo: BookRepository) : ViewModel() {
    val books: LiveData<List<Book>> = repo.getAllBooks()
    fun addBook(book: Book) = viewModelScope.launch { repo.insert(book) }
}
```

### 3.3. Пример взаимодействия

Пользователь вводит название → ViewModel валидирует → Repository пишет в Room → LiveData обновляет UI.

---

## Часть 4. Роль 3. Безопасность и валидация

### 4.1. Угрозы

- Слабый пароль
- Невалидные данные
- Утечка email

### 4.2. Модуль валидации

```kotlin
object Validator {
    fun validateTitle(title: String): String {
        require(title.isNotBlank()) { "Название не может быть пустым" }
        return title.trim()
    }
    fun validatePrice(price: Double): Double {
        require(price >= 0) { "Цена не может быть отрицательной" }
        return price
    }
    fun validateEmail(email: String): String {
        require("@" in email) { "Некорректный email" }
        return email
    }
}
```

### 4.3. Законы

152-ФЗ — согласие на обработку email. GDPR — право на удаление данных.

---

## Часть 5. Роль 4. QA и тестирование

### 5.1. Тест-план

- Модульные тесты: `Validator`, `Book`
- Интеграционные: Room DAO
- UI-тесты: экраны

### 5.2. Примеры тестов

```kotlin
@Test
fun `empty title throws exception`() {
    assertThrows(IllegalArgumentException::class.java) {
        Validator.validateTitle("")
    }
}

@Test
fun `negative price throws exception`() {
    assertThrows(IllegalArgumentException::class.java) {
        Validator.validatePrice(-1.0)
    }
}
```

### 5.3. Итоги тестирования

Всего тестов: **54**, ошибок: **0** (см. Презентацию).

---

## Часть 6. Роль 5. Техписатель и DevOps

### 6.1. Структура репозитория

```
home-library/
├── app/
│   ├── src/main/java/.../data/
│   ├── src/main/java/.../ui/
│   └── src/test/
├── docs/
│   ├── README.md
│   ├── diagrams/
│   └── examples/
├── presentation/
└── README.md
```

### 6.2. README

```markdown
# Home Library
Мобильное приложение для учёта домашней библиотеки.

## Установка
1. Открыть в Android Studio
2. Собрать APK
3. Установить на устройство

## Тесты
./gradlew test
```

### 6.3. Ветки GitHub

- `main` — стабильная
- `develop` — разработка
- `feature/...` — фичи

---

## Итог

Документация раскрывает все 5 ролей:
1. Архитектор ядра — классы, UML, DRY.
2. Frontend — экраны, инкапсуляция.
3. Безопасность — валидация, законы.
4. QA — тесты, чек-листы.
5. DevOps — репозиторий, README.```
View (Activity/Fragment, XML)
    ↓
ViewModel (LiveData/StateFlow)
    ↓
Repository (Room DAO)
    ↓
SQLite (Room)
```

**Плюсы монолита:** простота, один язык, легко тестировать.
**Минусы:** сложно масштабировать.

