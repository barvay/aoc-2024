import kotlin.io.path.Path
import kotlin.io.path.readLines

fun main() {
    var ans = 0L
    val input = Path("input.txt").readLines()
    input.forEach { line ->
        val nums = line.trim().replace(":", "").split(" ").map { it.toLong() }
        var match = false
        fun ck(i: Int, v: Long) {
            if (v > nums[0]) return
            if (i == nums.size) {
                if (v == nums[0] && !match) {
                    ans += nums[0]
                    match = true
                }
                return
            }
            ck(i + 1, v + nums[i])
            ck(i + 1, v * nums[i])
            ck(i + 1, "$v${nums[i]}".toLong())
        }
        ck(2, nums[1])
    }
    println(ans)
}
