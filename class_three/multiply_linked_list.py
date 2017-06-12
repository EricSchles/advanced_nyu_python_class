class MultiplyNode:
    def __init__(self, name, department, dob,
                 next_name=None, next_department=None, next_dob=None):
        self.name = name
        self.department = department
        self.dob = dob
        self.next_name = next_name
        self.next_department = next_department
        self.next_dob = next_dob

    def __str__(self):
        return repr(f'{self.name}, {self.department}, {self.dob}')

class MultiplyLinkedList:
    def __init__(self):
        self.name_head = None
        self.department_head = None
        self.dob_head = None

    def append(self, data: dict) -> None:
        if self.name_head is None:
            self.name_head = MultiplyNode(data["name"],
                                          data["department"],
                                          data["dob"])
            self.name_department = MultiplyNode(data["name"],
                                          data["department"],
                                          data["dob"])
            self.name_dob = MultiplyNode(data["name"],
                                          data["department"],
                                          data["dob"])
        else:
            cur_name = self.name_head
            name_ordering = []
            while cur_name:
                cur_name = cur_name.next_name
                name_ordering.append(
                    (cur_name.name, cur_name.department, cur_name.dob)
                )
            name_ordering.append((data["name"], data["department"], data["dob"]))
            sorted(name_ordering, key=lambda x: x[0])
            self.name_head = None
            cur = self.name_head
            cur = MultiplyNode(elem[0], elem[1], elem[2])
            for elem in name_ordering:
                cur.next_name = MultiplyNode(elem[0], elem[1], elem[2])
                cur = cur.next_name
                
            cur_department = self.department_head
            department_ordering = []
            while cur_department:
                cur_department = cur_department.next_department
                department_ordering.append(
                    (cur_department.name, cur_department.department, cur_department.dob)
                )
            department_ordering.append((data["name"], data["department"], data["dob"]))
            sorted(department_ordering, key=lambda x: x[1])
            self.department_head = None
            cur = self.department_head
            cur = MultiplyNode(elem[0], elem[1], elem[2])
            for elem in department_ordering:
                cur.next_department = MultiplyNode(elem[0], elem[1], elem[2])
                cur = cur.next_department
            
            cur_dob = self.dob_head
            dob_ordering = []
            while cur_dob:
                cur_dob = cur_dob.next_dob
                dob_ordering.append(
                    (cur_dob.name, cur_dob.department, cur_dob.dob)
                )
            dob_ordering.append((data["name"], data["department"], data["dob"]))
            sorted(dob_ordering, key=lambda x: x[2])
            self.dob_head = None
            cur = self.dob_head
            cur = MultiplyNode(elem[0], elem[1], elem[2])
            for elem in dob_ordering:
                cur.next_dob = MultiplyNode(elem[0], elem[1], elem[2])
                cur = cur.next_dob
            
