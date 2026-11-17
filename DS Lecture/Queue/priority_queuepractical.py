class node:
    def __init__(self,pid,name,priority):
        self.pid=pid
        self.name=name
        self.priority=priority
        self.next=None

class priorityQueue:
    def __init__(self):
        self.front=None
    #1 Add patient
    def enqueue(self,new_node):
        if self.front==None:
            self.front=new_node
            return

        if new_node.priority<self.front.priority:
            new_node.next=self.front
            self.front=new_node
            return

        temp=self.front

        while temp.next:
            if new_node.priority<temp.next.priority:
                break
            temp=temp.next

        new_node.next=temp.next
        temp.next=new_node

    # 2. Display the next patient to be treated. (display_next)
    def display_next(self):
        if self.front==None:
            print("no patient in the queue")
        else:
            print("Next patient to be treated:")
            print("Patient ID:", self.front.pid)
            print("Patient Name:", self.front.name)
            print("Priority:", self.front.priority)

    #3. Remove a patient from the queue after treatment. (dequeue)
    def dequeue(self):
        if self.front==None:
            print("Queue is Empty")
        else:
            temp=self.front
            print("Patient Treated(dequeue):",temp.name)
            self.front=self.front.next
            temp=None

    #4. Display all waiting patients in priority order(display_all)
    def display_all(self):
        if self.front==None:
            print("No waiting patient")
            return

        temp = self.front

        print("\nWaiting Patients:")
        print("ID\tName\tPriority")

        while temp:
            print(temp.pid, "\t", temp.name, "\t", temp.priority)
            temp = temp.next


pq = priorityQueue()

while True:

    print("\n----- HOSPITAL EMERGENCY MANAGEMENT -----")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient")
    print("4. Display All Patients")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        pid = int(input("Enter Patient ID: "))
        name = input("Enter Patient Name: ")
        priority = int(input("Enter Priority (1-Critical, 2-Serious, 3-Normal): "))

        if priority < 1 or priority > 3:
            print("Invalid priority")
        else:
            new_node = node(pid, name, priority)
            pq.enqueue(new_node)
            print("Patient added successfully")

    elif ch == 2:
        pq.display_next()

    elif ch == 3:
        pq.dequeue()

    elif ch == 4:
        pq.display_all()

    elif ch == 5:
        print("Exiting program")
        break

    else:
        print("Invalid choice")