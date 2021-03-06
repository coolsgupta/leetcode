class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle = abs((6 * hour * 5 + 0.5 * minutes) - 6 * minutes)
        return min(angle, 360 - angle)
