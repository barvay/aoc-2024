import kotlin.io.path.Path
import kotlin.io.path.readLines

fun main() {
    val input = Path("input.txt").readLines()
    var ans = 0L
    fun ck(a: List<Long>, asc: Boolean): Boolean {
        for (i in 1..a.lastIndex) {
            val diff = a[i] - a[i - 1]
            if ((asc && diff !in 1..3) || (!asc && diff !in -3..-1)) return false
        }
        return true
    }
    for (line in input) {
        val data = line.split(" ").map { it.toLong() }
        if (ck(data, true) || ck(data, false)) ans++
    }
    println(ans)
    ans = 0
    for (line in input) {
        val data = line.split(" ").map { it.toLong() }
        for (i in 0..data.lastIndex) {
            val temp = data.toMutableList().apply { removeAt(i) }
            if (ck(temp, true) || ck(temp, false)) {
                ans++
                break
            }
        }
    }
    println(ans)
}