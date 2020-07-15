class Solution:
  def angleClock(self, hour: int, minutes: int) -> float:
      angle = abs((minutes * 6) % 360 - (hour * 30 + minutes * 0.5) % 360)
      return min(angle, 360 - angle)