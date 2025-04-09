
def clock_angle(H, M):
    H = H % 12

    minute_angle = 6 * M
    hour_angle = 30 * H + 0.5 * M

    angle = abs(hour_angle - minute_angle)

    return min(angle, 360 - angle)

H = int(input())
M = int(input())
result = clock_angle(H, M)
print(result)
