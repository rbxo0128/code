<h2><a href="https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/?envType=daily-question&envId=2026-11-04">3505. Minimum Operations to Make Elements Within K Subarrays Equal</a></h2><h3>Hard</h3><hr>

<p>정수 배열 <code>nums</code>와 정수 <code>x</code>, <code>k</code>가 주어진다.</p>
<p>한 번의 연산으로 배열의 원소 하나를 1 증가시키거나 감소시킬 수 있다.</p>
<p>길이가 정확히 <code>x</code>이고 내부 원소들이 모두 같은 부분 배열을 서로 겹치지 않게 최소 <code>k</code>개 만들기 위한 최소 연산 횟수를 구한다.</p>

<p><strong>Example 1:</strong></p>
<pre>
Input: nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2
Output: 8
</pre>

<p><strong>Example 2:</strong></p>
<pre>
Input: nums = [9,-2,-2,-2,1,5], x = 2, k = 2
Output: 3
</pre>

<p><strong>Constraints:</strong></p>
<ul>
<li><code>2 &lt;= nums.length &lt;= 10^5</code></li>
<li><code>-10^6 &lt;= nums[i] &lt;= 10^6</code></li>
<li><code>2 &lt;= x &lt;= nums.length</code></li>
<li><code>1 &lt;= k &lt;= 15</code></li>
<li><code>2 &lt;= k * x &lt;= nums.length</code></li>
</ul>

### 풀이 기록

**결과: 시간 초과 (TLE)**

길이 <code>x</code>인 슬라이딩 윈도우를 정렬한 후 중앙값과의 절댓값 차이 합으로 각 구간의 최소 비용을 계산했다. 이후 DP로 겹치지 않는 <code>k</code>개의 구간을 선택했다.

매 윈도우를 다시 정렬하면서 비용을 구하기 때문에 시간 복잡도는 <code>O(n * x * log x + n * k)</code>로, 큰 입력에서 시간 초과가 발생한다. 개선하려면 이동하는 구간의 중앙값과 비용을 효율적으로 유지하는 자료구조가 필요하다.

### 분류

배열, 동적 계획법, 슬라이딩 윈도우, 정렬, 힙(우선순위 큐), 수학