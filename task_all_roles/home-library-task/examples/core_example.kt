// Роль 1: Архитектор ядра
// Пример иерархии классов для проекта "Домашняя библиотека"

// Базовый (абстрактный) класс
// Общие поля id и title вынесены сюда (принцип DRY)
abstract class LibraryItem(
    open val id: Int,
    open val title: String
) {
    // Абстрактный метод — каждый наследник реализует по-своему (полиморфизм)
    abstract fun getInfo(): String
}

// Дочерний класс — Книга
data class Book(
    override val id: Int,
    override val title: String,
    val genre: String,
    val format: String,
    val price: Double
) : LibraryItem(id, title) {

    // Переопределяем метод — своя реализация
    override fun getInfo(): String =
        "Книга: $title | Жанр: $genre | Формат: $format | Цена: $price руб."
}

// Дочерний класс — Полка
data class Shelf(
    val id: Int,
    val name: String,
    val createdAt: String
) {
    fun getInfo(): String = "Полка: $name | Создана: $createdAt"
}

// Пример использования
fun main() {
    val book1 = Book(1, "1984", "Классика", "Мягкая обложка", 549.0)
    val book2 = Book(2, "Sapiens", "Нон-фикшн", "Электронная книга", 1299.0)
    val shelf = Shelf(1, "К прочтению", "2026-04-24 07:52:09")

    println(book1.getInfo())
    println(book2.getInfo())
    println(shelf.getInfo())
}