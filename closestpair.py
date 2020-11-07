import random
def  squaredist(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1] -p2[1])**2)
def column_based_sort(array, column=0):
        return sorted(array, key=lambda x: x[column])
def dis_btwn_closest_pair(P, n, min_dis=float("inf")):
        for i in range(n - 1):
          for j in range(i + 1, n):
            current_dis = squaredist(P[i], P[j])
            if current_dis < min_dis:
                min_dis = current_dis
        return min_dis
def dis_btwn_closest_in_strip(P,n, min_dis=float("inf")):
        for i in range(min(6, n - 1), n):
          for j in range(max(0, i - 6), i):
             current_dis = squaredist(P[i], P[j])
             if current_dis < min_dis:
                min_dis = current_dis
        return min_dis
#Px--> points sorted on x, Py--> points sorted on y
def sqr_closest_pair_of_points(Px, Py, n):
        if n <= 3:
            return dis_btwn_closest_pair(Px, n)
        mid = n// 2
        closest_in_left = sqr_closest_pair_of_points(Px, Py[:mid], mid)
        closest_in_right = sqr_closest_pair_of_points(Py, Py[mid:], n - mid)
        closest_pair_dis = min(closest_in_left, closest_in_right)
        cross_strip = []
        for point in Px:
            if abs(point[0] - Px[mid][0]) < closest_pair_dis:
                cross_strip.append(point)

        closest_in_strip = dis_btwn_closest_in_strip(cross_strip, len(cross_strip), closest_pair_dis)
        return min(closest_pair_dis, closest_in_strip)
def closest_pair_of_points(P, n):
        Px = column_based_sort(points, column=0)
        Py = column_based_sort(points, column=1)
        return (sqr_closest_pair_of_points(Px, Py,n)) ** 0.5
#points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
points = [ ( random.uniform(0,1), random.uniform(0,1) ) for k in range(100) ]
print(*points)
print("Distance between the shortest pair is :", closest_pair_of_points(points, len(points)))
