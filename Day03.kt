import kotlin.io.path.Path
import kotlin.io.path.readLines

fun main() {
    val input = Path("input.txt").readLines()
    var ans = 0L
    var enabled = true
    input.forEach { line ->
        Regex("""(do\(\)|don't\(\)|mul\(\d+,\d+\))""").findAll(line.trim()).forEach { match ->
            when (match.value) {
                "do()" -> enabled = true
                "don't()" -> enabled = false
                else -> if (enabled) {
                    val (x, y) = match.value.removePrefix("mul(")
                        .removeSuffix(")")
                        .split(',')
                        .map { it.toInt() }
                    ans += x * y
                }
            }
        }
    }
    println(ans)
}
