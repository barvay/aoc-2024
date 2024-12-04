import kotlin.io.path.Path
import kotlin.io.path.readLines

fun main() {
    val grid = Path("input.txt").readLines()
    val w = grid[0].length
    val h = grid.size
    var ans = 0L
    fun ck1(x: Int, y: Int, dir: Pair<Int, Int>, need: Char = 'M'): Boolean {
        val nx = x + dir.first
        val ny = y + dir.second
        if (nx in 0 until w && ny in 0 until h && grid[ny][nx] == need) {
            return when (need) {
                'M' -> ck1(nx, ny, dir, 'A')
                'A' -> ck1(nx, ny, dir, 'S')
                'S' -> true
                else -> false
            }
        }
        return false
    }
    val directions = listOf(
        1 to 0, 1 to 1, 0 to 1, -1 to 1,
        -1 to 0, -1 to -1, 0 to -1, 1 to -1
    )
    for (i in 0 until h) {
        for (j in 0 until w) {
            if (grid[i][j] == 'X') {
                ans += directions.count { ck1(j, i, it) }
            }
        }
    }
    println(ans)
    ans = 0
    fun ck2(vararg chars: Char): Int {
        return when (chars.toList()) {
            listOf('M', 'S', 'M', 'S'),
            listOf('M', 'M', 'S', 'S'),
            listOf('S', 'M', 'S', 'M'),
            listOf('S', 'S', 'M', 'M') -> 1
            else -> 0
        }
    }
    for (i in 1 until h - 1) {
        for (j in 1 until w - 1) {
            if (grid[i][j] == 'A') {
                ans += ck2(
                    grid[i - 1][j - 1],
                    grid[i + 1][j - 1],
                    grid[i - 1][j + 1],
                    grid[i + 1][j + 1]
                )
            }
        }
    }
    println(ans)
}
