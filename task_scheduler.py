import heapq 
class TaskScheduler:
  def __init__(self):
    self.heap =[]
    self.counter = 0
  def insert(self, name, priority):
    heapq.heappush(self.heap, (-priority, self.counter, name))
    self.counter += 1
    print(f"INSERT: Added '{name}' with priority {priority}")
def extract_max(self)
 if not self.heap:
   print("No tasks left!")
   return None
neg_priority, _, name = heapq.heappop(self.heap)
print(f"EXTRACT-MAX: Running '{name}' with priority {-nag_priority}")
return name
def peek(self):
  if not self.heap:
    return None
  return self.heap[0][2]
def is_empty(self)
  return len(self.heap) == 0
def show_all(self):
  print("Current tasks:")
  for neg_p, _, name in sorted(self.heap)
     print(f" -{name} : priority {-nag_p}")
if __name__== "__main__":
  s = TaskScheduler()
  s.insert("Render Video", 2)
  s.insert("System Update", 10)
  s.insert("Download File", 5)
  s.insert("Antivirus Scan", 8)
  s.show_all()
  print("___Scheduler starts___")
  while not s.is_empty():
    s.extract_max()
