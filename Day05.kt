import kotlin.io.path.Path
import kotlin.io.path.readText

fun main() {
    val input = Path("input.txt").readText().replace("\r\n", "\n")
    val (toRules, toUpdates) = input.split("\n\n")
    val rules = toRules.lines()
        .filter { it.isNotBlank() }
        .map { line ->
            val (k, v) = line.split("|").map { it.toInt() }
            k to v
        }
    val updates = toUpdates.lines()
        .filter { it.isNotBlank() }
        .map { line ->
            line.split(",").map { it.toInt() }
        }
    var part1 = 0
    var part2 = 0
    updates.forEach { update ->
        val rule = rules.filter { it.first in update && it.second in update }
        val adj = mutableMapOf<Int, MutableList<Int>>()
        for ((u, v) in rule) {
            adj.getOrPut(u) { mutableListOf() }.add(v)
        }
        val vis = mutableSetOf<Int>()
        val stack = mutableListOf<Int>()
        fun dfs(x: Int) {
            if (x !in vis) {
                vis.add(x)
                adj[x]?.forEach { neighbor ->
                    dfs(neighbor)
                }
                stack.add(x)
            }
        }
        update.forEach { node ->
            if (node !in vis) {
                dfs(node)
            }
        }
        val ordered = stack.reversed()
        if (update == ordered) {
            part1 += update[update.size / 2]
        } else {
            part2 += ordered[ordered.size / 2]
        }
    }
    println(part1)
    println(part2)
}
