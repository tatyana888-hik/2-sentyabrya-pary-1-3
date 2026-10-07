import org.junit.jupiter.api.Test
import org.junit.jupiter.api.Assertions.*
import org.junit.jupiter.api.assertThrows

class ValidatorTest {

    @Test
    fun `valid title returns trimmed string`() {
        val result = Validator.validateTitle("  1984  ")
        assertEquals("1984", result)
    }

    @Test
    fun `empty title throws exception`() {
        assertThrows(IllegalArgumentException::class.java) {
            Validator.validateTitle("")
        }
    }

    @Test
    fun `whitespace title throws exception`() {
        assertThrows(IllegalArgumentException::class.java) {
            Validator.validateTitle("     ")
        }
    }

    @Test
    fun `negative price throws exception`() {
        assertThrows(IllegalArgumentException::class.java) {
            Validator.validatePrice(-1.0)
        }
    }

    @Test
    fun `zero price is allowed`() {
        val result = Validator.validatePrice(0.0)
        assertEquals(0.0, result)
    }

    @Test
    fun `valid email is lowercased`() {
        val result = Validator.validateEmail("User@Example.COM")
        assertEquals("user@example.com", result)
    }

    @Test
    fun `email without at throws exception`() {
        assertThrows(IllegalArgumentException::class.java) {
            Validator.validateEmail("userexample.com")
        }
    }

    @Test
    fun `short password throws exception`() {
        assertThrows(IllegalArgumentException::class.java) {
            Validator.validatePassword("123")
        }
    }
}

class BookTest {

    @Test
    fun `book creation works`() {
        val book = Book(1, "1984", "Классика", "Мягкая обложка", 549.0)
        assertEquals("1984", book.title)
        assertEquals(549.0, book.price)
    }

    @Test
    fun `polymorphism works`() {
        val book = Book(1, "1984", "Классика", "Мягкая", 549.0)
        val shelf = Shelf(1, "К прочтению", "2026-04-24")

        assertTrue(book.getInfo().contains("Книга"))
        assertTrue(shelf.getInfo().contains("Полка"))
    }
}