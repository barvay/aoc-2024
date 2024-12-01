import kotlin.io.path.Path
import kotlin.io.path.readText
import kotlin.math.abs

fun main() {

    fun part1(input: List<String>) {
        val (l, r) = input.map { it.split("   ").map(String::toInt) }
            .map { it[0] to it[1] }
            .unzip()
            .let { (l, r) -> l.sorted() to r.sorted() }
        println(l.indices.sumOf { abs(l[it] - r[it]).toLong() })
    }

    fun part2(input: List<String>) {
        val (l, r) = input.map { it.split("   ").map(String::toInt) }
            .map { it[0] to it[1] }
            .unzip()
        println(l.sumOf { x -> x.toLong() * r.count { it == x } })
    }

    val input = Path("input.txt").readText().trim().lines()
    part1(input)
    part2(input)
}