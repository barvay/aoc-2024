import kotlin.io.path.Path
import kotlin.io.path.readText
import kotlin.math.abs

fun main() {
    val input = Path("input.txt").readText().trim().lines()
    val (l, r) = input.map { it.split("   ").map(String::toInt) }
        .map { it[0] to it[1] }
        .unzip()
        .let { (l, r) -> l.sorted() to r.sorted() }
    println(l.indices.sumOf { abs(l[it] - r[it]).toLong() })
    val cnt = r.groupingBy { it }.eachCount()
    println(l.sumOf { x -> x.toLong() * (cnt[x] ?: 0) })
}