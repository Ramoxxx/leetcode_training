class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current_altitude = 0
        max_altitude = 0
        for alt_diff in gain:
            current_altitude += alt_diff
            max_altitude = max(max_altitude,current_altitude)
        return max_altitude
        