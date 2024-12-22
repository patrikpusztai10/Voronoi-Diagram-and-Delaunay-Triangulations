import math
import heapq
import matplotlib.pyplot as plt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Event:
    def __init__(self, x, point, arc=None):
        self.x = x
        self.point = point
        self.arc = arc
        self.valid = True

class Arc:
    def __init__(self, point, prev=None, next=None):
        self.point = point
        self.prev = prev
        self.next = next
        self.event = None
        self.s0 = None
        self.s1 = None

class Segment:
    def __init__(self, start):
        self.start = start
        self.end = None

    def finish(self, end):
        self.end = end

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def push(self, item):
        heapq.heappush(self.elements, (item.x, item))

    def pop(self):
        return heapq.heappop(self.elements)[1]

    def top(self):
        return self.elements[0][1]

    def empty(self):
        return len(self.elements) == 0

class Voronoi:
    def __init__(self, points):
        self.output = []
        self.arc = None
        self.points = PriorityQueue()
        self.event = PriorityQueue()

        self.x0, self.y0 = float('inf'), float('inf')
        self.x1, self.y1 = float('-inf'), float('-inf')

        for x, y in points:
            point = Point(x, y)
            self.points.push(point)
            self.x0 = min(self.x0, x)
            self.y0 = min(self.y0, y)
            self.x1 = max(self.x1, x)
            self.y1 = max(self.y1, y)

        dx = (self.x1 - self.x0) / 5.0
        dy = (self.y1 - self.y0) / 5.0
        self.x0 -= dx
        self.x1 += dx
        self.y0 -= dy
        self.y1 += dy

    def process(self):
        while not self.points.empty():
            if not self.event.empty() and self.event.top().x <= self.points.top().x:
                self.process_event()
            else:
                self.process_point()

        while not self.event.empty():
            self.process_event()

        self.finish_edges()

    def process_point(self):
        point = self.points.pop()
        self.arc_insert(point)

    def process_event(self):
        event = self.event.pop()
        if event.valid:
            seg = Segment(event.point)
            self.output.append(seg)

            arc = event.arc
            if arc.prev:
                arc.prev.next = arc.next
                arc.prev.s1 = seg
            if arc.next:
                arc.next.prev = arc.prev
                arc.next.s0 = seg

            if arc.s0:
                arc.s0.finish(event.point)
            if arc.s1:
                arc.s1.finish(event.point)

            if arc.prev:
                self.check_circle_event(arc.prev, event.x)
            if arc.next:
                self.check_circle_event(arc.next, event.x)

    def arc_insert(self, point):
        if self.arc is None:
            self.arc = Arc(point)
        else:
            arc = self.arc
            while arc:
                intersect, intersection = self.intersect(point, arc)
                if intersect:
                    next_intersect, _ = self.intersect(point, arc.next)
                    if arc.next and not next_intersect:
                        arc.next.prev = Arc(arc.point, arc, arc.next)
                        arc.next = arc.next.prev
                    else:
                        arc.next = Arc(arc.point, arc)
                    arc.next.s1 = arc.s1

                    arc.next.prev = Arc(point, arc, arc.next)
                    arc.next = arc.next.prev

                    segment = Segment(intersection)
                    self.output.append(segment)
                    arc.s1 = arc.next.s0 = segment

                    segment = Segment(intersection)
                    self.output.append(segment)
                    arc.next.s1 = arc.next.next.s0 = segment

                    self.check_circle_event(arc, point.x)
                    self.check_circle_event(arc.prev, point.x)
                    self.check_circle_event(arc.next, point.x)

                    return

                arc = arc.next

            arc = self.arc
            while arc.next:
                arc = arc.next

            arc.next = Arc(point, arc)
            start = Point(self.x0, (arc.next.point.y + arc.point.y) / 2)
            segment = Segment(start)
            arc.s1 = arc.next.s0 = segment
            self.output.append(segment)

    def check_circle_event(self, arc, x0):
        # Ensure `arc` is not None
        if arc is None:
            return

        # Invalidate the existing event if it exists and is outdated
        if arc.event and arc.event.x != x0:
            arc.event.valid = False
        arc.event = None

        # Ensure both previous and next arcs exist before calculating circle event
        if arc.prev is None or arc.next is None:
            return

        # Check for a circle event
        flag, x, center = self.circle(arc.prev.point, arc.point, arc.next.point)
        if flag and x > x0:
            arc.event = Event(x, center, arc)
            self.event.push(arc.event)

    def circle(self, a, b, c):
        if (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y) > 0:
            return False, None, None

        A = b.x - a.x
        B = b.y - a.y
        C = c.x - a.x
        D = c.y - a.y

        E = A * (a.x + b.x) + B * (a.y + b.y)
        F = C * (a.x + c.x) + D * (a.y + c.y)
        G = 2 * (A * (c.y - b.y) - B * (c.x - b.x))

        if G == 0:
            return False, None, None

        ox = (D * E - B * F) / G
        oy = (A * F - C * E) / G

        radius = math.sqrt((a.x - ox)**2 + (a.y - oy)**2)
        x = ox + radius
        return True, x, Point(ox, oy)

    def intersect(self, point, arc):
        if not arc:
            return False, None

        if arc.point.x == point.x:
            return False, None

        a = b = 0.0

        if arc.prev:
            a = self.intersection(arc.prev.point, arc.point, point.x).y
        if arc.next:
            b = self.intersection(arc.point, arc.next.point, point.x).y

        if (not arc.prev or a <= point.y) and (not arc.next or point.y <= b):
            px = ((arc.point.x)**2 + (arc.point.y - point.y)**2 - point.x**2) / (2 * arc.point.x - 2 * point.x)
            py = point.y
            return True, Point(px, py)

        return False, None

    def intersection(self, p0, p1, x):
        if p0.x == p1.x:
            return Point(0, (p0.y + p1.y) / 2)
        if p1.x == x:
            return Point(0, p1.y)
        if p0.x == x:
            return Point(0, p0.y)

        z0 = 2 * (p0.x - x)
        z1 = 2 * (p1.x - x)

        a = 1 / z0 - 1 / z1
        b = -2 * (p0.y / z0 - p1.y / z1)
        c = (p0.y**2 + p0.x**2 - x**2) / z0 - (p1.y**2 + p1.x**2 - x**2) / z1

        py = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
        px = ((p0.x)**2 + (p0.y - py)**2 - x**2) / (2 * p0.x - 2 * x)
        return Point(px, py)

    def finish_edges(self):
        l = self.x1 + (self.x1 - self.x0) + (self.y1 - self.y0)
        arc = self.arc
        while arc.next:
            if arc.s1:
                p = self.intersection(arc.point, arc.next.point, 2 * l)
                arc.s1.finish(p)
            arc = arc.next

    def get_output(self):
        return [(seg.start.x, seg.start.y, seg.end.x, seg.end.y) for seg in self.output if seg.end]

    def visualize_voronoi(points, edges):
        plt.title("Voronoi Diagram")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.axis("equal")

        x_points, y_points = zip(*points)
        plt.scatter(x_points, y_points, color='blue', label='Input Points', s=50, zorder=2)
        for edge in edges:
            (x1, y1, x2, y2) = edge
            plt.plot([x1, x2], [y1, y2], color='red', linewidth=1, zorder=1)
        plt.xlim(-10,10)
        plt.ylim(-10, 10)
        plt.legend()
        plt.grid(True)
        plt.show()

points = [(3, -5), (-6, 6), (6, -4), (5, -5),(9,10)]
voronoi = Voronoi(points)
voronoi.process()
edges = voronoi.get_output()
Voronoi.visualize_voronoi(points,edges)