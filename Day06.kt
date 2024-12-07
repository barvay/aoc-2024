import kotlin.io.path.Path
import kotlin.io.path.readLines

fun main() {
    val grid = Path("input.txt").readLines()
    val h = grid.size
    val w = grid[0].length
    lateinit var start: Pair<Int, Int>
    val obstructions = mutableSetOf<Pair<Int, Int>>()
    grid.forEachIndexed { y, row ->
        row.forEachIndexed { x, char ->
            when (char) {
                '#' -> obstructions += x to y
                '^' -> start = x to y
            }
        }
    }
    val dirs = listOf(
        0 to -1,
        1 to 0,
        0 to 1,
        -1 to 0,
    )
    var pos = start
    var dir = dirs[0]
    val visited = mutableSetOf(pos)
    while (pos.first in 0 until w && pos.second in 0 until h) {
        visited += pos
        val next = (pos.first + dir.first) to (pos.second + dir.second)
        if (next in obstructions) dir = dirs[(dirs.indexOf(dir) + 1) % dirs.size]
        else pos = next
    }
    println(visited.size)
    var ans = 0L
    visited.forEach { test ->
        val temp = obstructions + test
        val seen = mutableSetOf<Pair<Pair<Int, Int>, Pair<Int, Int>>>()
        pos = start
        dir = dirs[0]
        while (pos.first in 0 until w && pos.second in 0 until h) {
            if (pos to dir in seen) {
                ans++
                break
            }
            seen += (pos to dir)
            val next = (pos.first + dir.first) to (pos.second + dir.second)
            if (next in temp) dir = dirs[(dirs.indexOf(dir) + 1) % dirs.size]
            else pos = next
        }
    }
    println(ans)
}